from langchain_community.embeddings import HuggingFaceInferenceAPIEmbeddings
import keys 

embeddings_model = HuggingFaceInferenceAPIEmbeddings(
    model_name="sentence-transformers/all-mpnet-base-v2",
    api_key=keys.HUGGINGFACE_KEY
)
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

