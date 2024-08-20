from db_conn import conn

cur = conn.cursor()

cur.execute('CREATE TABLE product(product_id serial PRIMARY KEY,product_name varchar(255) NOT NULL,price decimal(10,2));')
cur.execute('CREATE TABLE category(category_id serial PRIMARY KEY,category_name varchar(255) NOT NULL,description varchar(255));')
cur.execute('CREATE TABLE brand(brand_id serial PRIMARY KEY,brand_name varchar(255) NOT NULL,description varchar(255));')

conn.commit()
cur.close()
conn.close()
