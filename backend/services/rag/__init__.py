from .loader import documents_loading, chunking
from .vectorstore import reset_vector_store, create_vectorstore, build_retrieval
from .agent import building_react_agent

def initialize_rag():
    docs = documents_loading()
    chunks = chunking(docs)
    vector_store = create_vectorstore(chunks)
    retriever, retrieval_tool = build_retrieval(vector_store)
    agent = building_react_agent(retrieval_tool)
    return agent
