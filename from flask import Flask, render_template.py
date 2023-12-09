from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Create a SQLite database (or use a different database of your choice)
conn = sqlite3.connect('patients.db')
cursor = conn.cursor()

# Create a table to store patient details
cursor.execute('''
    CREATE TABLE IF NOT EXISTS patients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        sex TEXT NOT NULL,
        weight REAL NOT NULL,
        height REAL NOT NULL,
        ecg TEXT NOT NULL,
        breathing_rate INTEGER NOT NULL
    )
''')
conn.commit()

@app.route('/')
def index():
    # Fetch all patients from the database
    cursor.execute('SELECT * FROM patients')
    patients = cursor.fetchall()
    return render_template('index.html', patients=patients)

@app.route('/add_patient', methods=['POST'])
def add_patient():
    # Get patient details from the form
    name = request.form['name']
    age = request.form['age']
    sex = request.form['sex']
    weight = request.form['weight']
    height = request.form['height']
    ecg = request.form['ecg']
    breathing_rate = request.form['breathingRate']

    # Insert patient details into the database
    cursor.execute('''
        INSERT INTO patients (name, age, sex, weight, height, ecg, breathing_rate)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (name, age, sex, weight, height, ecg, breathing_rate))

    conn.commit()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
