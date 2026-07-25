"""
🤖 AI Chatbot — Streamlit Frontend
===================================
A beautiful, generic chatbot UI that works with any OpenAI-compatible API.
Supports: OpenRouter, OpenAI, Groq, Together AI, Ollama, and more.

Usage:
    streamlit run chatbot.py
"""

import streamlit as st
import requests
import json
import os
from dotenv import load_dotenv

# ── Load environment variables ───────────────────────────────────────────────
load_dotenv()

# ── Page Configuration ───────────────────────────────────────────────────────
st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded",
)

# ── Custom CSS for Premium Look ──────────────────────────────────────────────
st.markdown("""
<style>
    /* ── Global ── */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    .stApp {
        font-family: 'Inter', sans-serif;
    }

    /* ── Header ── */
    .chat-header {
        text-align: center;
        padding: 1.5rem 0 1rem 0;
    }
    .chat-header h1 {
        font-size: 2rem;
        font-weight: 700;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.25rem;
    }
    .chat-header p {
        color: #888;
        font-size: 0.95rem;
        font-weight: 400;
    }

    /* ── Chat Messages ── */
    .stChatMessage {
        border-radius: 16px !important;
        margin-bottom: 0.75rem !important;
        padding: 0.75rem 1rem !important;
    }

    /* ── Sidebar ── */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1a1a2e 0%, #16213e 100%);
    }
    section[data-testid="stSidebar"] .stMarkdown h2,
    section[data-testid="stSidebar"] .stMarkdown h3 {
        color: #e0e0ff !important;
    }
    section[data-testid="stSidebar"] .stMarkdown p,
    section[data-testid="stSidebar"] .stMarkdown label {
        color: #c0c0e0 !important;
    }

    /* ── Divider ── */
    .sidebar-divider {
        border: none;
        border-top: 1px solid rgba(255,255,255,0.1);
        margin: 1rem 0;
    }

    /* ── Status badge ── */
    .status-badge {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
        margin-top: 0.5rem;
    }
    .status-connected {
        background: rgba(72, 199, 142, 0.2);
        color: #48c78e;
        border: 1px solid rgba(72, 199, 142, 0.3);
    }
    .status-disconnected {
        background: rgba(255, 99, 71, 0.2);
        color: #ff6347;
        border: 1px solid rgba(255, 99, 71, 0.3);
    }
</style>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# SIDEBAR — API Configuration
# ══════════════════════════════════════════════════════════════════════════════
with st.sidebar:
    st.markdown("## ⚙️ Configuration")
    st.markdown('<hr class="sidebar-divider">', unsafe_allow_html=True)

    # ── Preset Providers ─────────────────────────────────────────────────────
    provider = st.selectbox(
        "API Provider",
        ["OpenRouter", "OpenAI", "Groq", "Together AI", "Ollama (Local)", "Custom"],
        index=0,
        help="Select your LLM provider or choose Custom to enter your own URL."
    )

    PROVIDER_URLS = {
        "OpenRouter":     "https://openrouter.ai/api/v1/chat/completions",
        "OpenAI":         "https://api.openai.com/v1/chat/completions",
        "Groq":           "https://api.groq.com/openai/v1/chat/completions",
        "Together AI":    "https://api.together.xyz/v1/chat/completions",
        "Ollama (Local)": "http://localhost:11434/v1/chat/completions",
        "Custom":         "",
    }

    # ── API URL ──────────────────────────────────────────────────────────────
    default_url = PROVIDER_URLS.get(provider, "")
    if provider == "Custom":
        api_url = st.text_input("API URL", value="", placeholder="https://your-api.com/v1/chat/completions")
    else:
        api_url = st.text_input("API URL", value=default_url)

    # ── API Key ──────────────────────────────────────────────────────────────
    env_key = os.getenv("API_KEY", "")
    api_key = st.text_input(
        "API Key",
        value=env_key,
        type="password",
        help="Loaded from .env if available. You can override it here."
    )

    # ── Model Selection ──────────────────────────────────────────────────────
    DEFAULT_MODELS = {
        "OpenRouter":     "openai/gpt-oss-120b:free",
        "OpenAI":         "gpt-4o-mini",
        "Groq":           "llama-3.3-70b-versatile",
        "Together AI":    "meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
        "Ollama (Local)": "llama3",
        "Custom":         "",
    }
    model_name = st.text_input(
        "Model",
        value=DEFAULT_MODELS.get(provider, ""),
        help="Enter the model identifier for your chosen provider."
    )

    st.markdown('<hr class="sidebar-divider">', unsafe_allow_html=True)

    # ── Advanced Settings ────────────────────────────────────────────────────
    with st.expander("🔧 Advanced Settings"):
        temperature = st.slider("Temperature", 0.0, 2.0, 0.7, 0.05,
                                help="Higher = more creative, Lower = more focused.")
        max_tokens = st.number_input("Max Tokens", 64, 16384, 1024, 64,
                                     help="Maximum number of tokens in the response.")
        system_prompt = st.text_area(
            "System Prompt",
            value="You are a helpful, friendly AI assistant. Answer concisely and clearly.",
            height=100,
            help="Set the personality / behavior of the chatbot."
        )

    st.markdown('<hr class="sidebar-divider">', unsafe_allow_html=True)

    # ── Status ───────────────────────────────────────────────────────────────
    is_configured = bool(api_url and api_key and model_name)
    if is_configured:
        st.markdown(
            '<span class="status-badge status-connected">● Ready</span>',
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            '<span class="status-badge status-disconnected">● Not Configured</span>',
            unsafe_allow_html=True,
        )

    # ── Clear Chat ───────────────────────────────────────────────────────────
    if st.button("🗑️  Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()


# ══════════════════════════════════════════════════════════════════════════════
# MAIN CHAT AREA
# ══════════════════════════════════════════════════════════════════════════════

# ── Header ───────────────────────────────────────────────────────────────────
st.markdown("""
<div class="chat-header">
    <h1>🤖 AI Chatbot</h1>
    <p>Powered by any OpenAI-compatible API</p>
</div>
""", unsafe_allow_html=True)

# ── Initialise session state ─────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []

# ── Render chat history ──────────────────────────────────────────────────────
for msg in st.session_state.messages:
    with st.chat_message(msg["role"], avatar="🧑‍💻" if msg["role"] == "user" else "🤖"):
        st.markdown(msg["content"])


# ══════════════════════════════════════════════════════════════════════════════
# API CALL FUNCTION
# ══════════════════════════════════════════════════════════════════════════════

def get_ai_response(messages_history: list[dict]) -> str:
    """
    Sends the conversation to the configured API and returns the assistant's reply.
    Works with any OpenAI-compatible chat/completions endpoint.
    """
    # Build the messages payload (system prompt + conversation)
    api_messages = [{"role": "system", "content": system_prompt}] + messages_history

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": model_name,
        "messages": api_messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
    }

    try:
        response = requests.post(
            url=api_url,
            headers=headers,
            data=json.dumps(payload),
            timeout=120,
        )
        response.raise_for_status()
        data = response.json()

        # Standard OpenAI-compatible response parsing
        return data["choices"][0]["message"]["content"]

    except requests.exceptions.Timeout:
        return "⏳ **Request timed out.** The API took too long to respond. Please try again."
    except requests.exceptions.ConnectionError:
        return "🔌 **Connection error.** Could not reach the API. Check your URL and internet connection."
    except requests.exceptions.HTTPError as e:
        return f"❌ **HTTP Error {e.response.status_code}:**\n```\n{e.response.text[:500]}\n```"
    except (KeyError, IndexError):
        return f"⚠️ **Unexpected response format:**\n```json\n{json.dumps(data, indent=2)[:500]}\n```"
    except Exception as e:
        return f"💥 **Error:** {str(e)}"


# ══════════════════════════════════════════════════════════════════════════════
# CHAT INPUT & RESPONSE
# ══════════════════════════════════════════════════════════════════════════════

if prompt := st.chat_input("Type your message here…", disabled=not is_configured):
    # ── Add user message ─────────────────────────────────────────────────────
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="🧑‍💻"):
        st.markdown(prompt)

    # ── Get and display AI response ──────────────────────────────────────────
    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("Thinking…"):
            reply = get_ai_response(st.session_state.messages)
        st.markdown(reply)

    # ── Save assistant message ───────────────────────────────────────────────
    st.session_state.messages.append({"role": "assistant", "content": reply})
