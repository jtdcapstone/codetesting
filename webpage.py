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

# example.py

import streamlit as st
import tester
import reminder
import note

st.set_page_config(page_title="brAIn buddy", page_icon=":brain:", layout="wide") 

def authenticate_user():
    # Authentication logic here
    # Return True if authenticated, False otherwise
    pass

def main():
    st.subheader("brAIn buddy :brain:")

    if authenticate_user():
        st.write("Welcome!")

        # Sidebar navigation
        selected_app = st.sidebar.radio("Select an application:", ["Chatbot", "Reminder", "Notepad"])

        # Display the selected application
        if selected_app == "Chatbot":
            tester.main()
        elif selected_app == "Reminder":
            reminder.main()
        elif selected_app == "Notepad":
            note.main()

if __name__ == "__main__":
    main()

2024-05-08 19:54:14.641 Uncaught app exception
Traceback (most recent call last):
  File "/home/adams/.local/lib/python3.11/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 600, in _run_script
    exec(code, module.__dict__)
  File "/home/adams/cs403/CAPSTONE/webpage.py", line 12, in <module>
    st.set_page_config(page_title="brAIn buddy", page_icon=":brain:", layout="wide") ## Set layout wide to cover whole page.
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adams/.local/lib/python3.11/site-packages/streamlit/runtime/metrics_util.py", line 397, in wrapped_func
    result = non_optional_func(*args, **kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adams/.local/lib/python3.11/site-packages/streamlit/commands/page_config.py", line 260, in set_page_config
    ctx.enqueue(msg)
  File "/home/adams/.local/lib/python3.11/site-packages/streamlit/runtime/scriptrunner/script_run_context.py", line 130, in enqueue
    raise StreamlitAPIException(
streamlit.errors.StreamlitAPIException: `set_page_config()` can only be called once per app page, and must be called as the first Streamlit command in your script.

For more information refer to the [docs](https://docs.streamlit.io/library/api-reference/utilities/st.set_page_config).

