import streamlit as st
from agents import run_research
import time
import re

# =========================
# 🌑 MIDNIGHT TERMINAL CONFIG
# =========================
st.set_page_config(
    page_title="Deep Research // Midnight Terminal",
    page_icon="🌌",
    layout="wide"
)

def inject_terminal_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=VT323&family=Inter:wght@400;700&family=JetBrains+Mono:wght@400;700&display=swap');

    /* Global Styles */
    .stApp {
        background-color: #050505;
        color: #e0e0e0;
        font-family: 'Inter', sans-serif;
    }

    /* Terminal Headers */
    h1, h2, h3, .terminal-text {
        font-family: 'VT323', monospace !important;
        text-transform: uppercase;
        letter-spacing: 3px;
        color: #00f2ff !important;
        text-shadow: 0 0 10px rgba(0, 242, 255, 0.3);
    }

    h1 { font-size: 4.5rem !important; margin-bottom: 0 !important; }
    h2 { font-size: 2rem !important; }

    /* Dashboard Panels */
    .dashboard-panel {
        background-color: rgba(20, 20, 25, 0.8);
        border: 1px solid rgba(0, 242, 255, 0.2);
        padding: 2rem;
        margin-bottom: 1.5rem;
        border-radius: 4px;
        backdrop-filter: blur(10px);
    }

    /* Custom Scrollbar */
    ::-webkit-scrollbar { width: 8px; }
    ::-webkit-scrollbar-track { background: #050505; }
    ::-webkit-scrollbar-thumb { 
        background: #00f2ff; 
        border-radius: 4px;
        box-shadow: 0 0 5px rgba(0, 242, 255, 0.5);
    }

    /* Buttons */
    .stButton>button {
        background-color: transparent !important;
        color: #00f2ff !important;
        border: 1px solid #00f2ff !important;
        border-radius: 4px !important;
        font-family: 'VT323', monospace !important;
        font-size: 1.2rem !important;
        padding: 0.5rem 1rem !important;
        transition: all 0.3s !important;
        width: 100%;
        text-transform: uppercase;
    }

    .stButton>button:hover {
        background-color: rgba(0, 242, 255, 0.1) !important;
        box-shadow: 0 0 15px rgba(0, 242, 255, 0.3) !important;
        border: 1px solid #00f2ff !important;
    }

    /* Sidebar Customization */
    [data-testid="stSidebar"] {
        background-color: #0a0a0a !important;
        border-right: 1px solid rgba(0, 242, 255, 0.1);
    }
    
    [data-testid="stSidebar"] h2 {
        color: #00f2ff !important;
        font-size: 1.5rem !important;
    }

    /* Chat Input */
    [data-testid="stChatInput"] {
        border: 1px solid rgba(0, 242, 255, 0.3) !important;
        background-color: #0f0f0f !important;
        border-radius: 8px !important;
    }
    
    [data-testid="stChatInput"] textarea {
        color: #ffffff !important;
        background-color: transparent !important;
    }

    /* Status/Alerts */
    div[data-testid="stNotification"] {
        background-color: rgba(0, 242, 255, 0.05) !important;
        border: 1px solid rgba(0, 242, 255, 0.2) !important;
        color: #00f2ff !important;
        border-radius: 4px !important;
    }
    
    div[data-testid="stNotification"] p {
        color: #00f2ff !important;
    }

    /* Markdown styling */
    .markdown-content {
        line-height: 1.8;
        font-size: 1.05rem;
    }
    .markdown-content h1, .markdown-content h2, .markdown-content h3 {
        margin-top: 2rem !important;
    }
    
    /* Footer */
    .footer {
        position: fixed;
        bottom: 10px;
        right: 20px;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.8rem;
        opacity: 0.4;
        color: #00f2ff;
    }
    </style>
    """, unsafe_allow_html=True)

inject_terminal_css()

# =========================
# 🧠 SESSION STATE
# =========================
if "history" not in st.session_state:
    st.session_state.history = []

if "current_report" not in st.session_state:
    st.session_state.current_report = None

# =========================
# 📌 SIDEBAR
# =========================
with st.sidebar:
    st.markdown('<h2>SYSTEM ARCHIVE</h2>', unsafe_allow_html=True)
    
    if st.session_state.history:
        for i, item in enumerate(reversed(st.session_state.history)):
            if st.button(f"> {item['query'][:20]}...", key=f"hist_{i}"):
                st.session_state.current_report = item['report']
                st.session_state.current_query = item['query']
    else:
        st.markdown('<p style="opacity:0.5; font-size:0.8rem;">NO LOGS DETECTED</p>', unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("CLEAR ALL CACHE"):
        st.session_state.history = []
        st.session_state.current_report = None
        st.rerun()

    st.markdown('<div style="position:fixed; bottom:20px; left:20px; font-family:monospace; font-size:0.7rem; opacity:0.3;">'
                'NODE_ID: SS-01<br>'
                'STATUS: ONLINE<br>'
                'ENCRYPTION: AES-256'
                '</div>', unsafe_allow_html=True)

# =========================
# 🎯 MAIN UI
# =========================
st.markdown('<h1>DEEP RESEARCH</h1>', unsafe_allow_html=True)
st.markdown('<p style="font-family:JetBrains Mono; opacity:0.6; margin-top:-10px;">'
            '// AUTONOMOUS_RESEARCH_AGENT_v3.0</p>', unsafe_allow_html=True)

st.markdown('<div style="height: 30px;"></div>', unsafe_allow_html=True)

# Chat Input
user_input = st.chat_input("Input research parameters...")

if user_input:
    try:
        with st.status("INITIALIZING_AGENT_PIPELINE...", expanded=True) as status:
            status.write("📡 FETCHING_LIVE_DATA_STREAMS...")
            report = run_research(user_input)
            status.update(label="// ANALYSIS_COMPLETE", state="complete")
        
        st.session_state.current_report = report
        st.session_state.current_query = user_input
        
        # Save to history
        st.session_state.history.append({
            "query": user_input,
            "report": report
        })

    except Exception as e:
        st.error(f"FATAL_ERROR: {str(e)}")

# Display Report
if st.session_state.current_report:
    st.markdown(f'<h3>// RESEARCH_REPORT: {st.session_state.get("current_query", "UNNAMED")}</h3>', unsafe_allow_html=True)
    
    st.markdown('<div class="dashboard-panel markdown-content">', unsafe_allow_html=True)
    st.markdown(st.session_state.current_report)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Export options
    col_a, col_b = st.columns([1, 4])
    with col_a:
        st.download_button(
            label="💾 DOWNLOAD_LOG",
            data=st.session_state.current_report,
            file_name=f"research_log_{int(time.time())}.md",
            mime="text/markdown"
        )

# Footer
st.markdown('<div class="footer">OPERATOR: SANIDHYA // SYSTEM_SYNC_ACTIVE</div>', unsafe_allow_html=True)