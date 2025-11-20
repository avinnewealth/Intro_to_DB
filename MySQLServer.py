import mysql.connector
from  mysql.connector import Error

try:

    mydb = mysql.connector.connect (
        host = "localhost",
        user = "root",
        passwd = "Rayomide@1@@"
)
    if mydb.is_connected():
        mycursor = mydb.cursor()
        mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except Error as e:
    print(f"Error! {e}")

finally:
    if mydb.is_connected():
        mydb.close()
        mycursor.close()


# mycursor.execute("show databases")

# for i in mycursor:
#     print(i)