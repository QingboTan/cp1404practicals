"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

# score = float(input("Enter score: "))
# if score < 0:
#     print("Invalid score")
# else:
#     if score > 100:
#         print("Invalid score")
#     if score > 50:
#         print("Passable")
#     if score > 90:
#     print("Excellent")
# if score < 50:
#     print("Bad")

score = float(input("Enter score: "))
if 0 <= score < 50:
    result = "Bad"
elif 50 <= score < 90:
    result = "Passable"
elif 90 <= score <= 100:
    result = "Excellent"
else:
    result = "Invalid score"
print(result)

