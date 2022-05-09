# MySQL queries

create_customer_table = """
CREATE TABLE customer_table (
  first_name VARCHAR(40),
  last_name VARCHAR(40),
  street VARCHAR(40),
  zip VARCHAR(20),
  city VARCHAR(30),
  type VARCHAR(1),
  last_check_in_date date,       # yyyy-mm-dd
  job VARCHAR(30),
  phone VARCHAR(20),
  company VARCHAR(40)
  );
 """


full_name_list_sorted_alphabetically = """
SELECT first_name, last_name AS full_name
FROM customer_table
WHERE first_name <> '' AND last_name <> ''
ORDER BY first_name, last_name; 
"""


most_recent_check_in = """
SELECT *
FROM customer_table
WHERE last_check_in_date <> '0000-00-00'
ORDER BY last_check_in_date DESC
LIMIT 1;
"""


least_recent_check_in = """
SELECT *
FROM customer_table
WHERE last_check_in_date <> '0000-00-00'
ORDER BY last_check_in_date ASC
LIMIT 1;
"""
