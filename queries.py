# Queries

# Create customer table
create_customer_table = """
CREATE TABLE customer_table (
  first_name VARCHAR(40),
  last_name VARCHAR(40),
  street VARCHAR(40),
  zip VARCHAR(20),
  city VARCHAR(30),
  type VARCHAR(1),
  last_check_in_date VARCHAR(10),       # date type to be considered, wip
  job VARCHAR(30),
  phone VARCHAR(20),
  company VARCHAR(40)
  );
 """


 
