import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import PyMuPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

load_dotenv()

PINECONE_API_KEY=os.getenv("PINECONE_API_KEY")

def load_pdf(data):
    loader = DirectoryLoader(data,glob="*.pdf", loader_cls=PyMuPDFLoader)
    documents = loader.load()
    return documents

extraced_date = load_pdf("data/")

def text_splitter(extraced_date):
    text_split = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20)
    text_chunks = text_split.split_documents(extraced_date)
    return text_chunks

text_chunks = text_splitter(extraced_date)


def load_geneni_embeddings():
    embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key=os.getenv("GOOGLE_API_KEY"))
    return embeddings



