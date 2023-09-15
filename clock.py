import streamlit as st
import datetime as dt
import pandas as pd
import random as rd
import time

def make_clock():
    st.title(':orange[' + time.strftime("%H:%M") + ']')
    st.title(':violet[' + time.strftime("%d %B %Y") + ']')
    pass