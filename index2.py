import streamlit as st
import requests
st.header("Random joke generator App")
st.write('''The Random Joke App is a fun and interactive web application built using Streamlit and Python’s 
         Requests module.This project fetches real-time jokes from a public API and displays them to the user 
         with just one click.It demonstrates how Python can connect to external web APIs, handle JSON data, and 
         create a simple yet engaging user interface.''')
st.write("#### Why used")
st.write(" To fetch real time jokes from a public API using the request module and " 
"diaplay them instantly")
st.write("To learn how to integrate APIs and handle json data effeciently in python")
st.write("To build a simple and integrate web app using Streamlit withouit needing" \
"HTML OR CSS")
st.write("To make learning python fun and practical through a creative,beginner friendly" \
"project")
st.write("#### How It Works")
st.write("The user clicks the tell me a joke button on the streamlit app ")
st.write("The app sends a GET request to the official joke API using the request module")
st.write("The API sends back a random joke in JSON format which includes the setup" \
"and Punchline.")
st.write("The app Extract the setup and punchline from the JSON data and displays" \
"them on the web page using st.write().")

st.header("Random Joke App")
st.write("Click the Button Below To get a random joke and make your day better!")
if st.button("Tell me a joke!"):
    res=requests.get("https://official-joke-api.appspot.com/random_joke")
    joke=res.json()
    st.write(joke["setup"])
    st.write(joke["punchline"])
else:
    st.write("Click the button to hear a joke")    


