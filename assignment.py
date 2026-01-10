from datetime import datetime, date
from file_utils import read_table, append_row
from employee import employee_exists
from department import department_exists


ASSIGNMENT_FILE = "emp_dept.txt"
DATE_FORMAT = "%m-%d-%Y"


# -----------------------
# Date utility functions
# -----------------------

def _parse_date(date_str):
    if date_str == "Current":
        return None
    return datetime.strptime(date_str, DATE_FORMAT).date()


def _dates_overlap(start1, end1, start2, end2):
   
    end1 = end1 or date.max
    end2 = end2 or date.max
    return start1 <= end2 and start2 <= end1


# -----------------------
# Core assignment logic
# -----------------------

def assign_employee_to_department(emp_id, dept_id, start_date_str, end_date_str="Current"):
    

    if not employee_exists(emp_id):
        raise ValueError("Employee does not exist.")

    if not department_exists(dept_id):
        raise ValueError("Department does not exist.")

    start_date = _parse_date(start_date_str)
    end_date = _parse_date(end_date_str)

    if end_date is not None and end_date < start_date:
        raise ValueError("End date cannot be earlier than start date.")

    assignments = read_table(ASSIGNMENT_FILE)

    for record in assignments:
        if record["EmpID"] != str(emp_id):
            continue

        existing_start = _parse_date(record["StartDate"])
        existing_end = _parse_date(record["EndDate"])

        # Rule 1: no overlapping departments
        if _dates_overlap(start_date, end_date, existing_start, existing_end):
            # Rule 2: cannot assign same department if already active
            if record["DeptID"] == str(dept_id):
                raise ValueError("Employee is already assigned to this department during this period.")
            else:
                raise ValueError("Employee cannot be assigned to multiple departments at the same time.")

    assignment = {
        "EmpID": str(emp_id),
        "DeptID": str(dept_id),
        "StartDate": start_date_str,
        "EndDate": end_date_str
    }

    append_row(ASSIGNMENT_FILE, assignment)


# -----------------------
# Query functions
# -----------------------

def get_employees_on_date(query_date_str):
    
    query_date = _parse_date(query_date_str)
    results = []

    for record in read_table(ASSIGNMENT_FILE):
        start = _parse_date(record["StartDate"])
        end = _parse_date(record["EndDate"])

        if start <= query_date and (end is None or query_date <= end):
            results.append((record["EmpID"], record["DeptID"]))

    return results


def get_employees_in_date_range(start_date_str, end_date_str):
    
    range_start = _parse_date(start_date_str)
    range_end = _parse_date(end_date_str)

    if range_end < range_start:
        raise ValueError("End date cannot be earlier than start date.")

    results = []

    for record in read_table(ASSIGNMENT_FILE):
        start = _parse_date(record["StartDate"])
        end = _parse_date(record["EndDate"])

        if _dates_overlap(range_start, range_end, start, end):
            results.append(record)

    return results
