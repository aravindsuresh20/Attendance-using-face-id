from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Mock user credentials (replace with a proper authentication mechanism)
VALID_USERNAME = "admin"
VALID_PASSWORD = "password"

@app.route('/')
def login():
    return render_template('login.html', error=False)

@app.route('/authenticate', methods=['POST'])
def authenticate():
    username = request.form.get('username')
    password = request.form.get('password')

    if username == VALID_USERNAME and password == VALID_PASSWORD:
        return redirect(url_for('attendance'))
    else:
        return render_template('login.html', error=True)

@app.route('/attendance')
def attendance():
    selected_date = request.args.get('selected_date')
    
    if not selected_date:
        selected_date = datetime.now().strftime('%Y-%m-%d')
    
    formatted_date = datetime.strptime(selected_date, '%Y-%m-%d').strftime('%Y-%m-%d')

    conn = sqlite3.connect('attendance.db')
    cursor = conn.cursor()

    cursor.execute("SELECT name, time FROM attendance WHERE date = ?", (formatted_date,))
    attendance_data = cursor.fetchall()

    conn.close()

    return render_template('index1.html', selected_date=selected_date, attendance_data=attendance_data)

if __name__ == '__main__':
    app.run(debug=True)

