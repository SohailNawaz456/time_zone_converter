import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

# Define available time zones
TIME_ZONES = [
    "UTC",
    "Asia/Karachi",
    "America/New_York",
    "Europe/London",
    "Asia/Tokyo",
    "Australia/Sydney",
    "America/Los_Angeles",
    "Europe/Berlin",
    "Asia/Dubai",
    "Asia/Kolkata",
]

# App Title with Styling
st.title("🕒 Time Zone Converter 🌍")

# Multi-select for choosing time zones
st.sidebar.header("🌐 Select Timezones")
selected_timezone = st.sidebar.multiselect(
    "Choose Timezones:", TIME_ZONES, default=["UTC", "Asia/Karachi"]
)

# Display Selected Timezones with Current Time
st.subheader("⏳ Current Time in Selected Timezones")
st.write("---")
for tz in selected_timezone:
    current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    st.write(f"**📌 {tz}**: 🕰️ `{current_time}`")

# Divider for better UI
st.write("---")

# Time Conversion Section
st.subheader("🔄 Convert Time Between Timezones")
st.write("Select a time and convert it between different time zones.")

# User selects time and time zones
current_time = st.time_input("🕰️ Select Current Time:", value=datetime.now().time())
from_tz = st.selectbox("🌍 From Timezone", TIME_ZONES, index=0)
to_tz = st.selectbox("🌍 To Timezone", TIME_ZONES, index=1)

# Convert Time Button
if st.button("🔁 Convert Time"):
    dt = datetime.combine(datetime.today(), current_time, tzinfo=ZoneInfo(from_tz))
    converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d %I:%M:%S %p")

    # Display result with success message
    st.success(f"✅ **Converted Time in {to_tz}:** 🕰️ `{converted_time}`")
