from huggingface_hub import InferenceClient
from langchain.prompts import PromptTemplate
import keys

# 1. Initialize InferenceClient
model_id = "Helsinki-NLP/opus-mt-en-hi"   
client = InferenceClient(model=model_id, token= keys.HUGGINGFACE_KEY)

# 2. Create a PromptTemplate  
template_en_to_hi = """Translate the following English text to simple Hindi:

{text}

"""
prompt_en_to_hi = PromptTemplate.from_template(template=template_en_to_hi)

# 3. Format the prompt
english_text = "What did you learn about AI?"

prompt_en_to_hi = prompt_en_to_hi.format(text=english_text)
print(prompt_en_to_hi)


# 4. Use InferenceClient for translation
hindi_translation = client.translation(prompt_en_to_hi)

# 5. Print the translation
print(f"English: {english_text}")
print(f"Hindi: {hindi_translation.translation_text}")
