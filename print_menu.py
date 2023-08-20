def print_menu():
    print("Today's Menu:")
    print(" 1)Gumbo")
    print(" 2)Jambalaya")
    print(" 3)Quit\n")
quit_program = False
while not quit_program:
    print_menu()
    choice = int(input("Enter Choice: "))
    if choice == 3:
        print("Good Bye")
        quit_program = True
    else:
        print('Order: ', end="")
        if choice == 1:
            print("Gumbo")
        elif choice == 2:
            print("Jambalaya")
        print()