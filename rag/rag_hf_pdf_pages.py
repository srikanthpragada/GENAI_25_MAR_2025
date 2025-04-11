from langchain.chains import RetrievalQA

# pip install -qU langchain_community pypdf
from langchain_community.document_loaders import PyPDFLoader

from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = PyPDFLoader(
    r"courses_offered.pdf",
    mode="page")

docs = loader.load()
print("Number of pages loaded: ", len(docs))

model = "tinyllama"
embeddings = HuggingFaceEmbeddings("")

db = FAISS.from_documents(docs, embeddings)
llm = OllamaLLM(model=model)

# Retrieval-Augmented Question Answering (RAG) chain 
chain = RetrievalQA.from_chain_type(
    llm,
    retriever=db.as_retriever()
)

question = "What is the duration of AWS course?"
result = chain.invoke({"query": question})
print(result['result'])
