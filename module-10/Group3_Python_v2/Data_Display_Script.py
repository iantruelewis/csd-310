# Group 3 Milestone 2 Python Script to Display Database Table Data 09/28/2024



# Import the mysql.connector package to connect to MySQL
import mysql.connector

# Step 1 Establish a connection to MySQL
try:
    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Winters00&Dad",
        database="bacchus_winery"
    )
    print("Connected to Bacchus Winery database successfully!")

except mysql.connector.Error as err:
    print(f"Error: {err}")
    exit(1)

# Step 2 Create a cursor object to execute SQL queries
cursor = db_connection.cursor()

# Function fetches and displays data from table
def fetch_and_display_table_data(table_name):
    try:
        query = f"SELECT * FROM {table_name};"
        cursor.execute(query)
        rows = cursor.fetchall()

        if rows:
            print(f"\nData from the '{table_name}' table:")
            for row in rows:
                print(row)
        else:
            print(f"\nNo data found in the '{table_name}' table.")

    except mysql.connector.Error as err:
        print(f"Error fetching data from {table_name}: {err}")

# List of tables in Bacchus Winery database
tables = [
    "products",
    "suppliers",
    "supplier_products",
    "supply_orders",
    "supply_order_items",
    "shipment_tracking",
    "distributors",
    "sales_orders",
    "employees",
    "timekeeping",
    "department",
    "items_sold"
]

# Step 3 Loops through list of tables and displays their data
for table in tables:
    fetch_and_display_table_data(table)

# Step 4 Closes cursor and connection
cursor.close()
db_connection.close()

print("\nAll data from tables has been displayed successfully.")