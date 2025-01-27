import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout="wide", page_title="Análise da Turma")

st.title("Análise de Dados da Turma")

if "dados" not in st.session_state:
    st.session_state.dados = None

arquivo = st.file_uploader("Insira o arquivo CSV")

if arquivo is not None:
    st.session_state.dados = pd.read_csv(arquivo)
    st.session_state.dados['situacao'] = ["Aprovado" if nota >= 70 else "Reprovado"
                                          for nota in st.session_state.dados.Total]
else:
    st.session_state.dados = None

if st.session_state.dados is not None:
    dados = st.session_state.dados.copy()
    st.dataframe(st.session_state.dados, use_container_width=True)

    col1, col2 = st.columns([1, 3])
    
    with col1:
        media = dados['Total'].mean()
        mediana = dados['Total'].median()
        max = dados['Total'].max()
        min = dados['Total'].min()

        aluno_max = dados[dados.Total==max].Nome.values[0]
        aluno_min = dados[dados.Total==min].Nome.values[0]

        st.subheader("Estatísticas gerais")
        st.markdown(f':blue[Média:] {round(media, 1)}')
        st.markdown(f':blue[Mediana:] {round(mediana, 1)}')    
        st.markdown(f':blue[Máxima:] {round(max, 1)} ({aluno_max})')
        st.markdown(f':blue[Mínima:] {round(min, 1)} ({aluno_min})')

        agrupados = dados.groupby("situacao")["Nome"].count()

        pizza = plt.figure(figsize=(4,4))
        plt.pie(agrupados, labels=agrupados.index, autopct='%.1f%%')
        st.pyplot(pizza)

    with col2:
        st.subheader("Gráfico de desempenho: ")
        barras = plt.figure(figsize=(9,6))
        ax = sns.barplot(data=dados.sort_values(by='Total', ascending=False),
                         x='Total',
                         y='Nome')
        ax.tick_params(axis='y', labelsize=7)
        st.pyplot(barras)

