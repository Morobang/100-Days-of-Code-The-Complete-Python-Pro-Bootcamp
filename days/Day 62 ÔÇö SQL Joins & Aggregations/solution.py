# Day 62 — SQL Joins — SOLUTIONS
import sqlite3

def setup_schema():
    conn=sqlite3.connect(':memory:')
    conn.executescript('''
    CREATE TABLE products (id INT PRIMARY KEY, name TEXT, price REAL);
    CREATE TABLE customers (id INT PRIMARY KEY, name TEXT, city TEXT);
    CREATE TABLE orders (id INT PRIMARY KEY, customer_id INT, order_date TEXT);
    CREATE TABLE order_items (id INT PRIMARY KEY, order_id INT, product_id INT, qty INT);
    INSERT INTO customers VALUES (1,'Rocket','Pretoria'),(2,'Alice','Cape Town'),(3,'Bob','Durban');
    INSERT INTO products VALUES (1,'Tekken 8',1299),(2,'FC26',1199),(3,'KOF XV',999),(4,'Elden Ring',1199);
    INSERT INTO orders VALUES (1,1,'2025-01-10'),(2,1,'2025-02-15'),(3,2,'2025-01-20'),(4,3,'2025-03-01');
    INSERT INTO order_items VALUES (1,1,1,1),(2,1,2,1),(3,2,3,1),(4,3,1,2),(5,4,4,1);
    ''')
    conn.commit(); return conn

def customer_totals(conn):
    cur=conn.cursor()
    cur.execute('''SELECT c.name, SUM(p.price*oi.qty) as total
                   FROM customers c JOIN orders o ON c.id=o.customer_id
                   JOIN order_items oi ON o.id=oi.order_id
                   JOIN products p ON oi.product_id=p.id
                   GROUP BY c.name ORDER BY total DESC''')
    return cur.fetchall()

def top_customers(conn,n):
    cur=conn.cursor()
    cur.execute('''SELECT c.name, SUM(p.price*oi.qty) as total
                   FROM customers c JOIN orders o ON c.id=o.customer_id
                   JOIN order_items oi ON o.id=oi.order_id
                   JOIN products p ON oi.product_id=p.id
                   GROUP BY c.name ORDER BY total DESC LIMIT ?''',(n,))
    return cur.fetchall()

def unordered_products(conn):
    cur=conn.cursor()
    cur.execute('SELECT p.name FROM products p LEFT JOIN order_items oi ON p.id=oi.product_id WHERE oi.id IS NULL')
    return cur.fetchall()

def monthly_revenue(conn):
    cur=conn.cursor()
    cur.execute('''SELECT strftime('%Y-%m',o.order_date) as month, SUM(p.price*oi.qty) as rev
                   FROM orders o JOIN order_items oi ON o.id=oi.order_id
                   JOIN products p ON oi.product_id=p.id
                   GROUP BY month ORDER BY month''')
    return cur.fetchall()

def second_highest_spender(conn):
    cur=conn.cursor()
    cur.execute('''SELECT name FROM (
                     SELECT c.name, SUM(p.price*oi.qty) as total
                     FROM customers c JOIN orders o ON c.id=o.customer_id
                     JOIN order_items oi ON o.id=oi.order_id
                     JOIN products p ON oi.product_id=p.id
                     GROUP BY c.name ORDER BY total DESC
                   ) LIMIT 1 OFFSET 1''')
    row=cur.fetchone()
    return row[0] if row else None
