from huggingface_hub import InferenceClient
from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts.prompt import PromptTemplate
import keys 
import streamlit as st 

loader = PyPDFLoader(
    r"courses_offered.pdf",
    mode="page")

docs = loader.load()
#print('Loaded document count :', len(docs))

embeddings_model = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

# Facebook AI Similarity Search
db = FAISS.from_documents(docs,embeddings_model)

prompt_template = """:
Consider the following context and give a short answer for the given question.

{context}

Question:{question}
"""

prompt  = PromptTemplate.from_template(prompt_template)

#print('Created FAISS index')
retriever = db.as_retriever()
repo_id = "mistralai/Mistral-7B-Instruct-v0.3"
llm = InferenceClient(repo_id, token=keys.HUGGINGFACEKEY)

st.title("RAG Demo")
query = st.text_input("Enter query :")
if len(query) > 0:
    results = retriever.invoke(query)
    matching_docs_str = "\n".join([doc.page_content for doc in results])
    final_prompt = prompt.format(context=matching_docs_str, question=query)
    result =  llm.text_generation(final_prompt)
    st.write(result)
    