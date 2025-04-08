from huggingface_hub import InferenceClient
import keys 
model_id = "mistralai/Mistral-7B-Instruct-v0.2"
client = InferenceClient(model=model_id, 
                         token=keys.HUGGINGFACE_KEY
                         )

response = client.text_generation(
    "Who are the top 5 greatest footballers of all time? Just give names only",
    temperature=0.5, 
    frequency_penalty=1,
    max_new_tokens=200)
print(response)
