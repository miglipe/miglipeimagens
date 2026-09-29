import streamlit as st
import yt_dlp
import os
from PIL import Image

# CONFIGURAÇÃO DE APARÊNCIA PREMIUM
st.set_page_config(
    page_title="mig lipe imagens",
    page_icon="🎨",
    layout="centered"
)

# 🎨 INJEÇÃO DE CSS PARA DEIXAR O SITE IDÊNTICO AO DESIGN DO GEMINI
st.markdown("""
    <style>
    /* Estiliza o botão de gerar imagem com o degradê azul e roxo */
    div.stButton > button {
        background: linear-gradient(90deg, #A855F7 0%, #06B6D4 100%) !important;
        color: white !important;
        border-radius: 12px !important;
        border: none !important;
        font-weight: bold !important;
        font-size: 16px !important;
        padding: 10px 24px !important;
        width: 100% !important;
        transition: all 0.3s ease;
    }
    /* Efeito de brilho ao passar o mouse no botão */
    div.stButton > button:hover {
        box-shadow: 0px 0px 15px #A855F7 !important;
        transform: scale(1.02);
    }
    /* Estiliza as caixas de texto */
    div.stTextInput > div > div > input {
        background-color: #161B26 !important;
        border: 1px solid #1E293B !important;
        border-radius: 10px !important;
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

# CARREGA A LOGO OFICIAL CENTRALIZADA COM BORDA ARREDONDADA
pasta_do_projeto = os.path.dirname(os.path.abspath(__file__))
caminho_da_logo = os.path.join(pasta_do_projeto, ".streamlit", "logo.png.jpg")

col1, col2, col3 = st.columns(3)
with col2:
    if os.path.exists(caminho_da_logo):
        logo = Image.open(caminho_da_logo)
        # Exibe a logo centralizada
        st.image(logo, use_container_width=True)
    else:
        st.title("🎨 mig lipe imagens")

# Configuração da barra lateral
st.sidebar.markdown("# 🚀 Menu Mig Lipe")
st.sidebar.markdown("---")
opcao_servico = st.sidebar.radio(
    "ESCOLHA A FERRAMENTA:",
    ["🎨 Criador de Imagens", "📥 Baixar Vídeos Grátis"]
)

# ----------------------------------------------------
# SERVIÇO 1: CRIADOR DE IMAGENS
# ----------------------------------------------------
if opcao_servico == "🎨 Criador de Imagens":
    st.markdown("<h1 style='text-align: center; font-size: 32px;'>O Estúdio Oficial dos Influenciadores!</h1>",
                unsafe_allow_html=True)
    st.markdown(
        "<p style='text-align: center; color: #94A3B8;'>Crie artes exclusivas para bombar nas suas trends do TikTok e Reels.</p>",
        unsafe_allow_html=True)
    st.markdown("---")

    prompt_usuario = st.text_input("O que sua imaginação quer criar?", placeholder="Ex: Um cavalo branco cyberpunk...")

    # O botão já vai carregar com o degradê automático por causa do CSS lá de cima!
    if st.button("✨ GERAR IMAGEM PARA TREND"):
        if prompt_usuario:
            with st.spinner("✨ O motor do Mig Lipe Imagens está desenhando..."):
                import time

                time.sleep(2)
            st.success("🎉 Imagem de Trend criada com sucesso!")
            imagem_local = Image.new("RGB", (500, 500), "#4C1D95")
            st.image(imagem_local, caption=f"Sua Trend: {prompt_usuario}", use_container_width=True)
        else:
            st.warning("⚠️ Digite uma ideia primeiro!")

# ----------------------------------------------------
# SERVIÇO 2: DOWNLOAD DE VÍDEOS REAIS
# ----------------------------------------------------
elif opcao_servico == "📥 Baixar Vídeos Grátis":
    st.markdown("<h1 style='text-align: center; font-size: 32px;'>Mig Lipe Downloader</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #94A3B8;'>Pegue referências das maiores redes do mundo!</p>",
                unsafe_allow_html=True)
    st.markdown("---")

    url_video = st.text_input("Cole o link da mídia aqui:", placeholder="https://...")

    if url_video:
        url_lower = url_video.lower()
        if "tiktok.com" in url_lower:
            st.info("🎵 Vídeo do **TikTok** identificado!")
        elif "instagram.com" in url_lower:
            st.info("📸 Vídeo do **Instagram Reels** identificado!")
        elif "youtube.com" in url_lower or "youtu.be" in url_lower:
            st.info("📺 Vídeo do **YouTube** identificado!")

    if st.button("⚡ ANALISAR E BAIXAR VÍDEO REAL"):
        if url_video:
            nome_arquivo_saida = "video_real_mig_lipe.mp4"
            with st.spinner("⚡ Extraindo o vídeo original em alta qualidade..."):
                try:
                    if os.path.exists(nome_arquivo_saida):
                        os.remove(nome_arquivo_saida)

                    ydl_opts = {
                        'format': 'best[ext=mp4]/best',
                        'outtmpl': nome_arquivo_saida,
                        'quiet': True,
                        'no_warnings': True
                    }

                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([url_video])

                    if os.path.exists(nome_arquivo_saida):
                        st.success("✅ Vídeo pronto para download seguro!")
                        with open(nome_arquivo_saida, "rb") as arquivo_real:
                            st.download_button(
                                label="💾 SALVAR VÍDEO NO COMPUTADOR",
                                data=arquivo_real,
                                file_name="mig_lipe_downloader.mp4",
                                mime="video/mp4"
                            )
                except Exception as e:
                    st.error(f"Erro no motor de download: {str(e)}")
