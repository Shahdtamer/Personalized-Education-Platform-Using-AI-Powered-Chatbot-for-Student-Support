from langchain_community.document_loaders import CSVLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os
import shutil
from dotenv import load_dotenv
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # Get the parent directory of the current file
Data_path = os.path.join(BASE_DIR, "data", "coursea_data.csv")
chunk_size=1000
chunk_overlap=100
load_dotenv()
#Data ingestion
def documents_loading(Data_path: str):
 loader=CSVLoader(Data_path
                  , encoding="utf-8")
 docs=loader.load()
 return docs
#Chunking
def chunking(docs):
  text_splitter=RecursiveCharacterTextSplitter(chunk_size=chunk_size,
                                               chunk_overlap=chunk_overlap)
  chunks=text_splitter.split_documents(docs)
  return chunks
