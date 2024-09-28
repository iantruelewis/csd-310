# Hector Lara Mikaela June Robert Minkler Group 3 Milestone 2 Python Data insertion 9/27/2024
# Ian Lewis Group 3 Milestone 2 Python additional sample data insertion 09/28/24


#  Import package that allows Python to connect to MySQL and execute SQL queries.
import mysql.connector
import datetime

# Step 2: Establish a connection to MySQL
# We need to specify the host (usually localhost for local development),
# user (username for MySQL), password (your MySQL password).
try:

    config = {
        "user": "winery_user",
        "password": "Bacchus_SecretPassword#1",
        "host": "localhost",
        "database": "bacchus_winery",
        "raise_on_warnings": True
    }

    # connect to database
    db_connection = mysql.connector.connect(**config)

    print("Connection to the Baccus Winery database was successful!")

except mysql.connector.Error as err:
    print(f"Error: {err}")
    exit(1)

# Step 3: Create a cursor object to execute SQL queries
cursor = db_connection.cursor()


# insert department sample data
sql = "INSERT INTO department (depart_name) VALUES (%s)"
val = [
    ('Owner',),
    ('Finances',),
    ('Marketing',),
    ('Production',),
    ('Distribution',)
]
cursor.executemany(sql, val)


# Insert employees
sql = "INSERT INTO employees (first_name, last_name, department, job_title) VALUES (%s, %s, %s, %s);"
val = [
    ('Stan', 'Bacchus', '1', 'Owner'),
    ('Davis', 'Bacchus', '1', 'Owner'),
    ('Janet', 'Collins', '2', 'Accountant'),
    ('Roz', 'Murphy', '3', 'Marketing Manager'),
    ('Bob', 'Urlich', '3', 'Marketing Assistant'),
    ('Henry', 'Doyle', '4', 'Production Manager'),
    ('Maria', 'Costanza', '5', 'Distribution Manager'),
]
cursor.executemany(sql, val)


# insert timekeeping sample punches
sql = "INSERT INTO timekeeping (employee_id, in_or_out, punch_datetime) VALUES (%s, %s, %s)"
val = [
    (1, 'IN', datetime.datetime(2024, 9, 27, 8, 0, 0)),
    (1, 'OUT', datetime.datetime(2024, 9, 27, 17, 0, 0)),
    (2, 'IN', datetime.datetime(2024, 9, 27, 9, 0, 0)),
    (2, 'OUT', datetime.datetime(2024, 9, 27, 18, 0, 0)),
    (3, 'IN', datetime.datetime(2024, 9, 27, 7, 30, 0)),
    (3, 'OUT', datetime.datetime(2024, 9, 27, 16, 30, 0)),
    (4, 'IN', datetime.datetime(2024, 9, 27, 9, 0, 0)),
    (4, 'OUT', datetime.datetime(2024, 9, 27, 16, 30, 0)),
    (5, 'IN', datetime.datetime(2024, 9, 27, 7, 0, 0)),
    (5, 'OUT', datetime.datetime(2024, 9, 27, 14, 30, 0)),
    (6, 'IN', datetime.datetime(2024, 9, 27, 9, 0, 0)),
    (6, 'OUT', datetime.datetime(2024, 9, 27, 18, 30, 0)),
]
cursor.executemany(sql, val)


# INSERT 12 example shipments
sql = ("INSERT INTO shipment_tracking (ship_date, est_delivery_date, delivery_date, carrier, "
       "tracking_number) "
       "VALUES (%s, %s, %s, %s, %s)")
val = [
    ('2023-04-21', '2023-04-27', '2023-04-26', 'Fed-ups', '1234567890'),
    ('2023-04-22', '2023-04-24', '2023-04-24', 'Fed-ups', '1234567891'),
    ('2023-04-23', '2023-04-28', '2023-05-15', 'Postal Carrier', '5432167890'),
    ('2023-04-23', '2023-04-24', '2023-04-24', 'UPS', '5454545454545'),
    ('2023-04-24', '2023-05-01', '2023-04-29', 'UPS', '09876567899'),
    ('2023-04-25', '2023-04-27', '2023-04-27', 'Fed-ups', '234567899876540'),
    ('2023-06-10', '2023-06-12', '2023-06-13', 'Fed-ex', '107349823'),
    ('2023-06-10', '2023-06-12', '2023-06-13', 'Fed-ex', '107349834'),
    ('2023-06-10', '2023-06-12', '2023-06-14', 'Fed-ex', '10723823'),
    ('2023-06-11', '2023-06-13', '2023-06-15', 'Fed-ex', '10733464d49823'),
    ('2023-06-12', '2023-06-15', '2023-06-17', 'Fed-ups', '10734143319823'),
    ('2023-06-20', '2023-06-21', '2023-06-21', 'Fed-ex', '1214343'),
]
cursor.executemany(sql, val)


# INSERT 6  example supply_orders
sql = ("INSERT INTO supply_orders (order_date, shipment_id)"
       "VALUES (%s, %s)")
val = [
    ('2023-04-21', '1'),
    ('2023-04-21', '2'),
    ('2023-04-22', '3'),
    ('2023-04-23', '4'),
    ('2023-04-23', '5'),
    ('2023-04-24', '6'),
]
cursor.executemany(sql, val)


# Insert Suppliers
sql = ("INSERT INTO suppliers (supplier_name, contact_email, contact_phone, order_url, address1, address2, city, state, "
       "zip, country) "
       "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
val = [
    ('Put a Cork in it', 'Put@cork.init','928-867-5309', 'http://putacorkinit.com', '123 main', None, 'Phoenix', 'AZ', '85001', 'Petoria'),
    ('Boxes r Us', 'Boxes@r.us', '305-867-5309', 'http://boxesrus.com', '345 main', None, 'Miami', 'FL', '33101', 'Bikini Bottom'),
    ('Vats Up Tubes', 'Vats@up.tubes', '915-867-5309', 'http://vats.com', '567 main', None, 'El Paso', 'TX', '79901', 'Tatooine')
]
cursor.executemany(sql, val)


# Insert Distributors
sql = ("INSERT INTO distributors (distributor_name, contact_email, contact_phone, address1, address2, city, state, zip, "
       "country) "
       "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
val = [
    ('Grape Expectations', 'Grape@expec.tations','508-867-5309', '123 main', None, 'Fitchburg', 'MA', '01420', 'Petoria'),
    ('Sip Happens', 'Sip@hap.pens', '407-867-5309', '345 main', None, 'Ocoee', 'FL', '34761', 'Bikini Bottom'),
    ('Pour Decisions', 'Pour@ex.pectations', '540-867-5309', '234 main', None, 'Christiansburg', 'VA', '24073', 'Bikini Bottom'),
    ('Grape Minds Drink Alike', 'Grape@minds.alike', '804-867-5309', '567 main', None, 'Henrico', 'VA', '23228', 'Bikini Bottom'),
    ('Wine & Dandy', 'Wine@and.dandy', '815-867-5309', '789 main', None, 'Joliet', 'IL', '60435', 'Bikini Bottom'),
    ('Grape to meet you', 'Grape@meet.you', '901-867-5309', '567 main', 'Suite 678', 'Memphis', 'TN', '38103', 'Tatooine')
]
cursor.executemany(sql, val)


# Insert Products
sql = ("INSERT INTO products (product_name, product_description, wine_type, sales_price, on_hand_qty)"
       "VALUES (%s, %s, %s, %s, %s)")
val = [
    ('Merlot', ' Dry Wine','Red Wine', '39.99', '20'),
    ('Cabernet', 'Dry Wine', 'Red Wine', '29.99', '30'),
    ('Chablis', 'Dry Wine', 'White Wine', '34.99', '15'),
    ('Chardonnay', 'Dry Wine', 'White Wine', '19.99', '35')
]
cursor.executemany(sql, val)


# Insert Supplier Products
sql = ("INSERT INTO supplier_products (supplier_id, item_name, item_price, item_description, inv_on_hand, product_id)"
       "VALUES (%s, %s, %s, %s, %s, %s)")
val = [
    ('1', '1 inch corks', '0.05', '1 inch long corks', '10000', None),
    ('1', 'Std Bottle', '0.25', 'Standard Wine Bottle', '5000', None),
    ('2', 'Chardonnay Labels', '0.03', 'Bottle labels for Chardonnay', '900', '4'),
    ('2', 'Chablis Labels', '0.03', 'Bottle labels for Chablis', '3000', '3'),
    ('2', 'Wine Case 24 bottles', '1.23', 'Case for 24 wine bottles', '100', None),
    ('3', '1/4" tubing', '24.00', '10 feet of 1/4 tubing', '1', None),
]
cursor.executemany(sql, val)


# insert items from an order
sql = ("INSERT INTO supply_order_items (order_num, order_item, supplier_item_id, quantity)"
       "VALUES (%s, %s, %s, %s)")
val = [
    ('1', '1', '1', '1000'),
    ('1', '2', '2', '5000'),
    ('2', '1', '3', '1000'),
    ('2', '2', '5', '1000'),
    ('3', '1', '3', '100'),
    ('4', '1', '2', '500')
]
cursor.executemany(sql, val)


# insert sales orders
sql = ("INSERT INTO sales_orders (distributor_id, order_date, shipment_id)"
       "VALUES (%s, %s, %s)")
val = [
    ('1', '2023-06-10', '7'),
    ('2', '2023-06-10', '8'),
    ('3', '2023-06-10', '9'),
    ('3', '2023-06-11', '10'),
    ('6', '2023-06-12', '11'),
    ('6', '2023-06-20', '12')
]
cursor.executemany(sql, val)


# insert items sold
sql = ("INSERT INTO items_sold (transaction_num, order_item, product_id, quantity)"
       "VALUES (%s, %s, %s, %s)")
val = [
    ('1', '1', '1', '5'),
    ('1', '2', '2', '15'),
    ('2', '1', '1', '10'),
    ('2', '2', '4', '20'),
    ('3', '1', '4', '7'),
    ('4', '1', '2', '10')
]
cursor.executemany(sql, val)



# Commit to the database
db_connection.commit()

# Close the connection
cursor.close()
db_connection.close()

print("All tables were successfully created.")