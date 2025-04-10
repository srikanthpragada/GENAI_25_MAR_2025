from transformers import pipeline

query = pipeline("question-answering",
                 model="distilbert/distilbert-base-uncased-distilled-squad")

context = """
Srikanth Pragada is a trainer
Geneative AI batch is scheduled to start on 25-MAR-2025
Roberto Carlos is a footballer from Brazil
"""

result = query(question="Roberto Carlos is from which country?",
               context=context) 

print(result['answer'])

result = query(question="When Generative AI batch starts",
               context=context)  

print(result['answer'])
