def main():
    password = get_password()
    length_minimum = int(input("Enter password minimum length: "))
    while len(password) < length_minimum:
        print("Your password doesn't meet a minimum length")
        password = get_password()
    print("*" * len(password))


def get_password():
    password = str(input("Enter your password: "))
    return password


main()
