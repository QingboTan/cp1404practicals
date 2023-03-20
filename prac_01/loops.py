# a
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# b
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c
star_number = int(input("Number of stars:"))
for i in range(star_number):
    print("*", end='')
print()

# d
for i in range(star_number):
    for a in range(i+1):
        print("*", end='')
    print()

# for i in range(1, star_number + 1, 1):
#     print('*' * i)
# print()