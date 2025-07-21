def getMenuChoice():
    option = 0
    print("1 - Add Book")
    print("2 - List Books")
    print("3 - Exit")
    option = input("Please enter your option ")
    option = int(option)
    Books(option)


def Books(opt):
    if opt == 1:
        inpfilea = open("books.txt", "a")
        book = input("Type in the Book you want to add ")
        inpfilea.write(book)
        inpfilea.close()
        getMenuChoice()
    elif opt == 2:
        inpfiler = open("books.txt", "r")
        print(inpfiler.read())
        getMenuChoice()
    elif opt == 3:
        print("Goodbye")
    else:
        print("Invalid option")
        getMenuChoice()


getMenuChoice()
