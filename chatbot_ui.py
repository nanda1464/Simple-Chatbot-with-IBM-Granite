import streamlit as st
import requests

# Backend URL (Flask di localhost:5000)
BACKEND_URL = "http://localhost:5000/ask"

st.set_page_config(page_title="Chatbot", page_icon="🤖", layout="wide")

# CSS custom gaya mirip ChatGPT
st.markdown(
    """
    <style>
    body {
        background-color: #1e1e1e;
        color: #fff;
        font-family: "Segoe UI", sans-serif;
    }
    .sticky-header h1{
        margin: 0;
        font-size: 24px;
        colour: white;
    }
    .chat-container{
        display: felx;
        flex-direction: column;
    }
    .user-bubble {
        background-color: #005C4B;
        color: white;
        padding: 12px 16px;
        border-radius: 12px;
        margin: 8px 0;
        max-width: 75%;
        text-align: right;
        float: right;
        clear: both;
    }
    .bot-bubble {
        background-color: #333;
        color: white;
        padding: 12px 16px;
        border-radius: 12px;
        margin: 8px 0;
        max-width: 75%;
        text-align: left;
        float: left;
        clear: both;
    }
    /* Animasi muncul */
    @keyframes fadeIn {
        from {opacity: 0; transform: translateY(5px);}
        to {opacity: 1; transform: translateY(0);}
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown("<div class='sticky-header'><h1>Ask Granite 🤖</h1></div>", unsafe_allow_html=True)
st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
st.markdown("<div class='bot-bubble'>Halo, saya Granite. Ada yang bisa saya bantu?</div>", unsafe_allow_html=True)
st.markdown("<div class='user-bubble'>Hai! Bisa bantu saya jelaskan tentang AI?</div>", unsafe_allow_html=True)
st.markdown("<div class='bot-bubble'>Tentu! AI adalah kecerdasan buatan yang memungkinkan mesin belajar dari data.</div>", unsafe_allow_html=True)
st.markdown("<div class='user-bubble'>Mantap! Terima kasih 👍</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Session state untuk menyimpan chat
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Fungsi call ke backend
def send_question(question):
    try:
        response = requests.post(BACKEND_URL, json={"question": question})
        if response.status_code == 200:
            data = response.json()
            return data.get("answer", "⚠️ No answer received")
        else:
            return f"⚠️ Error {response.status_code}: {response.text}"
    except Exception as e:
        return f"⚠️ Backend connection error: {str(e)}"

# Tampilan chat
chat_placeholder = st.empty()
with chat_placeholder.container():
    st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
    for chat in st.session_state.chat_history:
        if chat["role"] == "user":
            st.markdown(f"<div class='user-bubble'>{chat['message']}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='bot-bubble'>{chat['message']}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Input Chat (mirip ChatGPT)
user_input = st.chat_input("Ketik pesan...")
if user_input:
    # Tambah pesan user
    st.session_state.chat_history.append({"role": "user", "message": user_input})

    # Kirim ke backend
    answer = send_question(user_input)

    # Tambah jawaban bot
    st.session_state.chat_history.append({"role": "bot", "message": answer})

    # Refresh tampilan agar auto-scroll ke pesan terbaru
    chat_placeholder.empty()
    with chat_placeholder.container():
        st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
        for chat in st.session_state.chat_history:
            if chat["role"] == "user":
                st.markdown(f"<div class='user-bubble'>{chat['message']}</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div class='bot-bubble'>{chat['message']}</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
