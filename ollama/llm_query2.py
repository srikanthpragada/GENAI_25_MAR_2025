from langchain_ollama import OllamaLLM
 
model = OllamaLLM(model="gemma3:1b")
print(model.invoke("Which is the capital of Spain?"))
