from abc import ABC, abstractmethod


class LaundryEquipment(ABC):

    def __init__(self, item_id, name):
        self.item_id = item_id
        self.name = name
        self._available = True

    # Encapsulation: controlled access to availability
    @property
    def available(self):
        return self._available

    # Borrow equipment
    def borrow(self):
        if self._available:
            self._available = False
            return True

        return False

    # Return equipment
    def return_item(self):
        if not self._available:
            self._available = True
            return True

        return False

    # Abstraction: child classes must implement this
    @abstractmethod
    def display_details(self):
        pass


# Child class 1
class Iron(LaundryEquipment):

    def __init__(self, item_id, name):
        super().__init__(item_id, name)

    # Method overriding
    def display_details(self):
        status = "Available" if self.available else "Borrowed"

        return (
            f"Equipment Type: Iron\n"
            f"ID: {self.item_id}\n"
            f"Name: {self.name}\n"
            f"Status: {status}"
        )


# Child class 2
class LaundryBasket(LaundryEquipment):

    def __init__(self, item_id, name):
        super().__init__(item_id, name)

    # Method overriding
    def display_details(self):
        status = "Available" if self.available else "Borrowed"

        return (
            f"Equipment Type: Laundry Basket\n"
            f"ID: {self.item_id}\n"
            f"Name: {self.name}\n"
            f"Status: {status}"
        )


# Child class 3
class WashingBucket(LaundryEquipment):

    def __init__(self, item_id, name):
        super().__init__(item_id, name)

    # Method overriding
    def display_details(self):
        status = "Available" if self.available else "Borrowed"

        return (
            f"Equipment Type: Washing Bucket\n"
            f"ID: {self.item_id}\n"
            f"Name: {self.name}\n"
            f"Status: {status}"
        )