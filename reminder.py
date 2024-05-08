import streamlit as st
import time
from plyer import notification

def main():
    st.title("Reminder App")
    st.write("Enter your reminder below:")

    text = st.text_input("Reminder:")
    minutes = st.number_input("In how many minutes?", min_value=1)

    if st.button("Set Reminder"):
        time.sleep(minutes * 60)
        st.write(text)
        send_notification(text)
        
 # Sidebar for listing reminders
    with st.sidebar:
        st.header("Your Reminders")
        if reminders:
            for idx, (text, dt) in enumerate(reminders, start=1):
                st.write(f"{idx}. {text} - {dt.strftime('%Y-%m-%d %H:%M')}")
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
