import sqlite3
from langchain.prompts import PromptTemplate
from huggingface_hub import InferenceClient
import keys 

db_path = r"courses.db"

def get_courses():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM courses")
    products = cursor.fetchall()
    conn.close()
    return products

def concate_course(course):
    course_id, title, description, duration, fee, prerequisite = course
    return f"Title: {title}\nDescription: {description}\nFee: {fee}\nDuration: {duration}\nPrerequisite: {prerequisite}"

# Load courses data
courses = get_courses()

context = ""
for course in courses:
    context += concate_course(course) + "\n\n"

#print(context)

prompt_template = """
You are a helpful assistant. You will be provided with a context and a question. Your task is to answer the question based on the context.
Context : 
{context}

Question: {question}
"""

prompt = PromptTemplate.from_template(prompt_template)
prompt_value = prompt.format(context=context, 
                question="What is the duration of Generative AI course?")

#print(prompt_value)


repo_id = "mistralai/Mistral-7B-Instruct-v0.3"
model = InferenceClient(repo_id, token=keys.HUGGINGFACEKEY, timeout=120)

response = model.text_generation( prompt_value);
print(response)











 