from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Function to connect to the database
def connect_db():
    return sqlite3.connect('mydatabase.db')

# Route for home page
@app.route('/')
def home():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    conn.close()
    return render_template('index.html', users=users)

# Route to add users
@app.route('/add', methods=['POST'])
def add_user():
    name = request.form['name']
    email = request.form['email']
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
    conn.commit()
    conn.close()
    return home()

if __name__ == '__main__':
    app.run(debug=True)
