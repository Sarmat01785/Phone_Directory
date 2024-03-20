class Phonebook:
    def __init__(self, file_path):
        self.file_path = file_path

    def add_contact(self, name, number):
        with open(self.file_path, "a", encoding="utf-8") as file:
            file.write(f"{name}:{number}\n")

    def remove_contact(self, name):
        contacts = self._read_contacts()
        updated_contacts = [contact for contact in contacts if contact.split(":")[0] != name]
        self._write_contacts(updated_contacts)

    def search_contact(self, name):
        contacts = self._read_contacts()
        for contact in contacts:
            if contact.split(":")[0] == name:
                return contact.split(":")[1]
        return "Контакт не найден."

    def display_all_contacts(self):
        contacts = self._read_contacts()
        if contacts:
            print("Телефонный справочник:")
            for contact in contacts:
                name, number = contact.split(":")
                print(f"{name}: {number}")
        else:
            print("Справочник пуст.")

    def _read_contacts(self):
        try:
            with open(self.file_path, "r") as file:
                contacts = file.read().splitlines()
                return contacts
        except FileNotFoundError:
            return []

    def _write_contacts(self, contacts):
        with open(self.file_path, "w") as file:
            for contact in contacts:
                file.write(f"{contact}\n")


def main():
    file_path = "phonebook.txt"
    phonebook = Phonebook(file_path)

    while True:
        print("\nТелефонный справочник:")
        print("1. Добавить контакт")
        print("2. Удалить контакт")
        print("3. Поиск контакта")
        print("4. Вывести все контакты")
        print("5. Выйти")

        choice = input("Выберите действие (1-5): ")

        if choice == "1":
            name = input("Введите имя контакта: ")
            number = input("Введите номер контакта: ")
            phonebook.add_contact(name, number)
            print("Контакт успешно добавлен.")
        elif choice == "2":
            name = input("Введите имя контакта для удаления: ")
            phonebook.remove_contact(name)
            print("Контакт успешно удален.")
        elif choice == "3":
            name = input("Введите имя контакта для поиска: ")
            result = phonebook.search_contact(name)
            print(result)
        elif choice == "4":
            phonebook.display_all_contacts()
        elif choice == "5":
            break
        else:
            print("Некорректный выбор. Попробуйте еще раз.")


if __name__ == "__main__":
    main()
