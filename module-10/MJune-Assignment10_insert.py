import datetime
import mysql.connector

try:
    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="MillieBop2020",
        database="winery"
    )
    print("Connection to the Winery database was successful!")

except mysql.connector.Error as err:
    print(f"Error: {err}")
    exit(1)

cursor = db_connection.cursor()
sql = "INSERT INTO department (depart_name) VALUES (%s)"
val = [
    ('Owner',),
    ('Finances',),
    ('Marketing',),
    ('Production',),
    ('Distribution',)
]

try:
    cursor.executemany(sql,val)
    db_connection.commit()
    print(cursor.rowcount, "departments were inserted.")
except mysql.connector.Error as err:
    print(f"Error inserting departments: {err}")

sql = "INSERT INTO employees (employee_id, first_name, last_name, department) VALUES (%s, %s, %s)"
val = [
    ('Stan', 'Bacchus', '01'),
    ('Davis', 'Bacchus', '01'),
    ('Janet', 'Collins', '02'),
    ('Roz', 'Murphy', '03'),
    ('Bob', 'Urlich', '04'),
    ('Henry', 'Doyle', '05'),
    ('Maria', 'Costanza', '06')
]

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


# Use executemany for multiple rows
cursor.executemany(sql, val)

db_connection.commit()

# Close the connection
cursor.close()
db_connection.close()

print(cursor.rowcount, "rows were inserted.")
