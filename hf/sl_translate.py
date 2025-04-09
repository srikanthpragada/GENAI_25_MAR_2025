# pip install -q streamlit
import streamlit as st
from huggingface_hub import InferenceClient
import keys

model_id = "Helsinki-NLP/opus-mt-en-hi"   
client = InferenceClient(model=model_id, token= keys.HUGGINGFACE_KEY)

st.title("English to Hindi")
text  = st.text_input("Enligsh Text", "" )
if len(text) > 0:
    prompt = f"""
    Translate the following English text to simple Hindi:
    
    {text}                
    """
    hindi = client.translation(prompt)
    st.write(hindi.translation_text)



     