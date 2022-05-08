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


# Function to query the db
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Degug: Query successful!") # delete before release
    except Error as err:
        print(f"Error: '{err}'")


# Funtion to read values from csv into table (parser)
def read_from_csv_into_db_table(connection, table, csv_dir):
    with open('customer_data.csv', newline='\n',  encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file)
        headers = next(csv_reader, None) 
        columns = len(headers)
        for row in csv_reader:
            empty_columns = 0
            handle_exceptions(row, headers)
            execute_query(connection, "INSERT INTO customer_table VALUES {};".format(tuple(row)))


# Handle empty fields and LOG exceptions
def handle_exceptions(row, headers):
    csv_required_fields = [2, 3, 4, 6, 9]
    empty_columns = 0

    for i in range(len(headers)):       
        if row[i] == '':
            if i in csv_required_fields:
                print("Warning: REQUIRED FIELD missing ->", headers[i], "in row", i)
            else:
                print("Warning: Field missing ->", headers[i], "in row", i)
        empty_columns += 1

    if empty_columns >= 0:
        message = "LOG -> line " + str(i) + " is empty!"
        logging.info(message)
        print(message)


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


# Print results from sql query 
def print_query_result(query_obj):
    print(headers)
    for row in query_obj:
        print(row)


# Main
def main():

    hostname = "localhost"
    user = "badger"
    password = "maps"
    database = "badger_db"
    csv_dir = "./customer_data.csv"
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

    # Parser: read data from csv file into table and LOG errors
    read_from_csv_into_db_table(connection, customer_table, csv_dir)




if __name__ == "__main__":
    main()