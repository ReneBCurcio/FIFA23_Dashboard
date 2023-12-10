import streamlit as st
import pandas as pd

st.set_page_config(
        layout="wide",
        page_title="FIFA 23")

df_data = st.session_state["data"]

clube = st.sidebar.selectbox("Clube",  df_data["Club"].value_counts().index)
df_clube = df_data[df_data["Club"] == clube]
df_filtrada = df_data[(df_data["Club"] == clube)].set_index("Name")

st.image(df_filtrada.iloc[0]["Club Logo"])
st.markdown("## {}".format(clube))

columns = ["Age", "Photo", "Flag", "Overall", 'Value(£)', 'Wage(£)', 'Joined', 
           'Height(cm.)', 'Weight(lbs.)',
           'Contract Valid Until', 'Release Clause(£)']

st.dataframe(df_filtrada[columns],
             column_config={
                 "Overall": st.column_config.ProgressColumn(
                     "Overall", format="%d", min_value=0, max_value=100
                 ),
                 "Wage(£)": st.column_config.ProgressColumn("Weekly Wage", format="£%f", 
                                                    min_value=0, max_value=df_filtrada["Wage(£)"].max()),
                "Photo": st.column_config.ImageColumn(),
                "Flag": st.column_config.ImageColumn("Country"),
             })

    