"""
У користувача буде адресна книга або книга контактів. Ця книга контактів містить записи. Кожен запис містить деякий набір полів.

Таким чином ми описали сутності (класи), які необхідно реалізувати. Далі розглянемо вимоги до цих класів та встановимо
їх взаємозв'язок, правила, за якими вони будуть взаємодіяти.

Користувач взаємодіє з книгою контактів, додаючи, видаляючи та редагуючи записи. Також користувач повинен мати
можливість шукати в книзі контактів записи за одним або кількома критеріями (полями).

Про поля також можна сказати, що вони можуть бути обов'язковими (ім'я) та необов'язковими (телефон або email наприклад).
Також записи можуть містити декілька полів одного типу (декілька телефонів наприклад). Користувач повинен мати
можливість додавати/видаляти/редагувати поля у будь-якому записі.

В цій домашній роботі ви повинні реалізувати такі класи:

Клас AddressBook, який наслідується від UserDict, та ми потім додамо логіку пошуку за записами до цього класу.
Клас Record, який відповідає за логіку додавання/видалення/редагування необов'язкових полів та зберігання
обов'язкового поля Name.
Клас Field, який буде батьківським для всіх полів, у ньому потім реалізуємо логіку, загальну для всіх полів.
Клас Name, обов'язкове поле з ім'ям.
Клас Phone, необов'язкове поле з телефоном та таких один запис (Record) може містити кілька.
Критерії приймання
Реалізовано всі класи із завдання.
Записи Record в AddressBook зберігаються як значення у словнику. Як ключі використовується значення Record.name.value.
Record зберігає об'єкт Name в окремому атрибуті.
Record зберігає список об'єктів Phone в окремому атрибуті.
Record реалізує методи для додавання/видалення/редагування об'єктів Phone.
AddressBook реалізує метод add_record, який додає Record у self.data.
"""
from collections import UserDict

class Field(): # буде батьківським для всіх полів, у ньому потім реалізуємо логіку, загальну для всіх полів
    def __init__(self, value):
        self.value = value
    pass

class Phone(Field): # необов'язкове поле з телефоном та таких один запис (Record) може містити кілька
    pass

class Name(Field): # обов'язкове поле з ім'ям
    def __int__(self, name: str):
        self.name = name
    pass

class Email(Field):
    pass


class Record(): #відповідає за логіку додавання/видалення/редагування необов'язкових полів та зберігання
    # обов'язкового поля Name.
    def __init__(self, name: Name, phones: list) -> None:
        self.name = name
        self.phones = [Phone(phone) for phone in phones]
        # self.emails = emails


    def add_phone(self, phone: Phone):
        phone_number = Phone(phone)
        if phone_number not in self.phones:
            self.phones.append(phone_number)

    # def add_email(self, email: Email):
    #     email_str = Email(email)
    #     if email_str not in self.emails:
    #         self.emails.append(email_str)

    def edit_phone(self, phone_old, phone_new: Phone):
        phone_number_old = Phone(phone_old)
        phone_number_new = Phone(phone_new)
        if phone_number_old in self.phones:
            index = self.phones.index(phone_number_old)
            self.phones[index] = phone_number_new
        else:
            Record.add_phone(phone_number_new)

    # def edit_email(self, email_old, email_new: Phone):
    #     email_str_old = Phone(email_old)
    #     email_str_new = Phone(email_new)
    #     if email_str_old in self.emails:
    #         index = self.emails.index(email_str_old)
    #         self.emails[index] = email_str_new
    #     else:
    #         Record.add_email(email_str_new)

    def del_phone(self, phone: Phone):
        phone_number = Phone(phone)
        if phone_number in self.phones:
            self.phones.remove(phone_number)

    # def del_email(self, email: Email):
    #     email_str = Email(email)
    #     if email_str in self.emails:
    #         self.emails.remove(email_str)

    pass


class AddressBook(UserDict): # наслідується від UserDict, та ми потім додамо логіку пошуку за записами до цього класу

    def add_record(self, record: Record):
        self.data[Record.name.value] = record

    pass


# Тест для перевірки від ментора
if __name__ == "__main__":
    name = Name('Bill')
    phone = Phone('1234567890')
    rec = Record(name, phone)
    ab = AddressBook()
    ab.add_record(rec)
    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].phones, list)
    assert isinstance(ab['Bill'].phones[0], Phone)
    assert ab['Bill'].phones[0].value == '1234567890'
    print('All Ok)')