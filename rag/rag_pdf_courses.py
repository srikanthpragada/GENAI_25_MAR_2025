from huggingface_hub import InferenceClient
from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts.prompt import PromptTemplate
import keys 

loader = PyPDFLoader(
    r"courses_offered.pdf",
    mode="page")

docs = loader.load()
print('Loaded document count :', len(docs))

# Facebook AI Similarity Search
db = FAISS.from_documents(docs, 
      HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2'))

print('Created FAISS index')

query = "Generative AI course fee"


repo_id = "mistralai/Mistral-7B-Instruct-v0.3"
llm = InferenceClient(repo_id, token=keys.HUGGINGFACEKEY, timeout=120)
 
prompt_template = """
Please answer the question using the context.

{context}

Question: {question}
Answer: 
"""

prompt  = PromptTemplate.from_template(prompt_template)

retriever = db.as_retriever()
results = retriever.invoke(query)

matching_docs_str = "\n".join([doc.page_content for doc in results])

final_prompt = prompt.format(context=matching_docs_str, question=query)

result =  llm.text_generation(final_prompt)
print(result)
