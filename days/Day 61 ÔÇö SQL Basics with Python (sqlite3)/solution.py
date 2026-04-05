# Day 61 — SQL Basics — SOLUTIONS
import sqlite3
from contextlib import contextmanager

def setup_db():
    conn=sqlite3.connect(':memory:')
    cur=conn.cursor()
    cur.execute('CREATE TABLE games (id INTEGER PRIMARY KEY, title TEXT, genre TEXT, price REAL)')
    games=[('Tekken 8','Fighting',1299),('Mortal Kombat 1','Fighting',1099),
           ('EA FC 25','Sports',1199),('Elden Ring','Action/RPG',1199),('GTA V','Open World',599)]
    cur.executemany('INSERT INTO games (title,genre,price) VALUES (?,?,?)',games)
    conn.commit(); return conn

def get_games_by_genre(conn,genre):
    cur=conn.cursor()
    cur.execute('SELECT * FROM games WHERE genre=?',(genre,))
    return cur.fetchall()

def update_price(conn,title,new_price):
    conn.execute('UPDATE games SET price=? WHERE title=?',(new_price,title))
    conn.commit()

def delete_game(conn,title):
    conn.execute('DELETE FROM games WHERE title=?',(title,))
    conn.commit()

def genre_stats(conn):
    cur=conn.cursor()
    cur.execute('SELECT genre,COUNT(*) as cnt,AVG(price) as avg_price FROM games GROUP BY genre ORDER BY cnt DESC')
    return cur.fetchall()

def search_games(conn,keyword):
    cur=conn.cursor()
    cur.execute('SELECT * FROM games WHERE title LIKE ?',(f'%{keyword}%',))
    return cur.fetchall()

@contextmanager
def database(filepath):
    conn=sqlite3.connect(filepath)
    conn.row_factory=sqlite3.Row
    try:
        yield conn.cursor()
        conn.commit()
    except Exception:
        conn.rollback(); raise
    finally:
        conn.close()
