import mysql.connector
from user import main

db = None
try: 
    db = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="root",
        port=3306
    )

    cursor = db.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS food_system")
    cursor.execute("USE food_system")
    print("Successfully connected to MySQL")
    main(db)

except mysql.connector.Error as error:
    print(f"Error: {error}")

finally:
    if db and db.is_connected():
        db.close()
        print("Connection closed")
