import mysql.connector


class DBLoader:

    def return_values_from_db(self):
        connection = None

        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Password@123",
                database="ecommerce"
            )

            cursor = connection.cursor()
            cursor.execute("SELECT * FROM products")

            for row in cursor.fetchall():
                title = row[1].strip()
                print(f"Title:******************** {title}")

        except Exception as e:
            print(e)
            raise RuntimeError("Failed to retrieve values from the database.")

        finally:
            if connection:
                connection.close()


# Example of how to use DBLoader

