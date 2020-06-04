import sqlite3

conn = sqlite3.connect('quotes.db')
curr = conn.cursor()

curr.execute("""create table quotes_tb(
    title text,
    author text,
    names text
)""")

curr.execute("""insert into quotes_tb values(
    'A',
    "B",
    'C'
)""")

conn.commit()
conn.close()