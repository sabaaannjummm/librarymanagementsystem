from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with a strong secret key

# MySQL connection setup — adjust credentials to your setup
db = mysql.connector.connect(
    host="localhost",
    user="user",
    password="root",
    database="library_db"
)
cursor = db.cursor()

# --------- Routes ---------

@app.route('/')
def index():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    # Fetch books
    cursor.execute("SELECT * FROM Books ORDER BY book_id DESC")
    books = cursor.fetchall()

    # Fetch members
    cursor.execute("SELECT * FROM Members ORDER BY member_id DESC")
    members = cursor.fetchall()

    return render_template('index.html', books=books, members=members)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password']

        cursor.execute("SELECT user_id, password_hash FROM Users WHERE username=%s", (username,))
        user = cursor.fetchone()

        if user and check_password_hash(user[1], password):
            session['user_id'] = user[0]
            session['username'] = username
            flash('Logged in successfully!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password', 'danger')
            return redirect(url_for('login'))

    return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password']
        confirm = request.form['confirm_password']

        if password != confirm:
            flash('Passwords do not match!', 'danger')
            return redirect(url_for('signup'))

        # Check if username exists
        cursor.execute("SELECT * FROM Users WHERE username=%s", (username,))
        if cursor.fetchone():
            flash('Username already taken!', 'danger')
            return redirect(url_for('signup'))

        hashed_pw = generate_password_hash(password)
        cursor.execute("INSERT INTO Users (username, password_hash) VALUES (%s, %s)", (username, hashed_pw))
        db.commit()
        flash('Account created! Please log in.', 'success')
        return redirect(url_for('login'))

    return render_template('signup.html')


@app.route('/logout')
def logout():
    session.clear()
    flash('Logged out successfully.', 'success')
    return redirect(url_for('login'))


@app.route('/add_book', methods=['POST'])
def add_book():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    title = request.form['title'].strip()
    author = request.form['author'].strip()
    genre = request.form['genre'].strip()

    if not (title and author and genre):
        flash('Please fill all book fields', 'danger')
        return redirect(url_for('index'))

    cursor.execute(
        "INSERT INTO Books (title, author, genre) VALUES (%s, %s, %s)",
        (title, author, genre)
    )
    db.commit()
    flash('Book added successfully!', 'success')
    return redirect(url_for('index'))


@app.route('/add_member', methods=['POST'])
def add_member():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    name = request.form['name'].strip()
    email = request.form['email'].strip()
    phone = request.form['phone'].strip()

    if not (name and email and phone):
        flash('Please fill all member fields', 'danger')
        return redirect(url_for('index'))

    cursor.execute(
        "INSERT INTO Members (name, email, phone) VALUES (%s, %s, %s)",
        (name, email, phone)
    )
    db.commit()
    flash('Member added successfully!', 'success')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
