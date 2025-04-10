import google.generativeai as genai
import keys 
import streamlit as st

if 'text' not in st.session_state:
     st.session_state.text = ""

genai.configure(api_key=keys.GOOGLEKEY)

def clear_text():
     st.session_state.text = ""

llm = genai.GenerativeModel('gemini-2.0-flash')
st.title("Gemini Demo ")
prompt = st.text_area("Enter your prompt", key="text", height=100)
# Button to clear the text area
st.button("Clear All", on_click=clear_text)

if len(st.session_state.text) > 0 :
     response = llm.generate_content(st.session_state.text)
     st.write(response.text)

