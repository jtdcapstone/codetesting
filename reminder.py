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
def write_reminder(reminders):
    with open("reminders.txt", "w") as file:
        for reminder in reminders:
            file.write(reminder + "\n")

# Function to remove a reminder from the text file
def remove_reminder(reminders, index):
    del reminders[index]
    write_reminder(reminders)

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
        reminders = read_reminders()
        reminders.append(f"{reminder_datetime.strftime('%Y-%m-%d %H:%M')} | {text}")
        write_reminder(reminders)
        st.write(text)

    # Process reminders
    process_reminders()

    # Sidebar for listing reminders
    with st.sidebar:
        st.header("Your Reminders")
        reminders = read_reminders()
        if reminders:
            for idx, reminder in enumerate(reminders, start=1):
                reminder_date, reminder_text = reminder.split("|")
                reminder_datetime = datetime.strptime(reminder_date.strip(), "%Y-%m-%d %H:%M")
                col1, col2, col3 = st.columns([1, 3, 1])
                with col1:
                    st.write(f"{idx}.")
                with col2:
                    if st.button(f"Edit Reminder {idx}"):
                        new_date = st.date_input("Edit Date:", value=reminder_datetime.date())
                        new_hours = st.number_input("Edit Hours (0-23):", min_value=0, max_value=23, value=reminder_datetime.hour)
                        new_minutes = st.number_input("Edit Minutes (0-59):", min_value=0, max_value=59, value=reminder_datetime.minute)
                        new_text = st.text_input("Edit Reminder:", value=reminder_text.strip())
                        if st.button("Save"):
                            reminders[idx - 1] = f"{get_reminder_datetime(new_date, new_hours, new_minutes).strftime('%Y-%m-%d %H:%M')} | {new_text}"
                            write_reminder(reminders)
                            st.success("Reminder updated successfully!")
                with col3:
                    if st.button(f"Delete Reminder {idx}"):
                        remove_reminder(reminders, idx - 1)
        else:
            st.write("No reminders set yet.")

if __name__ == "__main__":
    main()

ValueError: time data '2024-05-08 17:10' does not match format '%m/%d/%Y %H:%M'
Traceback:

File "/home/adams/.local/lib/python3.11/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 600, in _run_script
    exec(code, module.__dict__)
File "/home/adams/cs403/CAPSTONE/reminder.py", line 94, in <module>
    main()
File "/home/adams/cs403/CAPSTONE/reminder.py", line 65, in main
    process_reminders()
File "/home/adams/cs403/CAPSTONE/reminder.py", line 32, in process_reminders
    reminder_datetime = datetime.strptime(reminder.split("|")[0].strip(), "%m/%d/%Y %H:%M")
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/usr/lib64/python3.11/_strptime.py", line 568, in _strptime_datetime
    tt, fraction, gmtoff_fraction = _strptime(data_string, format)
                                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/usr/lib64/python3.11/_strptime.py", line 349, in _strptime
    raise ValueError("time data %r does not match format %r" %
