from flask import Flask, render_template, request
from src.helper import download_huggingface_embeddings
from langchain_community.vectorstores.chroma import Chroma
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers
from langchain.chains import RetrievalQA
from src.prompt import *

app = Flask(__name__)

embeddings = download_huggingface_embeddings()

dosearch = Chroma(persist_directory="db",embedding_function=embeddings)

retriever=dosearch.as_retriever(search_type="mmr",search_kwargs={"k":7})

prompt_template=PromptTemplate(
    input_variables=["context","question"],
    template=prompt
)

chain_type_kwargs={"prompt":prompt_template}

llm=CTransformers(
    model="model/llama-2-7b-chat.ggmlv3.q4_0.bin",
    model_type="llama",
    config={
        'max_new_tokens':512,
        'temperature':0.8
    }
)

qa = RetrievalQA.from_chain_type(llm=llm,chain_type="stuff",retriever=retriever,return_source_documents=True)

@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    print("Request ", request)
    msg = request.form["msg"]
    input = msg
    print(input)
    result = qa({"query":input})
    print("Response : ", result["result"])
    return str(result["result"])

if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)
