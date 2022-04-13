import sqlite3

sq_conn = sqlite3.connect('votes.db')

table1 = """
create table if not exists votes(
id integer primary key,
ivan integer,
farid integer
);
"""

cursor = sq_conn.cursor()
cursor.execute(table1)
sq_conn.commit()
cursor.close()
