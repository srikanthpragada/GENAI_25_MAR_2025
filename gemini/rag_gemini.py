from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
import keys 
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
import keys 
 
loader = PyPDFLoader(
    r"courses_offered.pdf",
    mode="page")

docs = loader.load()
print('Loaded document count :', len(docs))

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key= keys.GOOGLEKEY)

# Facebook AI Similarity Search
db = FAISS.from_documents(docs, embeddings)
                           
print('Created FAISS index')


retriever = db.as_retriever(search_type="similarity", 
                            search_kwargs={"k": 3})

llm = GoogleGenerativeAI(model="gemini-2.0-flash", 
                         api_key = keys.GOOGLEKEY)


prompt = PromptTemplate.from_template( """
Please answer the question using the context.

{context}

Question: {question}
"""     
)
question = "what is the duration of Generative AI course?"

matching_docs = retriever.invoke(question)
                                      
context = "\n\n".join(doc.page_content for doc in matching_docs)
chain = prompt | llm

response = chain.invoke( {'context' : context, 'question' : question} )
print(response)

 