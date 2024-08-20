from db.db_conn import conn
class BrandRepository():
    def fetch_all_brands(self):
        try:
            cur = conn.cursor()
            cur. execute ('SELECT brand_id, brand_name, description FROM brand')
            rows = cur.fetchall()
            brands = [{"brand_id":row[0],"brand_name":row[1],"description":row[2]} for row in rows]
            return brands
        finally:
            cur.close()
        

    def fetch_brand_by_id(self,id):
        try:

            cur = conn.cursor()
            cur. execute("SELECT brand_id, brand_name, description FROM brand WHERE brand_id = %s",(id,))
            data = cur.fetchone()
            print(data, type(data))
            if data:
                brand = {
                    "brand_id":data[0],
                    "brand_name":data[1],
                    "description":data[2]
                }
                return brand
            else:
                return None
        finally:
                cur.close()


    def add_brand(self,brand_name,description):
        cur = conn.cursor()
        try:        
            cur. execute ("INSERT INTO brand(brand_name,description) VALUES(%s,%s) RETURNING brand_id",(brand_name,description))
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

    def update_brand_data(self,brand_id,brand_name,description):
        cur = conn.cursor()
        try:
            cur.execute('UPDATE brand SET brand_name =%s,description=%s WHERE brand_id =%s',(brand_name,description,brand_id))
            conn.commit()
            return cur.rowcount
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cur.close()

        
    def delete_brand_data(self,brand_id):
        cur = conn.cursor()
        try:
            cur.execute("DELETE FROM brand WHERE brand_id =%s;",(brand_id,))
            conn.commit()
            return cur.rowcount
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cur.close()


