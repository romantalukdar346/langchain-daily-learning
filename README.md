# 📘 LangChain Daily Learning

Welcome to my daily learning journal with [LangChain](https://www.langchain.com/)!  
This repository includes hands-on practice, structured examples, and notes as I explore the core components of LangChain using Python.

---

## 🧠 Topics Covered

- ✅ LLMs vs ChatModels in LangChain
- ✅ Embedding Models and Vector Stores
- ✅ LangChain Expression Language (LCEL)
- ✅ Runnable chains (sequential, conditional, branching)
- ✅ Prompt engineering & dynamic template injection
- ✅ Parsing structured output
- ✅ .env management and modular code structure

---

## 🚀 How to Run Locally


## 📁 Project Structure

LANGCHAIN_MODELS/
├── 1.LLMs/ # Experiments with LLMs (e.g., OpenAI, HuggingFace)
├── 2.ChatModels/ # Conversational model usage
├── 3.EmbeddingModels/ # Embedding generation & vector store usage

├── Chain/
│ ├── Runnables/ # LCEL-based runnable examples
│ ├── conditional_chain.py
│ ├── parallel_chain.py
│ └── sequential_chain.py

├── LangChain/ # Generic utils or wrappers (if any)

├── Output/
│ └── Parsers/
│ └── structured_output.py # Output formatting examples

├── Prompt/
│ ├── 1_prompt_ui.py
│ ├── 2_Dynamic_prompt.py
│ ├── prompt_template.json
│ ├── chat_prompt_temp.py
│ ├── chatbot.py
│ ├── prompt_generator.py
│ ├── messages.py
│ └── sms_placeholder.py

├── chat_history.txt # Sample saved chat
├── .env # Environment variables (ignored in Git)
├── requirements.txt # Dependencies

```bash
# Create and activate virtual environment (optional)
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run a specific example
python Chain/sequential_chain.py
├── test.py # Sandbox script
