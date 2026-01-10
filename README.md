# Employee Department Management System

## Overview

This project is a **file-based Employee–Department Management System** developed as part of an interview assignment.  
It manages employees, departments, and their assignments over time using **plain text ASCII tables**, without using any database.

The focus of this project is:
- Clean low-level design
- Business rule enforcement
- Correct handling of date-based relationships
- Readable and maintainable code

---

## Features

### 1. Employee Management
- Add employees with:
  - Name
  - Age (validated: **18–65**)
  - City, State, County
- Employees are stored in a fixed-width ASCII table (`emp.txt`)

---

### 2. Department Management
- Add departments with a description
- Departments are stored in `department.txt`

---

### 3. Employee–Department Assignment
- Assign employees to departments with:
  - Start date
  - End date (`MM-DD-YYYY` or `Current`)

#### Enforced business rules:
- An employee cannot work in more than one department at the same time
- Assignment date ranges cannot overlap
- An employee cannot be assigned to the same department while already active
- Employees can return to a department after leaving it

Assignments are stored in `emp_dept.txt`.

---

### 4. Queries
- List employees working on a **specific date**
- List employees working within a **date range**
  - Employees may appear multiple times if they changed departments during the range

---

## Project Structure

PRISMPORTFOLIOTASK/
│
├── main.py # CLI entry point
├── employee.py # Employee-related logic
├── department.py # Department-related logic
├── assignment.py # Assignment logic & validations
├── file_utils.py # ASCII table read/write utilities
│
├── data/
│ ├── emp.txt # Employee table
│ ├── department.txt # Department table
│ └── emp_dept.txt # Assignment history table
│
└── README.md


---

## ASCII Table Format

All data is stored in **fixed-width ASCII tables**.

### Employee (`emp.txt`)

+--------+--------------+-----+-------------+------------+------------+
| EmpID | Name | Age | City | State | County |
+--------+--------------+-----+-------------+------------+------------+


### Department (`department.txt`)

+--------+--------------------------+
| DeptID | Description |
+--------+--------------------------+


### Assignment (`emp_dept.txt`)

+--------+--------+------------+------------+
| EmpID | DeptID | StartDate | EndDate |
+--------+--------+------------+------------+


---

## How to Run

### Requirements
- Python **3.8+**
- No external libraries required

## Error Handling

- The system validates and handles:
- Invalid employee age
- Invalid date formats
- Overlapping department assignments
- Non-existent employees or departments
- Invalid date ranges

Errors are displayed gracefully without crashing the application.



