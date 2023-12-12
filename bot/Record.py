import field


class Record:
    def __init__(self, name):
        self.name = field.Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(field.Phone(phone))

    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                return "Телефон видалено"
        return "Телефон не знайдено"

    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                return "Телефон оновлено"
        return "Старий телефон не знайдено"

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return "Телефон не знайдено"

    def __str__(self):
        return f"Ім'я контакту: {self.name.value}, телефони: {'; '.join(p.value for p in self.phones)}"
