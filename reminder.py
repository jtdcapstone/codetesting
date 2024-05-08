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

# Function to remove expired reminders
def remove_expired_reminders():
    now = datetime.now()
    with open("reminders.txt", "r+") as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            reminder_time = datetime.strptime(line.split("|")[0], "%Y-%m-%d %H:%M")
            if reminder_time > now:
                file.write(line)
        file.truncate()

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

    if st.button("Set Reminder"):File "/home/adams/.local/lib/python3.11/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 600, in _run_script
    exec(code, module.__dict__)
File "/home/adams/cs403/CAPSTONE/reminder.py", line 77, in <module>
    main()
File "/home/adams/cs403/CAPSTONE/reminder.py", line 53, in main
    remove_expired_reminders()
File "/home/adams/cs403/CAPSTONE/reminder.py", line 27, in remove_expired_reminders
    reminder_time = datetime.strptime(line.split("|")[0], "%Y-%m-%d %H:%M")
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/usr/lib64/python3.11/_strptime.py", line 568, in _strptime_datetime
    tt, fraction, gmtoff_fraction = _strptime(data_string, format)
                                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/usr/lib64/python3.11/_strptime.py", line 352, in _strptime
    raise ValueError("unconverted data remains: %s" %
        reminder_datetime = get_reminder_datetime(reminder_date, hours, minutes)
        write_reminder(f"{reminder_datetime.strftime('%Y-%m-%d %H:%M')} | {text}")
        st.write(text)
        send_notification(text, reminder_datetime)

    remove_expired_reminders()
        
    # Sidebar for listing reminders
    with st.sidebar:
        st.header("Your Reminders")
        reminders = read_reminders()
        if reminders:
            for idx, reminder in enumerate(reminders, start=1):
                st.write(f"{idx}. {reminder}")
        else:
            st.write("No reminders set yet.")

def send_notification(reminder, reminder_datetime):
    current_datetime = datetime.now()
    if current_datetime < reminder_datetime:
        time_to_wait = (reminder_datetime - current_datetime).total_seconds()
        time.sleep(time_to_wait)
        notification.notify(
            title="Reminder",
            message=reminder,
            timeout=10  # Notification timeout in seconds
        )

if __name__ == "__main__":
    main()

File "/home/adams/.local/lib/python3.11/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 600, in _run_script
    exec(code, module.__dict__)
File "/home/adams/cs403/CAPSTONE/reminder.py", line 77, in <module>
    main()
File "/home/adams/cs403/CAPSTONE/reminder.py", line 53, in main
    remove_expired_reminders()
File "/home/adams/cs403/CAPSTONE/reminder.py", line 27, in remove_expired_reminders
    reminder_time = datetime.strptime(line.split("|")[0], "%Y-%m-%d %H:%M")
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/usr/lib64/python3.11/_strptime.py", line 568, in _strptime_datetime
    tt, fraction, gmtoff_fraction = _strptime(data_string, format)
                                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/usr/lib64/python3.11/_strptime.py", line 352, in _strptime
    raise ValueError("unconverted data remains: %s" %
