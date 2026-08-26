from .loader import documents_loading,chunking
from .vectorstore import batchify,create_vectorstore,build_retrieval
from .agent import building_react_agent

docs=documents_loading("data/coursea_data.csv")
chunks=chunking(docs)
batches=batchify(chunks)
vector_db=create_vectorstore(chunks)
retrieval,retrieval_tool=build_retrieval(vector_db)
agent=building_react_agent(retrieval_tool)


