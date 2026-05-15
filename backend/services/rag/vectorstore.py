from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.tools.retriever import create_retriever_tool
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
Data_path = os.path.join(BASE_DIR, "data", "coursea_data.csv")
Chroma_Dir=os.path.join(BASE_DIR, "data", "chroma_db")
#reset vector store directory
def reset_vector_store():
 if os.path.exists(Chroma_Dir):
  shutil.rmtree(Chroma_Dir)
  print("Vector data base is clean")
 else:
  print("No existing vector data vase found")

#Batchifing
def batchify(chunks,batch_size=150):
 for i in range(0,len(chunks),batch_size):
  yield chunks[i:i+batch_size]

#Embeddings and Vector Data Base
def create_vectorstore(chunks):
 embeddings=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
 vector_store=Chroma(embedding_function=embeddings,
                     persist_directory=Chroma_Dir,
                     collection_name="my_collection")
 for batch in batchify(chunks,150):
  vector_store.add_documents(batch)
 return vector_store

 #Retrieval tool
def build_retrieval(vector_store):
  retriever=vector_store.as_retriever(search_kwargs={"k": 3})
  retrieval_tool=create_retriever_tool(retriever,
                                       name="education_knowledge_tool",
                                       description="Use this tool to recommend courses and study materials for students.")
  return retriever,retrieval_tool