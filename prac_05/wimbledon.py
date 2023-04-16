champions = {}
countries = {}


def main():
    read_file("wimbledon.csv")
    display_champion()
    display_country()


def read_file(filename):
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        for data in in_file.readlines()[1:]:
            data = data.split(",")
            if data[2] not in champions:
                champions[data[2]] = 1
                countries[data[1]] = 0
            else:
                champions[data[2]] += 1


def display_country():
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(", ".join(country for country in countries))


def display_champion():
    for champion in champions:
        print(f"{champion}: {champions[champion]}")


main()
