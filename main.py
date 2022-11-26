import time
granted = False
def grant():
    global granted
    granted = True
def login(name,password):
    success = False
    file = open("user_detail.txt","r")
    for i in file:
         a,b = i.split(",")
         b = b.strip()
         if(a==name and b==password):
             success = True
             break
    file.close()
    if(success):
        print("Login Successful!")
        grant()
    else:
        print("<xxx>WRONG USERNAME OR PASSWORD<xxx>")
     
		
        
def register(name,password):
    file = open("user_detail.txt","a")
    file.write("\n"+name+","+password)
    grant()
def access(option):
    global name
    if(option=="login"):
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        login(name,password)
    else:
        print("Enter your name and password to register")
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        register(name,password)



def begin():
    global option
	
    print("<<<------Welcome to our Game------>>>")
	

	
    option = input("login||reg: ")
    
    if(option!="login" and option!="reg"):
        begin()
	
        
begin()
access(option)

if(granted):
    print("✨------Welcome to our Game------✨")
    print("****USER DETAILS****")
    print("Username: ",name)




    print("----------------------------------------------------------------------------")


    print("                                                                          ")
    print("                          --                        ,,                    ")
    print("-7MMF'                mm  \/            `7MM...Mq. 7MM                    ")
    print("  MM                  MM  `'              MM   `MM. MM                    ")
    print("  MM         .gP-Ya mmMMmm  ,pP-Y-d       MM   ,M9  MM   ,6-Yb.`7M'   `MF'")
    print("  MM        ,M'   Yb  MM    8I   `.       ..99dM9   MM  8)   MM  VA   ,V  ")
    print("  MM      , 8M------  MM    `YMMMa.       MM        MM   ,pm9MM   VA ,V   ")
    print("  MM     ,M YM.    ,  MM    L.   I8       MM        MM  8M   MM    VVV    ")
    print(".JMMmmmmMMM  `Mbmmd'  `Mbmo M9mmmP'     .JMML.    .JMML.`Moo9^Yo.  ,V     ")
    print("                                                                  ,V      ")
    print("                                                               OOb-       ")
	
    print("-------------wait a seconds...--------------------------------------------")
	

    time.sleep(3.5)

    from main2 import print_menu





    

  