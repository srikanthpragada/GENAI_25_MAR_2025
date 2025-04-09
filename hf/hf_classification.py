from huggingface_hub import InferenceClient
import keys

model_id = "distilbert/distilbert-base-uncased-finetuned-sst-2-english"   
client = InferenceClient(model=model_id, 
                         token= keys.HUGGINGFACE_KEY)

result = client.text_classification("I admire the way you teach!")
print(result)
