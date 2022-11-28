import os
import time

def print_menu4():
    print("***********************************************************************************************")
    print('*                                                                                             *')
    print('*                                                                                             *')
    print('*                             ███████╗████████╗ █████╗  ██████╗██╗  ██╗                       *')
    print('*                             ██╔════╝╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝                       *')
    print('*                             ███████╗   ██║   ███████║██║     █████╔╝                        *')
    print('*                             ╚════██║   ██║   ██╔══██║██║     ██╔═██╗                        *')
    print('*                             ███████║   ██║   ██║  ██║╚██████╗██║  ██╗                       *')
    print('*                             ╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝                       *')
    print('*                                                                                             *')
    print("*                                             1.Play                                          *")
    print("*                                             2.How to Play                                   *")
    print("*                                             3.Back                                          *")
    print('*                                                                                             *')
    print("***********************************************************************************************")


    option=input("                                       Enter your choice: ")
    if option == "1":
    
     from stack import create_game
    elif option == "2":
     print("4 in a row is a game that........")
     
    elif option == "3":
          time.sleep(1.0)        
          from menu import print_menu1
          
print(print_menu4())