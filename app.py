import streamlit as st

# --- 1. SAYFA AYARLARI VE FONT KURULUMU ---
st.set_page_config(page_title="Para o Meu Amor ❤️", page_icon="💖", layout="centered")

# --- 2. GELİŞMİŞ GÖRSEL TASARIM (CSS) ---
def inject_css(yes_size):
    st.markdown(f"""
        <style>
        /* Google Fonts'tan romantik bir font çekiyoruz */
        @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@600&family=Poppins:wght@300;400&display=swap');

        /* Genel Yazı Tipleri */
        html, body, [class*="css"] {{
            font-family: 'Poppins', sans-serif;
        }}
        
        h1, h2, h3, .letter-text {{
            font-family: 'Dancing Script', cursive !important;
        }}

        /* Arka Plan: Yumuşak Gradyan Geçişi */
        .stApp {{
            background: linear-gradient(135deg, #ffafbd 0%, #ffc3a0 100%);
            background-attachment: fixed;
        }}

        /* Streamlit Arayüz Elemanlarını Gizleme */
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
        }}

        /* "Não" Butonu */
        div[data-testid="column"]:nth-of-type(2) button {{
            font-size: 16px !important;
            background-color: rgba(255, 255, 255, 0.7) !important;
            color: #31333F !important;
            border-radius: 15px !important;
            margin-top: 10px;
            border: 1px solid #ddd !important;
        }}

        /* Romantik Mektup Kutusu (Glassmorphism Efekti) */
        .letter-box {{
            padding: 40px;
            background: rgba(255, 255, 255, 0.85);
            border-radius: 30px;
            border-left: 10px solid #ff4b6b;
            box-shadow: 0 15px 35px rgba(0,0,0,0.1);
            margin-bottom: 30px;
            backdrop-filter: blur(10px);
        }}
        
        .letter-text {{
            font-size: 24px !important;
            color: #4a4a4a;
            line-height: 1.4;
        }}
        </style>
    """, unsafe_allow_html=True)

# --- 3. DURUM YÖNETİMİ (STATE MACHINE) ---
if 'step' not in st.session_state:
    st.session_state.step = 'quiz'
if 'yes_size' not in st.session_state:
    st.session_state.yes_size = 20

inject_css(st.session_state.yes_size)

# --- 4. UYGULAMA AKIŞI ---

# --- EKRAN 1: ŞARKI KİLİDİ ---
if st.session_state.step == 'quiz':
    st.markdown("<h1 style='text-align: center; color: white;'>🔐 Uma pequena surpresa...</h1>", unsafe_allow_html=True)
    st.write("<p style='text-align: center; color: white;'>Devam etmeden önce kalbimizin anahtarını doğrulamam gerek.</p>", unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div style="background: white; padding: 20px; border-radius: 20px;">', unsafe_allow_html=True)
        cevap = st.text_input("Qual é o nome da música do George Ezra que o Isa te enviou?", placeholder="A música que me faz lembrar você...")
        if st.button("Verificar ✨", use_container_width=True):
            if cevap.lower().strip() == "budapest":
                st.session_state.step = 'proposal'
                st.balloons()
                st.rerun()
            else:
                st.error("Ops! Essa não é a música. Tente novamente, pookie! 🎵")
        st.markdown('</div>', unsafe_allow_html=True)

# --- EKRAN 2: ROMANTİK MEKTUP VE ETKİLEŞİMLİ TEKLİF ---
elif st.session_state.step == 'proposal':
    st.markdown("<h1 style='text-align: center; color: #ff4b6b;'>Meu Amor, Minha Vida... 🌹</h1>", unsafe_allow_html=True)
    
    # Romantik Mektup
    st.markdown(f"""
    <div class="letter-box">
        <h2 style="color: #ff4b6b;">Minha Linda, ✨</h2>
        <p class="letter-text">
        Binlerce kilometre ötede olman, her sabah senin gülüşünle uyanmama engel değil. 
        Türkiye ve Brezilya arasındaki o devasa okyanus, kalplerimiz arasındaki köprünün yanında küçücük kalıyor. 
        Seninle konuşmak, sesini duymak ve o güzel Portekizceni dinlemek benim günümün en değerli anı.
        </p>
        <p class="letter-text">
        <i>Budapest</i> her çaldığında, kendimi senin yanında, elini tutarken hayal ediyorum. 
        Sana olan sevgim mesafelerle ölçülemez. Sen sadece sevgilim değil, 
        aynı zamanda benim en büyük ilham kaynağımsın.
        </p>
        <p class="letter-text">
        <b>Prometo estar sempre ao seu lado, cuidando de você e do nosso amor.</b> 
        Bu Sevgililer Günü'nde yan yana olamasak da, ruhumun seninle olduğunu bilmeni istiyorum.
        </p>
        <p align="right" class="letter-text"><i>Com todo o meu amor, <br>Seu Isa ❤️</i></p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<h3 style='text-align: center;'>Agora, eu tenho uma pergunta importante...</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 22px;'>Você aceita ser minha Valentine? ❤️</p>", unsafe_allow_html=True)
    
    # Etkileşimli Butonlar
    col1, col2 = st.columns([2, 1])
    
    with col1:
        if st.button("SIM! 😍", key="yes_btn"):
            st.session_state.step = 'success'
            st.rerun()
            
    with col2:
        if st.button("Não ❌", key="no_btn"):
            # Hayır butonu her tıklandığında Evet butonu büyür
            st.session_state.yes_size += 45 
            st.rerun()

# --- EKRAN 3: KUTLAMA VE SNOOPY SARILMASI ---
elif st.session_state.step == 'success':
    st.snow()
    st.markdown("<h1 style='text-align: center; color: #ff4b6b;'>A melhor resposta do mundo! ❤️</h1>", unsafe_allow_html=True)
    
    # YENİ SNOOPY ABRAZO GIF
    st.image("https://media.tenor.com/gfAyB3I48wcAAAAj/snoopy-abrazo-love.gif", use_container_width=True)
    
    st.markdown("""
        <div style="text-align: center; background: white; padding: 20px; border-radius: 20px; box-shadow: 0 10px 20px rgba(0,0,0,0.05);">
            <h2 style="color: #ff4b6b;">Eu sou o homem mais feliz do mundo!</h2>
            <p style="font-size: 20px;">Her saniye seni daha çok seviyorum. <br><b>Feliz Dia dos Namorados!</b> 🌹</p>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("Ler a carta novamente 🔄", use_container_width=True):
        st.session_state.step = 'proposal'
        st.session_state.yes_size = 20
        st.rerun()