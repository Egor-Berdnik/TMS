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

        query = """CREATE TABLE IF NOT EXISTS category
        (
        id serial primary key,
        name varchar(64)
        );"""

        cursor.execute(query)

        query = """CREATE TABLE IF NOT EXISTS products
        (
        id serial primary key,
        name varchar(64),
        price int,
        count int,
        description varchar(256),
        category_id serial references category(id)
        );"""
        cursor.execute(query)

        query = """CREATE TABLE IF NOT EXISTS orders
        (
        id serial primary key,
        product_count int,
        user_id int references customers(id),
        product_id int references products(id)
        );"""
        cursor.execute(query)

        conn.commit()

    # with conn.cursor() as cursor:
    #     query = """INSERT INTO customers (name, age, address, balance)
    #     VALUES ('John', 25, 'some address 1', 1000);"""
    #
    #     cursor.execute(query)
    #
    #     query = """INSERT INTO customers (name, age, address, balance)
    #     VALUES ('Mary', 24, 'some address 2', 2000);"""
    #
    #     cursor.execute(query)
    #
    #     query = """INSERT INTO category (name)
    #     VALUES ('category 1'), ('category 2');"""
    #
    #     query = """INSERT INTO products (name, price, count, description, category_id)
    #     VALUES ('product 1', 100, 10, 'some description 1', 1),
    #     ('product 2', 70, 15, 'some description 2', 2);"""
    #
    #     cursor.execute(query)
    #
    #     query = """INSERT INTO orders (product_count, user_id, product_id)
    #     VALUES (2, 1, 1), (5, 2, 2);"""
    #
    #     cursor.execute(query)
    #     conn.commit()

    # with conn.cursor() as cursor:
    #     query = """SELECT * FROM category;"""
    #     cursor.execute(query)
    #     data = cursor.fetchall()
    #     print(f"category data: {data}")
    #
    #     query = """SELECT * FROM products
    #     JOIN category ON products.category_id = category_id;"""
    #     cursor.execute(query)
    #     data = cursor.fetchall()
    #     for item in data:
    #         print(f"product id: {item[0]},\n"
    #               f"product name: {item[1]},\n"
    #               f"product price: {item[2]},\n"
    #               f"product count: {item[3]},\n"
    #               f"product description: {item[4]},\n"
    #               f"product category id: {item[6]},\n"
    #               f"product category name; {item[7]}")
    #         print('--------------------------------------')

    # with conn.cursor() as cursor:
    #     query = """ALTER TABLE products RENAME COLUMN count TO count_to_stock"""
    #     cursor.execute(query)
    #     conn.commit()
    #
    # with conn.cursor() as cursor:
    #     query = """ALTER TABLE products ADD COLUMN discount varchar(64);"""
    #     cursor.execute(query)
    #     conn.commit()

# with conn.cursor() as cursor:
#     query = """DELETE FROM orders USING customers WHERE orders.customer_id = customers.id"""
#     cursor.execute(query)
#     conn.commit()

#     query = """DELETE FROM orders WHERE customer_id IN (SELECT id FROM customers WHERE customers.id = orders.customer_id)"""
#     cursor.execute(query)
#     conn.commit()

# set transaction isolation level "name levela"

