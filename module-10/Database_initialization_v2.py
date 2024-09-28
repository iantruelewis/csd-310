# Hector Lara, Mikaela June, Robert Minkler Group 3 Milestone 2 Python init 9/27/2024
# Ian Lewis db connection edits for local access init 09/28/2024

# MUST SET ROOT PASSWORD

#  Import package that allows Python to connect to MySQL and execute SQL queries.
import mysql.connector

# Step 2: Establish a connection to MySQL
# We need to specify the host (usually localhost for local development),
# user (username for MySQL), password (your MySQL password).
try:
    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Winters00&Dad",
    )

    print("Connection to the Bacchus Winery database was successful!")

except mysql.connector.Error as err:
    print(f"Error: {err}")
    exit(1)

# Step 3: Create a cursor object to execute SQL queries
cursor = db_connection.cursor()

# Step 4: Create the 'bacchus_winery' database if it doesn't exist
cursor.execute("CREATE DATABASE IF NOT EXISTS bacchus_winery;")
print("Database 'bacchus_winery' created or already existed.")


# Step 5: Connect to the 'bacchus_winery' database now that it's created
db_connection.database = "bacchus_winery"

cursor.execute("SET FOREIGN_KEY_CHECKS=0;")

cursor.execute("""
DROP USER IF EXISTS 'winery_user'@'localhost';
""")

cursor.execute("""
CREATE USER 'winery_user'@'localhost' IDENTIFIED BY 'Bacchus_SecretPassword#1';
""")

cursor.execute("""
GRANT ALL PRIVILEGES ON bacchus_winery.* TO 'winery_user'@'localhost';
""")

cursor.execute("DROP TABLE IF EXISTS suppliers;")
cursor.execute("DROP TABLE IF EXISTS supplier_products;")
cursor.execute("DROP TABLE IF EXISTS supply_order_items;")
cursor.execute("DROP TABLE IF EXISTS supply_orders;")
cursor.execute("DROP TABLE IF EXISTS shipment_tracking;")
cursor.execute("DROP TABLE IF EXISTS sales_orders;")
cursor.execute("DROP TABLE IF EXISTS items_sold;")
cursor.execute("DROP TABLE IF EXISTS products;")
cursor.execute("DROP TABLE IF EXISTS distributors;")
cursor.execute("DROP TABLE IF EXISTS employees;")
cursor.execute("DROP TABLE IF EXISTS timekeeping;")
cursor.execute("DROP TABLE IF EXISTS department;")





# Step 6: Define SQL queries for creating each table
# These SQL statements will create the tables as per the ERD.
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    product_id INT NOT NULL AUTO_INCREMENT,
    product_name VARCHAR(45) NOT NULL,
    product_description VARCHAR(255),
    wine_type VARCHAR(25),
    sales_price DECIMAL(8,2),
    on_hand_qty INT,
    PRIMARY KEY (product_id)
);
""")

# Step 7: Now we can create the 'suppliers' table
cursor.execute("""
CREATE TABLE IF NOT EXISTS suppliers (
    supplier_id INT NOT NULL AUTO_INCREMENT,
    supplier_name VARCHAR(45) NOT NULL,
    contact_email VARCHAR(45),
    contact_phone VARCHAR(15),
    order_url VARCHAR(45),
    address1 VARCHAR(45),
    address2 VARCHAR(45),
    city VARCHAR(45),
    state CHAR(2),
    zip VARCHAR(10),
    country VARCHAR(45),
    PRIMARY KEY (supplier_id)
);
""")

# Step 8: Create the 'supplier_products' table, which references both 'suppliers' and 'products'
cursor.execute("""
CREATE TABLE IF NOT EXISTS supplier_products (
    supplier_item_id INT NOT NULL AUTO_INCREMENT,
    supplier_id INT NOT NULL,
    item_name VARCHAR(25) NOT NULL,
    item_price DECIMAL(8,2),
    item_description VARCHAR(45),
    inv_on_hand INT,
    product_id INT,
    PRIMARY KEY (supplier_item_id),
        
    CONSTRAINT fk_supplier_id
        FOREIGN KEY (supplier_id) 
        REFERENCES suppliers(supplier_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,
    CONSTRAINT fk_product_id
        FOREIGN KEY (product_id) 
        REFERENCES products(product_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);
""")

# Step 9: Create the 'supply_orders' table
cursor.execute("""
CREATE TABLE IF NOT EXISTS supply_orders (
    order_num INT NOT NULL AUTO_INCREMENT,
    order_date DATE NOT NULL,
    shipment_id INT,
    PRIMARY KEY (order_num),
    
    CONSTRAINT fk_shipment_id_sup
        FOREIGN KEY (shipment_id)
        REFERENCES shipment_tracking(shipment_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
        );
""")

# Step 10: Create the 'supply_order_items' table
cursor.execute("""
CREATE TABLE IF NOT EXISTS supply_order_items (
    order_num INT NOT NULL,
    order_item INT NOT NULL,
    supplier_item_id INT NOT NULL,
    quantity INT NOT NULL,
    PRIMARY KEY (order_num, order_item),
    
    CONSTRAINT fk_supplier_item_id
        FOREIGN KEY (supplier_item_id)
        REFERENCES supplier_products(supplier_item_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,
    CONSTRAINT fk_order_num
        FOREIGN KEY (order_num) 
        REFERENCES supply_orders(order_num)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);
""")

# Step 11: Create the 'shipment_tracking' table
cursor.execute("""
CREATE TABLE IF NOT EXISTS shipment_tracking (
    shipment_id INT NOT NULL AUTO_INCREMENT,
    ship_date DATE,
    est_delivery_date DATE,
    delivery_date DATE,
    carrier VARCHAR(45),
    tracking_number VARCHAR(128),
    PRIMARY KEY (shipment_id)
);
""")

# Step 12: Create the 'distributors' table
cursor.execute("""
CREATE TABLE IF NOT EXISTS distributors (
    distributor_id INT NOT NULL AUTO_INCREMENT,
    distributor_name VARCHAR(45) NOT NULL,
    contact_email VARCHAR(45),
    contact_phone VARCHAR(15),
    address1 VARCHAR(45),
    address2 VARCHAR(45),
    city VARCHAR(45),
    state CHAR(2),
    zip VARCHAR(10),
    country VARCHAR(45),
    PRIMARY KEY (distributor_id)
);
""")

# Step 13: Create the 'sales_orders' table, which references 'distributors' and 'shipment_tracking'
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales_orders (
    transaction_num INT NOT NULL AUTO_INCREMENT,
    distributor_id INT NOT NULL,
    order_date DATE NOT NULL,
    shipment_id INT,
    PRIMARY KEY (transaction_num),
    
    CONSTRAINT fk_distributor_id
        FOREIGN KEY (distributor_id)
        REFERENCES distributors(distributor_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,
    CONSTRAINT fk_shipment_id
        FOREIGN KEY (shipment_id)
        REFERENCES shipment_tracking(shipment_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);
""")

# Step 14: Create the 'employees' table
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    employee_id INT NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(15) NOT NULL,
    last_name VARCHAR(15) NOT NULL,
    department INT NOT NULL,
    job_title VARCHAR(45),
    PRIMARY KEY (employee_id),
    
    CONSTRAINT fk_department
        FOREIGN KEY (department)
        REFERENCES department (dept_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);
""")

# Step 15: Create the 'timekeeping' table
cursor.execute("""
CREATE TABLE IF NOT EXISTS timekeeping (
    punch_id INT NOT NULL AUTO_INCREMENT,
    employee_id INT NOT NULL,
    in_or_out ENUM('IN', 'OUT') NOT NULL,
    punch_datetime TIMESTAMP NOT NULL,
    PRIMARY KEY (punch_id),
    
    CONSTRAINT fk_employee_id
        FOREIGN KEY (employee_id)
        REFERENCES employees(employee_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);
""")

# Step 16: Create the 'department' table
cursor.execute("""
CREATE TABLE IF NOT EXISTS department (
    dept_id INT NOT NULL AUTO_INCREMENT,
    depart_name VARCHAR(15) NOT NULL,
    PRIMARY KEY (dept_id)
);
""")

# Step 17: Create the 'items_sold' table
cursor.execute("""
CREATE TABLE IF NOT EXISTS items_sold (
    transaction_num INT NOT NULL,
    order_item INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
  PRIMARY KEY (transaction_num, order_item),
  
  CONSTRAINT fk_transaction_num
    FOREIGN KEY (transaction_num)
    REFERENCES sales_orders (transaction_num)
    ON DELETE RESTRICT
    ON UPDATE CASCADE,
  CONSTRAINT fk_product_id_sold
    FOREIGN KEY (product_id)
    REFERENCES products (product_id)
    ON DELETE RESTRICT
    ON UPDATE CASCADE
);
""")

# Step 17: Commit to the database
db_connection.commit()

cursor.execute("SET FOREIGN_KEY_CHECKS=1;")

# Step 18: Close the connection
cursor.close()
db_connection.close()

print("All tables were successfully created.")