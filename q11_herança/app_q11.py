import streamlit as st
from datetime import date

# --- SUPERCLASSE ---
class Pessoa:
    def __init__(self, nome, data_nasc, endereco, telefones):
        self.nome = nome
        self.data_nasc = data_nasc
        self.endereco = endereco
        self.telefones = telefones

    @property
    def idade(self):
        hoje = date.today()
        return hoje.year - self.data_nasc.year - ((hoje.month, hoje.day) < (self.data_nasc.month, self.data_nasc.day))

# --- SUBCLASSES ---
class Funcionario(Pessoa):
    def __init__(self, nome, data_nasc, endereco, telefones, matricula, salario, data_adm, cargo):
        super().__init__(nome, data_nasc, endereco, telefones)
        self.matricula = matricula
        self.salario = salario
        self.data_adm = data_adm
        self.cargo = cargo

    def reajustar_salario(self, percentual):
        self.salario *= (1 + percentual/100)

class Cliente(Pessoa):
    def __init__(self, nome, data_nasc, endereco, telefones, codigo, profissao):
        super().__init__(nome, data_nasc, endereco, telefones)
        self.codigo = codigo
        self.profissao = profissao

# --- INTERFACE ---
st.title("👥 Gestão Unificada - Herança")

if 'pessoas' not in st.session_state:
    st.session_state.pessoas = []

tipo = st.radio("Selecione o tipo de cadastro:", ["Funcionário", "Cliente"])

with st.form("cadastro_pessoa"):
    st.subheader(f"Dados Básicos (Pessoa)")
    nome = st.text_input("Nome Completo")
    dt_nasc = st.date_input("Data de Nascimento", value=date(1990, 1, 1))
    
    if tipo == "Funcionário":
        st.subheader("Dados específicos de Funcionário")
        mat = st.number_input("Matrícula", step=1)
        sal = st.number_input("Salário", min_value=0.0)
        cargo = st.text_input("Cargo")
        if st.form_submit_button("Salvar Funcionário"):
            novo = Funcionario(nome, dt_nasc, "Rua X", ["123"], mat, sal, date.today(), cargo)
            st.session_state.pessoas.append(novo)
            st.success("Funcionário cadastrado!")
    else:
        st.subheader("Dados específicos de Cliente")
        cod = st.text_input("Código do Cliente")
        prof = st.text_input("Profissão")
        if st.form_submit_button("Salvar Cliente"):
            novo = Cliente(nome, dt_nasc, "Rua Y", ["456"], cod, prof)
            st.session_state.pessoas.append(novo)
            st.success("Cliente cadastrado!")

# Listagem Única demonstrando Polimorfismo
st.divider()
st.subheader("Lista Geral")
for p in st.session_state.pessoas:
    tipo_obj = "👔 Func" if isinstance(p, Funcionario) else "🛒 Cli"
    st.write(f"[{tipo_obj}] **{p.nome}** - Idade: {p.idade} anos")