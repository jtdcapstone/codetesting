import time
import plyer.notification

def main():
    print("What would you like to be reminded about?")
    text = str(input())
    
    print("In how many minutes?")
    minutes = float(input())
    
    # Convert minutes to seconds
    seconds = minutes * 60
    
    # Wait for the specified duration
    time.sleep(seconds)
    
    print(text)
    send_notification(text)

# Function to send notification
def send_notification(text):
    plyer.notification.notify(
        title="Reminder",
        message=text,
        timeout=10  # Notification timeout in seconds
    )

if __name__ == "__main__":
    main()
