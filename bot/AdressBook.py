from collections import UserDict


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, "Record not found")

    def delete(self, name):
        if name in self.data:
            del self.data[name]
            return "Record deleted"
        return "Record not found"
