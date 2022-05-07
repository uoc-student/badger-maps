import csv                          # read from csv file
import logging                      # log errors into a log file
import mysql.connector              # 
from mysql.connector import Error   # exception handler


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


# Function to create a database
def create_database(connection, query):
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            print("Database created successfully")
        except Error as err:
            print(f"Error: '{err}'")


# Function to query the db
def execute_query(connection, query):
    pass


# Function to print the results from a query 
def print_query_result(query_obj):
    pass


# Funtion to read from csv (parser)
def read_from_csv_to_db_table(connection, csv_dir):
    pass


# Queries
# Most recent check-in
# Least recent check-in
# Customer list sorted alphabetically



# Main
def main():

    hostname = "localhost"
    user = "badger"
    password = "maps"
    database = "badger_db"
    cvs_dir = "./customer_data.csv"

    # Establish connection with the database
    connection = create_server_connection(hostname, user, password, database)

    # Create database
    create_database(connection, "CREATE DATABASE " + database + ";")


if __name__ == "__main__":
    main()