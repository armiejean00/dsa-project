import time
import os


def clear():
    os.system('clear||cls')
def print_menu():

    clear()
    print('\u001b[36;1m****************************************************************************************************************************')
    print('*                                                                                                                          *')
    print('*                                                                                                                          *')
    print('*                                             ███╗   ███╗███████╗███╗   ██╗██╗   ██╗                                       *')
    print('*                                             ████╗ ████║██╔════╝████╗  ██║██║   ██║                                       *')
    print('*                                             ██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║                                       *')
    print('*                                             ██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║                                       *')
    print('*                                             ██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝                                       *')
    print('*                                             ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝                                        *')
    print('*                                                                                                                          *')        
    print("*                                                                                                                          *")
    print("*                                                                1.Play                                                    *")
    print("*                                                                2.About                                                   *")
    print("*                                                                3.Exit                                                    *")
    print('*                                                                                                                          *')
    print("****************************************************************************************************************************\u001b[37m")


  
    option=input("Enter your choce: ")
    if option == "1":
        time.sleep(1.0)
        clear()
        from menu import print_menu1
    elif option == "2":
      clear()
      print("This is about games that implement queue, stack and linked-list.")
      print(print_menu())
    elif option == "3":
     exit()

print(print_menu())

