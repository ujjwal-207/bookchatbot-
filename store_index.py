import os 
from src.helper import load_pdf,embeddings
from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
load_dotenv()

PINECONE_API_KEY=os.getenv("PINECONE_API_KEY")

from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore

extraced_date = load_pdf("data/")

def text_splitter(extraced_date):
    text_split = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20)
    text_chunks = text_split.split_documents(extraced_date)
    return text_chunks
text_chunks = text_splitter(extraced_date)

pc = Pinecone(api_key= PINECONE_API_KEY)
index = pc.Index("bookchat")
vector_store= PineconeVectorStore.from_texts(
    [t.page_content for t in text_chunks],
    embedding=embeddings,
    index_name="bookchat")

