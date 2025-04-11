from langchain.chains import RetrievalQA
from langchain_community.document_loaders import PyPDFLoader
from langchain_ollama import OllamaLLM
from langchain_ollama import OllamaEmbeddings

from langchain_community.vectorstores import FAISS
from langchain_text_splitters import CharacterTextSplitter

loader = PyPDFLoader(
    r"courses_offered.pdf",
    mode="single")
docs = loader.load()

text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=128,
    chunk_overlap=20
)

texts = text_splitter.split_documents(docs)
embeddings = OllamaEmbeddings(model="nomic-embed-text")

db = FAISS.from_documents(texts, embeddings)
llm = OllamaLLM(model="gemma3:1b")

chain = RetrievalQA.from_chain_type(
    llm,
    retriever=db.as_retriever()
)

question = "Duration of AWS Course?"
result = chain.invoke({"query": question})
print(result['result'])
