from langchain_ollama import OllamaLLM
import streamlit as st

st.title("Gemma 3 Demo")
prompt = st.text_input("Enter your prompt", "")

if len(prompt)  > 0:
    model = OllamaLLM(model="gemma3:1b")
    response = model.invoke(prompt)
    st.write(f"Response: {response}")
