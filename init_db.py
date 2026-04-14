def init_db(conn):
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Cook (
        cook_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        rfc VARCHAR(50) UNIQUE
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Dish (
        dish_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        price DECIMAL(10,2) NOT NULL,
        cook_id INT NOT NULL,
        FOREIGN KEY (cook_id) REFERENCES Cook(cook_id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Ingredient (
        ingredient_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        cost DECIMAL(10,2)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Dish_Ingredient (
        dish_id INT NOT NULL,
        ingredient_id INT NOT NULL,
        PRIMARY KEY (dish_id, ingredient_id),
        FOREIGN KEY (dish_id) REFERENCES Dish(dish_id),
        FOREIGN KEY (ingredient_id) REFERENCES Ingredient(ingredient_id)
    )
    """)

    conn.commit()