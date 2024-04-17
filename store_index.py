from src.helper import load_pdf, text_splitter, download_huggingface_embeddings, download_llama2_model
from langchain_community.vectorstores.chroma import Chroma

extraceted_data = load_pdf("data/")
text_chunk = text_splitter(extracted_data=extraceted_data)
embeddings = download_huggingface_embeddings()

dosearch = Chroma.from_documents(documents=text_chunk, embedding=embeddings, persist_directory="db")
dosearch.persist()

download_llama2_model()
