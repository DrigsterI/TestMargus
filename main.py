import copy

import regex as re
from tabulate import tabulate


filename = "contacts.txt"


def check_name():
    while True:
        name = input("Name: ")
        if re.match(r'^[\p{L} ]+$', name, re.U):
            break
        else:
            print("Name must have only letters and spaces")
    return name


def check_phone():
    while True:
        phone = input("Phone: ")
        if re.match(r'^[+]?(372[ ]?)?[2-7]([ ]?[0-9]){6,7}$', phone):
            break
        else:
            print("Not a phone number")
    return phone


def check_age():
    while True:
        age = input("Age: ")
        if age.isnumeric():
            break
        else:
            print("Age must be a number")
    return age


def check_email():
    while True:
        email = input("Email: ")
        if re.match(r'^[\w\d.]+@[\w\d]+\.[\w\d]+$', email):
            break
        else:
            print("Not email")
    return email


def check_index(maxLen):
    while True:
        index = input("Index of contact")
        if index.isnumeric():
            index = int(index)
        else:
            print("Index must be number")
        if index < maxLen:
            break
        else:
            print("Index is lager than amount of contacts")
    return index


def read_db(filename):
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


def write_db(db, filename):
    with open(filename, "w", encoding='utf-8') as file:
        data = []
        database = copy.deepcopy(db)
        for contact in database:
            contact.pop(0)
            data.append(", ".join(contact) + "\n")
        file.write("".join(data))


def add(db):
    print("\n")
    print("You are trying to add contact.")
    name = check_name()
    phone = check_phone()
    age = check_age()
    email = check_email()
    index = int(db[-1][0]) + 1
    contact = [index, name, phone, age, email]
    print(contact)
    db.append(contact)
    write_db(db, filename)


def edit(db):
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

def print_db(db):
    print("\n")
    print(tabulate(db, headers=["Index", "Name", "Phone", "Age", "Email"]))
    print("\n")


def print_menu():
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
        elif inpt == "4":
            print("You are trying to delete contact.")
            index = check_index(len(db))
            db.pop(index)
            write_db(db, filename)

        print_menu()
        inpt = str(input("Chose action: "))



if __name__ == '__main__':
    main()
