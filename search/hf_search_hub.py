from langchain_community.embeddings import HuggingFaceInferenceAPIEmbeddings
import keys 

# 1. Initialize HuggingFaceInferenceAPIEmbeddings
embeddings_model = HuggingFaceInferenceAPIEmbeddings(
    api_key=keys.HUGGINGFACEKEY,
    model_name="sentence-transformers/all-MiniLM-L6-v2"  # or any model available via Inference API
)

from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
 

# 2. Sample Data 
documents = [
    Document(page_content="LangChain is a framework."),
    Document(page_content="Ollama allows running LLMs locally."),
    Document(page_content="FAISS is for similarity search."),
    Document(page_content="Bill Gates Founded Microsoft"),
    Document(page_content="Real Madrid won UEFA Champions League 13 times.")
]

# 3. Create FAISS index from documents
vectorstore = FAISS.from_documents(documents, embeddings_model)

# 4. Perform a similarity search
query = "Bill Gates"
results = vectorstore.similarity_search(query, k=1)  # Get the top 2 results

# 5. Print the results
print("Results:", results[0].page_content)
 

