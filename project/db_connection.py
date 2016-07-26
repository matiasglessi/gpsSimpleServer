import pymysql


class SqlConnection:
    def __init__(self):
        print('MySQL connector initialized')

    @staticmethod
    def connect():
        return pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='mysql')

    def consult(self, query, params=None):
        conn = self.connect()
        try:
            with conn.cursor() as cursor:
                # Read a all records
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                return cursor.fetchall()
        except:
            raise Exception('Exception trying to run query')
        finally:
            if conn:
                conn.close()

    def modify(self, query, params=None):
        print(query, params)
        conn = self.connect()
        try:
            with conn.cursor() as cursor:
                # Create a new record
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)

            conn.commit()
        except:
            raise Exception('Exception trying to run query')
        finally:
            if conn:
                conn.close()
