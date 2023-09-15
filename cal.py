import streamlit as st
import datetime as dt
import pandas as pd
import random as rd

def make_calendar():
    rd.seed(10)
    cal_df = get_random_calander(3)

    st.title("Calendar")
    cal_show_cols = ["Today", "Tomorrow"]
    for i in range(2,6):
        d = dt.datetime.today() + dt.timedelta(days = i)
        cal_show_cols += [d.strftime("%A")]

    data = []
    for i in range(0,6):
        d = dt.datetime.today() + dt.timedelta(days = i)
        d_str = d.strftime("%d/%m/%y")
        cal_date = cal_df[cal_df["Date"] == d_str]
        data += [cal_date]


    today, tmr, three = st.columns([1,1,1])
    days_cols_1 = [today, tmr, three]

    for i in range(0,3):
        days_cols_1[i].subheader(cal_show_cols[i])
        days_cols_1[i].write(create_markdown(data[i]))

    four, five, six = st.columns([1,1,1])
    days_cols_2 = [four, five, six]

    for i in range(3,6):
        days_cols_2[i-3].subheader(cal_show_cols[i])
        days_cols_2[i-3].write(create_markdown(data[i]))
    return

def get_random_calander(start_date_int):
    cols = ["Event_Name", "Date", "Start", "End", "Comments", "Tags"]
    df = pd.DataFrame(columns = cols)
    id = 1

    events = ["Meeting", "Dinner", "Basketball rv", "tennis"]
    tags = ["green", "blue", "red","white"]

    for j in range(1,5):
        for i in range(start_date_int, start_date_int + 6):
            name = events[j-1] + "_" + str(id)
            id += 1
            date = "0" + str(i) + "/09/23"
            start_int = rd.randint(0, 22)
            end_int = rd.randint(start_int + 1, 24)
            start = str(start_int) + ":00"
            end = str(end_int) + ":00"
            if len(start) < 5:
                start = "0" + start
            if len(end) < 5:
                end = "0" + end
            new_row = {
                "Event_Name" : name,
                "Date" : date,
                "Start" : start,
                "End" : end,
                "Comments" : str(rd.randint(1,2)),
                "Tags": tags[id%4]
            }
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    return df

def create_markdown(df):
    dct = {
    "red" : "🟥",
    "green" : "🟩",
    "blue" : "🟦",
    "white": "⬜"
    }
    
    string = "|Event " + " &nbsp; " * 14 + "|Time |  \n |---|---|  \n"
    df["INT"] = df["Start"].str.slice(stop = 2).astype('int32')
    df = df.sort_values(by = "INT")
    df.reset_index()
    white_spaces = 20
    for index, row in df.iterrows():
        string += "|"
        string += dct[row["Tags"]] + " "
        string += row["Event_Name"]
        white_spaces_left = white_spaces - len(row["Event_Name"])
        string += " | " + row["Start"] + " -- " + row["End"] + "|  \n"
    return string   


def make_upcoming_md():
    dct = {
    "red" : "🟥",
    "green" : "🟩",
    "blue" : "🟦",
    "white": "⬜"
    }
    rd.seed(10)

    cal_df = get_random_calander(3)
    df = cal_df[cal_df["Comments"] == "1"]
    df["datetime"] = df.apply(lambda row : dt.datetime.strptime(
        row["Date"] + row["Start"], '%d/%m/%y%H:%M'), axis = 1)
    df["timestamp"] = df.apply( lambda row : row["datetime"].timestamp(), axis = 1)
    df = df[df["datetime"] > dt.datetime.now()]
    df = df.sort_values(by = "timestamp").head(5)

    string = "|Event " + " &nbsp; " * 14 + "|Date |Time |  \n |---|---|---|  \n"
    for index, row in df.iterrows():
        string += "|"
        string += dct[row["Tags"]] + " "
        string += row["Event_Name"] + " | " + row["Date"]
        string += " | " + row["Start"] + " -- " + row["End"] + "|  \n"

    return string






    

