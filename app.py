# Création d'un interpréteur de requêtes SQL qui nous permet d'aller taper dans une table et d'afficher les résultats
# dans l'application

import streamlit as st
import pandas as pd
import duckdb

st.write("Hello world!")
data = {"a": [1, 2, 3], "b": [4, 5, 6]}
df = pd.DataFrame(data)

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
    sql_query = st.text_area(label="entrez votre input")
    #st.write(input_text)
    #st.dataframe(df)

    df_after_sql_query = duckdb.sql(sql_query).df()
    st.dataframe(df_after_query)

with tab2:
    st.header("A dog")

with tab3:
    st.header("An owl")
