# Assignment 1 – Documentation Report

**Course:** MCA Semester I – Python Programming & Relational Database
**Assignment:** Mini Project – Console Record-Management Application
**Name:** Nilesh Verma
**Roll No:** 58

## 1. Objective

To design and implement a fully functional, menu-driven console
application in Python that manages records (add, view, search, update,
delete) and persists them to disk, while demonstrating mastery of core
Python concepts: data types, control flow, functions, exception
handling, and file I/O.

## 2. Problem Statement

Organizations frequently need a simple way to store and manage
structured records — for example, student details — without the
overhead of a database server. This project implements such a system
as a console application, using a JSON file as lightweight persistent
storage.

## 3. System Design

### 3.1 Data Model

Each record is stored as a Python dictionary with the following
fields:

| Field  | Type  | Description                     |
|--------|-------|----------------------------------|
| id     | int   | Unique, auto-generated identifier |
| name   | str   | Student's full name              |
| course | str   | Course enrolled in               |
| age    | int   | Student's age                    |
| marks  | float | Marks obtained (out of 100)      |

All records are held in memory as a list of dictionaries during
execution, and the entire list is serialized to `records.json` after
every add, update, or delete operation.

### 3.2 Module / Function Breakdown

| Function              | Responsibility                                         |
|------------------------|--------------------------------------------------------|
| `load_records()`       | Reads `records.json` at startup; handles missing/corrupt file |
| `save_records()`       | Writes the current record list back to `records.json`  |
| `get_non_empty_string()` | Validates non-blank text input                        |
| `get_valid_integer()`  | Validates integer input                                 |
| `get_valid_float()`    | Validates decimal input                                 |
| `get_next_id()`        | Computes the next unique record ID                     |
| `add_record()`         | Collects input and appends a new record                |
| `view_records()`       | Prints all records in tabular form                     |
| `find_record_by_id()`  | Helper lookup used by search/update/delete             |
| `search_record()`      | Searches by ID or partial name match                   |
| `update_record()`      | Edits fields of an existing record                     |
| `delete_record()`      | Removes a record after user confirmation               |
| `display_menu()`       | Prints the main menu                                    |
| `main()`               | Runs the menu loop and dispatches to the right function |

### 3.3 Menu Flow

```
Start
  → Load records from file
  → Loop:
      1. Add Record
      2. View All Records
      3. Search Record
      4. Update Record
      5. Delete Record
      6. Exit (break loop, save state already persisted)
```

## 4. Concepts Demonstrated

- **Data types & variables:** strings, integers, floats, dictionaries,
  and lists are used to represent and store record data.
- **Conditional statements & loops:** `if`/`elif`/`else` drive menu
  dispatch and validation; `while` loops re-prompt on invalid input and
  keep the main menu running; `for` loops iterate over records for
  display and search.
- **Functions:** every distinct piece of logic (I/O, validation, CRUD
  operations) is isolated into its own function rather than one large
  script block.
- **Exception handling:** `try`/`except` blocks catch invalid numeric
  input (`ValueError`), file read/write problems (`IOError`), malformed
  JSON (`json.JSONDecodeError`), and any unexpected runtime error at
  the top level of the main loop, so the application never crashes
  ungracefully.
- **File I/O:** the `json` module is used to serialize/deserialize the
  record list to `records.json`, giving the application persistent
  storage across runs.
- **Menu-driven design:** a clear numbered menu, validated choice
  input, and a dispatch structure make the application easy to use and
  extend.

## 5. Testing

The application was tested manually for the following scenarios:

1. Starting the application with no existing data file (creates an
   empty record list without error).
2. Adding multiple records and confirming they appear correctly in
   the "View All Records" screen.
3. Searching by exact ID and by partial/case-insensitive name.
4. Updating a record, including leaving fields blank to keep existing
   values, and entering invalid data for a field to confirm graceful
   fallback.
5. Deleting a record, including cancelling the delete confirmation.
6. Entering invalid menu options and invalid numeric input to confirm
   the application re-prompts instead of crashing.
7. Restarting the application to confirm previously saved records are
   reloaded correctly from `records.json`.

## 6. Conclusion

This project successfully implements a working console-based
record-management system that fulfils all the assignment requirements:
a menu-driven interface, full CRUD functionality, function-based
structure, robust exception handling, and persistent file storage. The
resulting codebase is modular, readable, and easy to extend with
additional fields or features in the future.
