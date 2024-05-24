import io
import random
from datetime import timedelta, datetime

import pandas as pd
import duckdb

con = duckdb.connect(database="data/exercises_sql_tables.duckdb", read_only=False)

# ------------------------------------------------------------
# EXERCISES LIST
# ------------------------------------------------------------

data = {
    "theme": ["cross_joins", "cross_joins", "cross_joins", "inner_joins"],
    "exercise_name": ["beverages_and_food", "sizes_and_trademarks", "hours_and_quarters", "salaries_and_seniorities"],
    "tables": [["beverages", "food_items"], ["sizes", "trademarks"], ["hours", "quarters"], ["salaries", "seniorities"]],
    "last_reviewed": ["1970-01-01", "1970-01-01", "1970-01-01", "1960-01-01"],
}
memory_state_df = pd.DataFrame(data)
con.execute("CREATE TABLE IF NOT EXISTS memory_state AS SELECT * FROM memory_state_df")


# ------------------------------------------------------------
# CROSS JOIN EXERCISES
# ------------------------------------------------------------
csv = """
beverage,price
orange juice,2.5
Expresso,2
Tea,3
"""
beverages = pd.read_csv(io.StringIO(csv))
con.execute("CREATE TABLE IF NOT EXISTS beverages AS SELECT * FROM beverages")

csv2 = """
food_item,food_price
cookie juice,2.5
chocolatine,2
muffin,3
"""
food_items = pd.read_csv(io.StringIO(csv2))
con.execute("CREATE TABLE IF NOT EXISTS food_items AS SELECT * FROM food_items")


sizes = """
size
XS
M
L
XL
"""
sizes = pd.read_csv(io.StringIO(sizes))
con.execute("CREATE TABLE IF NOT EXISTS sizes AS SELECT * FROM sizes")

trademarks = """
trademark
Nike
Asphalte
Abercrombie
Lewis
"""
trademarks = pd.read_csv(io.StringIO(trademarks))
con.execute("CREATE TABLE IF NOT EXISTS trademarks AS SELECT * FROM trademarks")


hours = '''
hour
08
09
10
11
12
'''
hours = pd.read_csv(io.StringIO(hours))
con.execute("CREATE TABLE IF NOT EXISTS hours AS SELECT * FROM hours")


quarters = '''
quarter
00
15
30
45
'''
quarters = pd.read_csv(io.StringIO(quarters))
con.execute("CREATE TABLE IF NOT EXISTS quarters AS SELECT * FROM quarters")

# ------------------------------------------------------------
# INNER JOIN EXERCISES
# ------------------------------------------------------------
salaries = '''
salary,employee_id
2000,1
2500,2
2200,3
'''
salaries = pd.read_csv(io.StringIO(salaries))
con.execute("CREATE TABLE IF NOT EXISTS salaries AS SELECT * FROM salaries")

seniorities = '''
employee_id,seniority
1,2ans
2,4ans
'''
seniorities = pd.read_csv(io.StringIO(seniorities))
con.execute("CREATE TABLE IF NOT EXISTS seniorities AS SELECT * FROM seniorities")







con.close()
