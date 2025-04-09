#pip install google-generativeai

import keys 
import google.generativeai as genai

genai.configure(api_key=keys.GOOGLEKEY)

model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content("5 big cities in India")
print(response.text)
 
