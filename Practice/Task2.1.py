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
        name_ = str(input("Введите Ваше имя: "));
        age_ = int(input("Введите Ваш возраст: "));
        address_ = input("Введите Ваш адрес: ");
        balance_ = int(input("Введите Ваш баланс: "));

        customer = (name_, age_, address_, balance_)

        cursor.execute("INSERT INTO customers (name, age, address, balance) VALUES (%s, %s, %s, %s)", customer)
 