
# 🧠 KnowSphere – Product Requirements Document (PRD)

## 📌 Project Name
**KnowSphere** – *Your Intelligent Knowledge Universe*

---

## 🎯 Overview
**KnowSphere** is a smart, AI-powered knowledge base chatbot that enables users to chat with uploaded documents using advanced Retrieval-Augmented Generation (RAG). It supports both voice and text interfaces and offers a secure, role-based system for document management and user interaction.

---

## ✅ Objectives
- Enable chat over user-uploaded PDFs and documents.
- Use RAG with vector databases to ensure contextual, accurate responses.
- Provide admin-user role segregation.
- Offer seamless voice-to-voice interaction.
- Persistent, scalable backend with customizable UI.

---

## 🖥️ Frontend

### Option 1: Next.js Web App
- Tech: Next.js, TailwindCSS, shadcn/ui, Zustand/Redux
- Upload PDFs/Docs
- Real-time chat with typing/voice input
- Responsive UI for desktop & mobile
- Role-based dashboards

### Option 2: Flutter Web App
- Tech: Flutter Web, Riverpod/Bloc, Lottie for animations
- Optimized for full cross-platform experience
- WebSpeech API integration (for voice I/O)
- Material 3 or custom UI theming

---

## 🧠 Backend

### Option 1: Node.js with Express
- File Upload (Multer)
- REST APIs for chat, user roles, document management
- WebSocket for real-time voice/text chat

### Option 2: Python with FastAPI
- Async endpoints
- Built-in OpenAPI docs
- Seamless integration with LangChain/LlamaIndex

---

## 🧠 OpenAI + RAG Layer
- LangChain / LlamaIndex for:
  - Chunking documents
  - Embedding + Query planning
- Embeddings: OpenAI, Cohere, or Hugging Face
- Vector DB: Pinecone / Qdrant / ChromaDB
  - Persistent, scalable search
  - Metadata tagging for user/session tracking

---

## 🎙️ Voice Input / Output (Bonus)
- Voice Input: Web Speech API (Next.js) / `dart:html` for Flutter Web
- Voice Output: Text-to-speech via Web Speech API or OpenAI's TTS
- Optional: Whisper API integration for more accurate speech-to-text

---

## 🔐 Roles & Permissions

### Admin:
- Upload/Remove documents
- View analytics / query logs
- Manage users

### User:
- Upload personal docs (optional)
- Chat with public or personal documents
- Voice and text input modes

---

## 🗃️ Database Choices
- User/Auth: PostgreSQL / MongoDB
- Vector Store: Pinecone / Qdrant / ChromaDB
- Sessions / Chat Logs: Firebase / Supabase / Redis for speed

---

## 📦 Core Features

| Feature | Description |
|--------|-------------|
| 🧾 PDF/Doc Upload | Admin/User uploads documents |
| 🔍 RAG-based Chat | Real-time chat based on retrieved content |
| 🔊 Voice Input/Output | Speak and listen to responses |
| 🔒 Auth + Roles | JWT or Firebase Auth with Admin/User roles |
| 🧠 Vector DB Integration | Fast search over embedded docs |
| 📄 Chat Logs | Store and retrieve past sessions |
| ⚙️ Admin Dashboard | Analytics, user mgmt, doc mgmt |
| 🌗 Light/Dark Mode | Optional theme toggling |
| 🌐 Multilingual Support | (Optional phase 2) |

---

## 🧪 Future Enhancements (Phase 2+)
- Multilingual Chatbot
- Mobile Flutter App version
- Knowledge Graph integration
- Document summarization
- Email ingestion / Zapier Integration

---

## 🔤 Name Suggestions

### App Name: `KnowSphere`
> Your personal sphere of knowledge.

### GitHub Repository Suggestions:
- `knowsphere-ai-chat`
- `knowsphere-docbot`
- `knowsphere-rag-chat`
- `knowsphere-ai`
- `knowsphere-voice-doc-chat`
