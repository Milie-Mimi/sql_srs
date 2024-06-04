# pylint: disable=missing-module-docstring
import os
import logging
import duckdb
import streamlit as st
from datetime import date, timedelta

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
# CONFIG PAGE
# ------------------------------------------------------------
st.set_page_config(
    page_title="SQL_SRS",
    page_icon="🎯",
    layout="wide",
)

st.markdown(
    """
                <style>
                .text-font {
                    font-size:20px;
                    text-align: justify;
                }
                </style>
                """,
    unsafe_allow_html=True,
)

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
    st.table(result)
    try:
        result = result[solution_df.columns]
        st.dataframe(result.compare(solution_df))
        if result.compare(solution_df).shape == (0, 0):
            st.write("Correct !")
            st.balloons()
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
    st.image("pictures/DuckDB.PNG", caption="DuckDB logo")
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
st.header("SQL questions with :blue[SRS] :sunglasses:", divider="rainbow")

with st.expander("**What is SRS?**"):
    st.write(
        """
        Spaced repetition is an evidence-based learning technique that is usually performed with flashcards. 
        **Newly introduced and more difficult flashcards are shown more frequently**, while older and less difficult 
        flashcards are shown less frequently in order to exploit the psychological spacing effect. 
        The use of spaced repetition has been proven to **increase the rate of learning**.

        Spaced repetition is commonly applied in contexts in which **a learner must acquire many items 
        and retain them indefinitely in memory**. 
        It is, therefore, well suited for the problem of vocabulary acquisition in the course of 
        second-language learning (works also for programming language).

        Source: Wikipedia
    """
    )
    st.image("pictures/SRS.JPG")

st.subheader("Question:")
with open(f"questions/{exercise_name}.txt", "r") as f:
    question = f.read()

st.write(question)


# ------------------------------------------------------------
# QUERY
# ------------------------------------------------------------
st.subheader("Réponse")
form = st.form("my_form")
query = form.text_area(label="code SQL", key="user_input")
form.form_submit_button("Submit")

if query:
    check_users_solution(query)

# cols_srs = st.columns(3)
for n_days in [2, 7, 21]:
    if st.button(f"Revoir dans {n_days} jours"):
        next_review = date.today() + timedelta(days=n_days)
        con.execute(
            f"UPDATE memory_state SET last_reviewed = '{next_review}' WHERE exercise_name = '{exercise_name}'"
        )
        st.rerun()

if st.button("Reset"):
    con.execute(f"UPDATE memory_state SET last_reviewed = '1970-01-01'")
    st.rerun()


# ------------------------------------------------------------
# TABS
# ------------------------------------------------------------
tab1, tab2 = st.tabs(["Tables", "Solution"])

with tab1:
    exercise_tables = exercise.loc[0, "tables"]
    exercise_tables_len = len(exercise_tables)
    cols = st.columns(exercise_tables_len)
    for i in range(0, exercise_tables_len):
        cols[i].write(exercise_tables[i])
        df_table = con.execute(f"SELECT * FROM {exercise_tables[i]}").df()
        cols[i].table(df_table)


with tab2:
    st.write(answer)
    df_answer = con.execute(answer).df()
    st.table(df_answer)


# streamlit run app.py


# To DO:
# Ajouter des Thèmes et des questions
# Boutons revoir en colonnes
# -> Rendre l'UI encore plus agréable
# -> Créer un système d'authentification pour avoir plusieurs utilisateurs
# -> Formatter le SQL qui affiche la réponse
# -> Si vous en voyez d'autres, lancez vous :)
#
#
# Je rembourse l'inscription au programme à celui ou celle qui fera la plus belle app d'ici début Décembre :D
# (Personne ne va oser se lancer, si vous le faites vous serez en compétition contre même pas 5 personnes ;) )
