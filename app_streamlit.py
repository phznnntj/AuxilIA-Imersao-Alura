import streamlit as st
import time
from AuxilIA import SistemaAgentesIA, gemini_model

# Inicialização do sistema de agentes
if gemini_model:
    sistema = SistemaAgentesIA(gemini_model)
else:
    st.error("O modelo Gemini não foi carregado corretamente. Verifique a configuração da API Key.")
    st.stop()

# Injeção de CSS personalizado
st.markdown(
    """
    <style>
    body {
        color: #f0f0f0;
        background-color: #1E1E1E;
    }
    .stApp {
        background-color: #1E1E1E; /* Garante que o fundo do app também seja dark */
    }
    .title-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        margin-bottom: 20px;
    }
    .title {
        color: #8EF9F3;
        font-size: 2.5em;
        margin-bottom: 5px;
    }
    .subtitle {
        color: #FAFAFA;
        font-size: 1em;
        opacity: 0.8;
    }
    .stChatMessage {
        background-color: #333333;
        color: #FAFAFA;
        border-radius: 8px;
        padding: 10px 15px;
        margin-bottom: 10px;
        border: 1px solid #555555;
    }
    .stChatMessage.user {
        background-color: #4CAF50;
        color: #FAFAFA;
    }
    .stChatMessage.assistant {
        background-color: #2196F3;
        color: #FAFAFA;
    }
    .stChatInputContainer {
        background-color: #333333 !important;
        border-top: 1px solid #555555 !important;
        padding: 10px;
        border-radius: 0;
    }
    .stChatInputContainer textarea {
        color: #FAFAFA !important;
    }
    .stChatInputContainer button {
        background-color: #8EF9F3;
        color: #1E1E1E;
        border: none;
        border-radius: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Título e Subtítulo Centralizados
st.markdown("<div class='title-container'><h1 class='title'>🤖 AuxilIA</h1><p class='subtitle'>Seu dia com eficiência e uma pitada de inteligência.</p></div>", unsafe_allow_html=True)

# Inicializa o estado da sessão para armazenar o histórico do chat
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Olá! Como posso ajudar seu empreendimento hoje?"}]

# Exibe as mensagens do chat
for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Campo de entrada para o usuário digitar a mensagem
prompt = st.chat_input("Digite sua pergunta aqui...")

# Processa a entrada do usuário
if prompt:
    # Adiciona a mensagem do usuário ao histórico do chat
    st.session_state["messages"].append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Simula a resposta do assistente (seu agente)
    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            full_response = sistema.executar_consulta(prompt)
            time.sleep(1)  # Simula um tempo de resposta
        st.markdown(full_response)

    # Adiciona a resposta do assistente ao histórico do chat
    st.session_state["messages"].append({"role": "assistant", "content": full_response})