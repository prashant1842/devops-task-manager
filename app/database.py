import os
import mysql.connector


def get_connection():
    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST", "mysql"),
        user="root",
        password="root",
        database="devops_task_manager"
    )

    return connection


if __name__ == "__main__":
    connection = get_connection()

    if connection.is_connected():
        print("Successfully connected to MySQL!")

    connection.close()