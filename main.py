
import mysql.connector
from mysql.connector import Error

import create_database_query as cdq
import create_data_table_queries as cdtq

# create function to establish connection from main.py to MySQL
def create_server_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_password,
            database = db_name
        )
        print("MySQL Database Connection Successful!!")
    except Error as err:
        print(f"Error: {err}")

    return connection

#create a function that will create a database
def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database Created Successfully!!")
    except Error as err:
        print(f"Error: '{err}'")

# create work horse function to execute queries
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query Successful!!")
    except Error as err:
        print(f"Error: '{err}'")


# call function to establish connection from main.py to MySQL
connection = create_server_connection("localhost", "root","student", "school")


#call execute function to create data tables
execute_query(connection, cdtq.create_teacher_table)
execute_query(connection, cdtq.create_client_table)
execute_query(connection, cdtq.create_course_table)
execute_query(connection,cdtq.create_participant_table)