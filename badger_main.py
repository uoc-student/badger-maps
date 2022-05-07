import csv                          # read from csv file
import logging                      # log errors into a log file
import mysql.connector              # 
from mysql.connector import Error   # exception handler
import queries                      # queries to db are in a separate file


# Function to establish a conncetion with the db
def create_server_connection(host_name, user_name, user_password, user_db):
    conneciton = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            password = user_password,
            database = user_db
            )
        print("MySQL connection with " + user_db + " by " + user_name + " established successfully!")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


"""
# Function to create a database
def create_database(connection, query):
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            print("Database created successfully")
        except Error as err:
            print(f"Error: '{err}'")
"""


# Function to query the db
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Degug: Query successful!") # delete before release
    except Error as err:
        print(f"Error: '{err}'")


# Funtion to read from csv (parser)
def read_from_csv_into_db_table(connection, csv_dir):
    pass


 # Read returned data from sql queries
def read_sql_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")


# Function to print the results from a sql query 
def print_query_result(query_obj):
    for row in query_obj:
        print(row)


# Main
def main():

    hostname = "localhost"
    user = "badger"
    password = "maps"
    database = "badger_db"
    cvs_dir = "./customer_data.csv"
    customer_table = "customer_table"
    log_file = "badger.log"

    logging.basicConfig(filename = log_file, level = logging.INFO)

    # Establish connection with the database
    connection = create_server_connection(hostname, user, password, database)

    # Create database
    execute_query(connection, "CREATE DATABASE " + database + ";")

    # Drop table if exists (to avoid duplicates), else create table
    execute_query(connection, "DROP TABLE " + customer_table + ";")
    execute_query(connection, queries.create_customer_table) 




if __name__ == "__main__":
    main()