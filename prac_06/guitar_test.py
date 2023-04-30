from prac_06.guitar import Guitar

gibson = Guitar("Gibson L-5 CES", 1922, 16035.4)
another = Guitar("Another Guitar", 2013, 10000)

print(gibson.get_age())
print(another.get_age())
print(gibson.is_vintage())
print(another.is_vintage())
