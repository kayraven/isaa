import streamlit as st

# --- 1. CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Para o Meu Amor ❤️", page_icon="💖", layout="centered")

# --- 2. CSS MASTER (SF PRO & BOTÕES GIGANTES) ---
def inject_css(yes_size):
    st.markdown(f"""
        <style>
        /* Apple SF Pro Font Ailesi */
        html, body, [class*="css"], h1, h2, h3, p, div {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif !important;
        }}

        /* Background Gradient */
        .stApp {{
            background: linear-gradient(135deg, #ffafbd 0%, #ffc3a0 100%);
            background-attachment: fixed;
        }}

        /* BOTÃO TEXTO BRANCO (CRÍTICO) */
        button p {{
            color: white !important;
            font-weight: bold !important;
        }}

        /* TELA 1 E 3: BOTÕES ÚNICOS E ESCUROS */
        .stButton > button {{
            background-color: #1e1e1e !important;
            color: white !important;
            border-radius: 12px !important;
            border: none !important;
            width: 100% !important;
            height: 55px !important;
        }}

        /* TELA DE PEDIDO (ORANTISIZ BUTONLAR) */
        /* Botão SIM! Gigante */
        div[data-testid="column"]:nth-of-type(1) button {{
            background-color: #ff4b6b !important;
            font-size: {yes_size}px !important;
            min-height: 100px !important;
            box-shadow: 0 10px 20px rgba(0,0,0,0.1) !important;
        }}
        
        div[data-testid="column"]:nth-of-type(1) button p {{
            font-size: {yes_size}px !important;
        }}

        /* Botão Não Pequeno */
        div[data-testid="column"]:nth-of-type(2) button {{
            background-color: #333333 !important;
            font-size: 16px !important;
            min-height: 45px !important;
            margin-top: 35px !important;
            opacity: 0.8;
        }}

        /* Caixa da Carta (Alta Opacidade) */
        .letter-box {{
            padding: 40px;
            background: rgba(255, 255, 255, 0.98);
            border-radius: 25px;
            border-left: 10px solid #ff4b6b;
            box-shadow: 0 15px 35px rgba(0,0,0,0.1);
            margin-bottom: 25px;
        }}

        .letter-text {{
            font-size: 19px !important;
            color: #222222 !important;
            line-height: 1.6;
            text-align: left;
        }}

        h1, h3 {{
            color: #d63384 !important;
            text-align: center !important;
            font-weight: 800 !important;
        }}
        </style>
    """, unsafe_allow_html=True)

# --- 3. GESTÃO DE ESTADO (3 PERGUNTAS) ---
if 'step' not in st.session_state:
    st.session_state.step = 'quiz1'
if 'yes_size' not in st.session_state:
    st.session_state.yes_size = 40

inject_css(st.session_state.yes_size)

# --- 4. FLUXO DO APLICATIVO ---

# PERGUNTA 1: MÚSICA
if st.session_state.step == 'quiz1':
    st.markdown("<h1>🔐 Pergunta 1 de 3</h1>", unsafe_allow_html=True)
    st.write("<p style='text-align: center; font-size: 18px; color: #333;'>Vamos começar com a nossa música...</p>", unsafe_allow_html=True)
    cevap1 = st.text_input("Qual é o nome da música do George Ezra que o Kayra te enviou?", placeholder="A música que nos une...")
    if st.button("Continuar ✨", key="btn1"):
        if cevap1.lower().strip() == "budapest":
            st.session_state.step = 'quiz2'
            st.rerun()
        else:
            st.error("Ops! Tente novamente, meu amor! 🎵")

# PERGUNTA 2: COMIDA FAVORITA
elif st.session_state.step == 'quiz2':
    st.markdown("<h1>🔐 Pergunta 2 de 3</h1>", unsafe_allow_html=True)
    st.write("<p style='text-align: center; font-size: 18px; color: #333;'>Essa é fácil! Uma sobre o meu gosto...</p>", unsafe_allow_html=True)
    cevap2 = st.text_input("Qual é a primeira letra da comida favorita do Kayra?", placeholder="Apenas uma letra...")
    if st.button("Continuar ✨", key="btn2"):
        if cevap2.lower().strip() == "m":
            st.session_state.step = 'quiz3'
            st.rerun()
        else:
            st.error("Hummm, não é essa letra. Tente de novo! 🍕")

# PERGUNTA 3: QUEM É VOCÊ?
elif st.session_state.step == 'quiz3':
    st.markdown("<h1>🔐 Pergunta 3 de 3</h1>", unsafe_allow_html=True)
    st.write("<p style='text-align: center; font-size: 18px; color: #333;'>A última para abrir o seu presente!</p>", unsafe_allow_html=True)
    cevap3 = st.text_input("Quem é você?", placeholder="Dica: começa con 'p' e termina com 'ookie'")
    if st.button("Abrir meu presente ❤️", key="btn3"):
        if cevap3.lower().strip() == "pookie":
            st.session_state.step = 'proposal'
            st.balloons()
            st.rerun()
        else:
            st.error("Como você não sabe quem você é?! rsrs Tente de novo! 🥰")

# TELA DE PEDIDO (MEKTUP VE ORANTISIZ BUTONLAR)
elif st.session_state.step == 'proposal':
    st.markdown("<h1>Meu Amor, Minha Vida... 🌹</h1>", unsafe_allow_html=True)
    st.markdown(f"""
    <div class="letter-box">
        <h2 style="color: #ff4b6b; margin-top: 0;">Minha Linda, ✨</h2>
        <p class="letter-text">
        Mesmo a milhares de quilômetros de distância, acordar com o seu sorriso em meus pensamentos é o melhor começo de dia. 
        O oceano gigante entre o Brasil e a Turquia parece pequeno perto da conexão dos nossos corações. 
        Falar com você e ouvir sua voz é o momento mais precioso do meu dia.
        </p>
        <p class="letter-text">
        Sempre que <i>Budapest</i> toca, eu me imagino ao seu lado, segurando sua mão. 
        O meu amor por você não se mede em distância; ele cresce a cada dia. Você não é apenas minha namorada, você é minha maior inspiração.
        </p>
        <p class="letter-text">
        <b>Prometo estar sempre ao seu lado, cuidando de você e do nosso amor.</b>
        </p>
        <p align="right" class="letter-text" style="margin-top: 20px;"><i>Com todo o meu amor, <br>Seu Baby, Kay ❤️</i></p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<h3>Você aceita ser minha Valentine? ❤️</h3>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    with col1:
        if st.button("SIM! 😍", key="yes_btn"):
            st.session_state.step = 'success'
            st.rerun()
    with col2:
        if st.button("Não ❌", key="no_btn"):
            st.session_state.yes_size += 55
            st.rerun()

# TELA DE SUCESSO (CELEBRAÇÃO)
elif st.session_state.step == 'success':
    st.snow()
    st.markdown("<h1>A melhor resposta do mundo! ❤️</h1>", unsafe_allow_html=True)
    st.image("https://media.tenor.com/gfAyB3I48wcAAAAj/snoopy-abrazo-love.gif", use_container_width=True)
    st.markdown("""
        <div style="text-align: center; background: rgba(255,255,255,0.95); padding: 30px; border-radius: 20px; margin-top: 20px;">
            <h2 style="color: #ff4b6b;">Eu sou o homem mais feliz do mundo!</h2>
            <p style="font-size: 20px; color: #333;">Te amo mais a cada segundo. <br><b>Feliz Dia dos Namorados!</b> 🌹</p>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("Ler a carta novamente 🔄", key="reset_btn"):
        st.session_state.step = 'proposal'
        st.session_state.yes_size = 40
        st.rerun()