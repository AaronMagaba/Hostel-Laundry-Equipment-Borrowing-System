
from datetime import date

from borrowing_record import BorrowingRecord


class HostelSystem:

    def __init__(self):
        # Collections managed by the HostelSystem
        self.students = []
        self.equipment = []
        self.records = []

    # Register a new student
    def register_student(self, student):

        for existing_student in self.students:
            if existing_student.student_id == student.student_id:
                return False

        self.students.append(student)
        return True

    # Add new laundry equipment
    def add_equipment(self, item):

        # Duck typing: check whether the object
        # provides the operations our system needs.
        required_attributes = ["item_id", "name", "available"]
        required_methods = ["borrow", "return_item", "display_details"]

        if not all(hasattr(item, attr) for attr in required_attributes):
            return False

        if not all(callable(getattr(item, method, None))
                   for method in required_methods):
            return False

        for existing_item in self.equipment:
            if existing_item.item_id == item.item_id:
                return False

        self.equipment.append(item)
        return True

    # Find a student using their ID
    def find_student(self, student_id):

        for student in self.students:
            if student.student_id == student_id:
                return student

        return None

    # Find equipment using its ID
    def find_equipment(self, item_id):

        for item in self.equipment:
            if item.item_id == item_id:
                return item

        return None

    # Display students
    def view_students(self):
        return list(self.students)

    # Display all equipment
    def view_equipment(self):
        return list(self.equipment)

    # Display only available equipment
    def view_available_equipment(self):

        return [
            item for item in self.equipment
            if item.available
        ]

    # Borrow equipment
    def borrow_equipment(self, student_id, item_id, due_date):

        student = self.find_student(student_id)
        item = self.find_equipment(item_id)

        if student is None or item is None:
            return None

        if not item.available:
            return None

        if not isinstance(due_date, date):
            return None

        if due_date <= date.today():
            return None

        # Update equipment availability
        if not item.borrow():
            return None

        # Generate a unique borrowing record ID
        record_id = f"BR{len(self.records) + 1:03d}"

        # Create a borrowing record
        record = BorrowingRecord(
            record_id,
            student,
            item,
            date.today(),
            due_date
        )

        self.records.append(record)

        return record

    # Return borrowed equipment
    def return_equipment(self, record_id):

        for record in self.records:

            if record.record_id == record_id:

                if not record.is_active():
                    return False

                # Update equipment availability
                if not record.equipment.return_item():
                    return False

                # Complete the borrowing record
                record.complete_record(date.today())

                return True

        return False

    # View all borrowing records
    def view_borrowing_records(self):
        return list(self.records)
