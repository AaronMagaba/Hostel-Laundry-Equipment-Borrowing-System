
from datetime import date

from student import Student
from equipment import Iron, LaundryBasket, WashingBucket
from hostel_system import HostelSystem


# Create the main application object
hostel = HostelSystem()


def register_student():
    print("\n--- REGISTER STUDENT ---")

    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    room_number = input("Enter room number: ")

    student = Student(student_id, name, room_number)

    if hostel.register_student(student):
        print("Student registered successfully!")
    else:
        print("Registration failed. Student ID may already exist.")


def add_equipment():
    print("\n--- ADD LAUNDRY EQUIPMENT ---")
    print("1. Iron")
    print("2. Laundry Basket")
    print("3. Washing Bucket")

    choice = input("Select equipment type: ")

    item_id = input("Enter equipment ID: ")
    name = input("Enter equipment name: ")

    if choice == "1":
        item = Iron(item_id, name)
    elif choice == "2":
        item = LaundryBasket(item_id, name)
    elif choice == "3":
        item = WashingBucket(item_id, name)
    else: 
        print("Invalid equipment type.")
        return

    if hostel.add_equipment(item):
        print("Equipment added successfully!")
    else:
        print("Equipment could not be added. Check the ID or equipment interface.")


def view_equipment():
    print("\n--- LAUNDRY EQUIPMENT ---")

    equipment = hostel.view_equipment()

    if not equipment:
        print("No equipment registered yet.")
        return

    for item in equipment:
        status = "Available" if item.available else "Borrowed"

        print(f"\nID: {item.item_id}")
        print(f"Name: {item.name}")
        print(f"Status: {status}")
        print(item.display_details())


def view_students():
    print("\n--- REGISTERED STUDENTS ---")

    students = hostel.view_students()

    if not students:
        print("No students registered.")
        return

    for student in students:
        print(f"\nID: {student.student_id}")
        print(f"Name: {student.name}")
        print(f"Room: {student.room_number}")


def borrow_equipment():
    print("\n--- BORROW EQUIPMENT ---")

    student_id = input("Enter student ID: ")
    item_id = input("Enter equipment ID: ")
    due_date_input = input("Enter return date (YYYY-MM-DD): ")

    try:
        due_date = date.fromisoformat(due_date_input)
    except ValueError:
        print("Invalid date format.")
        return

    record = hostel.borrow_equipment(
        student_id,
        item_id,
        due_date
    )

    if record:
        print("\nEquipment borrowed successfully!")
        print(f"Borrowing Record ID: {record.record_id}")
        print(f"Return Date: {record.due_date}")
    else:
        print("Borrowing failed. Check student ID, equipment availability and due date.")


def return_equipment():
    print("\n--- RETURN EQUIPMENT ---")

    record_id = input("Enter borrowing record ID: ")

    if hostel.return_equipment(record_id):
        print("Equipment returned successfully!")
    else:
        print("Return failed. Invalid record or equipment already returned.")


def view_borrowing_records():
    print("\n--- BORROWING RECORDS ---")

    records = hostel.view_borrowing_records()

    if not records:
        print("No borrowing records found.")
        return

    for record in records:
        status = "Active" if record.is_active() else "Returned"

        print(f"\nRecord ID: {record.record_id}")
        print(f"Student: {record.student.name}")
        print(f"Equipment: {record.equipment.name}")
        print(f"Borrowed: {record.borrow_date}")
        print(f"Due date: {record.due_date}")
        print(f"Return date: {record.return_date}")
        print(f"Status: {status}")


def main():

    while True:

        print("\n===================================")
        print(" HOSTEL LAUNDRY BORROWING SYSTEM")
        print("===================================")

        print("1. Register Student")
        print("2. Add Laundry Equipment")
        print("3. View Students")
        print("4. View Equipment")
        print("5. Borrow Equipment")
        print("6. Return Equipment")
        print("7. View Borrowing Records")
        print("8. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            register_student()

        elif choice == "2":
            add_equipment()

        elif choice == "3":
            view_students()

        elif choice == "4":
            view_equipment()

        elif choice == "5":
            borrow_equipment()

        elif choice == "6":
            return_equipment()

        elif choice == "7":
            view_borrowing_records()

        elif choice == "8":
            print("Thank you for using the Hostel Laundry System!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
