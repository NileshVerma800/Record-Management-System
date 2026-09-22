import json
import os

DATA_FILE = "records.json"


def load_records():
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r") as file:
            content = file.read().strip()
            if not content:
                return []
            return json.loads(content)
    except (json.JSONDecodeError, IOError) as error:
        print(f"[Warning] Could not read data file properly ({error}). "
              f"Starting with an empty record list.")
        return []


def save_records(records):
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(records, file, indent=4)
    except IOError as error:
        print(f"[Error] Could not save records to file: {error}")


def get_non_empty_string(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty. Please try again.")


def get_valid_integer(prompt):
    while True:
        raw_value = input(prompt).strip()
        try:
            return int(raw_value)
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def get_valid_float(prompt):
    while True:
        raw_value = input(prompt).strip()
        try:
            return float(raw_value)
        except ValueError:
            print("Invalid input. Please enter a numeric value (e.g. 78.5).")


def get_next_id(records):
    if not records:
        return 1
    return max(record["id"] for record in records) + 1


def add_record(records):
    print("\n--- Add New Record ---")
    name = get_non_empty_string("Enter student name: ")
    course = get_non_empty_string("Enter course name: ")
    age = get_valid_integer("Enter age: ")
    marks = get_valid_float("Enter marks (out of 100): ")

    new_record = {
        "id": get_next_id(records),
        "name": name,
        "course": course,
        "age": age,
        "marks": marks,
    }

    records.append(new_record)
    save_records(records)
    print(f"Record added successfully with ID: {new_record['id']}")


def view_records(records):
    print("\n--- All Records ---")
    if not records:
        print("No records found.")
        return

    header = f"{'ID':<5}{'Name':<20}{'Course':<20}{'Age':<6}{'Marks':<8}"
    print(header)
    print("-" * len(header))
    for record in records:
        print(f"{record['id']:<5}{record['name']:<20}{record['course']:<20}"
              f"{record['age']:<6}{record['marks']:<8}")


def find_record_by_id(records, record_id):
    for record in records:
        if record["id"] == record_id:
            return record
    return None


def search_record(records):
    print("\n--- Search Record ---")
    print("1. Search by ID")
    print("2. Search by Name")
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        record_id = get_valid_integer("Enter record ID: ")
        record = find_record_by_id(records, record_id)
        if record:
            print("\nRecord found:")
            print(record)
        else:
            print("No record found with that ID.")

    elif choice == "2":
        keyword = get_non_empty_string("Enter name (or part of it): ").lower()
        matches = [r for r in records if keyword in r["name"].lower()]
        if matches:
            print(f"\n{len(matches)} matching record(s) found:")
            for record in matches:
                print(record)
        else:
            print("No matching records found.")

    else:
        print("Invalid choice.")


def update_record(records):
    print("\n--- Update Record ---")
    record_id = get_valid_integer("Enter the ID of the record to update: ")
    record = find_record_by_id(records, record_id)

    if not record:
        print("No record found with that ID.")
        return

    print("Leave a field blank to keep its current value.")

    new_name = input(f"Name [{record['name']}]: ").strip()
    new_course = input(f"Course [{record['course']}]: ").strip()
    new_age = input(f"Age [{record['age']}]: ").strip()
    new_marks = input(f"Marks [{record['marks']}]: ").strip()

    if new_name:
        record["name"] = new_name
    if new_course:
        record["course"] = new_course
    if new_age:
        try:
            record["age"] = int(new_age)
        except ValueError:
            print("Invalid age entered; keeping the previous value.")
    if new_marks:
        try:
            record["marks"] = float(new_marks)
        except ValueError:
            print("Invalid marks entered; keeping the previous value.")

    save_records(records)
    print("Record updated successfully.")


def delete_record(records):
    print("\n--- Delete Record ---")
    record_id = get_valid_integer("Enter the ID of the record to delete: ")
    record = find_record_by_id(records, record_id)

    if not record:
        print("No record found with that ID.")
        return

    confirm = input(f"Are you sure you want to delete '{record['name']}'? "
                     f"(y/n): ").strip().lower()
    if confirm == "y":
        records.remove(record)
        save_records(records)
        print("Record deleted successfully.")
    else:
        print("Deletion cancelled.")


def display_menu():
    print("\n===== Console Record-Management Application =====")
    print("1. Add Record")
    print("2. View All Records")
    print("3. Search Record")
    print("4. Update Record")
    print("5. Delete Record")
    print("6. Exit")


def main():
    records = load_records()

    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()

        try:
            if choice == "1":
                add_record(records)
            elif choice == "2":
                view_records(records)
            elif choice == "3":
                search_record(records)
            elif choice == "4":
                update_record(records)
            elif choice == "5":
                delete_record(records)
            elif choice == "6":
                print("Exiting application. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a number from 1 to 6.")
        except Exception as error:
            print(f"[Unexpected Error] {error}")


if __name__ == "__main__":
    main()
