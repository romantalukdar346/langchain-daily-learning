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

| Path                       | Description                                       |
| -------------------------- | ------------------------------------------------- |
| `1.LLMs/`                  | Experiments with LLMs (e.g., OpenAI, HuggingFace) |
| `2.ChatModels/`            | Conversational model usage                        |
| `3.EmbeddingModels/`       | Embedding generation & vector store usage         |
|                            |                                                   |
| `Chain/`                   | Chain logic and flow examples                     |
| ├── `Runnables/`           | LCEL-based runnable examples                      |
| ├── `conditional_chain.py` | If/else logic using RunnableBranch                |
| ├── `parallel_chain.py`    | Parallel chain execution                          |
| └── `sequential_chain.py`  | Simple sequential flow                            |
|                            |                                                   |
| `LangChain/`               | Generic utilities or wrappers (if any)            |
|                            |                                                   |
| `Output/Parsers/`          |                                                   |
| └── `structured_output.py` | Output formatting using parsers                   |
|                            |                                                   |
| `Prompt/`                  | Prompt engineering and generation                 |
| ├── `1_prompt_ui.py`       | Prompt interface example                          |
| ├── `2_Dynamic_prompt.py`  | Dynamic prompt construction                       |
| ├── `prompt_template.json` | Template configuration (JSON)                     |
| ├── `chat_prompt_temp.py`  | Chat prompt example                               |
| ├── `chatbot.py`           | Basic chatbot script                              |
| ├── `prompt_generator.py`  | Prompt generation tool                            |
| ├── `messages.py`          | Message formatting                                |
| └── `sms_placeholder.py`   | Placeholder SMS prompt                            |
|                            |                                                   |
| `.env`                     | Environment variables (API keys, etc.)            |
| `requirements.txt`         | Python dependencies                               |

```bash
# Create and activate virtual environment (optional)
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run a specific example
python Chain/sequential_chain.py
├── test.py # Sandbox script
