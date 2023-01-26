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
        product_ = input("Введите имя продукта: ");

        # query = """SELECT name, price FROM products WHERE id=2"""
        cursor.execute("SELECT name, price FROM products VALUE (%s, %s)", product_)
        data = cursor.fetchone()
        for item in data:
            print(f"product name: {item[0]},\n"
                  f"product price: {item[1]},\n"
                  f"product count: {item[2]},\n"
                  f"product description: {item[3]},\n"
                  f"product category name; {item[6]}")
            print('--------------------------------------')
