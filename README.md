### Объявление класса Phonebook

```python
class Phonebook:
```

Это начало объявления класса `Phonebook`. Класс в Python - это способ объединения данных и функций в одну структуру.

### Метод инициализации

```python
    def __init__(self, file_path):
        self.file_path = file_path
```

- `def __init__(self, file_path):` - Это специальный метод, который называется конструктором. Он автоматически вызывается при создании нового объекта класса `Phonebook`. В него передается параметр `file_path`, который представляет собой путь к файлу, в котором будут храниться контакты.
- `self.file_path = file_path` - Эта строка сохраняет переданный путь к файлу внутри объекта класса, делая его доступным для всех методов класса.

### Метод добавления контакта

```python
    def add_contact(self, name, number):
        with open(self.file_path, "a", encoding="utf-8") as file:
            file.write(f"{name}:{number}\n")
```

- `def add_contact(self, name, number):` - Определение метода `add_contact`, который принимает два параметра: `name` (имя контакта) и `number` (номер телефона).
- `with open(self.file_path, "a", encoding="utf-8") as file:` - Это контекстный менеджер для работы с файлами. Он открывает файл, находящийся по пути `self.file_path` в режиме добавления (`"a"`) с кодировкой `utf-8`. Открытый файл доступен как переменная `file`.
- `file.write(f"{name}:{number}\n")` - Записывает строку с именем и номером контакта в файл, разделяя их двоеточием. `\n` добавляет перевод строки, чтобы следующий контакт начинался с новой строки.

### Метод удаления контакта

```python
    def remove_contact(self, name):
        contacts = self._read_contacts()
        updated_contacts = [contact for contact in contacts if contact.split(":")[0] != name]
        self._write_contacts(updated_contacts)
```

- `def remove_contact(self, name):` - Определение метода `remove_contact`, который принимает один параметр: `name` - имя контакта, который нужно удалить.
- `contacts = self._read_contacts()` - Чтение текущего списка контактов с помощью метода `_read_contacts`.
- `updated_contacts = [...]` - Создание нового списка контактов, исключая те, чье имя совпадает с заданным для удаления.
- `self._write_contacts(updated_contacts)` - Перезапись файла с обновленным списком контактов методом `_write_contacts`.

### Метод поиска контакта

```python
    def search_contact(self, name):
        contacts = self._read_contacts()
        for contact in contacts:
            if contact.split(":")[0] == name:
                return contact.split(":")[1]
        return "Контакт не найден."
```

- `def search_contact(self, name):` - Метод `search_contact` предназначен для поиска номера телефона по имени контакта.
- `contacts = self._read_contacts()` - Получаем список всех контактов.
- `for contact in contacts:` - Идем по каждому контакту в списке.
- `if contact.split(":")[0] == name:` - Разделяем строку контакта по двоеточию и проверяем, совпадает ли имя с искомым.
- `return contact.split(":")[1]` - Если имя совпало, возвращаем номер телефона.
- `return "Контакт не найден."` - Если контакт с заданным именем не найден, возвращаем сообщение об этом.

### Метод отображения всех контактов

```python
    def display_all_contacts(self):
        contacts = self._read_contacts()
        if contacts:
            print("Телефонный справочник:")
            for contact in contacts:
                name, number = contact.split(":")
                print(f"{name}: {number}")
        else:
            print("Справочник пуст.")
```

- `def display_all_contacts(self):` - Метод для вывода всех контактов на экран.
- `contacts = self._read_contacts()` - Чтение списка контактов.
- `if contacts:` - Проверка, есть ли контакты.
- `for contact in contacts:` - Если контакты есть, перебираем их.
- `name, number = contact.split
(":")` - Разделяем строку на имя и номер.
- `print(f"{name}: {number}")` - Выводим имя и номер каждого контакта.
- `else:` - Если контактов нет, сообщаем об этом.

### Вспомогательные методы для чтения и записи контактов

```python
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
```

- `def _read_contacts(self):` - Приватный метод для чтения контактов из файла.
- `with open(self.file_path, "r") as file:` - Открывает файл в режиме чтения.
- `contacts = file.read().splitlines()` - Читает все строки файла, разделяя их и создавая список контактов.
- `return contacts` - Возвращает список контактов.
- `except FileNotFoundError:` - Если файл не найден, возвращает пустой список.
- `def _write_contacts(self, contacts):` - Приватный метод для записи контактов в файл.
- `with open(self.file_path, "w") as file:` - Открывает файл в режиме записи.
- `for contact in contacts:` - Перебирает контакты и записывает их в файл.

### Функция main

```python
def main():
    file_path = "phonebook.txt"
    phonebook = Phonebook(file_path)
```

- `def main():` - Объявление функции `main`, которая является точкой входа в программу.
- `file_path = "phonebook.txt"` - Определение пути к файлу телефонной книги.
- `phonebook = Phonebook(file_path)` - Создание объекта `phonebook` экземпляра класса `Phonebook`.

### Интерактивное меню

```python
    while True:
        print("\nТелефонный справочник:")
        # Код опущен для краткости...
        choice = input("Выберите действие (1-5): ")
```

- `while True:` - Начало бесконечного цикла для интерактивного меню.
- `print("\nТелефонный справочник:")` - Вывод заголовка меню.
- `choice = input("Выберите действие (1-5): ")` - Запрос у пользователя выбрать действие.

### Обработка выбора пользователя

```python
        if choice == "1":
            # Код для добавления контакта...
        elif choice == "2":
            # Код для удаления контакта...
        # Продолжение условий для других пунктов меню...
        elif choice == "5":
            break
        else:
            print("Некорректный выбор. Попробуйте еще раз.")
```

- `if choice == "1":` - Если пользователь выбирает `1`, выполняется код добавления контакта.
- `elif choice == "2":` -