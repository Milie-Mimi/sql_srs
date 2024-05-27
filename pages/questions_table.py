import duckdb
import streamlit as st

# ------------------------------------------------------------
# CONFIG PAGE
# ------------------------------------------------------------
st.set_page_config(
    page_title="Questions_list",
    page_icon="📂",
    layout="wide",
)

# ------------------------------------------------------------
# CONFIG TEXTE
# ------------------------------------------------------------
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
# TITRE DE LA PAGE
# ------------------------------------------------------------
st.title("Table des différentes questions")

con = duckdb.connect(database="data/exercises_sql_tables.duckdb", read_only=False)
select_exercise_query = f"SELECT * FROM memory_state"


exercise = (
    con.execute(select_exercise_query)
    .df()
    .sort_values("last_reviewed")
    .reset_index(drop=True)
)
st.dataframe(exercise)


