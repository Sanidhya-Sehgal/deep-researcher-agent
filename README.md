# 🔎 Deep Research Agent

A hybrid AI-powered research agent that automates topic research, analysis, and structured report generation — using a combination of local and cloud LLMs.

---

## ✨ Features

* **Hybrid LLM Architecture** — Seamlessly switch between local (Ollama) and cloud (Groq) inference
* **Wikipedia Data Scraping** — Automatically fetches topic summaries to ground responses in real data
* **Structured Report Generation** — Produces clean, readable reports with Introduction, Key Concepts, Applications, and Conclusion
* **Streamlit Web UI** — Interactive chat-style interface with search history
* **MCP Server** — Exposes the research agent as a tool for Claude Desktop or Cursor
* **CLI Support** — Run research directly from your terminal

---

## 🧠 How It Works

1. **Scrape** — Fetches a Wikipedia summary for the given topic
2. **Fallback** — If no Wikipedia data is found, the LLM generates context from its own knowledge
3. **Analyze & Report** — The LLM synthesizes the data into a structured, detailed report

```
Input Topic → Wikipedia Scraper → LLM Analysis → Structured Report
```

---

## 🔀 LLM Modes

| Mode | Engine | When to use |
|------|--------|-------------|
| 🟢 Local | Ollama (`llama3`) | Offline / privacy-first usage |
| 🔵 Cloud | Groq (`llama3-8b-8192`) | Faster responses, no local setup |

Switch modes via the `USE_LOCAL` environment variable.

---

## 📦 Prerequisites

* Python 3.10+
* [Ollama](https://ollama.com) installed and running locally *(for local mode)*
* [Groq API key](https://console.groq.com) *(for cloud mode)*

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/deep-researcher-agent.git
cd deep-researcher-agent
```

---

## ⚙️ Virtual Environment Setup (Recommended)

### 🪟 Windows (PowerShell)

#### Create virtual environment

```bash
python -m venv .venv
```

#### Activate it

```bash
.\.venv\Scripts\Activate
```

#### Upgrade pip

```bash
python -m pip install --upgrade pip
```

#### Install dependencies

```bash
pip install -r requirements.txt
```

---

### 🐧 Mac / Linux

#### Create virtual environment

```bash
python3 -m venv .venv
```

#### Activate it

```bash
source .venv/bin/activate
```

#### Upgrade pip

```bash
pip install --upgrade pip
```

#### Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Setup

Create a `.env` file in the root directory:

```env
USE_LOCAL=true
GROQ_API_KEY=your_groq_api_key_here
```

---

## 🖥️ Usage

### 🔹 Web Interface (Recommended)

```bash
streamlit run app.py
```

Open your browser at:
http://localhost:8501

---

### 🔹 Command Line

```bash
python agents.py
```

---

### 🔹 MCP Server (Claude Desktop / Cursor)

Add the following to your `.cursor/mcp.json` or `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "deep_researcher_agent": {
      "command": "python",
      "args": [
        "C:/path/to/your/project/server.py"
      ],
      "env": {
        "USE_LOCAL": "false",
        "GROQ_API_KEY": "your_groq_api_key_here"
      }
    }
  }
}
```

> Replace `C:/path/to/your/project/server.py` with your actual file path.

Then restart Claude Desktop — you'll see `deep_researcher_agent` available as a tool.

---

## ⚠️ Important Notes

### 🟢 Local Mode (Ollama)

Start the Ollama server:

```bash
ollama serve
```

Pull the model:

```bash
ollama pull llama3
```

---

### 🔵 Cloud Mode (Groq)

Set in your `.env`:

```env
USE_LOCAL=false
```

---

## 🧪 Example Queries

Try researching:

```
Artificial Intelligence
Model Context Protocol
Blockchain Technology
Neural Networks
```

---

## 📁 Project Structure

```
deep-researcher-agent/
├── app.py              # Streamlit web interface
├── agents.py           # Core research workflow & LLM logic
├── server.py           # MCP server
├── requirements.txt    # Python dependencies
├── pyproject.toml      # Project metadata
├── .env                # Environment variables (not committed)
└── README.md           # This file
```

---

## ⚙️ Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `USE_LOCAL` | `true` | Use Ollama locally (`true`) or Groq cloud (`false`) |
| `GROQ_API_KEY` | — | Required only when `USE_LOCAL=false` |

---

## 🛠️ Tech Stack

* [Streamlit](https://streamlit.io) — Web UI
* [Ollama](https://ollama.com) — Local LLM inference
* [Groq](https://groq.com) — Cloud LLM inference
* [Wikipedia REST API](https://en.wikipedia.org/api/rest_v1/) — Data source
* [FastMCP](https://github.com/jlowin/fastmcp) — MCP server

---

## 🚨 Common Issues

### ModuleNotFoundError

```bash
pip install -r requirements.txt
```

---

### Ollama not responding

```bash
ollama serve
```

---

### Slow response in local mode

Switch to cloud mode:

```env
USE_LOCAL=false
```

---

## 💡 Pro Tips

Check which Python is active:

```bash
where python    # Windows
which python    # Mac/Linux
```

Deactivate virtual environment when done:

```bash
deactivate
```

---

## ❤️ Author

Developed by **Sanidhya** 🚀