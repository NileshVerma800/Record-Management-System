# Console Record-Management Application

**MCA Semester I – Python Programming & Relational Database**
**Assignment 1: Mini Project – Console Record-Management Application**

**Name:** Nilesh Verma
**Roll No:** 58

## Project Description

A menu-driven, console-based Python application for managing student
records. It lets a user add, view, search, update, and delete records,
and persists all data to a local JSON file so nothing is lost between
runs. The project is built entirely with core Python — no external
libraries or frameworks are required.

## Features

- **Add Record** – create a new student record (name, course, age, marks)
  with an auto-generated unique ID.
- **View All Records** – display every record in a clean, formatted table.
- **Search Record** – look up a record by exact ID or by a partial,
  case-insensitive name match.
- **Update Record** – edit any field of an existing record; press Enter
  on a field to leave it unchanged.
- **Delete Record** – remove a record by ID, with a confirmation prompt.
- **Persistent storage** – all records are saved to `records.json` after
  every change, so data survives program restarts.
- **Robust input validation** – invalid numbers, empty strings, and bad
  menu choices are caught and re-prompted instead of crashing the app.
- **Graceful file handling** – a missing or corrupted data file is
  handled without crashing the program.

## Technologies / Concepts Used

- Python 3
- Data types & variables (`str`, `int`, `float`, `dict`, `list`)
- Conditional statements (`if` / `elif` / `else`)
- Loops (`while`, `for`)
- Functions (each feature is implemented as its own function)
- Exception handling (`try` / `except` for input errors and file errors)
- File I/O using the built-in `json` module
- Menu-driven console application design

## Project Structure

```
record_manager/
├── main.py            # Application source code
├── records.json        # Data file (auto-created/updated by the app)
└── README.md            # Project documentation
```

## How to Run the Application

1. Make sure Python 3 is installed:
   ```
   python3 --version
   ```
2. Download or clone this repository.
3. Navigate to the project folder:
   ```
   cd record_manager
   ```
4. Run the application:
   ```
   python3 main.py
   ```
5. Use the on-screen menu (options 1–6) to manage records. Data is
   automatically saved to `records.json` in the same folder.

## Sample Input / Output

```
===== Console Record-Management Application =====
1. Add Record
2. View All Records
3. Search Record
4. Update Record
5. Delete Record
6. Exit
Enter your choice (1-6): 1

--- Add New Record ---
Enter student name: Amit Sharma
Enter course name: MCA
Enter age: 22
Enter marks (out of 100): 88.5
Record added successfully with ID: 1
```

```
--- All Records ---
ID   Name                Course              Age   Marks
-----------------------------------------------------------
1    Amit Sharma         MCA                 22    88.5
2    Rahul Kumar         BSc IT              21    75.0
```



## GitHub Repository

Repository link:(https://github.com/NileshVerma800/Record-Management-System/)
