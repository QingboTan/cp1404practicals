CODE_TO_COLOURS = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a", "Aureolin": "#fdee00", "Amaranth": "#e52b50",
                   "Amber": "#ffbf00", "Amethyst": "#9966cc", "Aqua": "#00ffff", "Apricot": "#fbceb1", "Beige": "#f5f5dc",
                   "Beaver": "#9f8170"}

print(CODE_TO_COLOURS)
colour_name = input("Enter colour: ").title()
while colour_name != "":
    if colour_name in CODE_TO_COLOURS:
        print(CODE_TO_COLOURS[colour_name])
    else:
        print("Invalid Input")
    colour_name = input("Enter colour: ").title()
print("Thank you")
