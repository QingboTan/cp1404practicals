import random
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45
NUMBERS_PER_LINE = 6


number_of_rows = int(input("How many quick picks? "))
for i in range(number_of_rows):
    quick_pick = []
    while len(quick_pick) < NUMBERS_PER_LINE:
        numbers = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        quick_pick.append(numbers)
    quick_pick.sort()
    print("{:2} {:2} {:2} {:2} {:2} {:2}".format(*quick_pick))
