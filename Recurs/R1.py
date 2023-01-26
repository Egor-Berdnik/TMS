import psycopg2


def get_connection(dbname):
    connection psycopg2.connect(
        dbname=dbname,
        host='127.0.0.1',
        user='postgres',
        password='12345'
    )

    return get_connection


with get_connection('test_db') as conn:
    with conn.curser() as curser:
        query = """CREATE TABLE IF NOT EXISTS customers 
        (
        id serial primary key,
        name varchar(64),
        age int,
        address varchar(64),
        balance int
        );"""

        cursor.execute(query)
        conn.commit()