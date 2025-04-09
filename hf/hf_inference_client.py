from huggingface_hub import InferenceClient
import keys 
model_id = "mistralai/Mistral-7B-Instruct-v0.2"
client = InferenceClient(model=model_id, 
                         token=keys.HUGGINGFACE_KEY)

response = client.text_generation("Which is the capital of Spain?")
print(response)
