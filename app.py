# pylint: disable=missing-module-docstring

import duckdb
import streamlit as st


# ------------------------------------------------------------
# CONNECTION BDD
# ------------------------------------------------------------

con = duckdb.connect(database="data/exercises_sql_tables.duckdb", read_only=False)

#ANSWER_STR = """
#SELECT * FROM beverages
#CROSS JOIN food_items"""


#solution_df = duckdb.sql(ANSWER_STR).df()


# ------------------------------------------------------------
# SIDEBAR
# ------------------------------------------------------------

with st.sidebar:
    theme = st.selectbox(
        "What would you like to review",
        ("cross_joins", "GroupBy", "Windows Functions"),
        index=None,
        placeholder="Select a theme...",
    )
    st.write("You selected:", theme)

    exercise = con.execute(f"SELECT * FROM memory_state WHERE theme = '{theme}'").df()
    st.write(exercise)

st.header("enter your code:")
query = st.text_area(label="code SQL", key="user_input")
#if query:
#    result = duckdb.sql(query).df()
#    st.dataframe(result)
#
#    try:
#        result = result[solution_df.columns]
#        st.dataframe(result.compare(solution_df))
#    except KeyError as e:
#        st.write("Some columns are missing")
#
#    n_lines_difference = result.shape[0] - solution_df.shape[0]
#    if n_lines_difference != 0:
#        st.write(
#            f"result has a {n_lines_difference} lines difference with the solution"
#        )
#
#
#tab1, tab2 = st.tabs(["Tables", "Solution"])
#
#with tab1:
#    st.write("table: beverages")
#    st.dataframe(beverages)
#    st.write("table: food_items")
#    st.dataframe(food_items)
#    st.write("expected:")
#    st.dataframe(solution_df)
#
#with tab2:
#    st.write(ANSWER_STR)

# streamlit run app.py
