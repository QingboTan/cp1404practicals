MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    print(MENU)
    choice = get_choice()
    while choice != "Q":
        if choice == "C":
            celsius = get_temperature("Celsius: ")
            fahrenheit = celsius * 9.0 / 5 + 32
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = get_temperature("Fahrenheit: ")
            celsius = 5 / 9 * (fahrenheit - 32)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = get_choice()
    print("Thank you.")


def get_temperature(prompt):
    temperature = float(input(prompt))
    return temperature


def get_choice():
    choice = input(">>> ").upper()
    return choice


main()
