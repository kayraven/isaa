import streamlit as st

# --- 1. SAYFA AYARLARI ---
st.set_page_config(page_title="Para o Meu Amor ❤️", page_icon="💖", layout="centered")

# --- 2. YENİ CSS: APPLE FONTU VE RENK DÜZELTMELERİ ---
def inject_css(yes_size):
    st.markdown(f"""
        <style>
        /* Apple Font Ailesi (SF Pro) */
        html, body, [class*="css"], h1, h2, h3, p, div {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol" !important;
            color: #333333; /* Varsayılan metin rengini koyu gri yap */
        }}

        /* Arka Plan: Yumuşak Gradyan */
        .stApp {{
            background: linear-gradient(135deg, #ffafbd 0%, #ffc3a0 100%);
            background-attachment: fixed;
        }}

        /* Başlıkların Rengi (Daha belirgin bir pembe) */
        h1, h2, h3 {{
            color: #e91e63 !important;
            font-weight: 600 !important;
        }}

        /* Streamlit Arayüzünü Gizle */
        #MainMenu {{visibility: hidden;}}
        footer {{visibility: hidden;}}
        header {{visibility: hidden;}}

        /* Dinamik Büyüyen "SIM!" Butonu */
        div[data-testid="column"]:nth-of-type(1) button {{
            font-size: {yes_size}px !important;
            height: auto !important;
            width: 100% !important;
            background-color: #ff4b6b !important;
            color: white !important;
            border-radius: 25px !important;
            border: none !important;
            transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            box-shadow: 0 10px 20px rgba(255, 75, 107, 0.4);
            font-weight: bold !important;
        }}

        /* "Não" Butonu */
        div[data-testid="column"]:nth-of-type(2) button {{
            font-size: 16px !important;
            background-color: rgba(255, 255, 255, 0.8) !important;
            color: #333333 !important;
            border-radius: 15px !important;
            margin-top: 10px;
            border: 1px solid #ccc !important;
            font-weight: 500 !important;
        }}

        /* Romantik Mektup Kutusu (Daha Okunaklı) */
        .letter-box {{
            padding: 40px;
            background: rgba(255, 255, 255, 0.95); /* Daha opak beyaz */
            border-radius: 30px;
            border-left: 10px solid #ff4b6b;
            box-shadow: 0 15px 35px rgba(0,0,0,0.1);
            margin-bottom: 30px;
        }}
        
        .letter-text {{
            font-size: 18px !important;
            color: #333333 !important; /* Koyu renk metin */
            line-height: 1.6;
        }}

        /* Giriş Kutusu Stili */
        .stTextInput input {{
            border-radius: 15px;
            border: 2px solid #ff4b6b;
            padding: 10px;
        }}
        </style>
    """, unsafe_allow_html=True)

# --- 3. DURUM YÖNETİMİ ---
if 'step' not in st.session_state:
    st.session_state.step = 'quiz'
if 'yes_size' not in st.session_state:
    st.session_state.yes_size = 20

inject_css(st.session_state.yes_size)

# --- 4. UYGULAMA AKIŞI (TAMAMEN PORTEKİZCE) ---

# --- EKRAN 1: ŞARKI KİLİDİ ---
if st.session_state.step == 'quiz':
    st.markdown("<h1 style='text-align: center;'>🔐 Uma pequena surpresa...</h1>", unsafe_allow_html=True)
    # Türkçe metin Portekizceye çevrildi ve renk sorunu çözüldü
    st.write("<p style='text-align: center; font-size: 18px;'>Precisamos confirmar a chave do nosso coração antes de continuar.</p>", unsafe_allow_html=True)
    
    # Gereksiz st.container ve beyaz kutu kaldırıldı.
    cevap = st.text_input("Qual é o nome da música do George Ezra que o Isa te enviou?", placeholder="A música que nos une...")
    if st.button("Verificar ✨", use_container_width=True):
        if cevap.lower().strip() == "budapest":
            st.session_state.step = 'proposal'
            st.balloons()
            st.rerun()
        else:
            st.error("Ops! Essa não é a música. Tente novamente, meu amor! 🎵")

# --- EKRAN 2: ROMANTİK MEKTUP VE TEKLİF ---
elif st.session_state.step == 'proposal':
    st.markdown("<h1 style='text-align: center;'>Meu Amor, Minha Vida... 🌹</h1>", unsafe_allow_html=True)
    
    # Mektup Metni (Okunaklı Font ve Renk)
    st.markdown(f"""
    <div class="letter-box">
        <h2 style="color: #ff4b6b; margin-top: 0;">Minha Linda, ✨</h2>
        <p class="letter-text">
        Mesmo a milhares de quilômetros de distância, acordar com o seu sorriso em meus pensamentos é o melhor começo de dia. 
        O oceano gigante entre o Brasil e a Turquia parece pequeno perto da conexão dos nossos corações. 
        Falar com você, ouvir sua voz e esse seu sotaque lindo em português é o momento mais precioso do meu dia.
        </p>
        <p class="letter-text">
        Sempre que <i>Budapest</i> toca, eu me imagino ao seu lado, segurando sua mão. 
        O meu amor por você não se mede em distância; ele cresce com cada risada que compartilhamos, 
        com cada apoio que damos um ao outro. Você não é apenas minha namorada, 
        você é minha maior inspiração.
        </p>
        <p class="letter-text">
        <b>Prometo estar sempre ao seu lado, cuidando de você e do nosso amor.</b> 
        Mesmo não estando juntos fisicamente neste Dia dos Namorados, quero que saiba que minha alma está com você.
        </p>
        <p align="right" class="letter-text" style="margin-top: 20px;"><i>Com todo o meu amor, <br>Seu Isa ❤️</i></p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<h3 style='text-align: center;'>Agora, eu tenho uma pergunta que vem do fundo do meu coração...</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 22px; font-weight: bold;'>Você aceita ser minha Valentine? ❤️</p>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        if st.button("SIM! 😍", key="yes_btn"):
            st.session_state.step = 'success'
            st.rerun()
            
    with col2:
        if st.button("Não ❌", key="no_btn"):
            st.session_state.yes_size += 45 
            st.rerun()

# --- EKRAN 3: KUTLAMA VE SNOOPY SARILMASI ---
elif st.session_state.step == 'success':
    st.snow()
    st.markdown("<h1 style='text-align: center;'>A melhor resposta do mundo! ❤️</h1>", unsafe_allow_html=True)
    
    # Snoopy Abrazo GIF
    st.image("https://media.tenor.com/gfAyB3I48wcAAAAj/snoopy-abrazo-love.gif", use_container_width=True)
    
    # Kutlama Mesajı (Okunaklı Font ve Renk)
    st.markdown("""
        <div style="text-align: center; background: rgba(255,255,255,0.9); padding: 30px; border-radius: 20px; box-shadow: 0 10px 20px rgba(0,0,0,0.1); margin-top: 20px;">
            <h2 style="color: #ff4b6b; margin: 0;">Eu sou o homem mais feliz do mundo!</h2>
            <p style="font-size: 20px; color: #333; margin-top: 15px;">Te amo mais a cada segundo. <br><b>Feliz Dia dos Namorados!</b> 🌹</p>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("Ler a carta novamente 🔄", use_container_width=True):
        st.session_state.step = 'proposal'
        st.session_state.yes_size = 20
        st.rerun()