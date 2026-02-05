import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Para o Meu Amor", page_icon="💖", layout="centered")

# --- GERENCIAMENTO DE ESTADO (SESSION STATE) ---
if 'step' not in st.session_state:
    st.session_state.step = 'quiz'
if 'size' not in st.session_state:
    st.session_state.size = 20

# --- TELA 1: O TESTE DA MÚSICA ---
if st.session_state.step == 'quiz':
    st.title("🔐 Uma entrada especial...")
    st.write("Antes de continuar, eu preciso que você lembre de um momento nosso...")
    
    # Pergunta sobre a música
    cevap = st.text_input("Qual é o nome da música do George Ezra que o Isa te enviou?", placeholder="Digite o nome da música aqui...")
    
    if st.button("Verificar ✨"):
        if cevap.lower().strip() == "budapest":
            st.session_state.step = 'offer'
            st.balloons()
            st.rerun()
        else:
            st.error("Hummm, essa não é a música, pookie. Tente de novo! 🎵")

# --- TELA 2: O PEDIDO (VALENTINE) ---
elif st.session_state.step == 'offer':
    st.title("Meu Amor, Minha Vida... 🌹")
    
    st.markdown("""
    ### A distância é apenas um número...
    
    Mesmo com os quilômetros entre nós e o Brasil, meu coração bate no seu ritmo. 
    Você é a minha melhor história e cada momento com você, mesmo de longe, é especial.
    
    **Tenho uma pergunta muito importante para você:**
    """)
    
    st.subheader("Você aceita ser minha Valentine? ❤️")
    
    # Colunas para os botões
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # O botão SIM cresce conforme ela tenta clicar no NÃO
        if st.button("SIM! 😍", key="yes", use_container_width=True, type="primary"):
            st.session_state.step = 'success'
            st.rerun()
            
    with col2:
        if st.button("Não ❌", key="no"):
            st.session_state.size += 40  # O botão SIM fica gigante
            st.rerun()
    
    # CSS para fazer o botão SIM crescer dinamicamente
    st.markdown(f"""
        <style>
        div[data-testid="column"]:nth-of-type(1) button {{
            font-size: {st.session_state.size}px !important;
            height: auto !important;
            transition: all 0.3s ease;
        }}
        </style>
    """, unsafe_allow_html=True)

# --- TELA 3: CELEBRAÇÃO FINAL ---
elif st.session_state.step == 'success':
    st.snow() # Efeito de neve/gelo (ou use st.balloons() se preferir)
    st.title("Eu te amo muito! ❤️")
    st.header("Feliz Dia dos Namorados, meu amor!")
    
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJpZzR4ZzR4ZzR4ZzR4ZzR4ZzR4ZzR4ZzR4ZzR4ZzR4JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZ25vcmUmY3Q9Zw/l4pTdcifPKUYMlWg0/giphy.gif")
    
    st.write("Você me faz a pessoa mais feliz do mundo. Mal posso esperar pelo nosso próximo momento juntos!")
    
    if st.button("Recomeçar 🔄"):
        st.session_state.step = 'quiz'
        st.session_state.size = 20
        st.rerun()