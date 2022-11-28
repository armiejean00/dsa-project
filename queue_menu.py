import os
import time

def clear():
    os.system('clear||cls')
def print_menu3():
    print("********************************************************************************************")
    print('*                                                                                          *')
    print('*                                                                                          *')
    print('*                           ██████╗ ██╗   ██╗███████╗██╗   ██╗███████╗                     *')
    print('*                          ██╔═══██╗██║   ██║██╔════╝██║   ██║██╔════╝                     *')
    print('*                          ██║   ██║██║   ██║█████╗  ██║   ██║█████╗                       *')
    print('*                          ██║▄▄ ██║██║   ██║██╔══╝  ██║   ██║██╔══╝                       *')
    print('*                          ╚██████╔╝╚██████╔╝███████╗╚██████╔╝███████╗                     *')
    print('*                           ╚══▀▀═╝  ╚═════╝ ╚══════╝ ╚═════╝ ╚══════╝                     *')
    print('*                                                                                          *')
    print("*                                             1.Play                                       *")
    print("*                                             2.How to Play                                *")
    print("*                                             3.Back                                       *")
    print('*                                                                                          *')
    print("********************************************************************************************")



    option=input("                                        Enter your choice: ")
    if option == "1":
        time.sleep(2.0)
        from wordguess import main

    elif option == "2":
      
      print('This game')
      

 
    elif option == "3":
      clear()
      from menu import print_menu1

print(print_menu3())
     
      
