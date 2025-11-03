import requests
import streamlit as st

# Function to call joke endpoint (/p1)
def get_joke(input_text):
    response = requests.post(
        url="http://localhost:8000/p1/invoke",
        json={
            "input": {"subject": input_text},
            "config": {},
            "kwargs": {}
        }
    )

    response.raise_for_status()  # will raise HTTPError if something goes wrong
    return response.json()["output"]

# Function to call sad story endpoint (/p2)
def get_story(input_text):
    response = requests.post(
        url="http://localhost:8000/p1/invoke",
        json={
            "input": {"subject": input_text},
            "config": {},
            "kwargs": {}
        }
    )

    response.raise_for_status()
    return response.json()["output"]

# Streamlit UI
st.title("Ollama LLM with Streamlit")

input_text1 = st.text_input("Enter a subject for a joke:")
input_text2 = st.text_input("Enter a subject for a sad story:")

if input_text1:
    try:
        joke = get_joke(input_text1)
        st.write("### Joke:")
        st.write(joke)
    except requests.exceptions.RequestException as e:
        st.error(f"Error connecting to server: {e}")

if input_text2:
    try:
        story = get_story(input_text2)
        st.write("### Sad Story:")
        st.write(story)
    except requests.exceptions.RequestException as e:
        st.error(f"Error connecting to server: {e}")
