import os

# Conteúdo do README.md
readme_content = """# 🚀 Projeto de Análise e Desenvolvimento de Sistemas I
## Lista 01: Exercitando Modelagem UML - Identificando Classes, Atributos e Métodos

**Instituição:** Centro Universitário de João Pessoa - UNIPÊ  
**Curso:** CST em Análise e Desenvolvimento de Sistemas  
**Disciplina:** Análise e Projeto de Sistemas I  
**Professor:** Ricardo Roberto de Lima  
**Período:** 3°

---

## 📋 Descrição do Projeto

Este projeto apresenta a implementação técnica e análise de 11 cenários de negócio focados em **Programação Orientada a Objetos (POO)** e **Modelagem UML**. Cada questão foi desenvolvida para demonstrar a transição entre o levantamento de requisitos e o código funcional em Python.

- **Diagramas de Classes:** Gerados via PlantUML.
- **Interface Interativa:** Desenvolvida com Streamlit (Python).
- **Especificação:** Requisitos Funcionais (RF) e Não-Funcionais (RNF) detalhados por questão.

---

## 📁 Estrutura do Repositório

```text
TRABALHO_LISTA_01/
├── q01_conta_luz/             # Lógica de consumo e tarifas
├── q02_texto_saida/           # Configuração de componentes visuais
├── q03_boneco_movimento/      # Controle de estados e coordenadas
├── q04_horario_remedios/      # Gestão de horários e atrasos (Maurício)
├── q05_gastos_diarios/        # Agregação de despesas (Vera)
├── q06_comanda_eletronica/    # Sistema de PDV (Joaquim)
├── q07_lista_compras/         # Planejamento vs Efetivo (Carolina)
├── q08_colecao_cd's/          # Cadastro básico (Adriano)
├── q09_colecao_atualizada/    # Relacionamentos M:N e Coletâneas
├── q10_sala_reuniao/          # Gestão de conflitos de agenda (Patrícia)
├── q11_herança/               # Implementação de Herança e Especialização
├── .gitignore                 # Arquivo para ignorar a pasta .venv
└── README.md                  # Documentação principal

Questão,Foco Principal,Conceito OO Aplicado
01,Conta de Luz,Atributos e Métodos
02,TextoSaída,Encapsulamento de Estilos
03,Movimento,"Gerenciamento de Estados (X, Y)"
04,Medicamentos,Lógica de Datas e Horas
05,Finanças,Atributos Derivados (Totais)
06,PDV,Composição de Objetos
07,Compras,Validação de Dados
08/09,Coleções,Multiplicidade e Associações
10,Reservas,Busca e Conflito de Horários
11,Herança,Generalização (Classe Pessoa)

🛠️ Tecnologias e Ferramentas
Linguagem: Python 3.12+

Framework Web: Streamlit

Modelagem: PlantUML (padrão UML 2.5)

Interface: Pandas para exibição de tabelas

Versionamento: Git/GitHub

Como Executar
1.Clone o repositório:
https://github.com/Victor-crate/trabalho-analise-sistemas.git

2.Ative o ambiente virtual:
# No Windows
.venv\\Scripts\\activate

3.Instale as dependências:

pip install streamlit pandas

4.Execute uma aplicação:

cd q10_sala_reuniao
streamlit run app_q10.py

👨‍💻 Autor
Desenvolvido por: [Victor Luís]
Instituição: UNIPÊ - João Pessoa/PB

Este projeto é parte integrante da nota da disciplina de Análise e Projeto de Sistemas I.