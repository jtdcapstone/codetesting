#example.py

#imports
import streamlit as st
import os
import time


st.set_page_config(page_title="brAIn buddy", page_icon=":brain:", layout="wide") ## Set layout wide to cover whole page.

credentials = {
	"admin": "admin",
	"jadab": "JadaB!123",
	"tessa": "TessA!123",
	"daylat": "DaylaT!123"
}

def creds_entered():
	
	username = st.session_state["user"].strip()
	password = st.session_state["passwd"].strip()
	
	if username in credentials and credentials[username] == password:
		
		st.session_state["authenticated"] = True
	else:
		st.session_state["authenticated"] = False
		if not st.session_state["passwd"]:
			st.warning("Please enter password.")
		elif not st.session_state["user"]:
			st.warning("Please enter username.")	
		else:
			
			st.error("Invalid Username/Password :face_with_raised_eyebrow:")

def authenticate_user():
	st.subheader("brAIn buddy :brain:")
	if "authenticated" not in st.session_state:
		
		st.text_input(label="Username: ", value="", key="user", on_change=creds_entered)
		st.text_input(label="Password: ", value="", key="passwd", type="password", on_change=creds_entered)
		return False
	else: 
		if st.session_state["authenticated"]:
			if st.button("Log Out"):
				st.session_state["authenticated"] = False
			return True
		else:
			st.text_input(label="Username: ", value="", key="user", on_change=creds_entered)
			st.text_input(label="Password: ", value="", key="passwd", type="password", on_change=creds_entered)
			return False
	return False
	
if authenticate_user():
	
	

	st.write("Welcome!")
	
	if st.button("Chatbot") == True:
		import tester
	elif st.button("Notepad") == True:
		import note
	elif st.button("Reminder") == True:
		import reminder
	else:
		time.sleep(10)
		st.write("Choose an application! :brain:")
