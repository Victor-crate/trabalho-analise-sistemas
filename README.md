# 🚀 Projeto de Análise e Desenvolvimento de Sistemas I
> **Lista 01: Exercitando Modelagem UML - Identificando Classes, Atributos e Métodos**

Este repositório contém a resolução técnica de 11 cenários de negócio, explorando os pilares da **Programação Orientada a Objetos (POO)** e a formalização via **UML**.

---

## 🎓 Informações Acadêmicas
* **Instituição:** Centro Universitário de João Pessoa - UNIPÊ
* **Curso:** CST em Análise e Desenvolvimento de Sistemas
* **Período:** 3° Período
* **Disciplina:** Análise e Projeto de Sistemas I
* **Professor:** Ricardo Roberto de Lima
* **Autor:** Victor Luís

---

## 📂 Estrutura do Projeto
O trabalho está organizado em módulos independentes para facilitar a correção e o entendimento:

| Questão | Tema | Conceito Chave |
| :--- | :--- | :--- |
| **Q01** | Conta de Luz | Atributos e Métodos |
| **Q02** | TextoSaída | Encapsulamento de Estilos |
| **Q03** | Boneco em Movimento | Gerenciamento de Coordenadas |
| **Q04** | Horário de Remédios | Lógica de Datas (Cenário Maurício) |
| **Q05** | Gastos Diários | Atributos Derivados (Cenário Vera) |
| **Q06** | Comanda Eletrônica | Sistema de PDV (Cenário Joaquim) |
| **Q07** | Lista de Compras | Planejamento de Estoque (Cenário Carolina) |
| **Q08/09** | Coleção de CDs | Associações e Multiplicidade (Cenário Adriano) |
| **Q10** | Sala de Reunião | Gestão de Conflitos (Cenário Patrícia) |
| **Q11** | Herança | Especialização de Classes (Pessoa/Cliente/Func.) |

---

## 🎯 Questões Abordadas

**Questão 01: Conta de Luz**

Cenário: Gabriel controla seus gastos mensais com conta de luz através de uma planilha Excel.

Objetivo: Identificar as classes, atributos e métodos para um sistema de gerenciamento de consumo de energia elétrica.

Classe Principal: ContaDeLuz

**Funcionalidades:**

•
Registrar consumo mensal de energia

•
Identificar mês com menor consumo

•
Identificar mês com maior consumo

---

**Questão 02: Classe TextoSaída**

Cenário: Criar uma classe que permita configurar um texto através de atributos para exibição em diferentes componentes.

Objetivo: Modelar uma classe de configuração de texto sem vínculo com linguagens de programação específicas.

Classes Principais: TextoSaida, Cor, TipoComponente

**Funcionalidades:**

•
Configurar tamanho da letra

•
Escolher cor da fonte e fundo

•
Selecionar tipo de componente (label, edit, memo)

---

**Questão 03: Classe Boneco em Movimento**

Cenário: Professor Ricardo Roberto decidiu criar uma classe que permita mover um boneco na tela.

Objetivo: Modelar um sistema de movimento de objetos em uma interface gráfica.

Classes Principais: Boneco, Direcao

**Funcionalidades:**

•
Mover boneco em diferentes direções

•
Controlar posição (X, Y)

•
Gerenciar direção atual

---

**Questão 04: Horário de Remédios**

Cenário: Aplicação de controle pessoal de horário de remédios para smartphone.

Objetivo: Modelar um sistema de agendamento e gerenciamento de medicações.

Classes Principais: Remedio, Horario, Planilha, Paciente, ControladorRemedio

**Funcionalidades:**

•
Cadastrar remédios com dosagem e duração

•
Sugerir horários de administração

•
Gerar planilha de horários diários

•
Reorganizar horários em caso de atraso

---

**Questão 05: Gastos Diários**

Cenário: Vera controla seus gastos diários através de uma planilha Excel.

Objetivo: Modelar um sistema de controle financeiro pessoal com relatórios.

Classes Principais: Gasto, TipoGasto, FormaPagamento, ControladorGastos, Relatorio

**Funcionalidades:**

•
Registrar gastos com tipo, data, valor e forma de pagamento

•
Gerar relatório mensal agrupado por tipo

•
Gerar relatório agrupado por forma de pagamento

•
Calcular totais mensais

---

**Questão 06: Comanda Eletrônica (PDV)**

Cenário: Sistema de controle de comanda eletrônica para padaria.

Objetivo: Modelar um sistema de ponto de venda (PDV) para estabelecimento comercial.

Classes Principais: Comanda, Produto, ItemComanda, Caixa, Venda

**Funcionalidades:**

•
Criar comandas com número único

•
Adicionar produtos à comanda

•
Calcular valor total

•
Processar pagamento

•
Emitir recibo

---

**Questão 07: Lista de Compras**

Cenário: Carolina controla sua lista de compras mensal através de uma planilha Excel.

Objetivo: Modelar um sistema de gerenciamento de lista de compras com controle de preços.

Classes Principais: Produto, ListaCompras, ItemLista, UnidadeCompra

**Funcionalidades:**

•
Cadastrar produtos com unidade de compra

•
Especificar quantidade prevista e efetiva

•
Atualizar preços mensalmente

•
Calcular total de compras

•
Exportar para Excel

---

**Questão 08: Coleção de CDs**

Cenário: Adriano deseja cadastrar sua coleção de CDs em um Palm-top.

Objetivo: Modelar um sistema simples de gerenciamento de coleção de CDs.

Classes Principais: CD, Artista, ColecaoCDs

**Funcionalidades:**

•
Cadastrar CDs com artista, título e ano

•
Adicionar/remover CDs da coleção

•
Buscar CDs por artista ou título

•
Visualizar total de CDs

---

**Questão 09: Coleção de CDs (Variação A)**

Cenário: Variação que inclui CDs de coletâneas com múltiplos artistas e músicas.

Objetivo: Modelar um sistema complexo de gerenciamento de coleção com relacionamento muitos-para-muitos (N:N).

Classes Principais: CD, Artista, Musica, Faixa, ColecaoCDs

**Funcionalidades:**

•
Cadastrar CDs com múltiplos artistas

•
Especificar se é coletânea ou duplo

•
Cadastrar músicas com duração de faixas

•
Buscar CDs por artista ou música

•
Gerar relatórios de associações

---

**Questão 10: Sala de Reunião**

Cenário: Patrícia controla o uso de três salas de reunião através de planilhas Excel.

Objetivo: Modelar um sistema complexo de agendamento de salas de reunião.

Classes Principais: SalaReuniao, Funcionario, Reuniao, Horario, AgendaReuniao

**Funcionalidades:**

•
Cadastrar salas com capacidade

•
Cadastrar funcionários com cargo e ramal

•
Agendar reuniões

•
Realocação de reuniões

•
Consultar salas livres em data/horário

•
Gerar relatório de ocupação

---

**Questão 11: Herança**

Cenário: Identificar classe comum entre Funcionário e Cliente.

Objetivo: Demonstrar o uso de herança para eliminar duplicação de código.

Classes Principais: Pessoa (superclasse), Funcionario (subclasse), Cliente (subclasse)

**Funcionalidades:**

•
Cadastrar pessoas com dados comuns

•
Especializar em Funcionário (matrícula, cargo, salário)

•
Especializar em Cliente (código, profissão)

•
Reajustar salário de funcionário

•
Promover funcionário

---

## 🚀 Como Executar o Projeto localmente

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/Victor-crate/trabalho-analise-sistemas.git](https://github.com/Victor-crate/trabalho-analise-sistemas.git)

---

2. **Acesse a pasta da questão desejada:**

    cd q10_sala_reuniao

---

3. **Inicie a interface:**

    streamlit run app_q10.py

---  

## 📝 Especificação de Requisitos

**Cada questão possui um arquivo requisitos_questao_XX.txt contendo:**

•
Requisitos Funcionais (RF ): O que o sistema deve fazer

•
Requisitos Não-Funcionais (RNF): Como o sistema deve se comportar (performance, segurança, usabilidade, etc.)

---

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3.x
* **Interface:** [Streamlit](https://streamlit.io/) (Visualização Interativa)
* **Modelagem:** PlantUML / Mermaid
* **Manipulação de Dados:** Pandas

---

## 📚 Conceitos Abordados

**Este projeto aborda os seguintes conceitos de Análise Orientada a Objetos:**

1.Identificação de Classes: Reconhecer entidades do domínio do problema

2.Atributos: Propriedades que caracterizam uma classe

3.Métodos: Comportamentos e operações de uma classe

4.Relacionamentos: Associações, agregações, composições e herança

5.Multiplicidade: Cardinalidade dos relacionamentos (1:1, 1:N, M:N)

6.Herança: Especialização e generalização de classes

7.Enumerações: Tipos com valores pré-definidos

8.Requisitos Funcionais e Não-Funcionais: Especificação completa de sistem

---

## 🎓 Objetivos de Aprendizado

**Ao estudar este projeto, você aprenderá:**

•
Como identificar classes em um cenário de negócio

•
Como modelar relacionamentos entre classes

•
Como especificar requisitos de forma clara

•
Como usar diagramas UML para comunicar design

•
Como aplicar princípios de orientação a objetos

•
Como estruturar um projeto de análise de sistemas

---

## 📄 Licença

**Este projeto é fornecido para fins educacionais. Todos os direitos reservados.**


