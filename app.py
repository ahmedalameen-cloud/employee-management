from flask import Flask, render_template, request, redirect, session
import mysql.connector
import psycopg2
import os
from psycopg2.extras import RealDictCursor
from functools import wraps

app = Flask(__name__)

# Secret key for login session
app.secret_key = os.environ.get(
    "SECRET_KEY",
    "employee-management-secret-key"
)


# ==============================
# LOGIN REQUIRED
# ==============================

def login_required(f):

    @wraps(f)
    def decorated_function(*args, **kwargs):

        if "admin_logged_in" not in session:
            return redirect("/login")

        return f(*args, **kwargs)

    return decorated_function


# ==============================
# DATABASE CONNECTION
# ==============================

def get_db_connection():

    database_url = os.environ.get("DATABASE_URL")

    # Render PostgreSQL
    if database_url:
        return psycopg2.connect(database_url)

    # Local Docker MySQL
    return mysql.connector.connect(
        host="mysql",
        user="employeeapp",
        password="Employee@123",
        database="employee_db"
    )


# ==============================
# CREATE DATABASE TABLE
# ==============================

def init_db():

    conn = get_db_connection()

    if os.environ.get("DATABASE_URL"):

        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                email VARCHAR(150) NOT NULL,
                department VARCHAR(100) NOT NULL,
                salary NUMERIC(12,2) NOT NULL
            )
        """)

    else:

        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                email VARCHAR(150) NOT NULL,
                department VARCHAR(100) NOT NULL,
                salary DECIMAL(12,2) NOT NULL
            )
        """)

    conn.commit()

    cursor.close()
    conn.close()


# ==============================
# HOME PAGE
# ==============================

@app.route("/")
def home():

    conn = get_db_connection()

    if os.environ.get("DATABASE_URL"):

        cursor = conn.cursor(
            cursor_factory=RealDictCursor
        )

    else:

        cursor = conn.cursor(
            dictionary=True
        )

    cursor.execute(
        "SELECT * FROM employees ORDER BY id DESC"
    )

    employees = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template(
        "index.html",
        employees=employees
    )


# ==============================
# LOGIN
# ==============================

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        admin_username = os.environ.get(
            "ADMIN_USERNAME",
            "admin"
        )

        admin_password = os.environ.get(
            "ADMIN_PASSWORD",
            "Admin@123"
        )

        if (
            username == admin_username
            and password == admin_password
        ):

            session["admin_logged_in"] = True

            return redirect("/")

        return render_template(
            "login.html",
            error="Invalid username or password"
        )

    return render_template("login.html")


# ==============================
# LOGOUT
# ==============================

@app.route("/logout")
def logout():

    session.clear()

    return redirect("/")


# ==============================
# ADD EMPLOYEE
# ==============================

@app.route("/add", methods=["GET", "POST"])
@login_required
def add_employee():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        department = request.form["department"]
        salary = request.form["salary"]

        conn = get_db_connection()

        cursor = conn.cursor()

        query = """
            INSERT INTO employees
            (name, email, department, salary)
            VALUES (%s, %s, %s, %s)
        """

        cursor.execute(
            query,
            (
                name,
                email,
                department,
                salary
            )
        )

        conn.commit()

        cursor.close()
        conn.close()

        return redirect("/")

    return render_template(
        "add_employee.html"
    )


# ==============================
# DELETE EMPLOYEE
# ==============================

@app.route("/delete/<int:id>", methods=["POST"])
@login_required
def delete_employee(id):

    conn = get_db_connection()

    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM employees WHERE id = %s",
        (id,)
    )

    conn.commit()

    cursor.close()
    conn.close()

    return redirect("/")


# ==============================
# START APPLICATION
# ==============================

if __name__ == "__main__":

    init_db()

    port = int(
        os.environ.get(
            "PORT",
            5000
        )
    )

    app.run(
        host="0.0.0.0",
        port=port
    )
