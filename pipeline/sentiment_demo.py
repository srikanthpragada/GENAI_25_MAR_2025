from transformers import pipeline

classifier = pipeline("sentiment-analysis", 
                      model = "distilbert/distilbert-base-uncased-finetuned-sst-2-english")
result = classifier("I love iPad")
print(result)

result = classifier("I could not stand Mr. Tom")
print(result)
           