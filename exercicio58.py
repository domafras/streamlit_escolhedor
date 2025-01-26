import streamlit as st
import random
import time

def escolha(lista):
    with st.spinner("Pensando..."):
        time.sleep(3)
        escolha_final = random.choice(lista)
        st.markdown(f"#### Sua escolha foi... :rainbow[{escolha_final}]")

st.title("Escolhedor")
aba1, aba2 = st.tabs(["Estática", "Dinâmica"])

# tab estática
with aba1:
    opcao1 = st.text_input("Insira a opção 1:")
    opcao2 = st.text_input("Insira a opção 2:")
    opcao3 = st.text_input("Insira a opção 3:")

    if st.button("Escolher", key="botao1"):
        lista_opcoes = [opcao1, opcao2, opcao3]
        escolha(lista_opcoes)

# tab dinâmica       
with aba2:
    if "lista_n_opcoes" not in st.session_state:
        st.session_state.lista_n_opcoes = []
        
    st.markdown(f'## Opções: {st.session_state.lista_n_opcoes}')

    nova_opcao = st.text_input("Insira uma nova opção:")
    
    # botão para inserir opção digitada
    if st.button("Inserir opção"):
        st.session_state.lista_n_opcoes.append(nova_opcao)
        st.rerun()

    # botão para apagar lista de opções 
    if st.button("Apagar lista"):
        st.session_state.lista_n_opcoes.clear()
        st.rerun()

    # botão para gerar escolha aleatória na lista
    if st.button("Escolher", key="botao2"):
        escolha(st.session_state.lista_n_opcoes)
