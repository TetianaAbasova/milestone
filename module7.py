# Part 1 - server
from flask import Flask, request, jsonify
import csv
from datetime import datetime

app = Flask(__name__)

def read_csv(name): #read csv Database
    with open(name, 'r', newline='') as file:
        return list(csv.DictReader(file))


def filter_employees_birthday(data, month, department):
    employees = []
    num_month = datetime.strptime(month, "%B").month
    for row in data:
        birthday = datetime.strptime(row['Birthday'], '%Y-%m-%d')
        if birthday.month == num_month and row["Department"] == department:
            employees.append(
                {
                    "id": data.index(row) + 1,
                    "name": row["Name"],
                    "birthday": birthday.strftime("%b %d")
                }
            )
    return employees


def filter_employees_anniversary(data, month, department):
    employees = []
    num_month = datetime.strptime(month, "%B").month
    for row in data:
        hire_date = datetime.strptime(row['HiringDate'], '%Y-%m-%d')
        if hire_date.month == num_month and row["Department"] == department:
            employees.append(
                {
                    "id": data.index(row) + 1,
                    "name": row["Name"],
                    "anniversary": hire_date.strftime("%b %d")
                }
            )
    return employees


@app.route("/birthdays", methods=["GET"])
def birthdays():
    month = request.args.get("month")
    department = request.args.get("department")

    if not month or not department:
        return jsonify({"error": " month and/or department empty"}), 400

    data = read_csv("database.csv")

    employees = filter_employees_birthday(data, month, department)

    return jsonify({
        "total": len(employees),
        "employees": employees
    })


@app.route("/anniversaries", methods=["GET"])
def anniversaries():
    month = request.args.get("month")
    department = request.args.get("department")

    if not month or not department:
        return jsonify({"error": " month and/or department empty"}), 400

    data = read_csv("database.csv")

    employees = filter_employees_anniversary(data, month, department)

    return jsonify({
        "total": len(employees),
        "employees": employees
    })


if __name__ == "__main__":
    app.run()