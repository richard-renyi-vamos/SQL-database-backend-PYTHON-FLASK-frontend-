import sqlite3

# Create/connect to a SQLite database
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# Create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    email TEXT
                 )''')

# Commit changes and close connection
conn.commit()
conn.close()
