from langchain_huggingface import HuggingFaceEmbeddings

embeddings_model = HuggingFaceEmbeddings(
    model_name='sentence-transformers/all-MiniLM-L6-v2')


embeddings = embeddings_model.embed_documents(
    [
        "This is beautiful",
        "That soup was awful",
        "Your hair looks great",
        "I work for 9 to 10 hours a day",
        "I love football and swimming"
    ]
)

print(len(embeddings), len(embeddings[0]))
print(embeddings[0][:10])  

