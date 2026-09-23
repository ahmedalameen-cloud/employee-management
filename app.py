from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)


def get_db_connection():
    return mysql.connector.connect(
        host="mysql",
        user="employeeapp",
        password="Employee@123",
        database="employee_db"
    )


@app.route("/")
def home():

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template("index.html", employees=employees)


@app.route("/add", methods=["GET", "POST"])
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
            (name, email, department, salary)
        )

        conn.commit()

        cursor.close()
        conn.close()

        return redirect("/")

    return render_template("add_employee.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
