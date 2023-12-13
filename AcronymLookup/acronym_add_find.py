def find_acronym():
    lookup = input("which acronym would you like to lookup?\n")

    try:
        found = False
        with open('acronyms.txt') as file:
            for line in file:
                if lookup in line:
                    print(line)
                    found = True
    except FileNotFoundError as e:
        print("File Not Found")
        return

    if not found:
        print("Acronym does not found")


def add_acronym():
    acronym = input("Which acronym would you like to add?\n")
    definition = input("Add the definition of that acronym\n")

    with open("acronyms.txt", 'a') as file:
        file.write('\n' + acronym + "-" + definition)
        print(acronym, "-", definition, "added successfully!")


def main():
    option = input('Do you want to "Add" or "Search"?\n').lower()

    if option == "add":
        add_acronym()
    elif option == "search":
        find_acronym()
    else:
        print('Choose "Add" or "Search"')
        main()


main()
