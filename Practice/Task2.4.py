# получение информации о всех заказах конерктоного пользователя - польз-ль вводит имя, находим в табл с заказами заказы его
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
        name_ = input("Введите Ваше имя: ");

        cursor.execute("select * from orders join customers on customers.id = orders.user_id WHERE customers.name = %s", (name_,))
        data = cursor.fetchone()
        print(f"order id: {data[0]},\n"
              f"customer name: {data[5]},\n"
              f"product_count: {data[1]},\n"
              f"product_id: {data[3]}")
        print('--------------------------------------')