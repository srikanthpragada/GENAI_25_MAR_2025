# Load document from Text File

from langchain_community.document_loaders.directory import DirectoryLoader
from langchain_community.document_loaders.text import TextLoader    

# Load the text file from the given directory
loader = DirectoryLoader(".", glob="*.txt", loader_cls=TextLoader)   

# Load the documents
docs = loader.load()
print("Loaded Documents", len(docs))

# Print the loaded documents
for doc in docs:
    print(doc.page_content[:50])  # Print the first 50 characters of each document
    print("-" * 50)
