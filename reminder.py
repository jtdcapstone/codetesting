import streamlit as st
import time
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

def main():
    st.title("Reminder App")
    st.write("Enter your reminder below:")

    text = st.text_input("Reminder:")
    minutes = st.number_input("In how many minutes?", min_value=1)

    if st.button("Set Reminder"):
        write_reminder(text)
        time.sleep(minutes * 60)
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
