from langchain_ollama import OllamaLLM
import streamlit as st

st.title("Llama 3.2 Demo")
prompt = st.text_input("Enter your prompt", "")

if len(prompt)  > 0:
    model = OllamaLLM(model="llama3.2")
    response = model.invoke(prompt)
    st.write(f"Response: {response}")
