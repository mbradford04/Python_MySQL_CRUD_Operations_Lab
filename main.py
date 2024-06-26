import mysql.connector
from mysql.connector import Error

import create_database_query as cdq
import create_data_table_queries as cdtq
import populate_data_tables_queries as pdtq
import read_data_tables_queries as rdtq

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


# create a function to read information from data tables from DB
def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")



# call function to establish connection from main.py to MySQL
connection = create_server_connection("localhost", "root","student", "school")

def displayAllDataTables():
    # display information from data tables in pycharm
    print("Information for Client Data Table: ")
    clientDataTable = read_query(connection, rdtq.display_client_table_information)
    for clientInformation in clientDataTable:
        print(clientInformation)
    print()

    print("Information for Teacher Table: ")
    teacherDataTable = read_query(connection, rdtq.display_teacher_table_information)
    for teacherInformation in teacherDataTable:
        print(teacherInformation)
    print()

    print("Information for Participant Table")
    participantDataTable = read_query(connection, rdtq.display_participant_table_information)
    for participantInformation in participantDataTable:
        print(participantInformation)
    print()

    print("Information for Course Table: ")
    courseDataTable = read_query(connection, rdtq.display_course_table_information)
    for courseInformation in courseDataTable:
        print(courseInformation)
    print()

displayAllDataTables()
