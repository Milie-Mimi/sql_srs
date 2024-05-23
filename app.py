# pylint: disable=missing-module-docstring
import ast

import duckdb
import streamlit as st

# ------------------------------------------------------------
# CONNECTION BDD
# ------------------------------------------------------------
con = duckdb.connect(database="data/exercises_sql_tables.duckdb", read_only=False)

# ANSWER_STR = """
# SELECT * FROM beverages
# CROSS JOIN food_items"""


# solution_df = duckdb.sql(ANSWER_STR).df()


# ------------------------------------------------------------
# SIDEBAR
# ------------------------------------------------------------
with st.sidebar:
    theme = st.selectbox(
        "What would you like to review",
        ("cross_joins", "GroupBy", "window_functions"),
        index=None,
        placeholder="Select a theme...",
    )
    st.write("You selected:", theme)

    exercise = con.execute(f"SELECT * FROM memory_state WHERE theme = '{theme}'").df()
    st.write(exercise)


# ------------------------------------------------------------
# HEADER
# ------------------------------------------------------------
st.header("enter your code:")

# ------------------------------------------------------------
# QUERY
# ------------------------------------------------------------
query = st.text_area(label="code SQL", key="user_input")
if query:
    result = con.execute(query).df()
    st.dataframe(result)
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

# ------------------------------------------------------------
# TABS
# ------------------------------------------------------------
tab1, tab2 = st.tabs(["Tables", "Solution"])

with tab1:
    exercise_tables = ast.literal_eval(
        exercise.loc[0, "tables"]
    )  # pour garder le format liste et non str
    for table in exercise_tables:
        st.write(f"table: {table}")
        df_table = con.execute(f"SELECT * FROM {table}").df()
        st.dataframe(df_table)

with tab2:
    exercise_name = exercise.loc[0, "exercise_name"]
    with open(f"answers/{exercise_name}.sql", "r") as f:
        answer = f.read()
    st.write(answer)


# streamlit run app.py
