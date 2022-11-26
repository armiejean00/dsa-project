import time
import os
print("This is about games that implement queue, stack and linked-list.")
def print_menu():

    print("::::    ::::  :::::::::: ::::    ::: :::    :::")
    print("+:+:+: :+:+:+ :+:        :+:+:   :+: :+:    :+:")
    print("+:+ +:+:+ +:+ +:+        :+:+:+  +:+ +:+    +:+")
    print("+#+  +:+  +#+ +#++:++#   +#+ +:+ +#+ +#+    +:+")
    print("+#+       +#+ +#+        +#+  +#+#+# +#+    +#+")
    print("#+#       #+# #+#        #+#   #+#+# #+#    #+#")
    print("###       ### ########## ###    ####  #########")
        
    print("************************************************")
    print("*                 1.Play                       *")
    print("*                 2.About                      *")
    print("*                 3.Exit                       *")
    print("************************************************")


print_menu()
option=input("Make a choice||...: ")
if option == "1":
    time.sleep(2.0)
    from menu import print_menu1
elif option == "2":
    print("This is about games that implement queue, stack and linked-list.")
    
elif option == "3":
    exit()



