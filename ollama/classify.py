from langchain_ollama import OllamaLLM

model = OllamaLLM(model="llama3.2:1b")
prompt = """Find the sentiment in the text below. Just give only sentiment without any details:

Text: I love iPad. 

Sentiment: 
"""
result = model.invoke(prompt) 
print(result)
