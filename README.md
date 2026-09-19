## Gemini Tools & Function Calling Codebook

A practical guide and implementation of Gemini’s tool usage and function calling capabilities. This project integrates multiple tools into a single execution script (`main.py`), demonstrating how Gemini can interact with external utilities in a modular and intelligent way.

---

### Features

* **Gemini Thinking Mode** – Simulates intelligent decision-making flow.
* **Code Execution Tool** – Dynamically runs code snippets in a controlled environment.
* **Google Search Tool** – Enables real-time search and information retrieval.
* **Function Calling Support** – Demonstrates structured function calls and responses via Gemini.

---

### File Structure

```plaintext
.
Gemini-Tools-Codebook/
│
├── main.py                                # Entry point – runs the full tool execution logic
├── GeminiLLM.py                           # Gemini LLM interface wrapper or helper functions
├── ToolSelector.py                        # Handles dynamic tool selection logic
├── Tool_GeminiThinking_AndMore.py         # Gemini Thinking Mode and possibly other tools
│
├── tools/
│   ├── __init__.py
│   ├── code_executor.py
│   ├── google_search.py
│   └── gemini_thinking.py
│
│
├── README.md                              # Project documentation
├── LICENSE                                # License information
├── .gitignore                             # Files/folders to ignore in version control
```
