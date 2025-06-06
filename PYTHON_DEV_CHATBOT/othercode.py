import streamlit as st
from openai import OpenAI

# Inicializar a API do OpenAI com sua chave de API
api_key = "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"
modelo = OpenAI(api_key=api_key)

# Escrever um título usando markdown no app Streamlit
st.write("### ChatBot do Ayrton")

def initialize_session_state():
    """
    Inicializa o estado de sessão. Verifica se a lista de mensagens já existe
    no estado de sessão do Streamlit. Se não existir, inicia uma lista vazia.
    Isso preserva o histórico de mensagens entre interações com o usuário.
    """
    if "lista_mensagens" not in st.session_state:
        st.session_state["lista_mensagens"] = []

def append_message(role, content):
    """
    Adiciona uma mensagem à lista de mensagens na sessão.
    - role: Indica quem está enviando a mensagem ('user' ou 'assistant')
    - content: O conteúdo da mensagem enviada
    """
    mensagem = {"role": role, "content": content}
    st.session_state["lista_mensagens"].append(mensagem)

def render_chat():
    """
    Renderiza o histórico de chat na interface do Streamlit.
    Itera sobre todas as mensagens armazenadas na sessão e as exibe.
    """
    for message in st.session_state["lista_mensagens"]:
        st.chat_message(message["role"]).write(message["content"])

# Inicializamos o estado da sessão
initialize_session_state()

# Captura a entrada do usuário pelo chat input do Streamlit
mensagem_usuario = st.chat_input("Escreva sua mensagem aqui")

if mensagem_usuario:
    # Adiciona a mensagem do usuário ao histórico
    append_message("user", mensagem_usuario)

    # Faz uma solicitação à API OpenAI para obter uma resposta
    resposta_modelo = modelo.chat.completions.create(
        messages=st.session_state["lista_mensagens"],
        model="gpt-3.5-turbo"
    )

    # Verifica se há escolhas na resposta e extrai o conteúdo
    if resposta_modelo.choices:
        resposta_ia = resposta_modelo.choices[0].message.content

        # Adiciona a resposta da IA ao histórico
        append_message("assistant", resposta_ia)

# Renderiza o chat após processamento das mensagens
render_chat()