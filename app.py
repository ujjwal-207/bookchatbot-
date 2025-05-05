from flask import Flask, render_template, jsonify, request
from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
from src.helper import load_geneni_embeddings
from src.prompt import *
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain

load_dotenv()

PINECONE_API_KEY=os.getenv("PINECONE_API_KEY")

app = Flask(__name__)
embeddings = load_geneni_embeddings()

pc = Pinecone(api_key= PINECONE_API_KEY)
docsearch = PineconeVectorStore.from_existing_index(index_name="bookchat",embedding=embeddings)
retriver = docsearch.as_retriever(search_type="similarity", search_kwargs={"k":3})

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)

question_answer_chain = create_stuff_documents_chain(llm, prompt)

rag_chain = create_retrieval_chain(retriver, question_answer_chain)

@app.route("/")
def index():
    return render_template('chat.html')


@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    response = rag_chain.invoke({"input": msg})
    print("Response : ", response["answer"])
    return str(response["answer"])

if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 8080, debug= True)