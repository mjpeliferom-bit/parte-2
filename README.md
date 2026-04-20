# 🌾 FarmTech Solutions — Sistema de Perdas na Colheita de Cana

## 📌 Sobre o Projeto

O agronegócio da cana-de-açúcar é um dos pilares da economia brasileira. No entanto, as perdas durante a colheita  causadas por diferentes tipos de máquinas e métodos  representam um prejuízo significativo para os produtores rurais.

O **FarmTech** é um sistema desenvolvido em Python que permite ao produtor simular e analisar as perdas na colheita de cana-de-açúcar, comparando diferentes máquinas colhedoras e calculando o impacto financeiro dessas perdas de forma clara e objetiva.

---

## 🎯 Problema Tratado

Produtores rurais muitas vezes não têm visibilidade sobre **quanto estão perdendo** durante a colheita e **qual o custo real** dessa perda. Este sistema oferece uma forma simples e acessível de calcular:

- Toneladas perdidas por tipo de máquina
- Prejuízo financeiro em reais
- Percentual de perda em relação à produção total
- Recomendação sobre a adequação da máquina utilizada

---

## 🗂️ Estrutura do Projeto

```
parte-2/
├── main.py          # Menu principal e interface com o usuário
├── calculos.py      # Estruturas de dados, funções de cálculo e validação
├── arquivos.py      # Manipulação de arquivos texto e JSON
├── database.py      # Conexão e operações com banco de dados Oracle
├── dados_agro.json  # Base de dados JSON com registros de colheita
└── README.md        # Documentação do projeto
```

---

## ⚙️ Funcionalidades

- Seleção de talhão e máquina colhedora
- Cálculo de perda em toneladas e percentual
- Cálculo de prejuízo financeiro em reais
- Validação de entradas do usuário (sem aceitar letras onde se espera número)
- Relatório limpo e de fácil leitura no terminal
- Avaliação automática do nível de perda (aceitável, moderada ou alta)
- Gravação e leitura de dados em arquivo JSON
- Integração com banco de dados Oracle

---

## 🐍 Tecnologias Utilizadas

- Python 3
- Manipulação de arquivos JSON
- Banco de dados Oracle (via `oracledb`)
- Estruturas de dados: dicionário, lista, tupla

---

## 👥 Integrantes

| Nome | Responsabilidade |
|------|-----------------|
| Bruna Camila | Arquiteta de Dados e Lógica (`calculos.py`) |
| Jonatas | Manipulação de Arquivos (`arquivos.py`) |
| Kaio | Banco de Dados (`database.py`) |

---

## ▶️ Como Executar

1. Clone o repositório
2. Acesse a pasta `parte-2`
3. Execute o sistema:

```bash
python main.py
```

---

## 📊 Exemplo de Uso

```
==================================================
   FARMTECH - SISTEMA DE PERDAS NA COLHEITA
==================================================

Talhão   : Talhão A
Área     : 50.0 hectares
Produção : 400.0 toneladas estimadas

Produção estimada (toneladas): 400
Preço por tonelada (R$): 120

Máquinas disponíveis:
  1. Colhedora Manual (índice de perda: 5%)
  2. Colhedora Mecânica A (índice de perda: 8%)
  3. Colhedora Mecânica B (índice de perda: 15%)

==================================================
              RELATÓRIO DE PERDAS
==================================================
  Talhão          : Talhão A
  Máquina usada   : Colhedora Manual
  Produção total  : 400.0 toneladas
  Perda estimada  : 20.0 toneladas (5.0%)
  Prejuízo        : R$ 2.400,00
==================================================
  ✔ Perda dentro do aceitável. Boa colheita!
==================================================
```
