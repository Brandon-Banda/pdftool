import mysql.connector


DB_CONFIG = {
    'user': 'root',
    'password': 'Albert2023',
    'host': 'localhost',  # or the host of your MySQL server
    'database': 'teamb',
    'raise_on_warnings': True
}

def connect_to_database():

	try:

		conn = mysql.connector.connect(**DB_CONFIG)

		if conn.is_connected():
		    print("Connection to the database was successful.")
		    return conn
		else:
		    print("Connection is established, but there is an issue.")
		    return None

	except mysql.connector.Error as err:
		print(f"Error: {err}")
		return None
def fetch_data_by_criterion(criterion, value):
	
    conn = connect_to_database()
    cursor = conn.cursor()
    query = f"SELECT * FROM `teamb` WHERE {criterion} = %s"  # Use parameterized queries
    cursor.execute(query, (value,))
    data = cursor.fetchall()
    conn.close()
    return data
