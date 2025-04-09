from huggingface_hub import InferenceClient
import keys 
model_id = "mistralai/Mistral-7B-Instruct-v0.2"
client = InferenceClient(model=model_id, 
                         token=keys.HUGGINGFACE_KEY
                         )

response = client.text_generation(
    "Write a story about AI",
    temperature=1.0, 
    max_new_tokens=200)

print(response)
