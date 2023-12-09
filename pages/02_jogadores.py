import streamlit as st

df_data = st.session_state["data"]
df_data

clube = st.sidebar.selectbox("Clube",  df_data["Club"].value_counts().index)
df_clube = df_data[df_data["Club"] == clube]
jogadores = st.sidebar.selectbox("Jogador",  df_clube["Name"].value_counts().index)

df_jogador = df_clube[df_clube["Name"] == jogadores].iloc[0]
st.image(df_jogador["Photo"])
st.title(df_jogador["Name"])