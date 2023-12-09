import streamlit as st

df_data = st.session_state["data"]

st.set_page_config(
        layout="wide",
        page_title="FIFA 23"
)

clube = st.sidebar.selectbox("Clube",  df_data["Club"].value_counts().index)
df_clube = df_data[df_data["Club"] == clube]
jogadores = st.sidebar.selectbox("Jogador",  df_clube["Name"].value_counts().index)

df_jogador = df_clube[df_clube["Name"] == jogadores].iloc[0]
st.image(df_jogador["Photo"])
st.title(df_jogador["Name"])

st.markdown("**Clube:** {}".format(df_jogador["Club"]))
st.markdown("**Posição:** {}".format(df_jogador["Position"]))

col1, col2, col3, col4 = st.columns(4)
col1.markdown("**Idade:** {}".format(df_jogador["Age"]))
col2.markdown("**Altura:** {}".format(df_jogador["Height(cm.)"]/100))
col3.markdown("**Peso:** {:.2f}".format(df_jogador["Weight(lbs.)"]*0.453 ))

st.subheader("**Overall** {}".format(df_jogador["Overall"]))
st.progress(int(df_jogador["Overall"]))
col1, col2, col3, col4 = st.columns(4)
col1.metric(label="Valor de mercado", value=f"£ {df_jogador['Value(£)']:,}")
col2.metric(label="Remuneração semanal", value=f"£ {df_jogador['Wage(£)']:,}")
col3.metric(label="Cláusula de rescisão", value=f"£ {df_jogador['Release Clause(£)']:,}")