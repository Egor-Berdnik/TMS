import psycopg2


def get_connection(dbname):
    connection = psycopg2.connect(
        dbname=dbname,
        host='127.0.0.1',
        user='postgres',
        password='88488848'
    )

    return connection


with get_connection('dbname') as conn:
    with conn.cursor() as cursor:
        query = """UPDATE products SET discount = 5 WHERE id = 1; 
        UPDATE products SET discount = 10 WHERE id = 2"""
        cursor.execute(query)
        conn.commit()

        # query = """DELETE FROM products S WHERE id = 3;
        # DELETE FROM products S WHERE id = 4"""
        # cursor.execute(query)
        # conn.commit()