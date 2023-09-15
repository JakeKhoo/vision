import streamlit as st
import datetime as dt
import pandas as pd
from cal import make_calendar, make_upcoming_md
from clock import make_clock
from todo import row_2
import time

def main():
    st.set_page_config(layout="wide") 
    make_clock()
    row_2()
    make_upcoming_md()
    make_calendar()


main()
while True:
    time.sleep(0.5)
    if time.strftime("%S") == "00":
        st.experimental_rerun() 

