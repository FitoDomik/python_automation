import mysql.connector
def connect_to_mysql(host, user, password, database):
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        print("Connection established successfully.")
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
def fetch_data_from_table(connection, query):
    cursor = connection.cursor(dictionary=True)  
    try:
        cursor.execute(query)
        result = cursor.fetchall()  
        return result
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    finally:
        cursor.close()
def sort_data(data, sort_by_column):
    return sorted(data, key=lambda x: x[sort_by_column])
def main():
    host = 'localhost'  
    user = 'root'  
    password = 'yourpassword'  
    database = 'yourdatabase'  
    connection = connect_to_mysql(host, user, password, database)
    if connection:
        query = "SELECT * FROM your_table"
        data = fetch_data_from_table(connection, query)
        if data:
            print("Original Data:")
            for row in data:
                print(row)
            sorted_data = sort_data(data, 'your_column_to_sort_by')  
            print("\nSorted Data:")
            for row in sorted_data:
                print(row)
        connection.close()
if __name__ == "__main__":
    main()