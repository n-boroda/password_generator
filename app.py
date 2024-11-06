import random


def password_generator(lenth:int) -> str:
    '''generates passwords'''
    password = ""
    letters = "qwertyuiopasdfghjklzxcvbnm"
    if input("should we add upper case?: ") == "yes":
        letters += "QWERTYUIOPASDFGHJKLZXCVBNM"
    if input("should we add digits?: ") == "yes":
        letters += "1234567890"
    if input("should we add special symbols?: ") == "yes":
        letters += "~!@#$%^&*()_+{]}[;',./|<>?"
    for i in range(lenth):
        password += random.choice(letters)
    return password


print(password_generator(int(input("enter the lenth of your password: "))))