import random
import string

def generate_password():
    while True:
        try:
            password_length = int(input("How long the password should be ? "))
        except ValueError:
            print("Invalid input. Please enter a number")
            continue
        character_types = input("What character types should be included (lowercase, uppercase, numbers, symbols) ? ").lower()
        numbers = string.digits
        symbols = string.punctuation
        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase

        pool = ""

        if "lowercase" in character_types:
            pool += lowercase

        if "uppercase" in character_types:
            pool += uppercase

        if "numbers" in character_types:
            pool += numbers

        if "symbols" in character_types:
            pool += symbols

        if pool == "":
            print("Please choose at least one character type!")
            continue

        output = ""

        for _ in range(password_length):

            output += random.choice(pool)
        print(output)

        another_password = input("Would you like to generate another password? Please enter YES or NO: ").upper()
        if another_password == "YES":
            continue

        elif another_password == "NO":
            break


if __name__ == "__main__":
    generate_password()
