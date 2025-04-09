#pip install -U langchain-google-genai
from langchain_google_genai import GoogleGenerativeAI
import keys 

llm = GoogleGenerativeAI(
         model="gemini-2.0-flash", api_key=keys.GOOGLEKEY)

print(llm.invoke("Give 2 best songs of singer Micheal Jackson"))

