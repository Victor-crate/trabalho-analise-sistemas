import streamlit as st
from datetime import datetime, timedelta

class Remedio:
    def __init__(self, paciente, remedio, data_ini, dias, vezes, dosagem, hora_ini):
        self.paciente = paciente
        self.remedio = remedio
        self.data_ini = data_ini
        self.dias = dias
        self.vezes = vezes
        self.dosagem = dosagem
        self.hora_ini = hora_ini # Objeto datetime.time
        
    @property
    def data_termino(self):
        return self.data_ini + timedelta(days=self.dias)

    def calcular_horarios(self, hora_base=None):
        if hora_base is None:
            hora_base = self.hora_ini
            
        intervalo = 24 // self.vezes
        horarios = []
        
        # Converte time para datetime para fazer cálculos
        data_base = datetime.combine(datetime.today(), hora_base)
        
        for i in range(self.vezes):
            proximo_horario = data_base + timedelta(hours=i * intervalo)
            horarios.append(proximo_horario.strftime("%H:%M"))
        return horarios

st.title("💊 Controle de Remédios - Maurício")

with st.sidebar:
    st.header("Cadastro de Prescrição")
    pac = st.text_input("Nome do Paciente", "Maurício")
    rem = st.text_input("Nome do Remédio")
    dat = st.date_input("Data de Início")
    dias = st.number_input("Duração (Dias)", min_value=1, value=5)
    vezes = st.selectbox("Vezes ao dia", [1, 2, 3, 4, 6, 8, 12], index=2)
    dos = st.text_input("Dosagem (ex: 500mg, 1 comprimido)")
    h_ini = st.time_input("Horário da 1ª Dose")

if rem:
    obj_rem = Remedio(pac, rem, dat, dias, vezes, dos, h_ini)
    
    col1, col2 = st.columns(2)
    col1.metric("Paciente", obj_rem.paciente)
    col2.metric("Tratamento até", obj_rem.data_termino.strftime("%d/%m/%Y"))
    
    st.subheader("🗓️ Planilha de Horários do Dia")
    
    # Lógica de Atraso
    atraso = st.checkbox("Houve atraso hoje?")
    if atraso:
        nova_hora = st.time_input("Informe a hora que tomou o remédio agora:")
        lista_horarios = obj_rem.calcular_horarios(nova_hora)
        st.warning("⚠️ Horários reorganizados devido ao atraso!")
    else:
        lista_horarios = obj_rem.calcular_horarios()

    # Exibição em formato de cards simples
    cols = st.columns(len(lista_horarios))
    for i, h in enumerate(lista_horarios):
        cols[i].button(f"{h}", key=f"btn_{i}")
        
    st.info(f"Intervalo entre doses: {24//vezes} horas.")
else:
    st.write("Preencha o nome do remédio para gerar a planilha.")