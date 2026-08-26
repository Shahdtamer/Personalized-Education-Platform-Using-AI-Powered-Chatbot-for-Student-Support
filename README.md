# 🎓 Personalized Education Platform — AI-Powered Chatbot for Student Support

A full-stack RAG (Retrieval-Augmented Generation) application that acts as an AI study assistant: students chat with an agent that recommends courses and learning resources from a knowledge base, with persistent conversation memory and user authentication.
---

## ✨ Features

- **Conversational AI agent** — a LangChain tool-calling agent powered by Google **Gemini 2.5 Flash**, prompted to answer educational questions and recommend courses using retrieved context (with anti-hallucination and "no relevant result" guardrails built into the system prompt).
- **RAG pipeline** — a Coursera course dataset is chunked (`RecursiveCharacterTextSplitter`), embedded with `sentence-transformers/all-MiniLM-L6-v2`, and stored in a persistent **ChromaDB** vector store, exposed to the agent as a retriever tool.
- **Per-session conversation memory** — chat history is tracked per session via LangChain's `RunnableWithMessageHistory`, so the agent can reference earlier turns.
- **User authentication** — register / login / logout backed by **Supabase Auth**, with user profiles stored in Postgres.
- **Chat persistence** — messages and sessions are saved to Supabase tables and can be fetched by session ID.
- **Streamlit frontend** — a multi-page app (Home, Login/Sign up, Chat) that talks to the FastAPI backend over REST.

## 🏗️ Architecture

```
User (Streamlit UI)
      │
      ▼
FastAPI backend  ──►  Supabase (Auth + Postgres: profiles, sessions, chat_history)
      │
      ▼
LangChain agent (Gemini 2.5 Flash)
      │
      ▼
Retriever tool ──► ChromaDB vector store ◄── HuggingFace embeddings ◄── Coursera course CSV
```

## 🧰 Tech Stack

| Layer | Technology |
|---|---|
| LLM / Agent | LangChain, Google Gemini (`gemini-2.5-flash`) |
| Retrieval | ChromaDB, HuggingFace `sentence-transformers` |
| Backend API | FastAPI |
| Frontend | Streamlit |
| Auth & Database | Supabase (Auth + Postgres) |
| Data | Pandas, CSV course dataset (~890 courses) |

## 📁 Project Structure

```
backend/
├── api/
│   ├── main.py            # FastAPI app entrypoint, routers
│   ├── auth_routes.py     # /auth/register, /auth/login, /auth/logout
│   └── chat_routes.py     # /chat/ (send message), /chat/history/{session_id}
├── db/
│   └── supabase_client.py # Supabase client init
└── services/
    ├── auth_service.py    # Supabase auth logic
    ├── chat_service.py    # Save/fetch chat history, create sessions
    └── rag/
        ├── loader.py       # CSV loading + chunking
        ├── vectorstore.py  # Embeddings + ChromaDB + retriever tool
        ├── agent.py        # Agent prompt, tool-calling agent, memory
        └── dependencies.py # Wires the RAG pipeline together at startup

frontend/
├── Home.py                # Landing page
├── pages/
│   ├── login.py            # Login / sign-up page
│   └── chat.py             # Chat interface
└── utils/
    ├── api.py               # HTTP calls to the FastAPI backend
    ├── auth.py              # Session/auth helpers
    └── styles.py            # Custom CSS

data/
├── coursea_data.csv        # Source dataset for the knowledge base
└── chroma_db/              # Persisted vector store
```

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- A [Supabase](https://supabase.com/) project (URL + service key)
- A [Google AI Studio](https://aistudio.google.com/) API key (for Gemini)

### Installation

```bash
git clone https://github.com/Shahdtamer/Personalized-Education-Platform-Using-AI-Powered-Chatbot-for-Student-Support.git
cd Personalized-Education-Platform-Using-AI-Powered-Chatbot-for-Student-Support
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_gemini_api_key
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_service_key
```

### Run the backend

```bash
uvicorn backend.api.main:app --reload
```

### Run the frontend

```bash
cd frontend
streamlit run frontend/Home.py
```

## 🗺️ Roadmap

- Expand the knowledge base beyond the current single Coursera course dataset.
- Add a progress-tracking dashboard for students.

## 📄 License

Apache License 2.0 — see [LICENSE](LICENSE) for details.
