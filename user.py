from init_db import init_db
import csv
from queries import *
import mysql.connector

def load_cook(conn):
    cursor = conn.cursor()

    with open("cook.csv") as file:
        reader = csv.reader(file)
        
        next(reader)

        data = [(row[0], row[1]) for row in reader]

    cursor.executemany(
        "INSERT INTO Cook (name, rfc) VALUES (%s, %s)",
        data
    )

    conn.commit()

def load_dish(conn):
    cursor = conn.cursor()

    with open("dish.csv") as file:
        reader = csv.reader(file)
        
        next(reader)

        data = [(row[0], row[1], row[2]) for row in reader]

    cursor.executemany(
        "INSERT INTO Dish (name, price,cook_id) VALUES (%s, %s, %s)",
        data
    )
    conn.commit()

def load_ingredient(conn):
    cursor = conn.cursor()

    with open("ingredient.csv") as file:
        reader = csv.reader(file)
        
        next(reader)

        data = [(row[0], row[1]) for row in reader]

    cursor.executemany(
        "INSERT INTO Ingredient (name, cost) VALUES (%s, %s)",
        data
    )
    conn.commit()

def load_dish_ingredient(conn):
    cursor = conn.cursor()

    with open("dish_ingredient.csv") as file:
        reader = csv.reader(file)
        
        next(reader)

        data = [(row[0], row[1]) for row in reader]

    cursor.executemany(
        "INSERT INTO Dish_Ingredient (dish_id, ingredient_id) VALUES (%s, %s)",
        data
    )
    conn.commit()

def drop_tables(conn):
    cursor = conn.cursor()

    tables = ["Dish_Ingredient", "Dish", "Ingredient", "Cook"]

    for table in tables: 
         cursor.execute(f"DROP TABLE IF EXISTS {table}" )

    conn.commit()

def drop_specific_table(conn, table_name):
    
    cursor = conn.cursor()

    if table_name not in ["Dish_Ingredient", "Dish", "Ingredient", "Cook"]:
        print("Table does not exist.")
        return
    try:
        cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
        conn.commit()
    except mysql.connector.Error as error:
        print(f"Error: {error}")


def main(conn):
    print("Creating tables...")
    init_db(conn)
    print("Tables ready")
    cursor = conn.cursor()
    print("Welcome to the Food System!")

    while True:
        print("\n=== Restaurant Database Menu ===")
        print("1. Insert all")
        print("2. Get ingredients that all cooks use")
        print("3. Get dishes of all cooks or a cook")
        print("4. Get who cooks a plate")
        print("5. Drop specific table")
        print("6. Drop all tables")
        print("7. Get amount of cooks that use all ingredients")
        print("0. Close")

        choice = input("Select an option: ")

        if choice == "1":
            load_cook(conn)
            load_dish(conn)
            load_ingredient(conn)
            load_dish_ingredient(conn)

        if choice == "2":
            cursor.execute(GET_INGREDIENTS_THAT_A_COOK_USE)
            result = cursor.fetchall()
            for cook, dish, ingredient in result:
                print(f"Cook: {cook}, Dish: {dish if dish else 'No dishes'}, Ingredients: {ingredient if ingredient else 'No Ingredients'}")
        
        if choice == "3":
            param = input("Cook name (empty to display all): ")
            if not param:
                cursor.execute(GET_COOKS_WITH_DISHES)
                results = cursor.fetchall()
                for cook, dish in results:
                    print(f"Cook: {cook}, Dish: {dish if dish else 'No dishes'}") 
            else:
                cursor.execute(GET_A_COOK_DISH, (param,))
                results = cursor.fetchone()
                if results: 
                    cook_name, dish_name = results
                    print(
                        f"Cook: {cook_name}, Dish: {dish_name if dish_name else 'No dishes'}")
                else:
                    print(f"Cook {cook} doesn't exist.")

        if choice == "4":
            param = input("Dish name: ")
            cursor.execute(GET_COOK_FROM_DISH, (param,))
            result = cursor.fetchone()
            if result:
                print(f"Cook: {result[1]}, Dish: {result[-1]}")
            else:
                print("No cook found for that dish.")

        if choice == "5":
            table = input("Table to drop: ")
            drop_specific_table(conn, table)

        if choice == "6":
            drop_tables(conn)

        if choice == "7":
            cursor.execute(GET_AMOUNT_OF_COOKS_THAT_USE_INGREDIENTS)
            result = cursor.fetchall()
            for ingredient, count in result:
                print(f"Ingredient: {ingredient}, Count: {count if count else 'No cooks'}")
            if not result: 
                print("No result")
        elif choice == "0":
            break 

