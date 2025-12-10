from mapa import create_map
import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

@st.cache_data
def load_data():
    d1 = pd.read_parquet('Dados_1.parquet')
    d2 = pd.read_parquet('Dados_2.parquet')
    df = pd.concat([d1, d2]).reset_index(drop=True)
    return df

df = load_data()

#-----------------SIDEBAR E FILTROS

st.sidebar.title('Crimes de SP')

municipio = st.sidebar.selectbox(
    'Cidade',
     df['NOME_MUNICIPIO'].unique().tolist()
)

df1 = df[df['NOME_MUNICIPIO'] == municipio]

bairro = st.sidebar.selectbox('Bairro', df1['BAIRRO'].unique().tolist())

df1 = df1[df1['BAIRRO'] == bairro]

#-----------------BODY

st.title(f'Crimes em {bairro}-{municipio}')


with st.container():
    col1, col2 = st.columns(2)
    with col1:
        with st.container(border=True, height='stretch'):
            st.metric('Quantidade de Crimes', df1['NOME_MUNICIPIO'].count())


    with col2:
        with st.container(border=True, height='stretch'):
            st.metric('Principal Crime', df1['NATUREZA_APURADA'].value_counts().reset_index()['NATUREZA_APURADA'].iloc[0])  

#-----------------MAPA

coordinates = df1[(df1['LATITUDE'].notnull()) & (df1['LONGITUDE'].notnull())]
coordinates = coordinates[(coordinates['LATITUDE'] != 0) | (coordinates['LONGITUDE'] != 0)]


create_map(coordinates[['LATITUDE', 'LONGITUDE', 'NATUREZA_APURADA', 'DESC_PERIODO', 'DESCR_SUBTIPOLOCAL', 'DATA_OCORRENCIA_BO']])


with open("mapa.html", "r", encoding="utf-8") as f:
    html_content = f.read()


st.components.v1.html(html_content, height=600, scrolling=True)

#python -m streamlit run app.py