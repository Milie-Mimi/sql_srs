# pylint: disable=missing-module-docstring
import os
import logging
import duckdb
import streamlit as st

# ------------------------------------------------------------
# SETUP
# ------------------------------------------------------------
# Création du dossier data
if "data" not in os.listdir():
    print("creating folder data")
    logging.error(os.listdir())
    logging.error("creating folder data")
    os.mkdir("data")

# On lance init_db.py pour créer la BDD
if "exercises_sql_tables.duckdb" not in os.listdir("data"):
    exec(open("init_db.py").read())
    # subprocess.run(["python", "init_db.py"])

con = duckdb.connect(database="data/exercises_sql_tables.duckdb", read_only=False)


# ------------------------------------------------------------
# FONCTIONS
# ------------------------------------------------------------
def check_users_solution(user_query: str) -> None:
    """
    Checks that user SQL query is correct by:
    1: checking the columns
    2: checking the values
    :param user_query: a string containing the query inserted by the user
    """
    result = con.execute(user_query).df()
    st.dataframe(result)
    try:
        result = result[solution_df.columns]
        st.dataframe(result.compare(solution_df))
    except KeyError as e:
        st.write("Some columns are missing")
    n_lines_difference = result.shape[0] - solution_df.shape[0]
    if n_lines_difference != 0:
        st.write(
            f"result has a {n_lines_difference} lines difference with the solution"
        )


# ------------------------------------------------------------
# SIDEBAR
# ------------------------------------------------------------
with st.sidebar:
    available_themes_df = con.execute("SELECT DISTINCT theme FROM memory_state").df()
    theme = st.selectbox(
        "What would you like to review",
        available_themes_df["theme"].unique(),
        index=None,
        placeholder="Select a theme...",
    )
    if theme:
        st.write("You selected:", theme)
        select_exercise_query = f"SELECT * FROM memory_state WHERE theme = '{theme}'"
    else:
        select_exercise_query = f"SELECT * FROM memory_state"

    exercise = (
        con.execute(select_exercise_query)
        .df()
        .sort_values("last_reviewed")
        .reset_index(drop=True)
    )
    st.write(exercise)
    exercise_name = exercise.loc[0, "exercise_name"]
    with open(f"answers/{exercise_name}.sql", "r") as f:
        answer = f.read()

    solution_df = con.execute(answer).df()

# ------------------------------------------------------------
# HEADER
# ------------------------------------------------------------
st.header("Question:")
with open(f"questions/{exercise_name}.txt", "r") as f:
    question = f.read()

st.write(question)


# ------------------------------------------------------------
# QUERY
# ------------------------------------------------------------
st.header("Réponse")
query = st.text_area(label="code SQL", key="user_input")
if query:
    check_users_solution(query)


# ------------------------------------------------------------
# TABS
# ------------------------------------------------------------
tab1, tab2 = st.tabs(["Tables", "Solution"])

with tab1:
    cols = st.columns(2)
    exercise_tables = exercise.loc[0, "tables"]
    #st.write(exercise_tables[0])
    for i in range(0, 2):
        cols[i].write(exercise_tables[i])
        df_table = con.execute(f"SELECT * FROM {exercise_tables[i]}").df()
        cols[i].table(df_table)
    #cols[i].write(exercise_tables[i])
    #df_table = con.execute(f"SELECT * FROM {exercise_tables[i]}").df()
    #cols[i].table(df_table)
#    for table in exercise_tables:
#        #col1, col2 = st.columns(2)
#        for col in st.columns(2):
#            col.write(f"table: {table}")
#            df_table = con.execute(f"SELECT * FROM {table}").df()
#            col.table(df_table)


# A modifier pour avoir les tables à côté
#with tab1:
#    exercise_tables = exercise.loc[0, "tables"]
#    for table in exercise_tables:
#        #col1, col2 = st.columns(2)
#        for col in st.columns(2):
#            col.write(f"table: {table}")
#            df_table = con.execute(f"SELECT * FROM {table}").df()
#            col.table(df_table)


with tab2:
    st.write(answer)
    df_answer = con.execute(answer).df()
    st.table(df_answer)



# streamlit run app.py
