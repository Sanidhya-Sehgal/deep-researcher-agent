import streamlit as st
from agents import run_research
import time
import re

st.set_page_config(
    page_title="Deep Research Agent",
    page_icon="🔎",
)

# =========================
# 🧠 INIT SESSION STATE
# =========================
if "history" not in st.session_state:
    st.session_state.history = []

if "selected_report" not in st.session_state:
    st.session_state.selected_report = None


# =========================
# 🎯 TITLE
# =========================
st.markdown(
    """
    <div style="text-align:center; padding: 20px 0;">
        <h1>🔎 AI Deep Research Agent</h1>
        <p style="font-size:18px;">
            Hybrid AI system using <b>Ollama (Local)</b> + <b>Groq (Cloud)</b>
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# =========================
# 📌 SIDEBAR
# =========================
with st.sidebar:
    st.header("⚙️ Configuration")

    st.markdown("### Mode")
    st.markdown(
        """
- 🟢 **Local Mode** → Uses Ollama  
- 🔵 **Cloud Mode** → Uses Groq API  
        """
    )

    st.markdown("---")

    st.header("🕘 Search History")

    # Show history
    for i, item in enumerate(reversed(st.session_state.history)):
        if st.button(item["query"], key=f"history_{i}"):
            st.session_state.selected_report = item["report"]

    # Clear history button
    if st.button("🗑 Clear History"):
        st.session_state.history = []
        st.session_state.selected_report = None

    st.markdown("---")

    st.header("📖 About")
    st.markdown(
        """
This AI Research Agent performs:

- 🔍 **Data Collection** (Wikipedia)
- 🧠 **Analysis** using LLM
- ✍️ **Report Generation**

Built with a hybrid architecture:
- Local LLM (Ollama)
- Cloud LLM (Groq)
        """
    )

    st.markdown("---")
    st.markdown("Developed by **Sanidhya** 🚀")


# =========================
# 💬 CHAT INPUT
# =========================
user_input = st.chat_input("Enter your research topic...")

if user_input:
    try:
        with st.status("Processing research...", expanded=True) as status:

            status.write("🔍 Fetching data...")
            time.sleep(0.5)

            status.write("🧠 Analyzing...")
            time.sleep(0.5)

            status.write("✍️ Generating report...")

            # Run pipeline
            report = run_research(user_input)

            status.update(label="✅ Research completed!", state="complete")

        # Clean output
        cleaned_report = re.sub(r"^```(?:[a-zA-Z]*)?\n?", "", report)
        cleaned_report = re.sub(r"\n?```$", "", cleaned_report)

        # Save to history
        st.session_state.history.append({
            "query": user_input,
            "report": cleaned_report
        })

        # Show latest report
        st.markdown("## 📄 Research Report")
        st.markdown(cleaned_report)

    except Exception as e:
        st.error(f"❌ Error: {e}")


# =========================
# 📜 SHOW SELECTED HISTORY
# =========================
if st.session_state.selected_report:
    st.markdown("## 📜 Previous Report")
    st.markdown(st.session_state.selected_report)