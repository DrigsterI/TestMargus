import copy

import regex as re
from tabulate import tabulate  # Library that helps to

filename = "contacts.txt"


def check_name():  # Checking name input
    while True:
        name = input("Name: ")
        if re.match(r'^[\p{L} ]+$', name, re.U):
            break
        else:
            print("Name must have only letters and spaces.")
    return name


def check_phone():  # Checking phone input
    while True:
        phone = input("Phone: ")
        if re.match(r'^[+]?(372[ ]?)?[2-7]([ ]?[0-9]){6,7}$', phone):
            break
        else:
            print("Not a phone number.")
    return phone


def check_age():  # Checking age input
    while True:
        age = input("Age: ")
        if age.isnumeric():
            break
        else:
            print("Age must be a number.")
    return age


def check_email():  # Checking email input
    while True:
        email = input("Email: ")
        if re.match(r'^[\w\d.]+@[\w\d]+\.[\w\d]+$', email):
            break
        else:
            print("Not email.")
    return email


def check_index(maxLen):  # Checking index input
    while True:
        index = input("Index of contact: ")
        if index.isnumeric():
            index = int(index)
        else:
            print("Index must be number.")
            continue
        if index < maxLen:
            break
        else:
            print("Index is lager than amount of contacts.")
            continue
    return index


def read_db(filename):  # Reading db from file
    with open(filename, "r", encoding='utf-8') as file:
        data = file.readlines()
        db = []
        i = 0
        for line in data:
            line = line.replace("\n", "")
            line = f"{i}, " + line
            db.append(line.split(", "))
            i = i + 1
        return db


def write_db(db, filename):  # Writing db to file
    with open(filename, "w", encoding='utf-8') as file:
        data = []
        database = copy.deepcopy(db)
        for contact in database:
            contact.pop(0)
            data.append(", ".join(contact) + "\n")
        file.write("".join(data))


def medium_age(db):  # Calculating medium age
    i = 0
    ageSum = 0
    for contact in db:
        i = i + 1
        ageSum = ageSum + int(contact[3])
    medAge = ageSum / i
    return medAge


def add(db):  # Adding contact
    print("\n")
    print("You are trying to add contact.")
    name = check_name()
    phone = check_phone()
    age = check_age()
    email = check_email()
    index = int(db[-1][0]) + 1
    contact = [index, name, phone, age, email]
    db.append(contact)
    write_db(db, filename)


def edit(db):  # Editing contact
    print("You are trying to edit contact.")
    print_db(db)
    index = check_index(len(db))
    contact = db[index]
    field = input("What you want to edit?(name/phone/age/email): ")
    contact[0] = db[-1][0]
    if field == "name":
        contact[1] = check_name()
    elif field == "phone":
        contact[2] = check_phone()
    elif field == "age":
        contact[3] = check_age()
    elif field == "email":
        contact[4] = check_email()
    write_db(db, filename)


def print_db(db):  # Printing database
    print("\n")
    print(tabulate(db, headers=["Index", "Name", "Phone", "Age", "Email"]))
    print("\n")
    medAge = round(medium_age(db))
    print(f"\tMedium age is {medAge}.")
    print("\n")


def print_menu():  # Printing menu
    print("1. List contacts")
    print("2. Add contact")
    print("3. Edit contact")
    print("4. Remove contact")
    print("5. Exit")


def main():
    db = read_db(filename)

    print_menu()
    inpt = str(input("Chose action: "))
    while inpt != "5":
        if inpt == "1":
            print_db(db)
        elif inpt == "2":
            add(db)
        elif inpt == "3":
            edit(db)
        elif inpt == "4":  # Deliting contact
            print("You are trying to delete contact.")
            index = check_index(len(db))
            db.pop(index)
            write_db(db, filename)

        print_menu()
        inpt = str(input("Chose action: "))


if __name__ == '__main__':
    main()
