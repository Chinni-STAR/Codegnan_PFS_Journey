""" import mysql.connector

conn = (mysql.connector.connect
    (
    host='localhost',
    user='root',
    password='root',
    database='flaskdb'))
print("Connected Successfully")

cursor=conn.cursor()
cursor.execute( "CREATE TABLE users(id INT, name VARCHAR(50))" )
conn.commit()


create table users(    
    id INT PRIMARY KEY AUTO_INCREMENT,    
    username VARCHAR(100),   
    email VARCHAR(100),    
    password VARCHAR(255),    
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP );

 """
import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='flaskdb'
)

print("Connected Successfully")

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users(
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(100),
    email VARCHAR(100),
    password VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS notes(
    note_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    title VARCHAR(200),
    content TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS uploads(
    file_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    filename VARCHAR(255),
    filepath VARCHAR(255),
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

conn.commit()

print("Tables created successfully")

cursor.close()
conn.close()