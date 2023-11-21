from enum import Enum


class Gender(Enum):

    FEMALE = "FEMALE"
    MALE = "MALE"
    NON_BINARY = "NON_BINARY"


class Guest:

    def __init__(self, id, name, age, city, phone_number, gender):
        '''
        Функція для ініціалізації основних атрибутів в класі Guest.
        '''
        self.id = id
        self.name = name
        self.age = age
        self.city = city
        self.phone_number = phone_number
        self.gender = gender

    def is_lucky_phone_number(self):
        '''
        Функція для визначення чи є номер користувача щасливим.
        '''
        if self.phone_number.count('7') > 3:
            print(f"Номер користувача {self.name} є щасливим.")
        else:
            print(f"Номер користувача {self.name} є не щасливим.")


class Party:

    def __init__(self, day, reason):
        '''
        Функція для ініціалізації основних атрибутів в класі Party.
        '''
        self.day = day
        self.reason = reason
        self.guests = []

    def add_guest(self, guest):
        '''
        Функція для додавання гостей в список і повернення його.
        '''
        return self.guests.append(guest)

    def find_average_age(self, gender):
        '''
        Функція для знаходження середнього арифметичного віку гостей згідно їхньої статті.
        '''
        total_age = 0
        index = 0
        for guest in self.guests:
            if guest.gender == gender:
                total_age += guest.age
                index += 1
        return total_age / index

    def list_sort(self):
        '''
        Функція для сортування гостей по їхньому id.
        '''
        sorted_guests = sorted(self.guests, key=lambda guest: guest.id)
        print("Список гостей за номером id:")
        for guest in sorted_guests:
            print(f"id: {guest.id}, Ім'я: {guest.name}, Вік: {guest.age}")
