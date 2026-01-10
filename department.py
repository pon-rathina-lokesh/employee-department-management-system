from file_utils import read_table, append_row, generate_next_id


DEPT_FILE = "department.txt"


def add_department(description):
    
    if not description or not description.strip():
        raise ValueError("Department description cannot be empty.")

    dept_id = generate_next_id(DEPT_FILE, "DeptID")

    department = {
        "DeptID": dept_id,
        "Description": description.strip()
    }

    append_row(DEPT_FILE, department)
    return dept_id


def get_all_departments():
   
    return read_table(DEPT_FILE)


def department_exists(dept_id):
    
    departments = read_table(DEPT_FILE)
    return any(dept["DeptID"] == str(dept_id) for dept in departments)
