class Phonebook:
    # Конструктор класса с параметром file_path, который указывает путь к файлу с контактами
    def __init__(self, file_path):
        self.file_path = file_path  # Инициализация переменной экземпляра file_path

    # Метод для добавления нового контакта с именем и номером телефона
    def add_contact(self, name, number):
        # Открытие файла для добавления (режим 'a') с кодировкой utf-8
        with open(self.file_path, "a", encoding="utf-8") as file:
            file.write(f"{name}:{number}\n")  # Запись нового контакта в файл

    # Метод для удаления контакта по имени
    def remove_contact(self, name):
        contacts = self._read_contacts()  # Чтение всех текущих контактов
        # Создание списка контактов, исключая контакт с указанным именем
        updated_contacts = [contact for contact in contacts if contact.split(":")[0] != name]
        self._write_contacts(updated_contacts)  # Перезапись файла с обновленным списком контактов

    # Метод для поиска контакта по имени
    def search_contact(self, name):
        contacts = self._read_contacts()  # Чтение всех текущих контактов
        for contact in contacts:  # Перебор всех контактов
            if contact.split(":")[0] == name:  # Если имя совпадает с искомым
                return contact.split(":")[1]  # Возвращаем номер телефона
        return "Контакт не найден."  # Если контакт не найден, возвращаем сообщение

    # Метод для отображения всех контактов
    def display_all_contacts(self):
        contacts = self._read_contacts()  # Чтение всех текущих контактов
        if contacts:  # Если список контактов не пуст
            print("Телефонный справочник:")  # Вывод заголовка
            for contact in contacts:  # Перебор всех контактов
                name, number = contact.split(":")  # Получение имени и номера из строки
                print(f"{name}: {number}")  # Вывод контакта
        else:
            print("Справочник пуст.")  # Если контактов нет, выводим сообщение

    # Приватный метод для чтения контактов из файла
    def _read_contacts(self):
        try:  # Блок обработки исключений
            with open(self.file_path, "r") as file:  # Открытие файла для чтения
                contacts = file.read().splitlines()  # Чтение всех строк и их разделение
                return contacts  # Возвращаем список контактов
        except FileNotFoundError:  # Если файл не найден
            return []  # Возвращаем пустой список

    # Приватный метод для записи контактов в файл
    def _write_contacts(self, contacts):
        with open(self.file_path, "w") as file:  # Открытие файла для записи
            for contact in contacts:  # Перебор всех контактов
                file.write(f"{contact}\n")  # Запись контакта в файл с новой строки


# Функция main - точка входа в программу
def main():
    file_path = "phonebook.txt"  # Задание пути к файлу с контактами
    phonebook = Phonebook(file_path)  # Создание экземпляра класса Phonebook

    while True:  # Начало бесконечного цикла для меню
        print("\nТелефонный справочник:")
        print("1. Добавить контакт")
        print("2. Удалить контакт")
        print("3. Поиск контакта")
        print("4. Вывести все контакты")
        print("5. Выйти")

        choice = input("Выберите действие (1-5): ")  # Запрос выбора у пользователя

        if choice == "1":  # Если выбор 1, то добавляем контакт
            name = input("Введите имя контакта: ")  # Запрос имени контакта
            number = input("Введите номер контакта: ")  # Запрос номера контакта
            phonebook.add_contact(name, number)  # Вызов метода добавления контакта
            print("Контакт успешно добавлен.")  # Вывод сообщения об успехе
        elif choice == "2":  # Если выбор 2, то удаляем контакт
            name = input("Введите имя контакта для удаления: ")  # Запрос имени контакта для удаления
            phonebook.remove_contact(name)  # Вызов метода удаления кон

            print("Контакт успешно удален.")  # Вывод сообщения об успехе
        elif choice == "3":  # Если выбор 3, то ищем контакт
            name = input("Введите имя контакта для поиска: ")  # Запрос имени контакта для поиска
            result = phonebook.search_contact(name)  # Вызов метода поиска контакта
            print(result)  # Вывод результата поиска
        elif choice == "4":  # Если выбор 4, то выводим все контакты
            phonebook.display_all_contacts()  # Вызов метода отображения всех контактов
        elif choice == "5":  # Если выбор 5, то выходим из программы
            break  # Прерывание цикла, завершение функции main
        else:
            print("Некорректный выбор. Попробуйте еще раз.")  # Вывод сообщения об ошибке при неверном выборе


# Проверка, что скрипт запущен как основная программа
if __name__ == "__main__":
    main()  # Вызов функции main
