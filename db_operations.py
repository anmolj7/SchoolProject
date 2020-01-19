import mysql.connector

DB_NAME = "SchoolProject"
TABLE_NAME = "Elements"


def db_connect(user="root", password="Anmol@1234"):
    conn = mysql.connector.connect(host="localhost", user=user, password=password)
    return conn


def if_exists(text_id, db_name=DB_NAME, table_name=TABLE_NAME):
    conn = db_connect()
    cursor = conn.cursor()
    cursor.execute(f'USE {db_name}')
    cursor.execute(f'SELECT EXISTS(SELECT * FROM {table_name} WHERE text_id="{text_id}")')
    res = cursor.fetchall()[0][0]
    return res


def create_database(name):
    conn = db_connect()
    cursor = conn.cursor()
    try:
        cursor.execute(f'CREATE DATABASE {name}')
    except mysql.connector.errors.DatabaseError as e:
        if str(e)[-15:] == "database exists":
            print('Database Already Exists.')
        else:
            print(str(e))

    conn.commit()
    cursor.close()
    conn.close()


def create_table(db_name=DB_NAME, table_name=TABLE_NAME):
    conn = db_connect()
    cursor = conn.cursor()
    cursor.execute(f'USE {db_name}')
    sql = f"""
        CREATE TABLE Elements(
        text_id text,
        element_symbol text NOT NULL,
        element_name text NOT NULL
    )
    """
    try:
        cursor.execute(sql)
    except Exception as e:
        if str(e)[-14:] == "already exists":
            print("Table Already exists.")
        else:
            print(str(e))

    conn.commit()
    cursor.close()
    conn.close()


def get_results(query, table_name=TABLE_NAME, db_name=DB_NAME):
    conn = db_connect()
    cursor = conn.cursor()
    cursor.execute(f'USE {db_name}')
    cursor.execute(f'SELECT {query} FROM {table_name}')
    res = cursor.fetchall()
    return res


def add_to_database(atomic_number, atomic_symbol, element_name, table_name=TABLE_NAME, db_name=DB_NAME):
    conn = db_connect()
    cursor = conn.cursor()

    temp_id = atomic_number

    cursor.execute(f'USE {db_name}')
    if not if_exists(atomic_number):
        cursor.execute(f'INSERT INTO {table_name} VALUES("{atomic_number}", "{atomic_symbol}", "{element_name}")')

    conn.commit()
    cursor.close()
    conn.commit()

    return temp_id


def main():
    create_database("SchoolProject")
    create_table()

    # Adding elements from elements.txt to mysql database for better storing operations!

    with open('elements.txt') as f:
        data = f.read().split('\n') # it's better than using readlines because the readlines operation leaves a '\n'
        # in every line.
    elements = [line.split() for line in data]
    for element in elements:
        add_to_database(*element)
    print(get_results("*"))


if __name__ == '__main__':
    main()