from huggingface_hub import InferenceClient
from langchain.chains import RetrievalQA
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
import keys 
from langchain_core.prompts.prompt import PromptTemplate

loader = WebBaseLoader("https://www.andrewng.org/about")    
docs = loader.load()
print("Number of documents loaded: ", len(docs))

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=256,
    chunk_overlap=50
)
texts = text_splitter.split_documents(docs)
print("Number of chunks created: ", len(texts))

# Facebook AI Similarity Search
db = FAISS.from_documents(docs, 
        HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2'))
print('Created FAISS index')

question = "What did Andrew Ng do in Baidu?"
retriever = db.as_retriever()

prompt_template = """
Give me answer to my question based on the context.

{context}

Question: {question}
"""

prompt  = PromptTemplate.from_template(prompt_template)

results = retriever.invoke(question)
print("Number of documents retrieved: ", len(results))

matching_docs_str = "\n".join([doc.page_content for doc in results])

final_prompt = prompt.format(context=matching_docs_str, question=question)

repo_id = "mistralai/Mistral-7B-Instruct-v0.3"
llm = InferenceClient(repo_id, token=keys.HUGGINGFACEKEY, timeout=120)
 
result =  llm.text_generation(final_prompt)
print(result)
