# AI Knowledge Base Backend

This is a FastAPI-based backend for an AI Knowledge Base application. It allows users to upload PDF documents, embed their content into a vector store, and query the documents using a question-answering system powered by LangChain and OpenAI.

## Prerequisites

- **Python 3.8+**: Ensure Python is installed. Verify with:
  ```bash
  python --version
  ```
  Download from [python.org](https://python.org) if needed.
- **OpenAI API Key**: Required for `langchain-openai`. Obtain one from [OpenAI](https://platform.openai.com).
- **Dependencies**: Ensure a `requirements.txt` file with the following:
  ```
  fastapi==0.115.0
  pydantic==2.9.2
  uvicorn==0.30.6
  langchain==0.3.0
  langchain-community==0.3.0
  langchain-openai==0.2.0
  chromadb==0.5.5
  PyPDF2==3.0.1
  python-multipart==0.0.9
  ```

## Project Setup

Follow these steps to set up the project in a virtual environment.

### Windows Setup

#### Step 1: Create a Virtual Environment
1. Open a Command Prompt or PowerShell in the project directory.
2. Create a virtual environment named `venv`:
   ```bash
   python -m venv venv
   ```

#### Step 2: Activate the Virtual Environment
1. Activate the virtual environment:
   ```bash
   venv\Scripts\activate
   ```
   You’ll see `(venv)` in your terminal prompt.

#### Step 3: Install Dependencies
1. Ensure `requirements.txt` is in the project directory.
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

#### Step 4: Set Environment Variables
1. Set your OpenAI API key:
   ```bash
   set OPENAI_API_KEY=your-key
   ```
   Replace `your-key` with your actual OpenAI API key.

### macOS/Linux Setup

#### Step 1: Create a Virtual Environment
1. Open a terminal in the project directory.
2. Create a virtual environment named `venv`:
   ```bash
   python3 -m venv venv
   ```

#### Step 2: Activate the Virtual Environment
1. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```
   You’ll see `(venv)` in your terminal prompt.

#### Step 3: Install Dependencies
1. Ensure `requirements.txt` is in the project directory.
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

#### Step 4: Set Environment Variables
1. Set your OpenAI API key:
   ```bash
   export OPENAI_API_KEY=your-key