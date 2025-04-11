from langchain.chains import RetrievalQA
from langchain_community.document_loaders import WebBaseLoader

# pip install - q langchain-ollama
from langchain_ollama import OllamaLLM
from langchain_ollama import OllamaEmbeddings

from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = WebBaseLoader("https://www.andrewng.org/about")    
docs = loader.load()
print("Number of documents loaded: ", len(docs))

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=256,
    chunk_overlap=50
)
texts = text_splitter.split_documents(docs)
print("Number of chunks created: ", len(texts))

embeddings = OllamaEmbeddings(model="llama3.2")

db = FAISS.from_documents(texts, embeddings)
llm = OllamaLLM(model="llama3.2")

chain = RetrievalQA.from_chain_type(
    llm,
    retriever=db.as_retriever()
)

question = "What did Andrew Ng do in Baidu?"
result = chain.invoke({"query": question})
print(result['result'])
