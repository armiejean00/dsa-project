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
	

	
    option = input("Login or Register  (Login,Reg): ")
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

    
    import pygame, sys
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1380, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.jpg")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(45).render(" I love chicken nuggets.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)
        
        
       


        PLAY_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(55), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        OPTIONS_TEXT = get_font(45).render("muahmuahh.", True, "white")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(55), base_color="White", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def about():
    while True:
        ABOUT_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        ABOUT_TEXT = get_font(45).render(" I love chicken.", True, "White")
        ABOUT_RECT = ABOUT_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(ABOUT_TEXT, ABOUT_RECT)
        
        
       


        ABOUT_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(55), base_color="White", hovering_color="Green")

        ABOUT_BACK.changeColor(ABOUT_MOUSE_POS)
        ABOUT_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ABOUT_BACK.checkForInput(ABOUT_MOUSE_POS):
                    main_menu()

        pygame.display.update()
    
def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(50).render("Let's Play", True, "#ff5c33")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=None, pos=(640, 250), 
                            text_input="PLAY", font=get_font(55), base_color="#d7fcd4", hovering_color="yellow")
        OPTIONS_BUTTON = Button(image=None, pos=(640, 350), 
                            text_input="OPTIONS", font=get_font(55), base_color="#d7fcd4", hovering_color="yellow")
        ABOUT_BUTTON = Button(image=None, pos=(640, 450), 
                            text_input="ABOUT", font=get_font(55), base_color="#d7fcd4", hovering_color="yellow")
                    
        QUIT_BUTTON = Button(image=None, pos=(640, 550), 
                            text_input="QUIT", font=get_font(55), base_color="#d7fcd4", hovering_color="yellow")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON,ABOUT_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if ABOUT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    about()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()