import sqlite3

conn = sqlite3.connect("Applications.db")
cursor = conn.cursor()

cursor.execute(
    """
create table if not exists applications (
    id integer primary key autoincrement,
    name text,
    email text,
    phone text,
    position text,
    message text,
    resume text
)
"""
)

cursor.execute(
    """
create table if not exists admin(
    id integer primary key,
    username text,
    password text
)
"""
)

cursor.execute("Insert or ignore into admin values (1, 'RajKamal', 'HolyWhat?')")

conn.commit()
conn.close()
print("DB Done.")
