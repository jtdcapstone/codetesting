###################################################################################################
# Jada Bryan, Tess Adams, & Dayla Thorne
# CSCI-403-01
# timer.py
# Program that works as a timer and gives alerts when task is complete
# 5/8/24
###################################################################################################

#import
import streamlit as st
import time
from plyer import notification

# Function to read tasks from the text file
def readTasks():
    try:
        file = open("tasks.txt", "r")
        tasks = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        tasks = []
    return tasks

# Function to write tasks to the text file
def writeTask(task):
    file = open("tasks.txt", "a") 
    file.write(task + "\n")

# Function to write tasks to the text file
def deleteTask(task):
	tasks = readTasks()
	tasks.remove(task)
	writeTask(tasks)

def main():
    st.title("Timer")
    st.write("Enter your task below:")

    text = st.text_input("Task:")
    minutes = st.number_input("In how many minutes?", min_value=1)

    if st.button("Set Task"):
        writeTask(text)
        time.sleep(minutes * 60)
        st.write(text)
        sendNotification(text)
        
        
    # Sidebar for listing tasks
    with st.sidebar:
        st.header("Your Tasks")
        tasks = readTasks()
        if tasks:
            for task in tasks:
            	sendNotification(task)
            	deleteTask(task)
            time.sleep(minutes * 60)	

        else:
            st.write("No tasks set yet.")

def sendNotification(task):
    notification.notify(
        title="Timer",
        message=task,
        timeout=10  # Notification timeout in seconds
    )


main()
