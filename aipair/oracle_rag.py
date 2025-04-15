import os
import cx_Oracle
from langchain.chains import RetrievalQA
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.prompts import PromptTemplate
from huggingface_hub import InferenceClient

# Configuration
ORACLE_DSN = "your_oracle_dsn"
ORACLE_USER = "your_username"
ORACLE_PASSWORD = "your_password"
HUGGINGFACE_API_KEY = "your_huggingface_api_key"
os.environ["HUGGINGFACEHUB_API_TOKEN"] = HUGGINGFACE_API_KEY

# Oracle Database Connection
def fetch_products():
    connection = cx_Oracle.connect(user=ORACLE_USER, password=ORACLE_PASSWORD, dsn=ORACLE_DSN)
    cursor = connection.cursor()
    cursor.execute("SELECT prodid, product_description, price FROM Products")
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return rows

# Prepare Data for Vector Store
def prepare_documents(products):
    documents = []
    for prodid, description, price in products:
        doc = {
            "content": f"Product ID: {prodid}\nDescription: {description}\nPrice: {price}",
            "metadata": {"prodid": prodid, "price": price}
        }
        documents.append(doc)
    return documents

# Initialize Vector Store
def initialize_vector_store(documents):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_store = FAISS.from_documents(documents, embeddings)
    return vector_store

# Initialize RAG Pipeline
def initialize_rag_pipeline(vector_store):
    retriever = vector_store.as_retriever()
    client = InferenceClient(model="gpt-4")
    prompt_template = PromptTemplate(
        input_variables=["context", "question"],
        template="Context: {context}\n\nQuestion: {question}\n\nAnswer:"
    )
    qa_chain = RetrievalQA.from_chain_type(
        retriever=retriever,
        chain_type="stuff",
        return_source_documents=True,
        prompt_template=prompt_template,
        llm=client
    )
    return qa_chain

# Main Function
def main():
    print("Fetching products from the database...")
    products = fetch_products()
    print(f"Fetched {len(products)} products.")

    print("Preparing documents...")
    documents = prepare_documents(products)

    print("Initializing vector store...")
    vector_store = initialize_vector_store(documents)

    print("Initializing RAG pipeline...")
    rag_pipeline = initialize_rag_pipeline(vector_store)

    print("Ready to answer questions!")
    while True:
        query = input("\nEnter your question about a product (or type 'exit' to quit): ")
        if query.lower() == "exit":
            break
        response = rag_pipeline.run(query)
        print("\nAnswer:", response["answer"])
        print("Source Documents:", response["source_documents"])

if __name__ == "__main__":
    main()