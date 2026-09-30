
import streamlit as st
import yt_dlp
import os
import tempfile
import uuid
from PIL import Image

def obter_caminho_cookies():
    if "YOUTUBE_COOKIES" in st.secrets:
        with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".txt") as f:
            f.write(st.secrets["YOUTUBE_COOKIES"])
            return f.name
    return None

# ============================================================
# CONFIGURAÇÃO
# ============================================================

st.set_page_config(
    page_title="Guelpe Downloader",
    page_icon="⬇️",
    layout="centered",
    initial_sidebar_state="expanded"
)


# ============================================================
# CSS
# ============================================================

st.markdown("""
<style>

    .stApp {
        background:
            radial-gradient(
                circle at 50% 0%,
                rgba(124, 58, 237, 0.14),
                transparent 38%
            ),
            #070A12;
        color: #FFFFFF;
    }

    .main .block-container {
        max-width: 850px;
        padding-top: 3rem;
        padding-bottom: 4rem;
    }

    /* SIDEBAR */

    section[data-testid="stSidebar"] {
        background:
            linear-gradient(
                180deg,
                #0B0F1A 0%,
                #080B13 100%
            );
        border-right: 1px solid rgba(148, 163, 184, 0.10);
    }

    section[data-testid="stSidebar"] h1 {
        color: #FFFFFF;
        font-size: 24px;
        font-weight: 800;
    }

    section[data-testid="stSidebar"] hr {
        border-color: rgba(148, 163, 184, 0.12);
    }

    section[data-testid="stSidebar"] label {
        color: #94A3B8 !important;
        font-size: 12px !important;
        font-weight: 700 !important;
    }


    /* LOGO */

    .guelpe-logo {
        text-align: center;
        margin-bottom: 15px;
    }

    .guelpe-icon {
        width: 82px;
        height: 82px;
        margin: 0 auto 20px auto;

        display: flex;
        align-items: center;
        justify-content: center;

        border-radius: 24px;

        background:
            linear-gradient(
                135deg,
                rgba(168, 85, 247, 0.20),
                rgba(6, 182, 212, 0.16)
            );

        border: 1px solid rgba(168, 85, 247, 0.35);

        box-shadow:
            0 0 40px rgba(168, 85, 247, 0.14),
            inset 0 0 25px rgba(6, 182, 212, 0.05);

        font-size: 38px;
    }

    .guelpe-title {
        font-size: 48px;
        line-height: 1;
        font-weight: 900;
        letter-spacing: -2px;

        background:
            linear-gradient(
                90deg,
                #C084FC,
                #818CF8,
                #22D3EE
            );

        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    .guelpe-subtitle {
        margin-top: 8px;

        color: #64748B;

        font-size: 14px;
        font-weight: 700;

        letter-spacing: 4px;
        text-transform: uppercase;
    }


    /* HERO */

    .hero-title {
        text-align: center;

        margin-top: 45px;
        margin-bottom: 8px;

        font-size: 32px;
        font-weight: 800;

        color: #F8FAFC;
    }

    .hero-description {
        text-align: center;

        color: #94A3B8;

        font-size: 15px;

        margin-bottom: 30px;
    }


    /* INPUT */

    div[data-testid="stTextInput"] label {
        color: #CBD5E1 !important;
        font-weight: 700 !important;
        font-size: 14px !important;
    }

    div[data-testid="stTextInput"] input {
        background-color: #0E1420 !important;

        color: #FFFFFF !important;

        border: 1px solid #1E293B !important;

        border-radius: 14px !important;

        padding: 15px !important;

        font-size: 15px !important;

        transition: all 0.25s ease;
    }

    div[data-testid="stTextInput"] input:focus {
        border-color: #8B5CF6 !important;

        box-shadow:
            0 0 0 1px #8B5CF6,
            0 0 25px rgba(139, 92, 246, 0.12) !important;
    }


    /* BOTÕES */

    div.stButton > button {
        width: 100%;

        min-height: 48px;

        border: none !important;

        border-radius: 13px !important;

        background:
            linear-gradient(
                90deg,
                #8B5CF6,
                #6366F1,
                #06B6D4
            ) !important;

        color: white !important;

        font-size: 14px !important;

        font-weight: 800 !important;

        letter-spacing: 0.5px;

        box-shadow:
            0 8px 25px rgba(99, 102, 241, 0.15);

        transition: all 0.25s ease;
    }

    div.stButton > button:hover {
        transform: translateY(-2px);

        box-shadow:
            0 12px 35px rgba(139, 92, 246, 0.28);
    }


    /* DOWNLOAD */

    div[data-testid="stDownloadButton"] > button {
        width: 100% !important;

        min-height: 50px !important;

        border-radius: 13px !important;

        border: 1px solid rgba(34, 211, 238, 0.35) !important;

        background:
            linear-gradient(
                90deg,
                rgba(6, 182, 212, 0.16),
                rgba(99, 102, 241, 0.16)
            ) !important;

        color: #67E8F9 !important;

        font-weight: 800 !important;

        transition: all 0.25s ease;
    }

    div[data-testid="stDownloadButton"] > button:hover {
        border-color: #22D3EE !important;

        box-shadow:
            0 0 25px rgba(34, 211, 238, 0.15);
    }


    /* CARDS */

    .guelpe-card {
        margin-top: 25px;

        padding: 22px;

        border-radius: 18px;

        background:
            linear-gradient(
                145deg,
                rgba(15, 23, 42, 0.90),
                rgba(10, 15, 27, 0.95)
            );

        border: 1px solid rgba(148, 163, 184, 0.10);

        box-shadow:
            0 15px 45px rgba(0, 0, 0, 0.20);
    }

    .success-card {
        margin-top: 25px;

        padding: 22px;

        border-radius: 18px;

        background:
            linear-gradient(
                145deg,
                rgba(16, 185, 129, 0.08),
                rgba(15, 23, 42, 0.95)
            );

        border: 1px solid rgba(16, 185, 129, 0.22);
    }

    .card-title {
        color: #F8FAFC;

        font-size: 17px;

        font-weight: 800;

        margin-bottom: 6px;
    }

    .card-text {
        color: #94A3B8;

        font-size: 14px;

        line-height: 1.6;
    }


    /* PLATAFORMA */

    .platform-badge {
        display: inline-block;

        margin-top: 8px;

        padding: 7px 12px;

        border-radius: 999px;

        background: rgba(139, 92, 246, 0.10);

        border: 1px solid rgba(139, 92, 246, 0.20);

        color: #C4B5FD;

        font-size: 12px;

        font-weight: 800;
    }


    /* TITULO DO VIDEO */

    .video-title {
        color: #F8FAFC;

        font-size: 18px;

        font-weight: 800;

        margin-top: 15px;

        margin-bottom: 8px;

        line-height: 1.4;
    }


    /* INFO */

    .video-info {
        color: #94A3B8;

        font-size: 13px;

        margin-top: 5px;
    }


    /* DIVISOR */

    .guelpe-divider {
        height: 1px;

        margin: 30px 0;

        background:
            linear-gradient(
                90deg,
                transparent,
                rgba(148, 163, 184, 0.15),
                transparent
            );
    }


    /* FOOTER */

    .guelpe-footer {
        margin-top: 70px;

        text-align: center;

        color: #475569;

        font-size: 12px;

        line-height: 1.7;
    }


    /* MOBILE */

    @media (max-width: 600px) {

        .main .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
            padding-top: 2rem;
        }

        .guelpe-title {
            font-size: 38px;
        }

        .guelpe-subtitle {
            font-size: 10px;
            letter-spacing: 3px;
        }

        .hero-title {
            font-size: 26px;
        }

        .hero-description {
            font-size: 14px;
        }

    }

</style>
""", unsafe_allow_html=True)


# ============================================================
# LOGO
# ============================================================

pasta_do_projeto = os.path.dirname(os.path.abspath(__file__))

caminho_da_logo = os.path.join(
    pasta_do_projeto,
    ".streamlit",
    "logo_guelpe.png"
)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.markdown("# 🚀 GUELPE")

st.sidebar.markdown("---")

opcao_servico = st.sidebar.radio(
    "ESCOLHA A FERRAMENTA:",
    [
        "📥 Downloader",
        "✨ Criador de Imagens"
    ]
)

st.sidebar.markdown("---")

st.sidebar.caption(
    "Guelpe Downloader\n"
    "Ferramentas simples para suas mídias."
)


# ============================================================
# LOGO PRINCIPAL
# ============================================================

if os.path.exists(caminho_da_logo):

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:

        logo = Image.open(caminho_da_logo)

        st.image(
            logo,
            use_container_width=True
        )

else:

    st.markdown(
        """
        <div class="guelpe-logo">

            <div class="guelpe-icon">
                ⬇️
            </div>

            <div class="guelpe-title">
                GUELPE
            </div>

            <div class="guelpe-subtitle">
                DOWNLOADER
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# DOWNLOADER
# ============================================================

if opcao_servico == "📥 Downloader":

    st.markdown(
        """
        <div class="hero-title">
            Baixe suas mídias rapidamente
        </div>

        <div class="hero-description">
            Cole o link da mídia abaixo e deixe o Guelpe
            identificar automaticamente a plataforma.
        </div>
        """,
        unsafe_allow_html=True
    )


    # ========================================================
    # CAMPO DE URL
    # ========================================================

    url_video = st.text_input(
        "🔗 LINK DA MÍDIA",
        placeholder="https://...",
        label_visibility="visible"
    )


    # ========================================================
    # BOTÃO DE ANÁLISE
    # ========================================================

    analisar = st.button(
        "⚡ ANALISAR MÍDIA"
    )


    if analisar:

        if not url_video.strip():

            st.warning(
                "⚠️ Cole um link antes de continuar."
            )

        else:

            url_video = url_video.strip()
            cookie_path = obter_caminho_cookies()

            opcoes_info = {
                "quiet": True,
                "no_warnings": True,
                "noplaylist": True,
                "cookiefile": cookie_path,
                "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1",
                "extractor_args": {
                    "youtube": {
                        "player_client": ["ios", "mweb"]
                    }
                }
            }

            # ------------------------------------------------
            # CONFIGURAÇÃO PARA APENAS ANALISAR
            # ------------------------------------------------

            opcoes_info = {
                "quiet": True,
                "no_warnings": True,
                "noplaylist": True,
                "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1",
                "extractor_args": {
                    "youtube": {
                        "player_client": ["ios", "mweb"]
                    }
                }
            }

            # ------------------------------------------------
            # IDENTIFICAR E EXTRAIR INFORMAÇÕES
            # ------------------------------------------------

            with st.spinner(
                "🔎 Identificando a plataforma e analisando a mídia..."
            ):

                try:

                    with yt_dlp.YoutubeDL(opcoes_info) as ydl:

                        info = ydl.extract_info(
                            url_video,
                            download=False
                        )


                    # ====================================================
                    # DADOS RETORNADOS PELO YT-DLP
                    # ====================================================

                    titulo = info.get(
                        "title",
                        "Mídia sem título"
                    )

                    thumbnail = info.get(
                        "thumbnail"
                    )

                    duracao = info.get(
                        "duration"
                    )

                    extrator = info.get(
                        "extractor_key"
                    )

                    nome_extrator = info.get(
                        "extractor"
                    )


                    # ------------------------------------------------
                    # TRATAR DURAÇÃO
                    # ------------------------------------------------

                    duracao_texto = "Não informado"

                    if duracao:

                        minutos = int(duracao // 60)

                        segundos = int(duracao % 60)

                        duracao_texto = (
                            f"{minutos}:{segundos:02d}"
                        )


                    # ====================================================
                    # RESULTADO DA ANÁLISE
                    # ====================================================

                    st.markdown(
                        """
                        <div class="success-card">

                            <div class="card-title">
                                ✓ Mídia encontrada!
                            </div>

                            <div class="card-text">
                                O Guelpe identificou automaticamente
                                uma fonte compatível.
                            </div>

                        </div>
                        """,
                        unsafe_allow_html=True
                    )


                    # ====================================================
                    # THUMBNAIL
                    # ====================================================

                    if thumbnail:

                        try:

                            st.image(
                                thumbnail,
                                use_container_width=True
                            )

                        except Exception:

                            pass


                    # ====================================================
                    # INFORMAÇÕES
                    # ====================================================

                    st.markdown(
                        f"""
                        <div class="guelpe-card">

                            <div class="card-title">
                                Plataforma detectada
                            </div>

                            <div class="platform-badge">
                                🌐 {extrator or nome_extrator or "Desconhecida"}
                            </div>

                            <div class="video-title">
                                {titulo}
                            </div>

                            <div class="video-info">
                                ⏱️ Duração: {duracao_texto}
                            </div>

                        </div>
                        """,
                        unsafe_allow_html=True
                    )


                    # ====================================================
                    # GUARDAR DADOS NA SESSÃO
                    # ====================================================

                    st.session_state["video_info"] = info

                    st.session_state["video_url"] = url_video

                    st.session_state["video_detected"] = True


                except Exception as erro:

                    st.session_state["video_detected"] = False

                    st.error(
                        """
                        ⚠️ Não foi possível analisar essa URL.

                        Verifique se o link está correto ou se a
                        plataforma permite acesso à mídia.
                        """
                    )


                    # ------------------------------------------------
                    # DETALHE TÉCNICO PARA DESENVOLVIMENTO
                    # ------------------------------------------------

                    with st.expander(
                        "🔧 Ver detalhe técnico"
                    ):

                        st.code(
                            str(erro)
                        )


    # ========================================================
    # DOWNLOAD
    # ========================================================

    if st.session_state.get(
        "video_detected",
        False
    ):

        st.markdown(
            "<div style='height: 15px'></div>",
            unsafe_allow_html=True
        )


        baixar = st.button(
            "⬇️ BAIXAR VÍDEO"
        )


        if baixar:

            info = st.session_state.get(
                "video_info"
            )

            url_para_download = st.session_state.get(
                "video_url"
            )


            if not info or not url_para_download:

                st.error(
                    "⚠️ Analise o link novamente."
                )

            else:

                # ------------------------------------------------
                # ARQUIVO TEMPORÁRIO ÚNICO
                # ------------------------------------------------

                nome_temporario = (
                    f"guelpe_{uuid.uuid4().hex}.mp4"
                )


                # ------------------------------------------------
                # OPÇÕES DO DOWNLOAD
                # ------------------------------------------------

                opcoes_download = {

                    "format":
                        "best[ext=mp4]/best",

                    "outtmpl":
                        nome_temporario,

                    "quiet":
                        True,

                    "no_warnings":
                        True,

                    "noplaylist":
                        True
                }


                with st.spinner(
                    "⬇️ Preparando seu vídeo..."
                ):

                    try:

                        with yt_dlp.YoutubeDL(
                            opcoes_download
                        ) as ydl:

                            ydl.download(
                                [url_para_download]
                            )


                        # ====================================================
                        # VERIFICAR ARQUIVO
                        # ====================================================

                        if os.path.exists(
                            nome_temporario
                        ):

                            # Ler o arquivo ANTES de apagar
                            with open(
                                nome_temporario,
                                "rb"
                            ) as arquivo:

                                dados_video = arquivo.read()


                            st.markdown(
                                """
                                <div class="success-card">

                                    <div class="card-title">
                                        ✓ Vídeo pronto!
                                    </div>

                                    <div class="card-text">
                                        Sua mídia foi processada
                                        com sucesso.
                                    </div>

                                </div>
                                """,
                                unsafe_allow_html=True
                            )


                            st.markdown(
                                "<div style='height: 15px'></div>",
                                unsafe_allow_html=True
                            )


                            # ====================================================
                            # BOTÃO FINAL
                            # ====================================================

                            st.download_button(
                                label="💾 SALVAR VÍDEO",
                                data=dados_video,
                                file_name="guelpe_downloader.mp4",
                                mime="video/mp4"
                            )


                        else:

                            st.error(
                                "⚠️ O arquivo não foi gerado."
                            )


                    except Exception as erro:

                        st.error(
                            """
                            ⚠️ Não foi possível baixar essa mídia.

                            A plataforma pode exigir autenticação,
                            bloquear o acesso ou o formato disponível
                            pode não ser compatível.
                            """
                        )


                        with st.expander(
                            "🔧 Ver detalhe técnico"
                        ):

                            st.code(
                                str(erro)
                            )


                    finally:

                        # ------------------------------------------------
                        # APAGAR ARQUIVO TEMPORÁRIO
                        # ------------------------------------------------

                        if os.path.exists(
                            nome_temporario
                        ):

                            try:

                                os.remove(
                                    nome_temporario
                                )

                            except Exception:

                                pass


    # ========================================================
    # RODAPÉ
    # ========================================================

    st.markdown(
        """
        <div class="guelpe-footer">

            Guelpe Downloader<br>

            Use o serviço de acordo com as regras
            das plataformas e os direitos aplicáveis.

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# CRIADOR DE IMAGENS
# ============================================================

elif opcao_servico == "✨ Criador de Imagens":

    st.markdown(
        """
        <div class="hero-title">
            Criador de Imagens
        </div>

        <div class="hero-description">
            Transforme suas ideias em imagens incríveis.
        </div>
        """,
        unsafe_allow_html=True
    )


    st.markdown(
        """
        <div class="guelpe-card">

            <div style="
                font-size: 50px;
                text-align: center;
                margin-bottom: 15px;
            ">
                ✨
            </div>

            <div class="card-title"
                 style="text-align: center;">

                Criador de Imagens

            </div>

            <div class="card-text"
                 style="
                    text-align: center;
                    margin-top: 10px;
                 ">

                Estamos preparando essa ferramenta
                para você.

                <br><br>

                <strong style="color: #C4B5FD;">
                    🚀 Em breve no Guelpe.
                </strong>

            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


    st.markdown(
        "<div style='height: 25px'></div>",
        unsafe_allow_html=True
    )


    st.info(
        "✨ O Criador de Imagens estará disponível "
        "em uma próxima atualização."
    )


    st.markdown(
        """
        <div class="guelpe-footer">

            Guelpe Downloader<br>

            Mais ferramentas chegando em breve.

        </div>
        """,
        unsafe_allow_html=True
    )