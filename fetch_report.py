# Part 2 - client
import requests


def print_employees(title, data):
    print(f"{title}")
    if data["total"] > 0:
        print(f"Total: {data['total']}")
        for employee in data["employees"]:
            print(f"- {employee['birthday']}, {employee['name']}")
    else:
        print(f"No {title.lower()} this month")


def fetch_report(month, department):
    urls = {
        "birthdays": f"http://127.0.0.1:5000/birthdays?month={month}&department={department}",
        "anniversaries": f"http://127.0.0.1:5000/anniversaries?month={month}&department={department}"
    }


    birthdays = requests.get(urls["birthdays"]).json()
    anniversaries = requests.get(urls["anniversaries"]).json()

    print(f"Report for {department} department for {month.capitalize()} fetched.")

    print_employees("Employees", birthdays)
    print_employees("Anniversaries", anniversaries)

fetch_report('july', 'IT')