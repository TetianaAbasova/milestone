# Part 2 - client
import requests
from dotenv import load_dotenv
import os
from datetime import datetime


load_dotenv()

BIRTHDAYS_URL = os.getenv("BIRTHDAYS_URL")
ANNIVERSARIES_URL = os.getenv("ANNIVERSARIES_URL")

def print_employees(title, data):
    print(f"{title}")
    if data["total"] > 0:
        print(f"Total: {data['total']}")
        for employee in data["employees"]:
            print(f"- {employee['birthday']}, {employee['name']}")
    else:
        print(f"No {title.lower()} this month")


def valid_date(month, year):
    try:
        datetime(year, month, 1)
        return True
    except ValueError:
        return False


def fetch_report(month, department):
    month = month.capitalize()

    try:
        month_number = datetime.strptime(month, "%B").month
    except ValueError:
        print(f"Invalid month: {month}")
        return

    year = datetime.now().year
    if not valid_date(month_number, year):
        print(f"Invalid date: {month} {year}")
        return

    urls = {
        "birthdays": f"{BIRTHDAYS_URL}?month={month}&department={department}",
        "anniversaries": f"{ANNIVERSARIES_URL}?month={month}&department={department}"
    }

    try:
        birthdays = requests.get(urls["birthdays"]).json()
        anniversaries = requests.get(urls["anniversaries"]).json()

        print(f"Report for {department} department for {month.capitalize()} fetched.")

        print_employees("Employees", birthdays)
        print_employees("Anniversaries", anniversaries)

    except requests.exceptions.RequestException as e:
        print(f"Error while fetching data: {e}")

fetch_report('july', 'IT')