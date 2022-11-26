
def print_menu1():


    print(" ::::::::      :::     ::::    ::::  ::::::::::")
    print(":+:    :+:   :+: :+:   +:+:+: :+:+:+ :+:       ")
    print("+:+         +:+   +:+  +:+ +:+:+ +:+ +:+       ")
    print(":#:        +#++:++#++: +#+  +:+  +#+ +#++:++#  ")
    print("+#+   +#+# +#+     +#+ +#+       +#+ +#+       ")
    print("#+#    #+# #+#     #+# #+#       #+# #+#       ")
    print(" ########  ###     ### ###       ### ##########")
        
    print("************************************************")
    print("*                 1.Stack                      *")
    print("*                 2.Queue                      *")
    print("*                 3.Link-List                  *")
    print("*                 4.Quit                       *")
    print("************************************************")
    
    while 1:

        ch = int(input("Enter your choice: "))
        if ch == 1:
          import stack_menu
          stack_menu4
        elif ch == 2:
            import queue_menu
            queue_menu3
        elif ch == 3:
            from link_menu import print_menu5
        elif ch == 4:
            break
        else:
            print("Wrong Choice!")
            
            return print_menu1()


print(print_menu1())