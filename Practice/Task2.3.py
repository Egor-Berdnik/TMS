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

        cursor.execute("select * from products join category on products.category_id = category.id WHERE products.name = %s", (product_,))
        data = cursor.fetchone()
        print(f"product id: {data[0]},\n"
              f"product name: {data[1]},\n"
              f"product price: {data[2]},\n"
              f"product count: {data[3]},\n"
              f"product description: {data[4]},\n"
              f"product discount: {data[6]},\n"
              f"product category_id: {data[5]},\n"
              f"product category name: {data[8]}")
        print('--------------------------------------')

