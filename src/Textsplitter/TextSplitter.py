from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


loader = TextLoader('data.txt')
documents = loader.load()


splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,     
    chunk_overlap=50,    
    separators=["\n\n", "\n", ".", " "] 
)


chunks = splitter.split_documents(documents)

for i, chunk in enumerate(chunks):
    print(f"🧩 Chunk {i+1}:\n{chunk.page_content}")
    print("-" * 50)
