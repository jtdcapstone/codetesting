import streamlit
import time
import plyer as notification

#reminder = user.ask("What do you want to be reminded about?")

def main():
	print("What would you like to be reminded about?")
	
	text = str(input())
	
	print("In how many minutes?")
	localTime = float(input())
	
	localTime = localTime * 60
	
	time.sleep(localTime)
	
	print(text)
	send_notification()

# Function to send notification
def send_notification(reminder):
    notification.notify(
        title="Reminder",
        message=reminder["text"],
        timeout=10  # Notification timeout in seconds
    )
main()
