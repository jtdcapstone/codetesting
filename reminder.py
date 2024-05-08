import streamlit as st
from datetime import datetime, timedelta
import os

# File path to store reminders
reminders_file = "reminders.txt"

# Function to load reminders from file
def load_reminders():
    reminders = []
    if os.path.exists(reminders_file):
        with open(reminders_file, "r") as file:
            for line in file:
                parts = line.strip().split(";")
                if len(parts) == 2:
                    text, dt_str = parts
                    dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
                    reminders.append((text, dt))
    return reminders

# Function to save reminders to file
def save_reminders(reminders):
    with open(reminders_file, "w") as file:
        for text, dt in reminders:
            file.write(f"{text};{dt.strftime('%Y-%m-%d %H:%M:%S')}\n")

# Streamlit UI
def main():
    st.title("Reminder Program")

    # Load reminders from file
    reminders = load_reminders()

    st.header("Add Reminder")
    reminder_text = st.text_input("Enter your reminder:")
    reminder_datetime = st.datetime_input("Reminder datetime:")
    if st.button("Add Reminder"):
        if reminder_text and reminder_datetime:
            reminders.append((reminder_text, reminder_datetime))
            save_reminders(reminders)
            st.success("Reminder added successfully!")
        else:
            st.warning("Please enter a reminder and select a datetime.")

    # Sidebar for listing reminders
    with st.sidebar:
        st.header("Your Reminders")
        if reminders:
            for idx, (text, dt) in enumerate(reminders, start=1):
                st.write(f"{idx}. {text} - {dt.strftime('%Y-%m-%d %H:%M')}")
        else:
            st.write("No reminders set yet.")

# Function to check reminders and notify if due
def check_reminders():
    now = datetime.now()
    reminders_to_delete = []
    reminders = load_reminders()
    for idx, (text, dt) in enumerate(reminders):
        if now >= dt:
            st.warning(f"Reminder: {text}")
            reminders_to_delete.append(idx)

    # Remove reminders after displaying
    for idx in reversed(reminders_to_delete):
        del reminders[idx]

    # Save updated reminders to file
    save_reminders(reminders)

if __name__ == "__main__":
    main()
    check_reminders()  # Call check_reminders after main() to continuously check reminders

