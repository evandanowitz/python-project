# Import the mysql.connector module
import mysql.connector

# Initialize a connection object called conn, which connects with following parameters:
# Based on user that was set up earlier
conn = mysql.connector.connect(
  host = 'localhost',
  user = 'cf-python',
  passwd = 'password'
)

# Initialize a cursor object from conn
cursor = conn.cursor()

