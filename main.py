from class_gu import Guest, Gender, Party


def println():
    guest_1 = Guest(1, "Тарас",17,"Львів","097-098-77-57", Gender.MALE)
    guest_2 = Guest(3, "Станіслав",21,"Рівне","099-222-46-93", Gender.MALE)
    guest_3 = Guest(2, "Настя",22,"Хмельницький","099-777-62-04", Gender.FEMALE)
    guest_4 = Guest(5, "Ярина",18,"Львів","067-078-71-47", Gender.FEMALE)
    guest_5 = Guest(4, "Alexandro",35,"Київ","088-454-78-94", Gender.NON_BINARY)

    party = Party("31/10/2023", "Halloween")
    party.add_guest(guest_1)
    party.add_guest(guest_2)
    party.add_guest(guest_3)
    party.add_guest(guest_4)
    party.add_guest(guest_5)

    print(guest_1.is_lucky_phone_number())
    print(guest_2.is_lucky_phone_number())
    print(guest_3.is_lucky_phone_number())
    print(guest_4.is_lucky_phone_number())
    print(guest_5.is_lucky_phone_number())

    print(f"Середній вік жінок на вечірці: {party.find_average_age(Gender.FEMALE)}")
    print(f"Середній вік чоловіків на вечірці: {party.find_average_age(Gender.MALE)}")

    party.list_sort()


if __name__ == "__main__":
    println()
