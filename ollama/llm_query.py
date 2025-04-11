from langchain_ollama import OllamaLLM
 
model = OllamaLLM(model="tinyllama")
print(model.invoke("Which is the capital of Spain?"))
