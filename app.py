import streamlit as st

st.set_page_config(page_title="Creadores Cuánticos", layout="centered")

# -------------------------
# CSS PREMIUM – estilo Apple
# -------------------------
st.markdown("""
<style>

body {
    background-color: #f1f1f5;
    font-family: 'Inter', sans-serif;
}

/* Expander estilo Apple */
.st-expander {
    background: rgba(255, 255, 255, 0.65) !important;
    backdrop-filter: blur(12px) saturate(180%);
    border-radius: 22px !important;
    border: 1px solid rgba(220,220,220,0.45);
    margin-bottom: 20px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.08);
    transition: all 0.25s ease-in-out;
}

/* Hover elegante */
.st-expander:hover {
    transform: scale(1.010);
    box-shadow: 0 10px 26px rgba(0,0,0,0.12);
}

/* Título del expander */
.st-expander > summary {
    font-size: 20px !important;
    font-weight: 600 !important;
    padding: 16px !important;
    color: #111111 !important;
    letter-spacing: -0.3px;
}

/* Al abrir */
details[open].st-expander {
    background: rgba(255,255,255,0.85) !important;
    box-shadow: 0 12px 30px rgba(0,0,0,0.14);
}

/* Iframe estilizado */
iframe {
    border-radius: 16px;
    margin-top: 6px;
}

/* Eliminar borde azul al dar clic */
summary:focus {
    outline: none !important;
}

</style>
""", unsafe_allow_html=True)


# -------------------------
# Episodios
# -------------------------
episodios = [
    ("Cómo RECIBIR Feedback como un PRO", "https://open.spotify.com/embed/episode/548hCacsZDwIctiFLpFDx9?utm_source=generator"),
    ("Cómo DAR feedback sin morir en el intento", "https://open.spotify.com/embed/episode/4tXta0z60h1OO0D2gV60NP?utm_source=generator"),
    ("La neurociencia del Feedback: Domina tu mente, transforma tu respuesta", "https://open.spotify.com/embed/episode/5bFQAK4XRJJxv9HthCSk69?utm_source=generator"),
    ("El poder de la palabra y las declaraciones cuánticas", "https://open.spotify.com/embed/episode/5Izkz87v8Aqgim0xlwFa9T?utm_source=generator"),
    ("Liderazgo sin cargo: La Influencia Silenciosa", "https://open.spotify.com/embed/episode/537n1KNX5o21iAMR2AU16o?utm_source=generator"),
    ("La Presencia como Acto Revolucionario", "https://open.spotify.com/embed/episode/7Ab3veW7OydVhN3VHXC2bn?utm_source=generator"),
    ("El hilo invisible: Sueños, miedos y legado", "https://open.spotify.com/embed/episode/4LxvhWuavfwWk7Y695XDh5?utm_source=generator"),
    ("No era falta de amor, era falta de conciencia", "https://open.spotify.com/embed/episode/6FYFEBbMBoWH5Enzzv6FTA?utm_source=generator"),
    ("Enfocarse en lo Crucialmente Importante", "https://open.spotify.com/embed/episode/0sC9ehQeXoSNGQ3w2RcdUu?utm_source=generator"),
    ("Disciplina, propósito y poder: el arte de ejecutar lo imposible", "https://open.spotify.com/embed/episode/2IxSw7eyX8lH3UXLHscmqQ?utm_source=generator")
]

st.title("🎙️ Creadores Cuánticos")

# -------------------------
# Buscador
# -------------------------
query = st.text_input("🔍 Buscar episodio por nombre:", "")

episodios_filtrados = [
    (titulo, url) for titulo, url in episodios 
    if query.lower() in titulo.lower()
]

st.write("---")

# -------------------------
# Mostrar resultados
# -------------------------
if not episodios_filtrados:
    st.info("No se encontró ningún episodio con ese nombre.")
else:
    for titulo, url in episodios_filtrados:
        st.subheader(f"🎧 {titulo}")
        st.components.v1.iframe(url, height=152)
        st.write("")

