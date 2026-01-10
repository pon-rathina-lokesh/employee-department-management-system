from employee import add_employee, get_all_employees
from department import add_department, get_all_departments
from assignment import (
    assign_employee_to_department,
    get_employees_on_date,
    get_employees_in_date_range
)


def print_menu():
    print("\n===================================")
    print(" Employee Department Management ")
    print("===================================")
    print("1. Add Employee")
    print("2. Add Department")
    print("3. Assign Employee to Department")
    print("4. List employees working on a date")
    print("5. List employees working in a date range")
    print("6. Exit")


def handle_add_employee():
    name = input("Enter name: ").strip()
    age = int(input("Enter age: "))
    city = input("Enter city: ").strip()
    state = input("Enter state: ").strip()
    county = input("Enter county: ").strip()

    emp_id = add_employee(name, age, city, state, county)
    print(f"Employee added successfully. EmpID = {emp_id}")


def handle_add_department():
    description = input("Enter department description: ").strip()
    dept_id = add_department(description)
    print(f"Department added successfully. DeptID = {dept_id}")


def handle_assign_employee():
    emp_id = input("Enter EmpID: ").strip()
    dept_id = input("Enter DeptID: ").strip()
    start_date = input("Enter start date (MM-DD-YYYY): ").strip()
    end_date = input("Enter end date (MM-DD-YYYY) or 'Current': ").strip()

    assign_employee_to_department(emp_id, dept_id, start_date, end_date)
    print("Employee assigned to department successfully.")


def handle_list_on_date():
    date_str = input("Enter date (MM-DD-YYYY): ").strip()
    results = get_employees_on_date(date_str)

    print(f"\nEmployees working on {date_str}:")
    print("-------------------------------")
    if not results:
        print("No employees found.")
        return

    print("EmpID   DeptID")
    for emp_id, dept_id in results:
        print(f"{emp_id:<7} {dept_id}")


def handle_list_in_range():
    start_date = input("Enter start date (MM-DD-YYYY): ").strip()
    end_date = input("Enter end date (MM-DD-YYYY): ").strip()

    results = get_employees_in_date_range(start_date, end_date)

    print(f"\nEmployees working between {start_date} and {end_date}:")
    print("-----------------------------------------------------")
    if not results:
        print("No employees found.")
        return

    print("EmpID   DeptID   StartDate    EndDate")
    for r in results:
        print(f"{r['EmpID']:<7} {r['DeptID']:<8} {r['StartDate']:<12} {r['EndDate']}")


def main():
    while True:
        print_menu()
        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                handle_add_employee()
            elif choice == "2":
                handle_add_department()
            elif choice == "3":
                handle_assign_employee()
            elif choice == "4":
                handle_list_on_date()
            elif choice == "5":
                handle_list_in_range()
            elif choice == "6":
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
