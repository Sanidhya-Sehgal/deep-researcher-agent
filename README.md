# 🔎 Deep Research Agent // System 02

**Live System:** [https://deep-research-system.streamlit.app/](https://deep-research-system.streamlit.app/)

An autonomous AI-powered research system designed to scan the live web, synthesize technical data, and generate structured reports with source citations. 

---

## ⚡ Midnight Terminal Edition
This version features the **"Midnight Terminal"** UI—a high-end, dark-themed dashboard built for technical professional environments.

## ✨ Key Features

*   **Autonomous Web Search** — Powered by **Agno (Phidata)** and **DuckDuckGo** for real-time, live data harvesting.
*   **Deep Reasoning Engine** — Uses **Llama 3.3 (70B)** via **Groq** for high-speed technical synthesis and logic.
*   **Midnight Terminal UI** — Sleek glassmorphic panels, electric cyan accents, and pixel-art elements for a professional "System Builder" aesthetic.
*   **Archive Sidebar** — Persistent session history to track previous research investigations.
*   **Markdown Export** — One-click report saving for documentation and technical logs.
*   **Hybrid LLM Support** — Switch to local mode (Ollama) via environment variables for privacy-first tasks.

---

## 🧠 How It Works

1.  **Ingest** — User provides a research parameter or complex technical topic.
2.  **Scan** — The agent autonomously constructs search queries and scans the live web using DuckDuckGo.
3.  **Refine** — Data is parsed, filtered for relevance, and cross-referenced.
4.  **Synthesize** — The LLM generates a structured report with Introduction, Key Concepts, Applications, and Citations.

---

## 📦 Tech Stack

*   **Framework**: [Agno](https://agno.com) (Agentic Workflow)
*   **LLM (Cloud)**: [Groq](https://groq.com) (Llama 3.3 70B)
*   **LLM (Local)**: [Ollama](https://ollama.com)
*   **Search Engine**: [DuckDuckGo](https://duckduckgo.com)
*   **Frontend**: [Streamlit](https://streamlit.io) (Custom CSS)

---

## 🚀 Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/Sanidhya-Sehgal/deep-researcher-agent.git
cd deep-researcher-agent
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Environment Config
Create a `.env` file:
```env
GROQ_API_KEY=your_api_key_here
USE_LOCAL=false
```

### 4. Run Locally
```bash
streamlit run app.py
```

---

## 🌎 Deployment
This app is optimized for **Streamlit Cloud**. To deploy:
1. Push this code to GitHub.
2. Link the repo on [share.streamlit.io](https://share.streamlit.io).
3. Add your `GROQ_API_KEY` to the **Secrets** section in the dashboard.

---

## ❤️ Author
Developed by **Sanidhya Sehgal** 🚀
[Portfolio](http://localhost:3000/) // [GitHub](https://github.com/Sanidhya-Sehgal)