MENU = ("(G)et a valid score (must be 0-100 inclusive)\n(P)rint result\n(S)how stars\n(Q)uit")


def main():
    print(MENU)
    choice = get_choice("Enter your choice: ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_score("Enter score: (Must be 0-100 inclusive)")
        elif choice == "P":
            result = check_score(score)
            print(f"Your result is {result}")
        elif choice == "S":
            print("*" * int(score))
        else:
            print("Invalid choice")
        print(MENU)
        choice = get_choice("Enter your choice: ").upper()
    print("Thank you, Bye!")


def get_choice(prompt):
    choice = str(input(prompt))
    return choice


def get_score(prompt):
    score = float(input(prompt))
    return score


def check_score(score):
    if score < 0 or score > 100:
        response = "Invalid score"
    elif score < 50:
        response = "Bad"
    elif score < 90:
        response = "Pass"
    else:
        response = "Excellent"
    return response


main()
