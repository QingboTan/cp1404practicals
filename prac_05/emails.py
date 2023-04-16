"""
emails
Estimate: 20 minutes
Actual:
"""

name_email_dictionary = {}
email_input = input("Email: ")
while email_input != "":
    choice = input(f"Is your name {email_input.split('@')[0]}?(Y/n)").lower()
    if choice == "n":
        name = input("Name: ")
    elif choice == "y":
        name = email_input.split('@')[0].title()
    else:
        print("Invalid choice")
        choice = input(f"Is your name {email_input.split('@')[0]}?(Y/n)").lower()
    name_email_dictionary[name] = email_input.title()
    email_input = input("Email: ")

for name, email in name_email_dictionary.items():
    print(f"{name} ({email})")
