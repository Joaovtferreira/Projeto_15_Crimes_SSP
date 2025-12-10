# 🛡 Projeto_15_Dashboard_Crimes_SP

Um dashboard interativo criado com **Streamlit** e **Folium** para visualizar a distribuição espacial e estatística dos crimes registrados no estado de São Paulo.  
Os dados utilizados são **públicos**, extraídos da SSP (Secretaria de Segurança Pública).

O objetivo do projeto é apresentar de forma simples e direta o total de ocorrências (BOs) por município e bairro, o principal tipo de crime registrado, além de exibir no mapa a localização de cada ocorrência.

---

## 🧠 Situação-Problema

A Secretaria de Segurança Pública disponibiliza dados públicos sobre ocorrências policiais registradas em São Paulo. Entretanto, para um cidadão comum ou até mesmo para estudantes de análise de dados, interpretar planilhas extensas é difícil.

Sua tarefa é desenvolver, com Python e Streamlit, um sistema capaz de:

- Permitir ao usuário escolher um **município**
- Filtrar automaticamente os **bairros** pertencentes a esse município
- Exibir:
  - O **número total de crimes** registrados naquele recorte
  - O **crime mais frequente** (campo `Natureza_Apurada`)
  - Um **mapa interativo** com marcadores representando cada ocorrência
- Exibir um **popup** ao clicar no marcador, com:
  - Natureza do crime  
  - Período do dia  
  - Data da ocorrência  

Esse projeto ajuda os alunos a praticarem:

- Manipulação de dados reais
- Integração Streamlit + Folium
- Filtros dependentes (Município → Bairros)
- Construção de dashboards interativos
- Uso de mapas para análise geográfica

---

## 🎯 Objetivo Educacional

- Compreender o tratamento de dados públicos  
- Aprender a criar filtros dinâmicos com Streamlit  
- Utilizar Folium para marcar pontos geográficos  
- Gerar popups informativos em mapas  
- Trabalhar com conceitos de **análise espacial**  
- Criar métricas simples (contagem e moda)  
- Organizar aplicações interativas e responsivas  

---

## 📌 Funcionalidades do Dashboard

### 🔎 Filtros Inteligentes
- **Município:** seleciona qualquer cidade presente no dataset  
- **Bairro:** lista apenas os bairros do município escolhido  

### 📊 Indicadores
Exibidos no topo do dashboard:

- **Total de Crimes (BOs registrados)**  
- **Principal Crime (Natureza Apurada mais recorrente)**  

### 🗺 Mapa Interativo com Folium
- Marcadores para cada ocorrência  
- Cores e ícones personalizáveis  
- **Popups** contendo:
  - Tipo de crime (`Natureza_Apurada`)
  - Período do dia (ex.: manhã, tarde, noite)
  - Data do BO  

### 🎯 Distribuição Espacial dos Crimes
O mapa permite visualizar:

- Concentração de ocorrências  
- Bairros mais críticos  
- Regiões com maior densidade criminal  

---



