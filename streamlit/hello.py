# pip install -q streamlit
import streamlit as st

st.title("Demo")
name = st.text_input("Enter your name", "" )
if len(name) > 0:
    st.write(f"Hello {name}, Welcome to the Streamlit App!")
     