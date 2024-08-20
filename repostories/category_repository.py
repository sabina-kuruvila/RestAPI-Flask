from db.db_conn import conn

class CategoryRepository:
    def fetch_all_categories(self):
        try:
            cur = conn.cursor()
            cur. execute ('SELECT category_id, category_name, description FROM category')
            rows = cur.fetchall()
            categories = [{"category_id":row[0],"category_name":row[1],"description":row[2]} for row in rows]
            return categories
        finally:
            cur.close()
        

    def fetch_category_by_id(self,id):
        try:

            cur = conn.cursor()
            cur. execute("SELECT category_id, category_name, description FROM category WHERE category_id = %s",(id,))
            data = cur.fetchone()
            print(data, type(data))
            if data:
                category = {
                    "category_id":data[0],
                    "category_name":data[1],
                    "description":data[2]
                }
                return category
            else:
                return None
        finally:
                cur.close()


    def add_category(self,category_name,description):
        cur = conn.cursor()
        try:        
            cur. execute ("INSERT INTO category(category_name,description) VALUES(%s,%s) RETURNING category_id",(category_name,description))
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

    def update_category_data(self,category_id,category_name,description):
        cur = conn.cursor()
        try:
            cur.execute('UPDATE category SET category_name =%s,description=%s WHERE category_id =%s',(category_name,description,category_id))
            conn.commit()
            return cur.rowcount
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cur.close()

        
    def delete_category_data(self,category_id):
        cur = conn.cursor()
        try:
            cur.execute("DELETE FROM category WHERE category_id =%s;",(category_id,))
            conn.commit()
            return cur.rowcount
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cur.close()