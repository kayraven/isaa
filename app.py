import streamlit as st

# --- 1. SAYFA AYARLARI ---
st.set_page_config(page_title="Para o Meu Amor ❤️", page_icon="💖", layout="centered")

# --- 2. GELİŞMİŞ CSS (SF PRO FONT VE BUTON DÜZELTMELERİ) ---
def inject_css(yes_size):
    st.markdown(f"""
        <style>
        /* SF Pro / Apple Font Ailesi */
        html, body, [class*="css"], h1, h2, h3, p, div {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif !important;
        }}

        /* Arka Plan */
        .stApp {{
            background: linear-gradient(135deg, #ffafbd 0%, #ffc3a0 100%);
            background-attachment: fixed;
        }}

        /* Tüm Butonlar İçin Metin Rengi Düzeltmesi (Beyaz Yazı) */
        button {{
            color: white !important;
            font-weight: bold !important;
        }}

        /* Dinamik Büyüyen SIM! Butonu */
        div[data-testid="column"]:nth-of-type(1) button {{
            font-size: {yes_size}px !important;
            height: auto !important;
            min-height: 80px !important; /* Başlangıçta bile büyük olması için */
            width: 100% !important;
            background-color: #ff4b6b !important;
            border-radius: 20px !important;
            border: none !important;
            box-shadow: 0 10px 20px rgba(0,0,0,0.15) !important;
        }}

        /* Küçük Não Butonu */
        div[data-testid="column"]:nth-of-type(2) button {{
            font-size: 16px !important;
            background-color: #333333 !important; /* Okunması için koyu gri/siyah arka plan */
            border-radius: 12px !important;
            margin-top: 20px !important;
            border: none !important;
        }}

        /* Giriş Sayfası Butonu (Verificar) */
        .stButton>button[kind="secondary"] {{
            background-color: #ff4b6b !important;
            width: 100% !important;
        }}

        /* Mektup Kutusu Tasarımı */
        .letter-box {{
            padding: 40px;
            background: rgba(255, 255, 255, 0.95);
            border-radius: 25px;
            border-left: 10px solid #ff4b6b;
            box-shadow: 0 15px 35px rgba(0,0,0,0.1);
            margin-bottom: 25px;
        }}
        
        .letter-text {{
            font-size: 18px !important;
            color: #333333 !important;
            line-height: 1.6;
        }}

        /* Başlıklar ve Metinler */
        h1, h2, h3 {{
            color: #e91e63 !important;
            text-align: center !important;
        }}
        
        p {{
            color: #4a4a4a !important;
        }}
        </style>
    """, unsafe_allow_html=True)

# --- 3. DURUM YÖNETİMİ ---
if 'step' not in st.session_state:
    st.session_state.step = 'quiz'
if 'yes_size' not in st.session_state:
    st.session_state.yes_size = 30 # Başlangıçta daha büyük bir buton için 30'dan başlattım

inject_css(st.session_state.yes_size)

# --- 4. UYGULAMA AKIŞI ---

# EKRAN 1: ŞARKI KİLİDİ
if st.session_state.step == 'quiz':
    st.markdown("<h1>🔐 Uma pequena surpresa...</h1>", unsafe_allow_html=True)
    st.write("<p style='text-align: center;'>Precisamos confirmar a chave do nosso coração antes de continuar.</p>", unsafe_allow_html=True)
    
    cevap = st.text_input("Qual é o nome da música do George Ezra que o Isa te enviou?", placeholder="Escreva aqui...")
    if st.button("Verificar ✨"):
        if cevap.lower().strip() == "budapest":
            st.session_state.step = 'proposal'
            st.balloons()
            st.rerun()
        else:
            st.error("Ops! Essa não é a música certa. Tente novamente! 🎵")

# EKRAN 2: ROMANTİK MEKTUP VE TEKLİF
elif st.session_state.step == 'proposal':
    st.markdown("<h1>Meu Amor, Minha Vida... 🌹</h1>", unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="letter-box">
        <h2 style="color: #ff4b6b; text-align: left !important; margin-top: 0;">Minha Linda, ✨</h2>
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
        <p align="right" class="letter-text" style="margin-top: 20px;"><i>Com todo o meu amor, <br>Seu Isa ❤️</i></p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<h3 style='margin-bottom: 20px;'>Você aceita ser minha Valentine? ❤️</h3>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        if st.button("SIM! 😍", key="yes_btn"):
            st.session_state.step = 'success'
            st.rerun()
            
    with col2:
        if st.button("Não ❌", key="no_btn"):
            st.session_state.yes_size += 50 # Her basışta SIM butonu agresifçe büyür
            st.rerun()

# EKRAN 3: KUTLAMA
elif st.session_state.step == 'success':
    st.snow()
    st.markdown("<h1>A melhor resposta do mundo! ❤️</h1>", unsafe_allow_html=True)
    
    st.image("https://media.tenor.com/gfAyB3I48wcAAAAj/snoopy-abrazo-love.gif", use_container_width=True)
    
    st.markdown("""
        <div style="text-align: center; background: rgba(255,255,255,0.9); padding: 30px; border-radius: 20px; margin-top: 20px;">
            <h2 style="color: #ff4b6b;">Eu sou o homem mais feliz do mundo!</h2>
            <p style="font-size: 18px; color: #333;">Te amo mais a cada segundo. <br><b>Feliz Dia dos Namorados!</b> 🌹</p>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("Ler a carta novamente 🔄"):
        st.session_state.step = 'proposal'
        st.session_state.yes_size = 30
        st.rerun()