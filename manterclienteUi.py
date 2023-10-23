import streamlit as st
import pandas as pd
from views import View
import time

class UI:
  def main():
    st.header("Cadastro de cliente")
    tab1, tab2, tab3, tab4 = st.tabs(['Listar', 'Inserir', 'Atualizar', 'Excluir'])
    with tab1:
      UI.cliente_listar()
    with tab2:
      UI.cliente_inserir()
    with tab3:
      UI.cliente_atualizar()
    with tab4:
      UI.cliente_excluir()
      
  def cliente_inserir():
    nome = st.text_input('Insira o nome do cliente')
    email = st.text_input('Insira o email do cliente')
    fone = st.text_input('Insira o número do cliente')
    if st.button("Inserir"):
      View.cliente_inserir(nome, email, fone)
      st.success("Cliente inserido com sucesso")
      time.sleep(2)
      st.rerun()

  def cliente_listar():
    clientes = View.cliente_listar()
    dic = []
    for c in clientes:
      dic.append(c.__dict__)
    df = pd.DataFrame(dic)
    st.dataframe(df)

  def cliente_atualizar():
    clientes = View.cliente_listar()
    op = st.selectbox("Atualização de clientes", clientes)
    nome = st.text_input('Insira o nome')
    email = st.text_input('Insira o email')
    fone = st.text_input('Insira o número')
    if st.button("Atualizar"):
      id = op.getId()
      View.cliente_atualizar(id, nome, email, fone)
      st.success("Cliente atualizado com sucesso")
      time.sleep(2)
      st.rerun()

  def cliente_excluir():
    clientes = View.cliente_listar()
    op = st.selectbox("Clientes", clientes)
    if st.button("Excluir"):
      id = op.getId()
      View.cliente_excluir(id)
      st.success("Cliente excluído com sucesso")
      time.sleep(2)
      st.rerun()
