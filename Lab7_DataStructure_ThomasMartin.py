candy_list = ["Candy bar", "Red vine", "gummies"]


def getMenuChoice():
    option = 0
    print("1 - Add Candy")
    print("2 - Remove Candy")
    print("3 - List candy")
    print("4 - Exit")
    option = input("Please enter your option ")
    option = int(option)
    candyStore(option)


def candyStore(opt):
    if opt == 1:
        candy = input("Type in the candy you want to add ")
        if candy in candy_list:
            print("It already is on the list")
            getMenuChoice()
        else:
            candy_list.append(candy)
            getMenuChoice()
    elif opt == 2:
        candy = input("Type in the candy you want to remove ")
        if candy in candy_list:
            candy_list.remove(candy)
            getMenuChoice()
        else:
            print("It is not on the list")
            getMenuChoice()
    elif opt == 3:
        print(candy_list)
        getMenuChoice()
    elif opt == 4:
        print("Goodbye")
    else:
        print("Invalid option")
        getMenuChoice()


getMenuChoice()