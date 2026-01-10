import os

DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)



TABLE_SCHEMAS = {
    "emp.txt": {
        "headers": ["EmpID", "Name", "Age", "City", "State", "County"],
        "widths":  [8, 14, 5, 13, 12, 12]
    },
    "department.txt": {
        "headers": ["DeptID", "Description"],
        "widths":  [8, 26]
    },
    "emp_dept.txt": {
        "headers": ["EmpID", "DeptID", "StartDate", "EndDate"],
        "widths":  [8, 8, 12, 12]
    }
}


def _build_separator(widths):
    return "+" + "+".join("-" * w for w in widths) + "+\n"

def _format_row(values, widths):
    row = "|"
    for value, width in zip(values, widths):
        row += f" {str(value).ljust(width - 2)}|"
    return row + "\n"

def read_table(filename):

    path = os.path.join(DATA_DIR, filename)
    schema = TABLE_SCHEMAS[filename]
    headers = schema["headers"]

    if not os.path.exists(path):
        return []

    with open(path, "r") as f:
        lines = f.readlines()


    data_lines = [
        line for line in lines[2:]
        if line.strip().startswith("|")
    ]

    rows = []
    for line in data_lines:
        parts = [p.strip() for p in line.strip("| \n").split("|")]
        row = dict(zip(headers, parts))
        rows.append(row)

    return rows

def append_row(filename, row_dict):

    path = os.path.join(DATA_DIR, filename)
    schema = TABLE_SCHEMAS[filename]

    values = [row_dict[h] for h in schema["headers"]]
    row_text = _format_row(values, schema["widths"])

    with open(path, "a") as f:
        f.write(row_text)

def generate_next_id(filename, id_field):
    rows = read_table(filename)
    if not rows:
        return "1"

    max_id = max(int(row[id_field]) for row in rows)
    return str(max_id + 1)



