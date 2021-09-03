import pandas as pd
from sqlalchemy import create_engine
engine = create_engine('sqlite:///product_data.sqlite')
sales = pd.read_sql_query('SELECT * from sales', engine)
orders = pd.read_sql_query('SELECT * from orders', engine)
low_inventory = pd.read_sql_query('SELECT * from inventory where (Pencils < 200) or (Pens < 200) or (Erasers < 200) or (Paper < 300) ',engine)
print(low_inventory)