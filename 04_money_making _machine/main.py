import streamlit as st
import random
import time
import requests

st.title("Money making machine")

def generate_money():
    return random.randint(1,10000)

st.subheader("Generate money")

if st.button("Generate Money"):
    
    with st.spinner("Generating money",show_time=True):
        time.sleep(2)

    st.success(f"you won: {generate_money()}$")


def get_side_hustle():
    try:
        response = requests.get("http://127.0.0.1:8000/side_hustles")
        if response.status_code == 200:
            
            hustle = response.json()
            return hustle
        else:
             st.error("no side hustle for you")

    except:  
       return st.error("no side hustle for you..")
    

st.subheader("Side Hustle ideas")

if st.button("peak hustle"):
   idea = get_side_hustle()
   hustle = str(idea)
   clean =hustle.replace("{", "").replace("}", "").replace("_", " ").replace("'", "")
   
   st.info(f"{clean}")
   

def get_money_qoutes():
    try:
        response = requests.get("http://127.0.0.1:8000/money_qoutes?apikey=N19_Zone")
        if response.status_code == 200:
            
            hustle = response.json()
            return hustle
        else:
             st.error("no qoute for today")

    except:  
       return st.error("no qoute for today..")
    

st.subheader("Money Qoutes")

if st.button("peakQoute"):
   idea = get_money_qoutes()
   qoutes = str(idea)
   clean =qoutes.replace("{", "").replace("}", "").replace("_", " ").replace("'", "")
   
   st.info(f"{clean}")
   