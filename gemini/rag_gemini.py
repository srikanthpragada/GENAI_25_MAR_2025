from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
import keys 
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain.schema import StrOutputParser
import keys 
 
loader = PyPDFLoader(
    r"courses_offered.pdf",
    mode="page")

docs = loader.load()
print('Loaded document count :', len(docs))

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key= keys.GEMINIKEY)

# Facebook AI Similarity Search
db = FAISS.from_documents(docs, embeddings)
                           
print('Created FAISS index')
question = "what is the duration of Generative AI course?"

retriever = db.as_retriever(search_type="similarity", 
                            search_kwargs={"k": 3})

llm = GoogleGenerativeAI(model="gemini-2.0-flash", 
                         api_key = keys.GEMINIKEY)

prompt = PromptTemplate.from_template(
    """Consider the following questions and answers from the given context:
Q: question
A: answer
{context}
Answer the following question. Give a short answer.
{question}
"""
)
                                      
context = "\n\n".join(doc.page_content for doc in docs)
chain = prompt | llm

response = chain.invoke( {'context' : context, 'question' : question} )
print(response)

 