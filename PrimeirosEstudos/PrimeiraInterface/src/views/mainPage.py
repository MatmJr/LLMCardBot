import streamlit as st
from src.models.textGen import geracao_texto


def paginaPrincipal():
    if "messages" not in st.session_state:
        st.session_state.messages = []

    messages = st.session_state["messages"]

    st.header("Bem-vindo(a)!", divider=True)

    st.markdown(
        """
    <style>
    .message-box {
        padding: 10px;
        border-radius: 5px;
        background-color: inherit; /* Herda a cor de fundo do tema */
        text-align: center;
        border: 1px solid rgba(0, 0, 0, 0.1); /* Sutil para light e dark mode */
        margin-bottom: 20px;
    }
    </style>
    <div class="message-box">
        <p> Pergunte algo para o CreditCardBot.</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    for message in messages:
        chat = st.chat_message(message["role"])
        chat.markdown(message["content"])

    prompt = st.chat_input("Pergunte algo")

    if prompt:
        new_msg = {"role": "user", "content": prompt}
        chat = st.chat_message(new_msg["role"])
        chat.markdown(new_msg["content"])
        messages.append(new_msg)
        st.session_state["mensagens"] = messages

        chat = st.chat_message("assistant")
        placeholder = chat.empty()
        resposta = geracao_texto(messages)
        placeholder.markdown(resposta + "▌")
        new_msg = {"role": "assistant", "content": resposta}
        messages.append(new_msg)
        st.session_state["messages"] = messages
