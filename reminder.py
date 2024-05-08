import streamlit as st
import time
from datetime import datetime, timedelta
from plyer import notification

# Function to read reminders from the text file
def read_reminders():
    try:
        with open("reminders.txt", "r") as file:
            reminders = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        reminders = []
    return reminders

# Function to write reminders to the text file
def write_reminder(reminder):
    with open("reminders.txt", "a") as file:
        file.write(reminder + "\n")

# Function to convert input time to seconds from the current time
def calculate_time_to_wait(hours, minutes):
    now = datetime.now()
    alarm_time = now.replace(hour=hours, minute=minutes, second=0, microsecond=0)
    if alarm_time < now:
        alarm_time += timedelta(days=1)  # If the alarm time is in the past, schedule it for the next day
    return (alarm_time - now).total_seconds()

def main():
    st.title("Reminder App")
    st.write("Enter your reminder below:")

    text = st.text_input("Reminder:")
    hours = st.number_input("Enter hours (0-23):", min_value=0, max_value=23, value=0)
    minutes = st.number_input("Enter minutes (0-59):", min_value=0, max_value=59, value=0)

    if st.button("Set Reminder"):
        write_reminder(text)
        time_to_wait = calculate_time_to_wait(hours, minutes)
        time.sleep(time_to_wait)
        st.write(text)
        send_notification(text)
        
    # Sidebar for listing reminders
    with st.sidebar:
        st.header("Your Reminders")
        reminders = read_reminders()
        if reminders:
            for idx, reminder in enumerate(reminders, start=1):
                st.write(f"{idx}. {reminder}")
        else:
            st.write("No reminders set yet.")

def send_notification(reminder):
    notification.notify(
        title="Reminder",
        message=reminder,
        timeout=10  # Notification timeout in seconds
    )

if __name__ == "__main__":
    main()
