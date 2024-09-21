# movies_queries.py

# 09/21/24
# Ian Lewis
# CSD310
# Module 7 Assignment


import mysql.connector

# Establishes connection to database
connection = mysql.connector.connect(
    host='127.0.0.1',
    user='movies_user',
    password='popcorn',
    database='movies'
)

# Creatse cursor object to execute SQL queries
cursor = connection.cursor()

# Query 1: Selects all fields from studio table
print("-- DISPLAYING Studio RECORDS --")
cursor.execute("SELECT studio_id, studio_name FROM studio")
studio_result = cursor.fetchall()
for row in studio_result:
    print(f"Studio ID: {row[0]}")
    print(f"Studio Name: {row[1]}\n")

# Query 2: Selects all fields from genre table
print("-- DISPLAYING Genre RECORDS --")
cursor.execute("SELECT genre_id, genre_name FROM genre")
genre_result = cursor.fetchall()
for row in genre_result:
    print(f"Genre ID: {row[0]}")
    print(f"Genre Name: {row[1]}\n")

# Query 3: Selects movie names for movies with a runtime of less than two hours
print("-- DISPLAYING Short Film RECORDS --")
cursor.execute("SELECT movie_name, runtime FROM movie WHERE runtime < 120")
runtime_result = cursor.fetchall()
for row in runtime_result:
    print(f"Film Name: {row[0]}")
    print(f"Runtime: {row[1]}\n")

# Query 4: Gets list of film names and directors grouped by director
print("-- DISPLAYING Director RECORDS in Order --")
cursor.execute("SELECT movie_name, director_name FROM movie ORDER BY director_name")
director_result = cursor.fetchall()
for row in director_result:
    print(f"Film Name: {row[0]}")
    print(f"Director: {row[1]}\n")

# Closes cursor and connection
cursor.close()
connection.close()