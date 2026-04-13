import streamlit as st
import pandas as pd

# --- MODELO ---
class Gasto:
    def __init__(self, tipo, data, valor, forma):
        self.tipo = tipo
        self.data = data
        self.valor = valor
        self.forma = forma

class PlanilhaVera:
    def __init__(self):
        self.gastos = []

    def adicionar(self, gasto):
        self.gastos.append(gasto)

    @property
    def total_geral(self):
        return sum(g.valor for g in self.gastos)

    def resumo_por_tipo(self):
        resumo = {}
        for g in self.gastos:
            resumo[g.tipo] = resumo.get(g.tipo, 0) + g.valor
        return resumo

    def resumo_por_forma(self):
        resumo = {}
        for g in self.gastos:
            resumo[g.forma] = resumo.get(g.forma, 0) + g.valor
        return resumo

# --- INTERFACE ---
st.title("📊 Planilha de Gastos da Vera")

if 'planilha' not in st.session_state:
    st.session_state.planilha = PlanilhaVera()

# Formulário de Cadastro
with st.expander("➕ Cadastrar Novo Gasto", expanded=True):
    col1, col2 = st.columns(2)
    with col1:
        tipo = st.selectbox("Tipo de Gasto", ["Remédio", "Roupa", "Refeição", "Transporte", "Outros"])
        data = st.date_input("Data do Gasto")
    with col2:
        valor = st.number_input("Valor (R$)", min_value=0.0, step=0.50)
        forma = st.selectbox("Forma de Pagamento", 
                             ["Dinheiro", "Cartão Crédito", "Cartão Débito", "Ticket Alimentação", "Refeição"])
    
    if st.button("Salvar Gasto"):
        novo_gasto = Gasto(tipo, data, valor, forma)
        st.session_state.planilha.adicionar(novo_gasto)
        st.success("Gasto registrado!")

# Exibição dos Resultados
if st.session_state.planilha.gastos:
    st.divider()
    st.metric("Total Acumulado", f"R$ {st.session_state.planilha.total_geral:.2f}")

    col_a, col_b = st.columns(2)
    
    with col_a:
        st.subheader("Por Tipo")
        df_tipo = pd.DataFrame(st.session_state.planilha.resumo_por_tipo().items(), columns=['Tipo', 'Total'])
        st.table(df_tipo)

    with col_b:
        st.subheader("Por Forma de Pagamento")
        df_forma = pd.DataFrame(st.session_state.planilha.resumo_por_forma().items(), columns=['Forma', 'Total'])
        st.table(df_forma)
else:
    st.info("Nenhum gasto cadastrado ainda.")