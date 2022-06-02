### -*-       Coding: utf-8         -*-
# Create an empty database with my usual client for testing.

import sqlite3

conn = None

try:
    conn = sqlite3.connect("FACTURE.sqlt")
except sqlite3.Error as e:
    print(e)

with open('SQLCREATE/CREATE_TABLE.sql', 'r', encoding="utf-8") as sql_file:
    sql_script = sql_file.read()

conn.execute('PRAGMA encoding="utf-8"')
print(sql_script)


cur = conn.cursor()
cur.executescript(sql_script)
conn.commit()
conn.close()
