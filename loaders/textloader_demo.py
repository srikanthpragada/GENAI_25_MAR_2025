# Load document from Text File

from langchain_community.document_loaders.text import TextLoader

# Load the text file
loader = TextLoader("./mlk.txt")
# Load the documents
docs = loader.load()

# Print the loaded documents
for doc in docs:
    print(doc.page_content[:50])  # Print the first 50 characters of each document
    print("-" * 80)
