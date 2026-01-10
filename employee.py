from file_utils import read_table, append_row, generate_next_id


EMP_FILE = "emp.txt"


def add_employee(name, age, city, state, county):
    """
    Adds a new employee after validating age.
    """
    if not (18 <= age <= 65):
        raise ValueError("Age must be between 18 and 65.")

    emp_id = generate_next_id(EMP_FILE, "EmpID")

    employee = {
        "EmpID": emp_id,
        "Name": name,
        "Age": str(age),
        "City": city,
        "State": state,
        "County": county
    }

    append_row(EMP_FILE, employee)
    return emp_id


def get_all_employees():
    """
    Returns all employees.
    """
    return read_table(EMP_FILE)


def employee_exists(emp_id):
    """
    Checks if an employee exists by EmpID.
    """
    employees = read_table(EMP_FILE)
    return any(emp["EmpID"] == str(emp_id) for emp in employees)

