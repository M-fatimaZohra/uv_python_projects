import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

st.title("Time Zone Converter")

time_zones = [
    "UTC",
    "Europe/London",
    "Europe/Paris",
    "Europe/Berlin",
    "Europe/Moscow",
    "Asia/Karachi",
    "Asia/Kolkata",
    "Asia/Dubai",
    "Asia/Tokyo",
    "Asia/Seoul",
    "Asia/Hong_Kong",
    "Asia/Singapore",
    "Asia/Shanghai",
    "Asia/Tehran",
    "Asia/Jakarta",
    "Africa/Cairo",
    "Africa/Johannesburg",
    "Australia/Sydney",
    "Australia/Melbourne",
    "Pacific/Auckland",
    "America/New_York",
    "America/Toronto",
    "America/Chicago",
    "America/Denver",
    "America/Los_Angeles",
    "America/Phoenix",
    "America/Halifax",
    "America/Sao_Paulo",
    "America/Bogota",
    "America/Argentina/Buenos_Aires",
    "America/Mexico_City",
    "America/Anchorage",
    "Pacific/Honolulu"
]

selected_time_zone = st.multiselect("select time zone",time_zones,default=["UTC","Asia/Kolkata"])

st.subheader("Selected Time Zones")

for tz in selected_time_zone:
    current_time = datetime.now(ZoneInfo(tz)).strftime( "%d-%b-%Y | %I:%M %p")
    st.write(f"##### Current time in {tz}: {current_time}")


st.subheader("Convert Time")
current_t = st.time_input("Enter current time zone",value=datetime.now().time().strftime("%I:%M"))
from_tz = st.selectbox("From Time Zone", time_zones, index=0)
to_tz = st.selectbox("To Time Zone", time_zones, index=1)

if st.button("Convert time"):
    date_time= datetime.combine(datetime.today(), current_t).replace(tzinfo=ZoneInfo(from_tz))
    converted_time= date_time.astimezone(ZoneInfo(to_tz)).strftime( "%d-%b-%Y | %I:%M %p")
    st.markdown(f"### :red[Converted time:] `{converted_time}`")
    
