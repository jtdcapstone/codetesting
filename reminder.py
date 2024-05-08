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

# Function to remove a reminder from the text file
def remove_reminder(reminder):
    reminders = read_reminders()
    reminders.remove(reminder)
    with open("reminders.txt", "w") as file:
        for reminder in reminders:
            file.write(reminder + "\n")

# Function to process reminders
def process_reminders():
    current_datetime = datetime.now()
    reminders = read_reminders()
    for reminder in reminders:
        reminder_datetime = datetime.strptime(reminder.split("|")[0].strip(), "%Y-%m-%d %H:%M")
        if current_datetime < reminder_datetime:
            time_to_wait = (reminder_datetime - current_datetime).total_seconds()
            time.sleep(time_to_wait)
            notification.notify(
                title="Reminder",
                message=reminder.split("|")[1].strip(),
                timeout=10  # Notification timeout in seconds
            )

# Function to convert input time to datetime object
def get_reminder_datetime(date, hours, minutes):
    reminder_datetime = datetime.combine(date, datetime.min.time())
    reminder_datetime = reminder_datetime.replace(hour=hours, minute=minutes)
    return reminder_datetime

def main():
    st.title("Reminder App")
    st.write("Enter your reminder below:")

    text = st.text_input("Reminder:")
    reminder_date = st.date_input("Select date:")
    hours = st.number_input("Enter hours (0-23):", min_value=0, max_value=23, value=0)
    minutes = st.number_input("Enter minutes (0-59):", min_value=0, max_value=59, value=0)

    if st.button("Set Reminder"):
        reminder_datetime = get_reminder_datetime(reminder_date, hours, minutes)
        write_reminder(f"{reminder_datetime.strftime('%Y-%m-%d %H:%M')} | {text}")
        st.write(text)

    # Process reminders
    process_reminders()

    # Sidebar for listing reminders
    with st.sidebar:
        st.header("Your Reminders")
        reminders = read_reminders()
        if reminders:
            for idx, reminder in enumerate(reminders, start=1):
                st.write(f"{idx}. {reminder}")
                if st.button(f"Delete Reminder {idx}"):
                    remove_reminder(reminder)
        else:
            st.write("No reminders set yet.")

if __name__ == "__main__":
    main()
