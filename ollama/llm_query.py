from langchain_ollama import OllamaLLM
 
model = OllamaLLM(model="llama3.2:1b")
print(model.invoke("Which is the capital of Spain?"))
