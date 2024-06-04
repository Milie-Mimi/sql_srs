import io

import pandas as pd
import duckdb

con = duckdb.connect(database="data/exercises_sql_tables.duckdb", read_only=False)

# ------------------------------------------------------------
# EXERCISES LIST
# ------------------------------------------------------------

data = {
    "theme": [
        "cross_joins",
        "cross_joins",
        "cross_joins",
        "inner_joins",
        "left_joins",
        "left_joins",
        "left_joins",
        "full_outer_joins",
    ],
    "exercise_name": [
        "cross_joins_1",
        "cross_joins_2",
        "cross_joins_3",
        "inner_joins_1",
        "left_joins_1",
        "left_joins_2",
        "left_joins_3",
        "full_outer_joins_1",
    ],
    "tables": [
        ["beverages", "food_items"],
        ["sizes", "trademarks"],
        ["hours", "quarters"],
        ["salaries", "seniorities"],
        ["orders", "customers", "products", "order_details"],
        ["orders", "customers", "products", "order_details"],
        ["orders", "customers", "products", "order_details"],
        ["df_customers", "df_stores", "df_store_products", "df_products"],
    ],
    "last_reviewed": [
        "1970-01-01",
        "1970-01-01",
        "1970-01-01",
        "1970-01-01",
        "1970-01-01",
        "1970-01-01",
        "1970-01-01",
        "1970-01-01",
    ],
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


hours = """
hour
08
09
10
11
12
"""
hours = pd.read_csv(io.StringIO(hours))
con.execute("CREATE TABLE IF NOT EXISTS hours AS SELECT * FROM hours")


quarters = """
quarter
00
15
30
45
"""
quarters = pd.read_csv(io.StringIO(quarters))
con.execute("CREATE TABLE IF NOT EXISTS quarters AS SELECT * FROM quarters")

# ------------------------------------------------------------
# INNER JOIN EXERCISES
# ------------------------------------------------------------
salaries = """
salary,employee_id
2000,1
2500,2
2200,3
"""
salaries = pd.read_csv(io.StringIO(salaries))
con.execute("CREATE TABLE IF NOT EXISTS salaries AS SELECT * FROM salaries")

seniorities = """
employee_id,seniority
1,2ans
2,4ans
"""
seniorities = pd.read_csv(io.StringIO(seniorities))
con.execute("CREATE TABLE IF NOT EXISTS seniorities AS SELECT * FROM seniorities")


# ------------------------------------------------------------
# LEFT JOIN EXERCISES
# ------------------------------------------------------------
orders_data = {"order_id": [1, 2, 3, 4, 5], "customer_id": [101, 102, 103, 104, 105]}
df_orders = pd.DataFrame(orders_data)
con.execute("CREATE TABLE IF NOT EXISTS orders AS SELECT * FROM df_orders")

customers_data = {
    "customer_id": [101, 102, 103, 104, 105, 106],
    "customer_name": [
        "Toufik",
        "Daniel",
        "Tancrède",
        "Kaouter",
        "Jean-Nicolas",
        "David",
    ],
}
df_customers = pd.DataFrame(customers_data)
con.execute("CREATE TABLE IF NOT EXISTS customers AS SELECT * FROM df_customers")

products_data = {
    "product_id": [101, 103, 104, 105],
    "product_name": ["Laptop", "Ipad", "Livre", "Petitos"],
    "product_price": [800, 400, 30, 2],
}
df_products = pd.DataFrame(products_data)
con.execute("CREATE TABLE IF NOT EXISTS products AS SELECT * FROM df_products")

order_details_data = {
    "order_id": [1, 2, 3, 4, 5],
    "product_id": [102, 104, 101, 103, 105],
    "quantity": [2, 1, 3, 2, 1],
}
df_order_details = pd.DataFrame(order_details_data)
con.execute(
    "CREATE TABLE IF NOT EXISTS order_details AS SELECT * FROM df_order_details"
)


# ------------------------------------------------------------
# FULL OUTER JOIN EXERCISES
# ------------------------------------------------------------
customers_data = {
    'customer_id': [11, 12, 13, 14, 15],
    'customer_name': ["Zeinaba", "Tancrède", "Israel", "Kaouter", "Alan"]
}
customers_data = pd.DataFrame(customers_data)
con.execute(
    "CREATE TABLE IF NOT EXISTS df_customers AS SELECT * FROM customers_data"
)

stores_data = {
    'store_id': [1, 2, 3, 4],
    'customer_id': [11, 12, 13, 15]
}
stores_data = pd.DataFrame(stores_data)
con.execute(
    "CREATE TABLE IF NOT EXISTS df_stores AS SELECT * FROM stores_data"
)

store_products_data = {
    'store_id': [1, 1, 1, 2, 2, 3, 4],
    'product_id': [101, 103, 105, 101, 103, 104, 105],
}
store_products_data = pd.DataFrame(store_products_data)
con.execute(
    "CREATE TABLE IF NOT EXISTS df_store_products AS SELECT * FROM store_products_data"
)

p_names = ["Cherry coke", "Laptop", "Ipad", "Livre",]
products_data = {
    'product_id': [100, 101, 103, 104],
    'product_name': p_names,
    'product_price': [3, 800, 400, 30]
}
products_data = pd.DataFrame(products_data)
con.execute(
    "CREATE TABLE IF NOT EXISTS df_products AS SELECT * FROM products_data"
)







con.close()


# python init_db.py
