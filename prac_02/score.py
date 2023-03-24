score = float(input("Enter score: "))
if score < 0 or score > 100:
    response = "Invalid score"
elif score < 50:
    response = "Bad"
elif score < 90:
    response = "Pass"
else:
    response = "Excellent"

print(response)
