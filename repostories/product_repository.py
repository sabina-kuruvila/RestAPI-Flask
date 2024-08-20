from db.db_conn import conn

class ProductRepository:
    def fetch_all_products(self):
        try:
            cur = conn.cursor()
            cur. execute ('SELECT product_id, product_name, price FROM product')
            rows = cur.fetchall()
            products = [{"product_id":row[0],"product_name":row[1],"price":row[2]} for row in rows]
            return products
        finally:
            cur.close()
        

    def fetch_product_by_id(self,id):
        try:

            cur = conn.cursor()
            cur. execute("SELECT product_id, product_name, price FROM product WHERE product_id = %s",(id,))
            data = cur.fetchone()
            print(data, type(data))
            if data:
                product = {
                    "product_id":data[0],
                    "product_name":data[1],
                    "price":data[2]
                }
                return product
            else:
                return None
        finally:
                cur.close()


    def add_product(self,product_name,price):
        cur = conn.cursor()
        try:        
            cur. execute ("INSERT INTO product(product_name,price) VALUES(%s,%s) RETURNING product_id",(product_name,price))
            data = cur.fetchone() 
            conn.commit()
            print(data,type(data))
            return data[0]
        except Exception as e:
            print(f"Insert failed:{e}")
            conn.rollback()
            return None
        finally:
            cur.close()

    def update_product_data(self,product_id,product_name,price):
        cur = conn.cursor()
        try:
            cur.execute('UPDATE product SET product_name =%s,price=%s WHERE product_id =%s',(product_name,price,product_id))
            conn.commit()
            return cur.rowcount
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cur.close()

        
    def delete_product_data(self,product_id):
        cur = conn.cursor()
        try:
            cur.execute("DELETE FROM product WHERE product_id =%s;",(product_id,))
            conn.commit()
            return cur.rowcount
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cur.close()