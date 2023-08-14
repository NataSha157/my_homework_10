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
    pass

class Email(Field):
    pass


class Record(): #відповідає за логіку додавання/видалення/редагування необов'язкових полів та зберігання
    # обов'язкового поля Name.
    def __init__(self, name: Name, phone: Phone = None) -> None:
        self.name = name
        self.phones = []
        if phone:
            self.phones.append(phone)  # якщо телефон прийде як обьект классу то додамо його в список
        # self.emails = emails


    def add_phone(self, phone: Phone):
        phone_number = Phone(phone)
        if phone_number.value not in [ph.value for ph in self.phones]:
            self.phones.append(phone_number)


    def edit_phone(self, phone_old, phone_new: Phone):
        phone_number_old = Phone(phone_old)
        phone_number_new = Phone(phone_new)
        if phone_number_old.value in [ph.value for ph in self.phones]:
            print(phone_number_old.value in [ph.value for ph in self.phones])
            print('self.phones[0].value =', self.phones[0].value)
            self.phones[0].value = phone_number_new.value
        else:
            self.phones.append(phone_number_new)
            print('self.phones[1].value =', self.phones[1].value)


    def del_phone(self, phone: Phone): # не розумію, як видалити об"єкт (пише, що його не існує)
        # phone_number = Phone(phone)
        # if phone_number.value in [ph.value for ph in self.phones]:
            # self.phones.remove(phone_number)
        pass


class AddressBook(UserDict): # наслідується від UserDict, та ми потім додамо логіку пошуку за записами до цього класу

    def add_record(self, record: Record):
        self.data[record.name.value] = record

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

