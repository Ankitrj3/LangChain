# Dependency Analysis

## Files Dependencies

### `main.py` - Streamlit UI
- **streamlit** - Web framework for creating the UI
- **promptTemplate** - Local module for generating names

### `promptTemplate.py` - Backend Logic
- **os** - Built-in (no install needed)
- **dotenv** (python-dotenv) - Load environment variables from .env
- **google.generativeai** (google-generativeai) - Google Gemini AI client
- **langchain_core.prompts** (langchain-core) - LangChain prompt templates
- **langchain_google_genai** (langchain-google-genai) - LangChain integration with Google Gemini

## All Required Packages

| Package | Version | Purpose |
|---------|---------|---------|
| streamlit | 1.40.1 | Web UI framework |
| langchain | 0.1.20 | LLM orchestration |
| langchain-core | 0.3.79 | Core LangChain utilities |
| langchain-google-genai | 2.0.10 | Google Gemini integration |
| google-generativeai | 0.8.3 | Google Gemini API client |
| python-dotenv | 1.0.1 | Load .env files |

## Installation

Install all dependencies at once:

```bash
cd /Users/ankitranjan/Desktop/LangChain/LangChainLLM
./venv/bin/pip install -r requirements.txt
```

Or install individually:

```bash
./venv/bin/pip install streamlit langchain langchain-core langchain-google-genai google-generativeai python-dotenv
```

## Environment Setup

Create a `.env` file:

```bash
GEMINI_API_KEY=your_api_key_here
```

Get your API key from: https://makersuite.google.com/app/apikey
