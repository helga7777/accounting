from application.salary import calculate_salary
from application.people import get_employees
from datetime import datetime


if __name__ == '__main__':
    calculate_salary()
    get_employees()
    datetime = datetime.now().date()
    print(datetime)
