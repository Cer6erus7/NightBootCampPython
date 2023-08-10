import psycopg2


# Problem 1

# conn = psycopg2.connect(dbname='globus', user='cer6erus7')
# cur = conn.cursor()
# cur.execute("SELECT COUNT(DISTINCT product_name) FROM globus")
# print(cur.fetchall())
# conn.close()
# cur.close()


# Problem 2

# conn = psycopg2.connect(dbname='globus', user='cer6erus7')
# cur = conn.cursor()
# cur.execute("SELECT product_name, day_to_expire, SUM(product_amount) FROM narodnii GROUP BY product_name, day_to_expire HAVING 3 > day_to_expire ORDER BY SUM(product_amount) DESC")
# for i in cur.fetchall():
#     print(i)
#
# conn.close()
# cur.close()


# Problem 3

# conn = psycopg2.connect(dbname='globus', user='cer6erus7')
# cur = conn.cursor()
#
# cur.execute("SELECT 'globus' AS store, SUM(product_amount) AS total_quantity FROM globus WHERE product_name = 'Snikers' UNION ALL SELECT 'narodnii' AS store, SUM(product_amount) AS total_quantity FROM narodnii WHERE product_name = 'Snikers'")
#
# for i in cur.fetchall():
#     print(i)
#
# conn.close()
# cur.close()


# Problem 4

# conn = psycopg2.connect(dbname='globus', user='cer6erus7')
# cur = conn.cursor()
# cur.execute("SELECT product_name, product_amount, product_type_id, day_to_expire FROM globus WHERE product_type_id = day_to_expire;")
# print("globus")
# for i in cur.fetchall():
#     print(i)
#
# cur.execute("SELECT product_name, product_amount, product_type_id, day_to_expire FROM globus WHERE product_type_id = day_to_expire;")
# print("\nnarodnii")
# for i in cur.fetchall():
#     print(i)
#
# conn.close()
# cur.close()


# Problem 5

# conn = psycopg2.connect(dbname='globus', user='cer6erus7')
# cur = conn.cursor()
# cur.execute("SELECT globus.product_name FROM globus FULL JOIN narodnii USING(product_name) WHERE narodnii.day_to_expire = globus.day_to_expire")
#
# for i in cur.fetchall():
#     print(i)
#
# conn.close()
# cur.close()


# Problem 6

# conn = psycopg2.connect(dbname='globus', user='cer6erus7')
# cur = conn.cursor()
# cur.execute("SELECT product_amount FROM globus WHERE product_name = 'Piyaz'")
# print(cur.fetchall())
# conn.close()
# cur.close()


# Problem 9

# conn = psycopg2.connect(dbname='globus', user='cer6erus7')
# cur = conn.cursor()
# cur.execute("SELECT * FROM narodnii WHERE product_amount BETWEEN 200 AND 1000")
#
# for i in cur.fetchall():
#     print(i)
#
# conn.close()
# cur.close()


# Problem 10

# conn = psycopg2.connect(dbname='globus', user='cer6erus7')
# cur = conn.cursor()
# cur.execute("SELECT globus.date_delivered, narodnii.date_delivered FROM globus INNER JOIN narodnii USING(product_name)")
#
# for i in cur.fetchall():
#     print(i)
#
# conn.close()
# cur.close()


# Problem 11

# conn = psycopg2.connect(dbname='globus', user='cer6erus7')
# cur = conn.cursor()
# cur.execute("SELECT globus.product_name, narodnii.product_name FROM globus LEFT JOIN narodnii USING(product_name)")
#
# for i in cur.fetchall():
#     print(i)
#
# conn.close()
# cur.close()


# Problem 12

# conn = psycopg2.connect(dbname='globus', user='cer6erus7')
# cur = conn.cursor()
# cur.execute("SELECT globus.product_name, narodnii.product_name FROM globus RIGHT JOIN narodnii USING(product_name)")
#
# for i in cur.fetchall():
#     print(i)
#
# conn.close()
# cur.close()


# Problem 14

# conn = psycopg2.connect(dbname='globus', user='cer6erus7')
# cur = conn.cursor()
# cur.execute("SELECT * FROM globus CROSS JOIN narodnii WHERE globus.product_amount = narodnii.product_amount")
#
# for i in cur.fetchall():
#     print(i)
#
# conn.close()
# cur.close()


# Problem 15

# conn = psycopg2.connect(dbname='globus', user='cer6erus7')
# cur = conn.cursor()
# cur.execute("SELECT product_name FROM globus WHERE product_name LIKE '%a' OR product_name LIKE '%b' OR product_name LIKE '%c' OR product_name LIKE '%d' OR product_name LIKE '%e' OR product_name LIKE '%f' OR product_name LIKE '%g'")
#
# for i in cur.fetchall():
#     print(i)
#
# conn.close()
# cur.close()

