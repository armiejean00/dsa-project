def print_menu3():
    print("********************************")
    print("*           1.Play             *")
    print("*           2.How to Play      *")
    print("*           3.Back             *")
    print("********************************")


    while 1:

        ch = int(input("Enter a choice: "))
        if ch == 1:
          import wordguess
          
        elif ch == 2:
            print("This game is wordguess")
        elif ch == 3:
            break

print(print_menu3())
