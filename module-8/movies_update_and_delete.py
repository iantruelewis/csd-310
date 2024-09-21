# movies_update_and_delete.py

# 09/21/24
# Ian Lewis
# CSD310
# Module 8 Assignment


import mysql.connector

# Establishes connection to database
try:
    db = mysql.connector.connect(
        host='127.0.0.1',
        user='movies_user',
        password='popcorn',
        database='movies'
    )
    cursor = db.cursor()
except mysql.connector.Error as err:
    print(f"Error connecting to the database: {err}")
    exit(1)

# Function displays films
def show_films(cursor, title):
    try:
        # Executes SQL query to perform inner joins between film, genre, and studio
        cursor.execute("""
        SELECT film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name'
        FROM film
        INNER JOIN genre ON film.genre_id = genre.genre_id
        INNER JOIN studio ON film.studio_id = studio.studio_id
        """)
        # Fetches all results
        films = cursor.fetchall()
        # Displays title
        print("\n -- {} --".format(title))
        # Iterates over results and displays each film's details
        for film in films:
            print(f"Film Name: {film[0]}\nDirector: {film[1]}\nGenre Name: {film[2]}\nStudio Name: {film[3]}\n")
    except mysql.connector.Error as err:
        print(f"Error displaying films: {err}")

try:
    # Inserts new film record (Inception)
    cursor.execute("""
    INSERT INTO film (film_name, film_director, genre_id, studio_id, film_releaseDate, film_runtime)
    VALUES ('Inception', 'Christopher Nolan', 2, 1, '2010', 148)
    """)
    db.commit()

    # Displays films after insert
    show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

    # Updates genre of 'Alien' to Horror
    cursor.execute("""
    UPDATE film
    SET genre_id = 1
    WHERE film_name = 'Alien'
    """)
    db.commit()

    # Displays films after updating 'Alien' genre to Horror
    show_films(cursor, "DISPLAYING FILMS AFTER UPDATE - ALIEN TO HORROR")

    # Deletes the film 'Gladiator' from database
    cursor.execute("DELETE FROM film WHERE film_name = 'Gladiator'")
    db.commit() # Commit the deletion

    # Displays films after deleting 'Gladiator'
    show_films(cursor, "DISPLAYING FILMS AFTER DELETE - GLADIATOR")

except mysql.connector.Error as err:
    print(f"An error occurred: {err}")
    db.rollback()

finally:
    # Closes database connection
    cursor.close()
    db.close()