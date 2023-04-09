# 1
numbers = []


def main():
    get_numbers(5, "Number: ")
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers)}")


def get_numbers(times, prompt):
    for i in range(times):
        numbers.append(int(input(prompt)))


main()

# 2
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = str(input("Your username: "))
if username in usernames:
    print("Access granted")
else:
    print("Access denied")
