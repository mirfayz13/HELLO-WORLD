import psycopg2

def connect(db, user, password, port, host):
    try:
        conn = psycopg2.connect(
            dbname = dbname,
            user = user,
            password = password,
            port = port,
            host = host
        )
        cur = conn.cursor()
        print("Sucesfully Connected")
        return conn, cur
    except Exception as e:
        print(f"Error: {e}")
        return None, None

def create_table(cur, table_name, column):
    try:
        create_table_query = f"CREATE TABLE {table_name} ({column});"
        cur.execute(create_table_query)
        print(f"Table '{table_name}' Succesfully Created!")
    except Exception as e:
        print(f"ERROR: {e}")


def insert_tables(cur,table_name, column, values):
    try:
        cur.execute(F"INSERT INTO {table_name} ({column}) VALUES ({values});")
        print("Data Entered ")
    except Exception as e:
        print(f"Error: {e}")


def add_column(cur,table_name, column):
    try:
        cur.execute(f"ALTER TABLE {table_name} ADD COLUMN {column};")
        print(f"Column '{column}' is added ")
    except Exception as e:
        print(f"Error : {e}")

def drop_table(cur,table_name):
    try:
        cur.execute(f"DROP TABLE {table_name};")
        print("Deleted Table!")
    except Exception as e:
        print(f"Error: {e}")

def select_from(cur,table_name):
    try:
        select_car_query = f'''select * from {table_name} ;'''
        cur.execute(select_car_query)
        for user in cur.fetchall():
              print(user)
    except Exception as e:
              print(f"Error in the name of table: {e}")


def main_menu():
    print("1. Create a new table")
    print("2. Add Colummn to the table")
    print("3. Adding information to the table")
    print("4. Drop table")
    print("5. See table ")

    choice = input("Select (1/2/3/4/5): ")
    return choice

dbname = input("DBNAME: ")
username = input("Username: ")
password = input("Password: ")
port = input("Port: ")
host = input("Host: ")

conn, cur = connect(db=dbname, user=username, password=password, port=port, host=host)
if conn:
    while True:
        user_choice = main_menu()
        if user_choice == "1":
            table_name = input(" Enter table name: ")
            column = input("column and type (id int, name varchar(30)):  ")
            create_table(cur, table_name, column)
        elif user_choice == "2":
            table_name = input(" Table name: ")
            column = input("column name and type (id int, name varchar(30)):  ")
            add_column(cur,column)
        elif user_choice == "3":
            table_name = input(" Table name: ")
            column = input("  column (... , ... ): ")
            values = input(" Enter information ('...' , '...'):")
            insert_tables(cur,table_name,column,values)
        elif user_choice == "4":
            table_name = input(" Table name: ")
            drop_table(cur,table_name)
        elif user_choice == "4":
            table_name = input(" Table name: ")
            select_from(cur,table_name)

        else:
            print("Error")
            continue

    conn.commit()
    conn.close()
else:
    print("ERROR")

