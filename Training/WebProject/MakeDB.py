import sqlite3

conn = sqlite3.connect("Library.db")
cursor = conn.cursor()

cursor.execute(
    """
create table if not exists books (
    id integer primary key autoincrement,
    title text,
    author text,
    pages integer,
    size integer,
    loc text
)"""
)

cursor.execute(
    """
create table if not exists users (
    id integer primary key autoincrement,
    username text unique not null,
    email text unique not null,
    password text not null,
    role text not null
)
"""
)
cursor.execute(
    "Insert or ignore into users (username, email, password, role) values (?, ?, ?, ?)",
    ("Admin", "Admin@gamil.com", "Admin", "admin"),
)


conn.commit()
conn.close()
print("DB Done.")
