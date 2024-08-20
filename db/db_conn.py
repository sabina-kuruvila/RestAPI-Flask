import psycopg2

conn = psycopg2.connect(dsn='postgresql://postgres:postgres123@localhost:5432/ecom_sample_db')