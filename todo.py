import json
import streamlit as st
from cal import make_upcoming_md

def row_2():
    data = json.load(open('metadata.json'))
    string = ""
    for i in data["todo"]:
        string += "- " + i + " \n "
    print(string)
    todo, impt = st.columns([1,1])

    todo.header("TODO List")
    todo.write(string)

    impt.header("Important Events")
    impt.markdown(make_upcoming_md())
    return


