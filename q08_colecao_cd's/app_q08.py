import streamlit as st

# --- MODELO ---
class CD:
    def __init__(self, artista, titulo, ano):
        self.artista = artista
        self.titulo = titulo
        self.ano = ano

class Colecao:
    def __init__(self):
        self.cds = []
    
    def adicionar(self, cd):
        self.cds.append(cd)
    
    @property
    def total_itens(self):
        return len(self.cds)

# --- INTERFACE (SIMULADOR DE PALM-TOP) ---
st.set_page_config(page_title="Palm-top Adriano", page_icon="💿")
st.title("💿 Coleção de CD's do Adriano")

if 'minha_colecao' not in st.session_state:
    st.session_state.minha_colecao = Colecao()

# Área de Cadastro
with st.form("cadastro_cd", clear_on_submit=True):
    st.subheader("Novo Cadastro")
    art = st.text_input("Artista ou Conjunto")
    tit = st.text_input("Título do CD")
    ano = st.number_input("Ano de Lançamento", min_value=1900, max_value=2026, value=2000)
    
    if st.form_submit_button("Cadastrar no Palm-top"):
        if art and tit:
            novo_cd = CD(art, tit, ano)
            st.session_state.minha_colecao.adicionar(novo_cd)
            st.success("CD adicionado com sucesso!")
        else:
            st.error("Preencha todos os campos.")

# Área de Listagem
st.divider()
st.subheader(f"📚 Minha Lista ({st.session_state.minha_colecao.total_itens} CDs)")

if st.session_state.minha_colecao.cds:
    for idx, item in enumerate(st.session_state.minha_colecao.cds):
        with st.container():
            st.write(f"**{idx+1}. {item.titulo}** - {item.artista} ({item.ano})")
else:
    st.info("O Adriano ainda não cadastrou nenhum CD.")