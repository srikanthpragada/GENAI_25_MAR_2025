from langchain_ollama import OllamaEmbeddings

embeddings_model = OllamaEmbeddings(model="nomic-embed-text")
embeddings = embeddings_model.embed_query("What is the use of Python language?")

print(len(embeddings))
print(embeddings[:10])

