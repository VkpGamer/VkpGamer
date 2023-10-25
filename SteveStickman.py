"""
Name: Vincent Penick

Date: 9/6/2023
Class: CSSE, Guillaume, Tri 1 2023 
Game: Steve Stickman

Description:
    This is a chose your own adventure game about a stickman that goes trough many rounds of shenanigans
"""
import os, random

#This is the tilte screen and start of the game
def Start():
    os.system('cls')
    print("\n░██████╗████████╗███████╗██╗░░░██╗███████╗  ░██████╗████████╗██╗░█████╗░██╗░░██╗███╗░░░███╗░█████╗░███╗░░██╗\n██╔════╝╚══██╔══╝██╔════╝██║░░░██║██╔════╝  ██╔════╝╚══██╔══╝██║██╔══██╗██║░██╔╝████╗░████║██╔══██╗████╗░██║\n╚█████╗░░░░██║░░░█████╗░░╚██╗░██╔╝█████╗░░  ╚█████╗░░░░██║░░░██║██║░░╚═╝█████═╝░██╔████╔██║███████║██╔██╗██║\n░╚═══██╗░░░██║░░░██╔══╝░░░╚████╔╝░██╔══╝░░  ░╚═══██╗░░░██║░░░██║██║░░██╗██╔═██╗░██║╚██╔╝██║██╔══██║██║╚████║\n██████╔╝░░░██║░░░███████╗░░╚██╔╝░░███████╗  ██████╔╝░░░██║░░░██║╚█████╔╝██║░╚██╗██║░╚═╝░██║██║░░██║██║░╚███║\n╚═════╝░░░░╚═╝░░░╚══════╝░░░╚═╝░░░╚══════╝  ╚═════╝░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝")
    play = input("\n1>Play\n2>How To Play\n3>Credits\n4>Quit\n>>")
    if play == "1":
        os.system('cls')
        print("(!YOU GET A BETTER EXERIENCE IF YOU DO IT IN ORDER!)")
        print("████████████████████████████████████████████████████████████████████████████████████████████████\n█─▄▄▄─█─█─██▀▄─██▄─▄▄─█─▄─▄─█▄─▄▄─█▄─▄▄▀███─▄▄▄▄█▄─▄▄─█▄─▄███▄─▄▄─█─▄▄▄─█─▄─▄─█▄─▄█─▄▄─█▄─▀█▄─▄█\n█─███▀█─▄─██─▀─███─▄▄▄███─████─▄█▀██─▄─▄███▄▄▄▄─██─▄█▀██─██▀██─▄█▀█─███▀███─████─██─██─██─█▄▀─██\n▀▄▄▄▄▄▀▄▀▄▀▄▄▀▄▄▀▄▄▄▀▀▀▀▄▄▄▀▀▄▄▄▄▄▀▄▄▀▄▄▀▀▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀▄▄▄▀▄▄▄▄▀▄▄▄▀▀▄▄▀\n")
        print("\n1.The Beginning\n█▀ ▀█▀ █▀▀ ▄▀█ █░░   ▀█▀ █░█ █▀▀   █▀▄▀█ █▀█ █▄░█ █▀▀ █▄█\n▄█ ░█░ ██▄ █▀█ █▄▄   ░█░ █▀█ ██▄   █░▀░█ █▄█ █░▀█ ██▄ ░█░")
        print("▄▀█ █▄░█ █▀▄\n█▀█ █░▀█ █▄▀")
        print("█▀ ▀█▀ █▀▀ ▄▀█ █░░   ▀█▀ █░█ █▀▀   █▀▀ █▀▀ █▀▄▀█\n▄█ ░█░ ██▄ █▀█ █▄▄   ░█░ █▀█ ██▄   █▄█ ██▄ █░▀░█")
        print("\n2.The Middle\n░█▀▀█ █▀▀█ █▀▀ █▀▀█ █ █ 　 ▀▀█▀▀ █  █ █▀▀ 　    ░█ █▀▀█  ▀  █  ")
        print("░█▀▀▄ █▄▄▀ █▀▀ █▄▄█ █▀▄ 　  ░█   █▀▀█ █▀▀ 　  ▄ ░█ █▄▄█ ▀█▀ █  ")
        print("░█▄▄█ ▀ ▀▀ ▀▀▀ ▀  ▀ ▀ ▀ 　  ░█   ▀  ▀ ▀▀▀ 　 ░█▄▄█ ▀  ▀ ▀▀▀ ▀▀▀")
        print("\n3.The End\n▀█▀ █▀▀▄ █▀▀  ▀  █   ▀▀█▀▀ █▀▀█ █▀▀█ ▀▀█▀▀ █▀▀ 　 ▀▀█▀▀ █  █ █▀▀ 　 ░█▀▀█ █▀▀█ █▀▀ █▀▀ ")
        print("░█  █  █ █▀▀ ▀█▀ █     █   █▄▄▀ █▄▄█   █   █▀▀ 　  ░█   █▀▀█ █▀▀ 　 ░█▀▀▄ █▄▄█ ▀▀█ █▀▀")
        print("▄█▄ ▀  ▀ ▀   ▀▀▀ ▀▀▀   ▀   ▀ ▀▀ ▀  ▀   ▀   ▀▀▀ 　  ░█   ▀  ▀ ▀▀▀ 　 ░█▄▄█ ▀  ▀ ▀▀▀ ▀▀▀")
        chapterslection = input("\n>>")
        if chapterslection == "1":
            os.system('cls')
            BorG = input("Steve is just chilling on the couch when he looks at his bank balence. 0 Dollers. He looks back up at the TV and sees that the bank is on the news for an attemt at being robbed and that their still recovering form it. He flips a channel and sees a huge jem inthe jewlery store... His eyes gleam as he gets up and walks to the door.\n1>Bank\n2>Gem\n3>Filp Coin\n>>")
            if BorG == "1":
                GameBank()
            elif BorG == "2":
                GameGem()
            elif BorG == "3":
                flipCoin = random.randrange(1,3)
                if flipCoin == 1:
                    GameBank()
                elif flipCoin == 2:
                    GameGem()
    #This is if the player gets an imposible number on the coin flip
                else:
                    os.system('cls')
                    print("How did you even get here?")
                    exit()
            else:
                os.system('cls')
                print("You change your mind and go bankrupt\n\nFAIL\nWasn't feeling it ay?\n")
                retry = input("Retry? Y/N ").upper()
                if retry == "Y":
                    Start() 
                else:
                    Start()
        elif chapterslection == "2":
            Gamejail()
        elif chapterslection == "3":
            GameITBstart()
        else:
            Start()
    elif play == "2":
        os.system('cls')
        print("╭╮╱╭╮╱╱╱╱╱╱╱╱╭━━━━╮╱╱╭━━━┳╮\n┃┃╱┃┃╱╱╱╱╱╱╱╱┃╭╮╭╮┃╱╱┃╭━╮┃┃\n┃╰━╯┣━━┳╮╭╮╭╮╰╯┃┃┣┻━╮┃╰━╯┃┃╭━━┳╮╱╭╮\n┃╭━╮┃╭╮┃╰╯╰╯┃╱╱┃┃┃╭╮┃┃╭━━┫┃┃╭╮┃┃╱┃┃\n┃┃╱┃┃╰╯┣╮╭╮╭╯╱╱┃┃┃╰╯┃┃┃╱╱┃╰┫╭╮┃╰━╯┃\n╰╯╱╰┻━━╯╰╯╰╯╱╱╱╰╯╰━━╯╰╯╱╱╰━┻╯╰┻━╮╭╯\n╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃\n╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯\n")
        print(">To start you need to type 1 on the main menu\n>A list of options will be shown each round\n>To pick an option type a vaild number and get your answer\n>If you type a wrong number you will fail\n>If you fail then you will need to restart via Y or N\n>If you restart you will start again from your last checkpoint if not you will be sent back to the main menu\n>To go back just type Y or N")
        HTPback = input("\nGoBack? Y/N ").upper()
        if HTPback == "Y":
            Start()
        else:
            print('\nUh... well shoot I didnt think you would say no...')
    elif play == "3":
        os.system('cls')
        print("╔═══╗──────╔╗╔╗\n║╔═╗║──────║╠╝╚╗\n║║─╚╬═╦══╦═╝╠╗╔╬══╗\n║║─╔╣╔╣║═╣╔╗╠╣║║══╣\n║╚═╝║║║║═╣╚╝║║╚╬══║\n╚═══╩╝╚══╩══╩╩═╩══╝\n")
        print(">Code and Story: Vincent Penick\n>Visuals: BIG TEXT Letters Font Generator\n>Inspiration: Henry Stickmin\n>Other Cool Guys: Chase Graber and Skyler Henderson\n>Many Thanks: You!")
        HTPback = input("\nGoBack? Y/N ").upper()
        if HTPback == "Y":
            Start()
        else:
            print('\nUh... well shoot I didnt think you would say no...')
    elif play == "4":
        print("\nHaha now your bankrupt FAIL+L+Ratio+Smh+Lmao+Ustupid+Broke")
        exit()
    else:
        os.system('cls')
        print("You go bankrupt\n\nFAIL\nAlready?\n")
        retry = input("Retry? Y/N ").upper()
        if retry == "Y":
            Start() 
        else:
            Start()

#This is the Bank path of the game
def GameBank():
    os.system('cls')
    bankEnd = input("You go out your house and start to walk\n26 hours later\nYou finally make it to the bank in the middle of the desert and go to the side of it\n1>Lazer\n2>Machine\n3>Ram\n4>Hide\n5>Wait\n6>Magic\n7>Sleep\n>>")
    if bankEnd == "1":
        os.system('cls')
        print("You take the lazer and charge it up... as soon as it starts to fire it turns around to face you and splits you in half\n\nFAIL\nWell that back fired\n")
        retry = input("Retry? Y/N ").upper()
        if retry == "Y":
           GameBank() 
        else:
            Start()
    elif bankEnd == "2":
        os.system('cls')
        print("You walk off and come back with an almost destroyed machine. You try and use it and it crashes down on top of you\n\nFAIL\nCheep isnt always the best\n")
        retry = input("Retry? Y/N ").upper()
        if retry == "Y":
           GameBank() 
        else:
            Start()
    elif bankEnd == "3":
        os.system('cls')
        print("You walk off and come back with a car. you ram into the wall and the carsh smashes the catches on fire\n\nFAIL\nHow did you even get a car?\n")
        retry = input("Retry? Y/N ").upper()
        if retry == "Y":
           GameBank() 
        else:
            Start()
    elif bankEnd == "4":
        os.system('cls')
        print("You go around a corner and hide\n24 DAYS LATER\n\nFAIL\nYou must be really good at hide and seek\n")
        retry = input("Retry? Y/N ").upper()
        if retry == "Y":
           GameBank() 
        else:
            Start()
    elif bankEnd == "5":
        os.system('cls')
        waitbank = input("You wait untill the front gate is open and sneek inside then you make your way to thd valt door\n1>Wait\n2>Break\n3>Magic\n>>")
        if waitbank == "1":
            os.system('cls')
            print("You wait in a corner untill someone opens the valt door and you sneak inside where you wait untill they leave. You try and walk your way to the money but you get caught by a lazer and alarms start going off\"FREEZE\"\n\nEnding:\nᖇ〇ᗷᗷᕮↁ Բᖇᕮᕮↁ〇Ⲙ\n\n")
            print("----------------------------------------------------------------------------------------\n")
            print("░█▀▀█ █▀▀█ █▀▀ █▀▀█ █ █ 　 ▀▀█▀▀ █  █ █▀▀ 　    ░█ █▀▀█  ▀  █  ")
            print("░█▀▀▄ █▄▄▀ █▀▀ █▄▄█ █▀▄ 　  ░█   █▀▀█ █▀▀ 　  ▄ ░█ █▄▄█ ▀█▀ █  ")
            print("░█▄▄█ ▀ ▀▀ ▀▀▀ ▀  ▀ ▀ ▀ 　  ░█   ▀  ▀ ▀▀▀ 　 ░█▄▄█ ▀  ▀ ▀▀▀ ▀▀▀")
            nextGame = input("\nPlay? Y/N ").upper()
            if nextGame == "Y":
                Gamejail()
            else:
                Start()
        elif waitbank == "2":
            os.system('cls')
            print("\nYou walk back a few steps then ram into the valt door head first\n\nFAIL\nBro thinks 9 + 10 = 21 lmao\n")
            retry = input("Retry? Y/N ").upper()
            if retry == "Y":
               GameBank() 
            else:
                Start()
        elif waitbank == "3":
            os.system('cls')
            print("You wave your hands and teleport outside \"Fire!\" then they look in shock\n\nFAIL\nWrong place definitely wrong time\n")
            retry = input("Retry? Y/N ").upper()
            if retry == "Y":
               GameBank() 
            else:
                Start()
        else:
            os.system('cls')
            print("You change your mind, walk back home, and go bankrupt\n\nFAIL\nWasn't feeling it ay?\n")
            retry = input("Retry? Y/N ").upper()
            if retry == "Y":
               GameBank() 
            else:
                Start()
    elif bankEnd == "6":
        os.system('cls')
        print("You wave your hands and teleport inside the wall\n\nFAIL\nAt least your INSIDE the bank\n")
        retry = input("Retry? Y/N ").upper()
        if retry == "Y":
           GameBank() 
        else:
            Start()
    elif bankEnd == "7":
        os.system('cls')
        print("You laydown on the ground and fall asleep\n\nFAIL\nAt least 8 hours of sleep is very important!\n")
        retry = input("Retry? Y/N ").upper()
        if retry == "Y":
           GameBank() 
        else:
            Start()
    else:
        os.system('cls')
        print("You change your mind, walk back home, and go bankrupt\n\nFAIL\nWasn't feeling it ay?\n")
        retry = input("Retry? Y/N ").upper()
        if retry == "Y":
           GameBank() 
        else:
            Start()

#This is the Jewery Store path of the game
def GameGem():
    os.system('cls')
    gemEnd = input("You grab your keys and get in your car\nYou drive up to the side of the store and get out of your car\n1>Ram\n2>Drill\n3>Bomb\n4>Transformation\n5>Shrink\n6>Magic\n>>")
    if gemEnd == "1":
        os.system('cls')
        print("You get back in your car and ram into the side of the store. Your car catches on fire\n\nFAIL\nYou really thought a normal car could break the wall?\n")
        retry = input("Retry? Y/N ").upper()
        if retry == "Y":
           GameGem() 
        else:
            Start()
    elif gemEnd == "2":
        os.system('cls')
        print("You take a drill from your car and place it on the ground next you start it and dgi into the ground. You come back up from the other side and see the huge gem, you try to grab it but police come into the room \"FREEZE\" \"DONT MOVE\"\n\nEnding:\nℂ𝕆ℕ𝕋ℝ𝔸𝔹𝔸ℕ𝔻 𝔽ℝ𝔼𝔼𝔻𝕆𝕄\n")
        print("----------------------------------------------------------------------------------------\n")
        print("░█▀▀█ █▀▀█ █▀▀ █▀▀█ █ █ 　 ▀▀█▀▀ █  █ █▀▀ 　    ░█ █▀▀█  ▀  █  ")
        print("░█▀▀▄ █▄▄▀ █▀▀ █▄▄█ █▀▄ 　  ░█   █▀▀█ █▀▀ 　  ▄ ░█ █▄▄█ ▀█▀ █  ")
        print("░█▄▄█ ▀ ▀▀ ▀▀▀ ▀  ▀ ▀ ▀ 　  ░█   ▀  ▀ ▀▀▀ 　 ░█▄▄█ ▀  ▀ ▀▀▀ ▀▀▀")
        nextGame = input("\nPlay? Y/N ").upper()
        if nextGame == "Y":
            Gamejail()
        else:
            Start()
    elif gemEnd == "3":
        os.system('cls')
        print("You place bombs on the side of he wall but as you try to but a spherical bomb on the pile it rolls off and detonates all the bombs\n\nFAIL\nYeah spherical objects kinda do this thing called roll\n")
        retry = input("Retry? Y/N ").upper()
        if retry == "Y":
           GameGem() 
        else:
            Start()
    elif gemEnd == "4":
        os.system('cls')
        print("You take a machine from your car and a note reads\nTransformator 3000: Just push the button and it will turn you into anything you think off!\nYou push the button and turn into water\n\nFAIL\nReally? out of everything you could have chosen, you chose water!?\n")
        retry = input("Retry? Y/N ").upper()
        if retry == "Y":
           GameGem() 
        else:
            Start()
    elif gemEnd == "5":
        os.system('cls')
        print("You take a machine from your car and a note reads\nShrinkinator 4000: Shoot it at your self and you'll become as small as you want!\nYou take the ray shoot yourself with it and become as small as an ant. You try to walk forward but a worm comes out the ground and attacks you\n\nFAIL\nlooks like someone forgot their not the only animal\n")
        retry = input("Retry? Y/N ").upper()
        if retry == "Y":
           GameGem() 
        else:
            Start()
    elif gemEnd == "6":
        os.system('cls')
        print("You wave your hands and teleport into the sky then fall down and break both of your legs\n\nFAIL\nYou should have brought your water bucket\n")
        retry = input("Retry? Y/N ").upper()
        if retry == "Y":
           GameGem() 
        else:
            Start()
    else:
        os.system('cls')
        print("You change your mind, walk back home, and go bankrupt\n\nFAIL\nWasn't feeling it ay?\n")
        retry = input("Retry? Y/N ").upper()
        if retry == "Y":
           GameGem() 
        else:
            Start()

#This is the secon part to the game AKA jail
def Gamejail():
    os.system('cls')
    jailEnd = input("Your sitting in your cell when a bag flies out the window and hit you in the head. your confused but you open it anyways and search inside\n1>Disguise\n2>Energy Drink\n3>Files\n4>File\n5>Rpg\n6>Plungers\n7>Phasetron\n8>Pickaxe\n>>")
    if jailEnd == "1":
        jailpathBag()
    elif jailEnd == "2":
       os.system('cls')
       print("You take out a drink and chug it down, time seems like it just stopped and you easily get out of your cell and walk out the front door. You try to take a step but you get a heart attack\n\nFAIL\nMaybe 27638 grams of pure caffeine isn't the best to drink\n")
       retry = input("Retry? Y/N ").upper()
       if retry == "Y":
          Gamejail() 
       else:
           Start()
    elif jailEnd == "3":
        os.system('cls')
        print("You take out some paperwork and look at it\n\nFAIL\nHope you like reading\n")
        retry = input("Retry? Y/N ").upper()
        if retry == "Y":
           Gamejail() 
        else:
            Start()
    elif jailEnd == "4":
        jailpathFile()
    elif jailEnd == "5":
        os.system('cls')
        print("You take out an RPG then with a determined face you point it forward and fire\n\nFAIL\nYeah there's a wall there… and your right next to it\n")
        retry = input("Retry? Y/N ").upper()
        if retry == "Y":
           Gamejail() 
        else:
            Start()
    elif jailEnd == "6":
        os.system('cls')
        print("You take out some plungers and crawl out the window you try to use the plungers to scale the wall but they dont support you and you fall\n\nFAIL\n\"For a guy in a suit, you're pretty stupid\"\n")
        retry = input("Retry? Y/N ").upper()
        if retry == "Y":
           Gamejail() 
        else:
            Start()
    elif jailEnd == "7":
        os.system('cls')
        print("You take out a machine and it reads\nPhasetron 1000: just pull the lever and you can go trough walls!\nYou pull the lever and phase through the cell ground, then the earth's ground, and now on the way to earth's core\n\nFAIL\nI wonder if there's some dinosaurs down there…\n")
        retry = input("Retry? Y/N ").upper()
        if retry == "Y":
           Gamejail() 
        else:
            Start()
    elif jailEnd == "8":
        jailpathPick()
    else:
        os.system('cls')
        print("You change your mind and take your hand out of the bag and sit back down\n\nFAIL\nBeing in prison is more fun?\n")
        retry = input("Retry? Y/N ").upper()
        if retry == "Y":
           Gamejail() 
        else:
            Start()

#This is the Jail/File path of the game
def jailpathFile():
    os.system('cls')
    File1 = input("You file the door and knock out the guard then run into a storage closet\n1>Box\n2>Weapon\n>>")
    if File1 == "1":
        os.system('cls')
        File2 = input("You grab the box and climb into the vents\n1>Left\n2>Right\n3>Middle\n>>")
        if File2 == "1":
            os.system('cls')
            print("You crawl trough the left side then fall right though the floor and into the middle of a meeting\n\nFAIL\nANGER! Your not supposed to be here!\n")
            retry = input("Retry? Y/N ").upper()
            if retry == "Y":
               jailpathFile() 
            else:
                Start()
        elif File2 == "2":
            os.system('cls')
            File3 = input("You crawl trough the right side then make it to the roof you look over the edge then at a crate behind you\n1>Parachute\n2>Jetpack\n3>Zipline\n4>Water Bucket\n>>")
            if File3 == "1":
                os.system('cls')
                print("You grab the parachute then jump of the edge but as you try to open the parachute a lunchbox, some pencils, and a notebook falls out\n\nFAIL\nHey! My lunch was in there!\n")
                retry = input("Retry? Y/N ").upper()
                if retry == "Y":
                   jailpathFile() 
                else:
                    Start()
            elif File3 == "2":
                os.system('cls')
                print("You grab the jetpack at use it. You start to fly out but it malfunctions and you fly right back into your cell\n\nFAIL\nOh hey! Welcome back!\n")
                retry = input("Retry? Y/N ").upper()
                if retry == "Y":
                   jailpathFile() 
                else:
                    Start()
            elif File3 == "3":
                print("You shoot the zipline out and it hits the floor. You try to slide down but your hands start to burn you hit the floor and you still alive!\n\nENDING:\nYou get run over by a car\n\nFAIL\nRight there! You were so close!\n")
                retry = input("Retry? Y/N ").upper()
                if retry == "Y":
                   jailpathFile() 
                else:
                    Start()
            elif File3 == "4":
                print("You grab the bucket and fall of the building but right before you hit the floor you splash the water under you and survive\n\nNow that's some minecraft for you!\nENDING: \n╔═╗────╔═╦═╗──────╔╦═╦╗\n║╬╠╦╦═╗║╦╣═╬═╦═╗╔═╬╣═╣╚╗\n║╔╣╔╣╬║║╩╬═║═╣╬╚╣╬║╠═║╔╣\n╚╝╚╝╚═╝╚═╩═╩═╩══╣╔╩╩═╩═╝\n────────────────╚╝\n\n")
                print("----------------------------------------------------------------------------------------\n")
                print("▀█▀ █▀▀▄ █▀▀  ▀  █   ▀▀█▀▀ █▀▀█ █▀▀█ ▀▀█▀▀ █▀▀ 　 ▀▀█▀▀ █  █ █▀▀ 　 ░█▀▀█ █▀▀█ █▀▀ █▀▀ ")
                print("░█  █  █ █▀▀ ▀█▀ █     █   █▄▄▀ █▄▄█   █   █▀▀ 　  ░█   █▀▀█ █▀▀ 　 ░█▀▀▄ █▄▄█ ▀▀█ █▀▀")
                print("▄█▄ ▀  ▀ ▀   ▀▀▀ ▀▀▀   ▀   ▀ ▀▀ ▀  ▀   ▀   ▀▀▀ 　  ░█   ▀  ▀ ▀▀▀ 　 ░█▄▄█ ▀  ▀ ▀▀▀ ▀▀▀")
                nextGame = input("\nPlay? Y/N ").upper()
                if nextGame == "Y":
                    GameITBstart()
                else:
                    Start()
        elif File2 == "3":
            os.system('cls')
            File4 = input("You crawl trough the right side then make it to the lobby\n1>Fight\n2>Sneek\n>>")
            if File4 == "1":
                os.system('cls')
                print("You run at the people with your fists flying and get shot\n\nFAIL\n\"never bring a fist to a gunfight with a lot of guns\"\n")
                retry = input("Retry? Y/N ").upper()
                if retry == "Y":
                   jailpathFile() 
                else:
                    Start()
            elif File4 == "2":
                os.system('cls')
                print("You crouch down and walk right though the crowd then make it outside. You get into a car and drive away\n\nsneak increased to 100\nENDING:\n🆂🅽🅴🅴🅺 𝟙𝟘𝟘\n")
                print("----------------------------------------------------------------------------------------\n")
                print("▀█▀ █▀▀▄ █▀▀  ▀  █   ▀▀█▀▀ █▀▀█ █▀▀█ ▀▀█▀▀ █▀▀ 　 ▀▀█▀▀ █  █ █▀▀ 　 ░█▀▀█ █▀▀█ █▀▀ █▀▀ ")
                print("░█  █  █ █▀▀ ▀█▀ █     █   █▄▄▀ █▄▄█   █   █▀▀ 　  ░█   █▀▀█ █▀▀ 　 ░█▀▀▄ █▄▄█ ▀▀█ █▀▀")
                print("▄█▄ ▀  ▀ ▀   ▀▀▀ ▀▀▀   ▀   ▀ ▀▀ ▀  ▀   ▀   ▀▀▀ 　  ░█   ▀  ▀ ▀▀▀ 　 ░█▄▄█ ▀  ▀ ▀▀▀ ▀▀▀")
                nextGame = input("\nPlay? Y/N ").upper()
                if nextGame == "Y":
                    GameITBstart()
                else:
                    Start()
            else:
                print("You stay there then eventually get arrested again\n\nFAIL\nBack for more?\n")
                retry = input("Retry? Y/N ").upper()
                if retry == "Y":
                   jailpathFile() 
                else:
                    Start()
    elif File1 == "2":
        os.system('cls')
        print("You grab a shovel and run out to 2 guys who have guns\n\nFAIL\n \"never bring a knife to a gunfight\" or a shovel in this case\n")
        retry = input("Retry? Y/N ").upper()
        if retry == "Y":
            jailpathFile() 
        else:
            Start()
    else:
        print("You stay there then eventually get arrested again\n\nFAIL\nBack for more?\n")
        retry = input("Retry? Y/N ").upper()
        if retry == "Y":
            jailpathFile() 
        else:
            Start()

#This is the Jail/Pickaxe path of the game
def jailpathPick():
    os.system('cls')
    Pick1 = input("You garb a pick out of the bag and mine down you then fall down right on top of someone and see a cafeteria\n1>Run\n2>Distraction\n3>Sneak\n4>Bending\n5>Stink Bomb\n>>")
    if Pick1 == "1":
        os.system('cls')
        Runpick = input("You sprint out the door so fast no one sees you now your outside and need to walk down the stairs\n1>Walk\n2>Run\n3>Fall\n>>")
        if Runpick == "1":
            os.system('cls')
            print("You walk down the stairs\n\n3 hours later\nENDING: \n█─▄▄▄▄█─█─█─▄▄─█─▄▄▄▄█─▄─▄─█▄─▄███▄─█─▄███▄─▄▄─█─▄▄▄▄█─▄▄▄─██▀▄─██▄─▄▄─█▄─▄▄─█\n█─██▄─█─▄─█─██─█▄▄▄▄─███─████─██▀██▄─▄█████─▄█▀█▄▄▄▄─█─███▀██─▀─███─▄▄▄██─▄█▀█\n▀▄▄▄▄▄▀▄▀▄▀▄▄▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀▄▄▄▄▄▀▀▄▄▄▀▀▀▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▀▀▀▄▄▄▄▄▀\n")
            print("----------------------------------------------------------------------------------------\n")
            print("▀█▀ █▀▀▄ █▀▀  ▀  █   ▀▀█▀▀ █▀▀█ █▀▀█ ▀▀█▀▀ █▀▀ 　 ▀▀█▀▀ █  █ █▀▀ 　 ░█▀▀█ █▀▀█ █▀▀ █▀▀ ")
            print("░█  █  █ █▀▀ ▀█▀ █     █   █▄▄▀ █▄▄█   █   █▀▀ 　  ░█   █▀▀█ █▀▀ 　 ░█▀▀▄ █▄▄█ ▀▀█ █▀▀")
            print("▄█▄ ▀  ▀ ▀   ▀▀▀ ▀▀▀   ▀   ▀ ▀▀ ▀  ▀   ▀   ▀▀▀ 　  ░█   ▀  ▀ ▀▀▀ 　 ░█▄▄█ ▀  ▀ ▀▀▀ ▀▀▀")
            nextGame = input("\nPlay? Y/N ").upper()
            if nextGame == "Y":
                GameITBstart()
            else:
                Start()
        elif Runpick == "2":
            print("You start to run down the stairs but half way though you pass out\nFAIL\n\nPE didn't teach you anything…")
            retry = input("Retry? Y/N ").upper()
            if retry == "Y":
                jailpathPick() 
            else:
                Start()
        elif Runpick == "3":
            print("You go to the rail and jump off the side then splat on the floor\nFAIL\n\nwhere's your cloud in a bottle?")
            retry = input("Retry? Y/N ").upper()
            if retry == "Y":
                jailpathPick() 
            else:
                Start()
        else:
            os.system('cls')
            print("You stay there then eventually get arrested again\n\nFAIL\nBack for more?\n")
            retry = input("Retry? Y/N ").upper()
            if retry == "Y":
                jailpathPick() 
            else:
                Start()
    elif Pick1 == "2":
        os.system('cls')
        print("\nYou go into the middle of the crowd and start dancing then everyone else starts dancing... and you keep on danceing\n\nFAIL\nOk… that's good… you can stop dancing now… THATS ENOUGH DANCING\n")
        retry = input("Retry? Y/N ").upper()
        if retry == "Y":
            jailpathPick() 
        else:
            Start()
        jailpathPick()
    elif Pick1 == "3":
        os.system('cls')
        print("you crouch down and try to sneek across but someone spots you\n\nFAIL\nshouldn't have put all your skill points in strength\n")
        retry = input("Retry? Y/N ").upper()
        if retry == "Y":
            jailpathPick() 
        else:
            Start()
    elif Pick1 == "4":
        os.system('cls')
        pickbending = input("You wave your hands and the whole cafeteria falls down to the floor then you walk outside\n1>Bending\n2>Magic\n>>")
        if pickbending == "1":
            os.system('cls')
            print("You jump up and wave your hands then a piler of earth smashes into your legs\n\nFAIL\nGood Idea Bad Execution\n")
            retry = input("Retry? Y/N ").upper()
            if retry == "Y":
                jailpathPick() 
            else:
                Start()
        elif pickbending == "2":
            os.system('cls')
            print("You wave your hands and teleport into a cell\n\nFAIL\nRight where you belong\n")
            retry = input("Retry? Y/N ").upper()
            if retry == "Y":
                jailpathPick() 
            else:
                Start()
        else:
            print("You stay there then eventually get arrested again\n\nFAIL\nBack for more?\n")
            retry = input("Retry? Y/N ").upper()
            if retry == "Y":
                jailpathPick() 
            else:
                Start()
    elif Pick1 == "5":
        os.system('cls')
        print("You throw out a stink bomb and the whole room fills with gas makeing everyone pass out... including you\n\nFAIL\nBro did you really just forget your gas mask? smh\n")
        retry = input("Retry? Y/N ").upper()
        if retry == "Y":
            jailpathPick() 
        else:
            Start()
    else:
        print("You stay there then eventually get arrested again\n\nFAIL\nBack for more?\n")
        retry = input("Retry? Y/N ").upper()
        if retry == "Y":
            jailpathPick() 
        else:
            Start()

#This is the Jail/Disguise path of the game
def jailpathBag():
    os.system('cls')
    Bag1 = input("You pull out a bag then hide inside it after awhile you get taken to a shoot where you fall down and end up in a room full fo bags then you start to search the other bags\n1>Bomb\n2>Knife\n3>Log\n4>Fire\n5>Old Machine\n6>Magic\n>>")
    if Bag1 == "1":
        os.system('cls')
        print("You take out a bomb then take out some matches, You light the bomb then throw it at the wall and it blows everything up\n\nFAIL\nyou're in a small room and you chose to use a bomb?\n")
        retry = input("Retry? Y/N ").upper()
        if retry == "Y":
            jailpathBag() 
        else:
            Start()
    elif Bag1 == "2":
        os.system('cls')
        print("You take out a knife then start to chip at the wall. You keep on chipping... and chipping... and\n\nFAIL\nLegend says to this day Steve is still chipping\n")
        retry = input("Retry? Y/N ").upper()
        if retry == "Y":
            jailpathBag() 
        else:
            Start()
    elif Bag1 == "3":
        os.system('cls')
        print("You take out a log and then try to ram it into the wall but the shock of the hit knocks you out\n\nFAIL\nKinetic energy is just the best isn't it?\n")
        retry = input("Retry? Y/N ").upper()
        if retry == "Y":
            jailpathBag() 
        else:
            Start()
    elif Bag1 == "4":
        os.system('cls')
        print("You take out a lighter then light one of the bags on fire. Then the whole room catches on fire\n\nFAIL\nEverything in there is flammable… including you\n")
        retry = input("Retry? Y/N ").upper()
        if retry == "Y":
            jailpathBag() 
        else:
            Start()
    elif Bag1 == "5":
        os.system('cls')
        print("You take out and old handheld machine then press the button... nothing happens... you press again and still nothing happens... then you smack the machine and it fires a lazer at the wall and makes a hole in it. You walk out and continue to walk forward\n\nSo that's what that does\nENDING:\nᕮﬡɢ⫯ﬡ∈∈ᖇ ⫯⟆ ᕮﬡᕍ⫯ᖺ∈ᖇ∈\n")
        print("----------------------------------------------------------------------------------------\n")
        print("▀█▀ █▀▀▄ █▀▀  ▀  █   ▀▀█▀▀ █▀▀█ █▀▀█ ▀▀█▀▀ █▀▀ 　 ▀▀█▀▀ █  █ █▀▀ 　 ░█▀▀█ █▀▀█ █▀▀ █▀▀ ")
        print("░█  █  █ █▀▀ ▀█▀ █     █   █▄▄▀ █▄▄█   █   █▀▀ 　  ░█   █▀▀█ █▀▀ 　 ░█▀▀▄ █▄▄█ ▀▀█ █▀▀")
        print("▄█▄ ▀  ▀ ▀   ▀▀▀ ▀▀▀   ▀   ▀ ▀▀ ▀  ▀   ▀   ▀▀▀ 　  ░█   ▀  ▀ ▀▀▀ 　 ░█▄▄█ ▀  ▀ ▀▀▀ ▀▀▀")
        nextGame = input("\nPlay? Y/N ").upper()
        if nextGame == "Y":
            GameITBstart()
        else:
            Start()
    elif Bag1 == "6":
        os.system('cls')
        print("You wave your hands then teleport in the middle of the ocean\n\nFAIL\nHope you know how to swim\n")
        retry = input("Retry? Y/N ").upper()
        if retry == "Y":
            jailpathBag() 
        else:
            Start()
    else:
        os.system('cls')
        print("You stay there then eventually get arrested again\n\nFAIL\nBack for more?\n")
        retry = input("Retry? Y/N ").upper()
        if retry == "Y":
            jailpathBag() 
        else:
            Start()

#The grand finally of the game
def GameITBstart():
    os.system('cls')
    print("You sudenly wake up in an interrogation room and hear a voice \"Steve stickman... you have been a bit of trouble lately and have a pretty big criminal record... but you seem to have abilitys that no one else could even fathom... so were here to hire you... to get rid of your criminal record and help us greatly... so what do you say? You in?\"")
    bigchoice = input("Y/N ").upper()
    if bigchoice == "Y":
        GameITB()
    else:
        os.system('cls')
        print("\"Oh well... It was worth a shot...\" You sudenly pass out\n")
        print("----------------------------------------------------------------------------------------\n")
        print("▒█▀▀▀ █░░ █▀▀ █▀▀ 　 ▀▀█▀▀ █░░█ █▀▀ 　 ▒█▀▀▀ █▀▀█ █▀▀ ░▀░ █░░ ░▀░ ▀▀█▀▀ █░░█ \n▒█▀▀▀ █░░ █▀▀ █▀▀ 　 ░▒█░░ █▀▀█ █▀▀ 　 ▒█▀▀▀ █▄▄█ █░░ ▀█▀ █░░ ▀█▀ ░░█░░ █▄▄█ \n▒█░░░ ▀▀▀ ▀▀▀ ▀▀▀ 　 ░▒█░░ ▀░░▀ ▀▀▀ 　 ▒█░░░ ▀░░▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ░░▀░░ ▄▄▄█")
        nextGame = input("\nPlay? Y/N ").upper()
        if nextGame == "Y":
            GameFTF()
        else:
            Start()

def GameITB():
    os.system('cls')
    print("\"Great! we'll be sending you in shortly...\" You blackout then wake up in a battle van \"Welcome Steve... To The Base...\" you look out the door and see a huge base with extremly high security \"Now Steve... we need you to go into that base and take out the leader of this... clan of some sorts... now just to get you in...\"")
    GameITBstartchoice = input("1>Slingshot\n2>Shoot In\n3>Walki Talki\n4>Sneak in\n>>")
    if GameITBstartchoice == "1":
        os.system('cls')
        print("You get into the sling shot and you launch right into the middle of the cafeteria that has a whole bunch of people\n\nFAIL\nHey, at least your inside\n")
        retry = input("Retry? Y/N ").upper()
        if retry == "Y":
            GameITB()
        else:
            Start()
    elif GameITBstartchoice == "2":
        os.system('cls')
        SIstartchoice = input("You get into a cannon \"Ready?\" You nod your head and fly off \n1>Wall\n2>Window\n3>Roof\n>>")
        if SIstartchoice == "1":
            os.system('cls')
            print("You fly out and straight into the wall\n\nFAIL\nYour a person... not a cannonball...\n")
            retry = input("Retry? Y/N ").upper()
            if retry == "Y":
                GameITB()
            else:
                Start()
        elif SIstartchoice == "2":
            SIWindow()
        elif SIstartchoice == "3":
            SIRoof()
    elif GameITBstartchoice == "3":
        WiTiStart()
    elif GameITBstartchoice == "4":
        SnIn()
    else:
        os.system('cls')
        print("\"SIR! THE BREAKS ARNT WORKING\" \"WHAT!?\" All three of you crash into the wall\n\nFAIL\nShould have picked something sooner\n")
        retry = input("Retry? Y/N ").upper()
        if retry == "Y":
            GameITB()
        else:
            Start()

def SnIn():
    os.system('cls')
    SnIn1 = input("You get droven to the back and you enter the garage and see a strong guard blocing the exit\n1>Boogie\n2>Distraction\n3>Persue\n>>")
    if SnIn1 == "1":
        os.system('cls')
        print("You start to default dance Then you get crushed by the ceiling\n\nFAIL\nDont. You. Dare.\n")
        retry = input("Retry? Y/N ").upper()
        if retry == "Y":
            SnIn()
        else:
            Start()
    elif SnIn1 == "2":
        os.system('cls')
        print("You grab their attention then point somewhere else but they run at you\n\nFAIL\nBut my plan was fool proof!\n")
        retry = input("Retry? Y/N ").upper()
        if retry == "Y":
            SnIn()
        else:
            Start()
    elif SnIn1 == "3":
        os.system('cls')
        SnIn2 = input("You walk up to him and look him dead in the eyes\n1>Boogie\n2>Rock Paper Scissors\n3>Fight\n4>Evade\n>>")
        if SnIn2 == "1":
            os.system('cls')
            print("You start to default dance then you get punched\n\nFAIL\nSTOP.\n")
            retry = input("Retry? Y/N ").upper()
            if retry == "Y":
                SnIn()
            else:
                Start()
        elif SnIn2 == "2":
            os.system('cls')
            print("You both play Rock Paper Scissors and you play rock and he pulls out a gun then shoots you\n\nFAIL\nRock, Paper, Scissors, Shoot!\n")
            retry = input("Retry? Y/N ").upper()
            if retry == "Y":
                SnIn()
            else:
                Start()
        elif SnIn2 == "3":
            os.system('cls')
            print("You try to punch him but he punches back harder\n\nFAIL\n\"WEAK\" -Minos Prime\n")
            retry = input("Retry? Y/N ").upper()
            if retry == "Y":
                SnIn()
            else:
                Start()
        elif SnIn2 == "4":
            os.system('cls')
            SnIn3 = input("You Evade right under his legs and go inside to look at the map then you see the vault and get intrigued\n1>Run\n2>Sneak\n3>Magic\n>>")
            if SnIn3 == "1":
                os.system('cls')
                print("You run then try to turn a corner and slip\n\nFAIL\nL+Ratio\n")
                retry = input("Retry? Y/N ").upper()
                if retry == "Y":
                    SnIn()
                else:
                    Start()
            elif SnIn3 == "2":
                os.system('cls')
                print("You try to sneak but someone catches you before you can\n\nFAIL\nHey! Your not in here for right now!\n")
                retry = input("Retry? Y/N ").upper()
                if retry == "Y":
                    SnIn()
                else:
                    Start()
            elif SnIn3 == "3":
                os.system('cls')
                SnIn4 = input("You teleport to the ocean the a valcano then a lab then to a flesh room then you telport into the vault then you see a huge gem\n1>Backpack\n2>Shrink\n3>Grab\n>>")
                if SnIn4 == "1":
                    os.system('cls')
                    print("You try to put the gem in a backpack but it breaks right through\n\nFAIL\nI its more than 15 pounds\n")
                    retry = input("Retry? Y/N ").upper()
                    if retry == "Y":
                        SnIn()
                    else:
                        Start()
                elif SnIn4 == "2":
                    os.system('cls')
                    SnIn5 = input("You take out a small machine\nJust put it on any object and it will shrink it down to be able to fit in your pocket!\nYou but the machine in the crystal and it shrinks down so your able to grab it you try to walk out but you hear people around the corner\n1>Tackle\n2>Rush\n3>Sneak\n4>Coin\n5>Gem\n>>")
                    if SnIn5 == "1":
                        os.system('cls')
                        print("\n\nFAIL\n\n")
                        retry = input("Retry? Y/N ").upper()
                        if retry == "Y":
                            SnIn()
                        else:
                            Start()
                    elif SnIn5 == "2":
                        os.system('cls')
                        retry = input("Retry? Y/N ").upper()
                        if retry == "Y":
                            SnIn()
                        else:
                            Start()
                    elif SnIn5 == "3":
                        os.system('cls')
                        retry = input("Retry? Y/N ").upper()
                        if retry == "Y":
                            SnIn()
                        else:
                            Start()
                    elif SnIn5 == "4":
                        os.system('cls')
                        retry = input("Retry? Y/N ").upper()
                        if retry == "Y":
                            SnIn()
                        else:
                            Start()
                    elif SnIn5 == "5":
                        os.system('cls')
                        retry = input("Retry? Y/N ").upper()
                        if retry == "Y":
                            SnIn()
                        else:
                            Start()
                    else:
                        os.system('cls')
                        retry = input("Retry? Y/N ").upper()
                        if retry == "Y":
                            SnIn()
                        else:
                            Start()
                elif SnIn4 == "3":
                    os.system('cls')
                    print("You try to grab it but it crushes you as soon as you take it off the pedestal\n\nFAIL\nYou need to go to the gym boi\n")
                    retry = input("Retry? Y/N ").upper()
                    if retry == "Y":
                        SnIn()
                    else:
                        Start()
                else:
                    os.system('cls')
                    print("You sit there and someone catches you\n\nFAIL\nI sure do love just stareing a pretty things\n")
                    retry = input("Retry? Y/N ").upper()
                    if retry == "Y":
                        SnIn()
                    else:
                        Start()
            else:
                os.system('cls')
                print("You sit there and someone catches you\n\nFAIL\nFor the love of god do something\n")
                retry = input("Retry? Y/N ").upper()
                if retry == "Y":
                    SnIn()
                else:
                    Start()
        else:
            os.system('cls')
            print("You stand there then the guard punches you\n\nFAIL\n\"DO SOMETHING! WHY DO YOU DO NOTHING!?\"\n")
            retry = input("Retry? Y/N ").upper()
            if retry == "Y":
                SnIn()
            else:
                Start()
    else:
        os.system('cls')
        print("You sit there and do nothing\n\nFAIL\nHello? is anyone there?\n")
        retry = input("Retry? Y/N ").upper()
        if retry == "Y":
            SnIn()
        else:
            Start()

def WiTiStart():
    os.system('cls')
    WiTi1 = input("They had you a walki talki \"Ok so this will be your helper Jeff\" You look at the walki talki then they drop you off on the roof \"Goodluck!\" They fly away and you here the walki talki go off \"Sup. Its me Jeff. For me to help you you kinda need to get inside\"\n1>Acid\n2>Fist\n3>Hammer\n4>Leg\n>>")
    if WiTi1 == "1":
        os.system('cls')
        print("You try to use the acid but it pours onto your foot\n\nFAIL\nI think you missed a spot\n")
        retry = input("Retry? Y/N ").upper()
        if retry == "Y":
            WiTiStart()
        else:
            Start()
    elif WiTi1 == "2":
        os.system('cls')
        print("You punch the roof and your hand starts to throb\n\nFAIL\nYou aint THAT strong my guy\n")
        retry = input("Retry? Y/N ").upper()
        if retry == "Y":
            WiTiStart()
        else:
            Start()
    elif WiTi1 == "3":
        os.system('cls')
        print("You hammer the floor and it bounes back at your face\n\nFAIL\nI dont think bor wants to build a shed\n")
        retry = input("Retry? Y/N ").upper()
        if retry == "Y":
            WiTiStart()
        else:
            Start()
    elif WiTi1 == "4":
        os.system('cls')
        WiTi2 = input("You kick a hidden hatch and it opens then you jump down to see a meeting that you have to get acroos\n1>Glue\n2>Tape\n3>Slime\n>>")
        if WiTi2 == "1":
            os.system('cls')
            print("You put dlue on you hands and try to climb the wall but you stick to it and you can get off\n\nFAIL\nSo thats where my super glue went...\n")
            retry = input("Retry? Y/N ").upper()
            if retry == "Y":
                WiTiStart()
            else:
                Start()
        elif WiTi2 == "2":
            os.system('cls')
            print("You wrap tape around your hands and try to climb the wall but you slide right off and scrape the wall\n\nFAIL\nHey! They just painted that!\n")
            retry = input("Retry? Y/N ").upper()
            if retry == "Y":
                WiTiStart()
            else:
                Start()
        elif WiTi2 == "3":
            os.system('cls')
            WiTi3 = input("You take put the slime on your hands and climb the wall then the ceiling and make it to the other side \"Great! Now we just gotta get to the other side of this hall without alerting the clan members\"\n1>Rush\n2>Vents\n3>Distration\n4>Magic\n>>")
            if WiTi3 == "1":
                os.system('cls')
                print("You rush staright into the members but they easily take you down\n\nFAIL\nSo looks like they went to the gym")
                retry = input("Retry? Y/N ").upper()
                if retry == "Y":
                    WiTiStart()
                else:
                    Start()
            elif WiTi3 == "2":
                WiTiVents()
            elif WiTi3 == "3":
                WiTiDistract()
            elif WiTi3 == "4":
                os.system('cls')
                print("You wave your arms then teleport inside a huge red airship\n\nFAIL\nWhoops wrong game")
                retry = input("Retry? Y/N ").upper()
                if retry == "Y":
                    WiTiStart()
                else:
                    Start()
            else:
                os.system('cls')
                print("You sit there and the member find you\n\nFAIL\nYou gotta move once a awhile")
                retry = input("Retry? Y/N ").upper()
                if retry == "Y":
                    WiTiStart()
                else:
                    Start()
            retry = input("Retry? Y/N ").upper()
            if retry == "Y":
                GameITB()
            else:
                Start()
        else:
           os.system('cls')
           print("You sit there and they finish their meeting dan spot you\n\nFAIL\nYeah meetings dont last forever...")
           retry = input("Retry? Y/N ").upper()
           if retry == "Y":
                WiTiStart()
           else:
                Start()
    else:
        os.system('cls')
        print("You sit there and do nothing \"Um... You gonna do something?\"\n\nFAIL\nEven Jeff wants you to do something bruh\n")
        retry = input("Retry? Y/N ").upper()
        if retry == "Y":
            WiTiStart()
        else:
            Start()

def WiTiDistract():
    os.system('cls')
    WiTiD1 = input("\"Ok... I have an Idea! wear you gas mask and go make a distraction or something\" You put on a gas mask the dsah out and start dancing. The members start to dance as well but a gas bomb was dropped into the room and it goes off then both the members pass out \"Nice job! Alright lets continue!\"\n1>Sprint\n2>Sneak\n>>")
    if WiTiD1 == "1":
        os.system('cls')
        print("You try to run for it but end up slipping on the floor halfway though\n\nFAIL\nOn your behalf there was no  wet floor sign")
        retry = input("Retry? Y/N ").upper()
        if retry == "Y":
            WiTiDistract()
        else:
            Start() 
    elif WiTiD1 == "2":
        os.system('cls')
        WiTiD2 = input("You sneak around to the leader's room and see the door\n1>Missle\n2>Lazer\n3>Jeff\n4>Drill\n>>")
        if WiTiD2 == "1":
            os.system('cls')
            WiTiD3 = input("\"Alright! Missle Incoming!\" You duck out the way and the door explodes open then the leader jumps up from his chair\n1>Jump\n2>Throw\n3>Run\n>>")
            if WiTiD3 == "1":
                os.system('cls')
                print("You jump up and try toget the leader but you both fall out the window unprepared\n\nFAIL\nYou gotta think things through\n")
                retry = input("Retry? Y/N ").upper()
                if retry == "Y":
                    WiTiDistract()
                else:
                    Start()
            elif WiTiD3 == "2":
                os.system('cls')
                print("You grab a pebble and shoot it at the leader but he just looks at you\n\nFAIL\n\"A pebble? Out over everything you could have used you used a pebble!?\"\n")
                retry = input("Retry? Y/N ").upper()
                if retry == "Y":
                    WiTiDistract()
                else:
                    Start()
            elif WiTiD3 == "3":
                os.system('cls')
                WiTiD4 = input("You run at the leader and both of you fly out the window \"Dont worry steve! I got this!\"\n1>Bucket\n2>Jeff\n3>Bottle\n4>Slime\n>>")
                if WiTiD4 == "1":
                    os.system('cls')
                    print("You try to use the bucket but nothing happens and you both hit the floor\n\nFAIL\nThere was nothing in it...\n")
                    retry = input("Retry? Y/N ").upper()
                    if retry == "Y":
                        WiTiDistract()
                    else:
                        Start()
                elif WiTiD4 == "2":
                    os.system('cls')
                    print("\"INCOMING!\" Jeff rams into both of you and you barly snatch onto the ledge of the helcopter \"Steve! You got him! Nice! Ya know... we make a pretty good team. :)\"\n\nENDING:\n┏━━━┓┏━┓╋╋╋╋╋╋╋╋╋╋╋╋┏┓╋┏┓\n┃┏━┓┃┃╋┣┓┏━┓┏┳┳━┳┳┓╋┃┣━┫┗┓\n┗┛┏┛┃┃┏┫┗┫╋┗┫┃┃┻┫┏┛┏┫┃╋┃╋┃\n┏━┛┏┛┗┛┗━┻━━╋┓┣━┻┛╋┗━┻━┻━┛\n┃┃┗━┓╋╋╋╋╋╋╋┗━\n")
                    trueend = input("Continue? Y/N ").upper()
                    if trueend == "Y":
                        Ending()
                    else:
                        Start()
                elif WiTiD4 == "3":
                    os.system('cls')
                    print("You try to use the bottle but nothing happens and you both hit the floor\n\nFAIL\nThere was nothing in it...\n")
                    retry = input("Retry? Y/N ").upper()
                    if retry == "Y":
                        WiTiDistract()
                    else:
                        Start()
                elif WiTiD4 == "4":
                    os.system('cls')
                    print("You try to use the slime but there wasnt enough of it and you both crash to the floor\n\nFAIL\nWhere are you even gonna get enough slime?\n")
                    retry = input("Retry? Y/N ").upper()
                    if retry == "Y":
                        WiTiDistract()
                    else:
                        Start()
                else:
                    os.system('cls')
                    retry = input("Retry? Y/N ").upper()
                    if retry == "Y":
                        WiTiDistract()
                    else:
                        Start()
            else:
                os.system('cls')
                print("You just stnad there and the leaer gets awat \"Uh... Steve? I think he got away...\"\n\nFAIL\nYeah I sure do wonder why\n")
                retry = input("Retry? Y/N ").upper()
                if retry == "Y":
                    WiTiDistract()
                else:
                    Start()
        elif WiTiD2 == "2":
            os.system('cls')
            print("\"Here we go!\" A lazer fires getting the door... and you \"Its open!... Steve?\"\n\nFAIL\nYippee! Its open!... wait\n")
            retry = input("Retry? Y/N ").upper()
            if retry == "Y":
                WiTiDistract()
            else:
                Start() 
        elif WiTiD2 == "3":
            os.system('cls')
            print("\"Alright! I got this!\" You then see a red dot on the floor then hear a whistle from above \"Air strike incoming!\"\n\nFAIL\nTo be fair it will open the door\n")
            retry = input("Retry? Y/N ").upper()
            if retry == "Y":
                WiTiDistract()
            else:
                Start() 
        elif WiTiD2 == "4":
            os.system('cls')
            retry = input("Retry? Y/N ").upper()
            if retry == "Y":
                WiTiDistract()
            else:
                Start() 
        else:
            os.system('cls')
            print("\"I can see that your there... why arnt you doing anything?\"\n\nFAIL\nI have the same question\n")
            retry = input("Retry? Y/N ").upper()
            if retry == "Y":
                WiTiDistract()
            else:
                Start() 
    else:
       os.system('cls')
       print("You stand there \"Um... Hello?\"\n\nFAIL\nMOVE YOUR BLOCKIN THE ROAD\n")
       retry = input("Retry? Y/N ").upper()
       if retry == "Y":
           WiTiDistract()
       else:
           Start() 
    
def WiTiVents():
    os.system('cls')
    WiTiV1 = input("You crawl into the vents and make it to a room to see an electric wall \"I could try and get that wall dowm\"\n1>Overload Power\n2>Shutdown Power\n3>Run Through\n>>")
    if WiTiV1 == "1":
        os.system('cls')
        print("\"Alright...\" The electric wall grows bigger and bigger then it explodes\n\nFAIL\nOverload = Heat\n")
        retry = input("Retry? Y/N ").upper()
        if retry == "Y":
            WiTiVents()
        else:
            Start()
    elif WiTiV1 == "2":
        os.system('cls')
        WiTiV2 = input("\"Alright...\" The power shuts down and you make it trough the vent and out on the other side. Emergency lights start to go off as you jump down and look at the map\n1>Leader's Room\n2>Vault\n3>Prison\n>>")
        if WiTiV2 == "1":
            os.system('cls')
            WiTiV3 = input("You go into the leader's room but cant find him \"Oh! I have an idea!\"\n1>Jeff\n2>Locator\n3>Heat Seeker\n4>Search Yourself\n>>")
            if WiTiV3 == "1":
                os.system('cls')
                print("\"Sweet!\" You then hear a missle whistling... toward you\n\nFAIL\nGuess that is one way to find the leader\n")
                retry = input("Retry? Y/N ").upper()
                if retry == "Y":
                    WiTiVents()
                else:
                    Start()
            elif WiTiV3 == "2":
                os.system('cls')
                WiTiV4 = input("You pull out a machine\nDetector 400: Just flip the switch and you'll find someone in no time!\nYou flip the switch to see the leader hiding in a locker so you take him out and signal Jeff \"Sweet! You got him! ok now we just gotta bring it back...\"\n1>Jeff\n2>Run\n3>Pick Up\n>>")
                if WiTiV4 == "1":
                    os.system('cls')
                    print("\"Alright Here I go!\" You start to see a shadow of a helcopter rapidly approaching the building\n\nFAIL\nCharles?\n")
                    retry = input("Retry? Y/N ").upper()
                    if retry == "Y":
                        WiTiVents()
                    else:
                        Start()
                elif WiTiV4 == "2":
                    os.system('cls')
                    print("You try to run out but get stopped by a wall of members\n\nFAIL\nThe backway is always the way\n")
                    retry = input("Retry? Y/N ").upper()
                    if retry == "Y":
                        WiTiVents()
                    else:
                        Start()
                elif WiTiV4 == "3":
                    os.system('cls')
                    print("\"Alright, Movein down\" You see a helicopter move down and you jump in \"Yo! Steve! Nice job man! know we just need to get back to sarge...\"\n\nENDING:\n╭━━━┳━━━┳━━━┳━━━┳━╮╭━╮╭╮╭╮╭┳━━━┳━━━┳╮╭━╮\n╰╮╭╮┃╭━╮┃╭━━┫╭━╮┃┃╰╯┃┃┃┃┃┃┃┃╭━╮┃╭━╮┃┃┃╭╯\n╱┃┃┃┃╰━╯┃╰━━┫┃╱┃┃╭╮╭╮┃┃┃┃┃┃┃┃╱┃┃╰━╯┃╰╯╯\n╱┃┃┃┃╭╮╭┫╭━━┫╰━╯┃┃┃┃┃┃┃╰╯╰╯┃┃╱┃┃╭╮╭┫╭╮┃\n╭╯╰╯┃┃┃╰┫╰━━┫╭━╮┃┃┃┃┃┃╰╮╭╮╭┫╰━╯┃┃┃╰┫┃┃╰╮\n╰━━━┻╯╰━┻━━━┻╯╱╰┻╯╰╯╰╯╱╰╯╰╯╰━━━┻╯╰━┻╯╰━╯\n")
                    trueend = input("Continue? Y/N ").upper()
                    if trueend == "Y":
                        Ending()
                    else:
                        Start()
                else:
                    os.system('cls')
                    print("You just sit there then the leader knocks you out\n\nFAIL\nDid you forget he was there?\n")
                    retry = input("Retry? Y/N ").upper()
                    if retry == "Y":
                        WiTiVents()
                    else:
                        Start()
            elif WiTiV3 == "3":
                os.system('cls')
                print("You pull a machine out of your pocket\nHeat Seeker 6000: Just push the button and you can see whatever makes heat!\nYou push the button but all it shows is everything being hot\n\nFAIL\nThere goes my 600 bucks\n")
                retry = input("Retry? Y/N ").upper()
                if retry == "Y":
                    WiTiVents()
                else:
                    Start()
            elif WiTiV3 == "4":
                os.system('cls')
                print("You search yourself for awhile but then some guards find you\n\nFAIL\nSo you know how to hide but not seek?\n")
                retry = input("Retry? Y/N ").upper()
                if retry == "Y":
                    WiTiVents()
                else:
                    Start()
            else:
                os.system('cls')
                print("You just stand there \"Meh, Ima do my plan anyways\" You then hear a missle whistling... toward you\n\nFAIL\nTo be fair you didnt say jeff couldnt")
                retry = input("Retry? Y/N ").upper()
                if retry == "Y":
                    WiTiVents()
                else:
                    Start()
        elif WiTiV2 == "2":
            os.system('cls')
            print("You go to the vault but there is guards there and they take you down\n\nFAIL\nThe Vault has the leader's life in there! We cant just leave it!\n")
            retry = input("Retry? Y/N ").upper()
            if retry == "Y":
                WiTiVents()
            else:
                Start()
        elif WiTiV2 == "3":
            os.system('cls')
            print("You go to the prison and see everybody has been let lose then one of them attacks you\n\nFAIL\nNo power? No lock.\n")
            retry = input("Retry? Y/N ").upper()
            if retry == "Y":
                WiTiVents()
            else:
                Start()
        else:
            os.system('cls')
            print("You just stay there untill you get knocked out by a dude running\n\nFAIL\nJust like in the cartoons\n")
            retry = input("Retry? Y/N ").upper()
            if retry == "Y":
                WiTiVents()
            else:
                Start()
    elif WiTiV1 == "3":
        os.system('cls')
        print("You run straight into the electric wall and get electrocuted\n\nFAIL\nWhat did you think was gonna happen?\n")
        retry = input("Retry? Y/N ").upper()
        if retry == "Y":
            WiTiVents()
        else:
            Start()
    else:
       os.system('cls')
       print("You sit still \"Hello?\"\n\nFAIL\nDont leave him hangin!\n")
       retry = input("Retry? Y/N ").upper()
       if retry == "Y":
           WiTiVents()
       else:
           Start()

def SIWindow():
    os.system('cls')
    Window1 = input("You fly through the window ontop of some poeple in the armory and some other people see you. You look to your side and see some weapons\n1>Gun\n2>Sword\n3>Bat\n4>Brass Knuckles\n>>")
    if Window1 == "1":
        os.system('cls')
        print("You grab the gun and fire... but its out of ammo\n\nFAIL\nDo you think they just keep those loaded?\n")
        retry = input("Retry? Y/N ").upper()
        if retry == "Y":
            SIWindow()
        else:
            Start()
    elif Window1 == "2":
        os.system('cls')
        Window2 = input("You grab the sword and knock both of them out and continue to the leader's room where theres some guards\n1>Wait\n2>Sneak\n3>Distraction\n4>Charge\n>>")
        if Window2 == "1":
            WindowWait()
        elif Window2 == "2":
            os.system('cls')
            print("You try to sneak by but they catch you\n\nFAIL\nthis doesnt work with everybody\n")
            retry = input("Retry? Y/N ").upper()
            if retry == "Y":
                SIWindow()
            else:
                Start()
        elif Window2 == "3":
            os.system('cls')
            print("You run out and start to dance and they start danceing too but the leader walks out then runs away\n\nFAIL\nDances are very scary ok?\n")
            retry = input("Retry? Y/N ").upper()
            if retry == "Y":
                SIWindow()
            else:
                Start()
        elif Window2 == "4":
            WindowCharge()
        else:
            os.system('cls')
            print("You walk out and they catch you\n\nFAIL\nFinally you did some- wait... did you just fail?\n")
            retry = input("Retry? Y/N ").upper()
            if retry == "Y":
                SIWindow()
            else:
                Start()
    elif Window1 == "3":
        os.system('cls')
        print("You grab the bat and charge in but they shoot you\n\nFAIL\nIts a WOODEN bat verses METAL guns\n")
        retry = input("Retry? Y/N ").upper()
        if retry == "Y":
            SIWindow()
        else:
            Start()
    elif Window1 == "4":
        os.system('cls')
        print("You grab and wear the knuckles but as you turn around they are already behind you\n\nFAIL\nThose things are always tighter than you think\n")
        retry = input("Retry? Y/N ").upper()
        if retry == "Y":
            SIWindow()
        else:
            Start()
    else:
        os.system('cls')
        print("You sit there and the people kill you\n\nFAIL\nCome on... do something...\n")
        retry = input("Retry? Y/N ").upper()
        if retry == "Y":
            SIWindow()
        else:
            Start()

def WindowWait():
    os.system('cls')
    WiWa1 = input("You wait by the door then the guards go on a shift switch so you take your chance to get inside and see the leader counting his cash\n1>Lunge\n2>Sneak\n3>Talk\n>>")
    if WiWa1 == "1":
        os.system('cls')
        print("You try to lunge for him but he moves out the way and you fly out the window\n\nFAIL\nYeah he can kinda do this thing called move\n")
        retry = input("Retry? Y/N ").upper()
        if retry == "Y":
            WindowWait()
        else:
            Start()
    elif WiWa1 == "2":
        os.system('cls')
        WiWa2 = input("You sneak behind the leader and reach into your back pocket\n1>Rope\n2>Knife\n3>Cloth\n>>")
        if WiWa2 == "1":
             os.system('cls')
             ("You grab the rope out of your pocket and ry to tie up the leader but its to small\n\nFAIL\nIt was a rope big enough to fit in your pocket...\n")
             retry = input("Retry? Y/N ").upper()
             if retry == "Y":
                 WindowWait()
             else:
                 Start()
        elif WiWa2 == "2":
             os.system('cls')
             print("You ake a knife and stab him but the gaurds walk in on you !DEAD BODY REPORTED!\n\nFAIL\nSteve Sus\n")
             retry = input("Retry? Y/N ").upper()
             if retry == "Y":
                 WindowWait()
             else:
                 Start()
        elif WiWa2 == "3":
             os.system('cls')
             print("You grab the cloth out of your pocket and put it on the leaders mouth knocking him out. Then you grab him and walk outside \"Steve! Your back! And you have the leader I see... Good job on that, we'll take him from here\" They grab the leader and throw him in the van \"Welp now your no longer wanted. Come to think of it you might acually make a great spy...\"\nENDING:\n╭━━━┳━╮╱╭┳━━━┳━━━┳╮╭━┳╮╱╱╭╮╭━━━┳━━╮╭━━━┳╮╱╭┳━━━┳━━━━┳━━┳━━━┳━╮╱╭╮\n┃╭━╮┃┃╰╮┃┃╭━━┫╭━╮┃┃┃╭┫╰╮╭╯┃┃╭━╮┃╭╮┃╰╮╭╮┃┃╱┃┃╭━╮┃╭╮╭╮┣┫┣┫╭━╮┃┃╰╮┃┃\n┃╰━━┫╭╮╰╯┃╰━━┫┃╱┃┃╰╯╯╰╮╰╯╭╯┃┃╱┃┃╰╯╰╮┃┃┃┃┃╱┃┃┃╱╰┻╯┃┃╰╯┃┃┃┃╱┃┃╭╮╰╯┃\n╰━━╮┃┃╰╮┃┃╭━━┫╰━╯┃╭╮┃╱╰╮╭╯╱┃╰━╯┃╭━╮┃┃┃┃┃┃╱┃┃┃╱╭╮╱┃┃╱╱┃┃┃┃╱┃┃┃╰╮┃┃\n┃╰━╯┃┃╱┃┃┃╰━━┫╭━╮┃┃┃╰╮╱┃┃╱╱┃╭━╮┃╰━╯┣╯╰╯┃╰━╯┃╰━╯┃╱┃┃╱╭┫┣┫╰━╯┃┃╱┃┃┃\n╰━━━┻╯╱╰━┻━━━┻╯╱╰┻╯╰━╯╱╰╯╱╱╰╯╱╰┻━━━┻━━━┻━━━┻━━━╯╱╰╯╱╰━━┻━━━┻╯╱╰━╯\n")
             trueend = input("Continue? Y/N ").upper()
             if trueend == "Y":
                 Ending()
             else:
                 Start()
        else:
             os.system('cls')
             print("You sit behind the leader then after hes done counting his money he spots you\n\nFAIL\nBro you suck at hide n seek\n")
    elif WiWa1 == "3":
        os.system('cls')
        print("You try to say something but get lauched out the room\n\nFAIL\nHere charisma will get you nowhere\n")
        retry = input("Retry? Y/N ").upper()
        if retry == "Y":
            WindowWait()
        else:
            Start()
    else:
        os.system('cls')
        print("You sit there and the leader looks up to see you\n\nFAIL\nThis isnt a museum about looking at the leader\n")
        retry = input("Retry? Y/N ").upper()
        if retry == "Y":
            WindowWait()
        else:
            Start()

def WindowCharge():
    os.system('cls')
    WiCa1 = input("You charge in with your sword and beat the two gaurds teh barge you way into the leader's room. He jumps up from his desk \"GAH! What!? Who are you!? arg! Dosnt matter Im out!\" He falls backwards out the window\n1>Parachute\n2>Water Bucket\n3>Bottle\n4>Fall\n5>Leader\n>>")
    if WiCa1 == "1":
        os.system('cls')
        print("You jump down and open the parachute but by the time you hit the floor the leader is already gone\n\nFAIL\nSafe is nice and all... but its not fast\n")
        retry = input("Retry? Y/N ").upper()
        if retry == "Y":
            WindowCharge()
        else:
            Start()
    elif WiCa1 == "2":
        os.system('cls')
        print("You fall down and try to pour the water under you but you miss by one block\n\nFAIL\nMLGs are harder than you think\n")
        retry = input("Retry? Y/N ").upper()
        if retry == "Y":
            WindowCharge()
        else:
            Start()
    elif WiCa1 == "3":
        os.system('cls')
        WiCa2 = input("you grab out a bottle and it seems to have a cloud in it then you strap it to your leg and jump down and just before you hit the floor you jump using the cloud and make it to the floor before the leader\n1>Slime\n2>Bed\n3>Hay\n4>Trampoline\n5>Catch\n>>")
        if WiCa2 == "1":
            os.system('cls')
            print("You place some slime on the floor and the leader hits it but doesnt survive\n\nFAIL\nThat was a pile of slime not a block\n")
            retry = input("Retry? Y/N ").upper()
            if retry == "Y":
                WindowCharge()
            else:
                Start()
        elif WiCa2 == "2":
            os.system('cls')
            print("You scoot over a bed and the leader falls right onto it and... uh...\n\nFAIL\nHe was just a little sleepy\n")
            retry = input("Retry? Y/N ").upper()
            if retry == "Y":
                WindowCharge()
            else:
                Start()
        elif WiCa2 == "3":
            os.system('cls')
            print("You scoot over a hay stack and the leader lands in it a gets stabbed by a needle\n\nFAIL\nThere it is! I found it!\n")
            retry = input("Retry? Y/N ").upper()
            if retry == "Y":
                WindowCharge()
            else:
                Start()
        elif WiCa2 == "4":
            os.system('cls')
            WiCa3 = input("You scoot over a trampoline and the leader bounes off of it and onto a ledge\n1>Sniper\n2>Net\n3>Rope\n4>Grapple\n>>")
            if WiCa3 == "1":
                os.system('cls')
                print("You snipe him\n\nFAIL\nWhat were you trying to do? be apart of TF2?\n")
                retry = input("Retry? Y/N ").upper()
                if retry == "Y":
                    WindowCharge()
                else:
                    Start()
            elif WiCa3 == "2":
                os.system('cls')
                print("You throw out a net but the leader breaks it before it even covers him\n\nFAIL\nI think the net was expired...\n")
                retry = input("Retry? Y/N ").upper()
                if retry == "Y":
                    WindowCharge()
                else:
                    Start()
            elif WiCa3 == "3":
                os.system('cls')
                print("You try to throw the rope and miss\n\nFAIL\nThis isnt like the western cowboy movies\n")
                retry = input("Retry? Y/N ").upper()
                if retry == "Y":
                    WindowCharge()
                else:
                    Start()
            elif WiCa3 == "4":
                os.system('cls')
                WiCa4 = input("You grapple the leader and grab him into your grasp but as you try to leave you see the exit is guarded\n1>Rush\n2>Attack\n3>Intimidate\n>>")
                if WiCa4 == "1":
                    os.system('cls')
                    print("You rush past both of then and they try to shoot you down but you sneak off and make it to the van \"Steve! You're back! And I see you have him... Good Job... though you could have brought him in a better way... dosnt matter, at least you got him\" They take him and throw him in the van \"Well Your free to go now.\"\n\nENDING:\n╭━━┳━━┳━┳┳╮╭┳┳━━┳━━┳━┳┳━━┳━┳━┳━━┳━┳┳━━╮\n┃━━╋┃┃┫╭┫╭╯┃╭┻┃┃┻╮╮┃┃┃┃╭╮┃╋┃╋┣┃┃┫┃┃┃╭━┫\n┣━━┣┃┃┫╰┫╰╮┃╰┳┃┃┳┻╯┃┃┃┃┣┫┃╭┫╭╋┃┃┫┃┃┃╰╮┃\n╰━━┻━━┻━┻┻╯╰┻┻━━┻━━┻┻━┻╯╰┻╯╰╯╰━━┻┻━┻━━╯")
                    trueend = input("Continue? Y/N ").upper()
                    if trueend == "Y":
                        Ending()
                    else:
                        Start()
                elif WiCa4 == "2":
                    os.system('cls')
                    print("You charge in and get shot down\n\nFAIL\nThey have guns... you have a person\n")
                    retry = input("Retry? Y/N ").upper()
                    if retry == "Y":
                        WindowCharge()
                    else:
                        Start()
                elif WiCa4 == "3":
                    os.system('cls')
                    print("You come out in front of them with the leader in your hands then get shot down\n\nFAIL\nI think you have the thing they need...\n")
                    retry = input("Retry? Y/N ").upper()
                    if retry == "Y":
                        WindowCharge()
                    else:
                        Start()
                else:
                    os.system('cls')
                    print("\n\nFAIL\n\n")
                    retry = input("Retry? Y/N ").upper()
                    if retry == "Y":
                        WindowCharge()
                    else:
                        Start() 
            else:
                os.system('cls')
                print("You stand there and the leader gets away\n\nFAIL\nYou kinda need to do something...\n")
                retry = input("Retry? Y/N ").upper()
                if retry == "Y":
                    WindowCharge()
                else:
                    Start()
        elif WiCa2 == "5":
            os.system('cls')
            print("You try to catch the leader and he falls right trough you arms\n\nFAIL\nYour accuracy sucks")
            retry = input("Retry? Y/N ").upper()
            if retry == "Y":
                WindowCharge()
            else:
                Start()
        else:
            os.system('cls')
            print("You sit there and the leader hits the floor\n\nFAIL\nHe kinda needs something to land on if your trying to keep him alive\n")
            retry = input("Retry? Y/N ").upper()
            if retry == "Y":
                WindowCharge()
            else:
                Start()
    elif WiCa1 == "4":
        os.system('cls')
        print("You fall and break both your legs\n\nFAIL\nReally? I thought this was commen sense!\n")
        retry = input("Retry? Y/N ").upper()
        if retry == "Y":
            WindowCharge()
        else:
            Start()
    elif WiCa1 == "5":
        os.system('cls')
        print("You fall right ontop of the leader makeing you survive but not the leader\n\nFAIL\nHey at least your still breathing\n")
        retry = input("Retry? Y/N ").upper()
        if retry == "Y":
            WindowCharge()
        else:
            Start()
    else:
        os.system('cls')
        print("You sit there and the leader gets away\n\nFAIL\nHe'll come back... maybe... most unlikely... he wont...\n")
        retry = input("Retry? Y/N ").upper()
        if retry == "Y":
            WindowCharge()
        else:
            Start()

def SIRoof():
    os.system('cls')
    Roofbegin = input("You fly up straight into the air and land ontop of the roof\n1>Hammer\n2>Hammer\n3>Hammer\n>>")
    if Roofbegin == "1":
        os.system('cls')
        print("You hit the roof and it barly cracks\n\nFAIL\nGotta hit harder than that\n")
        retry = input("Retry? Y/N ").upper()
        if retry == "Y":
            SIRoof()
        else:
            Start()
    elif Roofbegin == "2":
        os.system('cls')
        SIHammer2 = input("You smash the floor and fall into the building then you hear people starting to run twoards you\n1>Right Hallway\n2>Middle Staircase\n3>Left Room\n>>")
        if SIHammer2 == "1":
            os.system('cls')
            print("You run into the right hallway and right into people with guns\n\nFAIL\nSo thats where the footsteps came from\n")
            retry = input("Retry? Y/N ").upper()
            if retry == "Y":
                SIRoof()
            else:
                Start()
        elif SIHammer2 == "2":
            os.system('cls')
            SImiddlestair = input("You run up the stairs and find two people with guns talking to eachother you havnt grabbed their attention yet\n1>Rock\n2>Tackle\n3>Bar\n4>Pickpocket\n>>")
            if SImiddlestair == "1":
                os.system('cls')
                print("You hit one of them with a rock and the other spots you\n\nFAIL\nARG! Hey! Gaurds!\n")
                retry = input("Retry? Y/N ").upper()
                if retry == "Y":
                    SIRoof()
                else:
                    Start()
            elif SImiddlestair == "2":
                os.system('cls')
                print("You tackle one of them but the other shoots you\n\nFAIL\nYeah theres two of them...\n")
                retry = input("Retry? Y/N ").upper()
                if retry == "Y":
                    SIRoof()
                else:
                    Start()
            elif SImiddlestair == "3":
                os.system('cls')
                Bar = input("You grab a bar and strangle both of them then contine down the hall after hearing people comeing this way you dive into a room and hear \"Yeah the leader says hes going to be in the valt for awhile counting his riches for some reason but Im not gonna judge\" They walk away and you look out to see a map\n1>Valt\n2>Leader's Room\n3>Take out Gaurds\n>>")
                if Bar == "1":
                    os.system('cls')
                    ITBRoofValt()
                elif Bar == "2":
                    os.system('cls')
                    print("You try to go to the leaders room but get stopped by guards\n\nFAIL\nDid you really think they wouldnt guard the Leader's Room?\n")
                    retry = input("Retry? Y/N ").upper()
                    if retry == "Y":
                        SIRoof()
                    else:
                        Start()
                elif Bar == "3":
                    os.system('cls')
                    print("You go after the gaurds but you forgot that you dont have a weapon and they have guns\n\nFAIL\nShould have just stayed on task\n")
                    retry = input("Retry? Y/N ").upper()
                    if retry == "Y":
                        SIRoof()
                    else:
                        Start()
                else:
                    os.system('cls')
                    print("You stay there then get caught by other guards\n\nFAIL\nDo you just like standing still or something?\n")
                    retry = input("Retry? Y/N ").upper()
                    if retry == "Y":
                        SIRoof()
                    else:
                        Start()
            elif SImiddlestair == "4":
                os.system('cls')
                print("You pickpocket one of them for all their stuff W!Encumbered! You can no longer move\n\nFAIL\nYou really needed EVERYTHING?\n")
                retry = input("Retry? Y/N ").upper()
                if retry == "Y":
                    SIRoof()
                else:
                    Start()
        elif SIHammer2 == "3":
            os.system('cls')
            print("You run into the room to the left and the door lockes behind you. You try to open it but it dosnt budge\n\nFAIL\nSurvival bunkers are useful... sometimes\n")
            retry = input("Retry? Y/N ").upper()
            if retry == "Y":
                SIRoof()
            else:
                Start()
        else:
            os.system('cls')
            print("You sit there and the people rush into the room and kill you\n\nFAIL\nMove or Die\n")
            retry = input("Retry? Y/N ").upper()
            if retry == "Y":
                SIRoof()
            else:
                Start()
    elif Roofbegin == "3":
        os.system('cls')
        print("You try to hit the roof as hard as you can but you hit yourself\n\nFAIL\nBit too hard...\n")
        retry = input("Retry? Y/N ").upper()
        if retry == "Y":
            SIRoof()
        else:
            Start()
    else:
        os.system('cls')
        print("You sit there then get sniped\n\nFAIL\nTry acually getting inside the building next time\n")
        retry = input("Retry? Y/N ").upper()
        if retry == "Y":
            SIRoof()
        else:
            Start()

def ITBRoofValt():
    os.system('cls')
    Valtstart = input("You run to the valt but hide around the corner because you see a ton of guards at the valt's door\n1>Distraction\n2>Bomb\n3>Lazer\n4>Charge\n>>")
    if Valtstart == "1":
        os.system('cls')
        print("You go out and start to dance but they dont start danceing as well and just kill you\n\nFAIL\nWhy they no like dancing :(\n")
        retry = input("Retry? Y/N ").upper()
        if retry == "Y":
            ITBRoofValt()
        else:
            Start()
    elif Valtstart == "2":
        os.system('cls')
        print("You call an air strike and veryone blows up... and your right next to them\n\nFAIL\nExplosions arnt the solver of all problems\n")
        retry = input("Retry? Y/N ").upper()
        if retry == "Y":
            ITBRoofValt()
        else:
            Start()
    elif Valtstart == "3":
        os.system('cls')
        ValtRoof1 = input("You get a lazer dropped from the roof and you fire it and it takes away the door and all the gaurds and a scared leader hides in his pile of gold\n1>Hunt him dowm\n2>Leave him be\n>>")
        if ValtRoof1 == "1":
            os.system('cls')
            Valtroof2 = input("You go into the room and grab him from the cash by the troat and hold him up to the lazer he pleads that he'll premote you to leader if you spare him\n1>Kill\n2>Take\n3>Leave\n4>Spare\n>>")
            if Valtroof2 == "1":
                os.system('cls')
                print("You snap his neck and go back \"Steve! Your already back? Did you get him?\" You knod your head yes \"Nice work... wait... where is he?\" You look down \"Steve... where is he\"\n\nFAIL\nHe was wanted ALIVE not dead")
                retry = input("Retry? Y/N ")
                if retry == "Y":
                    ITBRoofValt()
                else:
                    Start()
            elif Valtroof2 == "2":
                os.system('cls')
                print("You walk out with the leader in your grasp \"Steve! Your back! and you brought the leader! Nice work now just throw him in the van\" You throw him in the van and they handcuff him \"Well that setles our deal, conisder your  criminal record removed!\"\n\nENDING:\n┏━━┓╋╋╋╋╋╋╋╋╋┏┓╋╋╋╋╋┏┓╋┏┓╋╋╋╋╋┏┓\n┃┏┓┃╋╋╋╋╋╋╋╋┏┛┗┓╋╋╋╋┃┃╋┃┃╋╋╋╋┏┛┗┓\n┃┗┛┗┳━━┳┓┏┳━╋┓┏╋┓╋┏┓┃┗━┛┣┓┏┳━╋┓┏╋━━┳━┓\n┃┏━┓┃┏┓┃┃┃┃┏┓┫┃┃┃╋┃┃┃┏━┓┃┃┃┃┏┓┫┃┃┃━┫┏┛\n┃┗━┛┃┗┛┃┗┛┃┃┃┃┗┫┗━┛┃┃┃╋┃┃┗┛┃┃┃┃┗┫┃━┫┃\n┗━━━┻━━┻━━┻┛┗┻━┻━┓┏┛┗┛╋┗┻━━┻┛┗┻━┻━━┻┛\n╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋┏━┛┃\n╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋┗━━┛\n")
                trueend = input("Continue? Y/N ").upper()
                if trueend == "Y":
                    Ending()
                else:
                    Start()
            elif Valtroof2 == "3":
                os.system('cls')
                print("You walk away and back ouside to the van \"Steve! Your already back? Did you get him?\" You shake your head no \"WHAT!? YOU JUST LEFT HIM BE!?\" You get put into hand cuffs \"I gave you a simple job and you didnt fallow it. So now you're under arest\"\n")
                print("----------------------------------------------------------------------------------------\n")
                print("▒█▀▀▀ █░░ █▀▀ █▀▀ 　 ▀▀█▀▀ █░░█ █▀▀ 　 ▒█▀▀▀ █▀▀█ █▀▀ ░▀░ █░░ ░▀░ ▀▀█▀▀ █░░█ \n▒█▀▀▀ █░░ █▀▀ █▀▀ 　 ░▒█░░ █▀▀█ █▀▀ 　 ▒█▀▀▀ █▄▄█ █░░ ▀█▀ █░░ ▀█▀ ░░█░░ █▄▄█ \n▒█░░░ ▀▀▀ ▀▀▀ ▀▀▀ 　 ░▒█░░ ▀░░▀ ▀▀▀ 　 ▒█░░░ ▀░░▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ░░▀░░ ▄▄▄█")
                nextGame = input("\nPlay? Y/N ").upper()
                if nextGame == "Y":
                    GameFTF()
                else:
                    Start()
            elif Valtroof2 == "4":
                os.system('cls')
                print("You let the leader down and agree to his pleads. Then you sit down in the leader's room and get the leader's badge\n\nENDING:\n╭━╮╱╱╱╱╭╮╭╮╭━╮╱╱╱╱╱╱╱╱╱╭╮╭╮\n┃╋┣━╮╭━╋╋╯┃┃╋┣┳┳━┳━━┳━╮┃╰╋╋━┳━┳╮\n┃╮┫╋╰┫╋┃┃╋┃┃╭┫╭┫╋┃┃┃┃╋╰┫╭┫┃╋┃┃┃┃\n╰┻┻━━┫╭┻┻━╯╰╯╰╯╰━┻┻┻┻━━┻━┻┻━┻┻━╯\n╱╱╱╱╱╰╯\n")
                trueend = input("Continue? Y/N ").upper()
                if trueend == "Y":
                    Ending()
                else:
                    Start()
            else:
                os.system('cls')
                print("You just sit there then randomly the lazer goes off\n\nFAIL\nYeah that thing is kind of active\n")
                retry = input("Retry? Y/N ").upper()
                if retry == "Y":
                    ITBRoofValt()
                else:
                    Start()
        else:
            os.system('cls')
            print("You walk away and back ouside to the van \"Steve! Your already back? Did you get him?\" You shake your head no \"WHAT!? YOU JUST LEFT HIM BE!?\" You get put into hand cuffs \"I gave you a simple job and you didnt fallow it. So now you're under arest\"")
            print("----------------------------------------------------------------------------------------\n")
            print("▒█▀▀▀ █░░ █▀▀ █▀▀ 　 ▀▀█▀▀ █░░█ █▀▀ 　 ▒█▀▀▀ █▀▀█ █▀▀ ░▀░ █░░ ░▀░ ▀▀█▀▀ █░░█ \n▒█▀▀▀ █░░ █▀▀ █▀▀ 　 ░▒█░░ █▀▀█ █▀▀ 　 ▒█▀▀▀ █▄▄█ █░░ ▀█▀ █░░ ▀█▀ ░░█░░ █▄▄█ \n▒█░░░ ▀▀▀ ▀▀▀ ▀▀▀ 　 ░▒█░░ ▀░░▀ ▀▀▀ 　 ▒█░░░ ▀░░▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ░░▀░░ ▄▄▄█")
            nextGame = input("\nPlay? Y/N ").upper()
            if nextGame == "Y":
                GameFTF()
            else:
                Start()
    elif Valtstart == "4":
        os.system('cls')
        print("You run into the gaurds but they gun you down\n\nFAIL\nWhat? Did you think the military would help you or something?\n")
        retry = input("Retry? Y/N ").upper()
        if retry == "Y":
            ITBRoofValt()
        else:
            Start()
    else:
        os.system('cls')
        print("You stay there and get found by other guards\n\nFAIL\nTheres more gaurds than just the ones at the valt ya know\n")
        retry = input("Retry? Y/N ").upper()
        if retry == "Y":
            ITBRoofValt()
        else:
            Start()
def GameFTF():
    os.system('cls')
    print("▒█░▒█ ▒█▄░▒█ ▒█▀▀▄ ▒█▀▀▀ ▒█▀▀█ 　 ▒█▀▀█ ▒█▀▀▀█ ▒█▄░▒█ ▒█▀▀▀█ ▀▀█▀▀ ▒█▀▀█ ▒█░▒█ ▒█▀▀█ ▀▀█▀▀ ▀█▀ ▒█▀▀▀█ ▒█▄░▒█ \n▒█░▒█ ▒█▒█▒█ ▒█░▒█ ▒█▀▀▀ ▒█▄▄▀ 　 ▒█░░░ ▒█░░▒█ ▒█▒█▒█ ░▀▀▀▄▄ ░▒█░░ ▒█▄▄▀ ▒█░▒█ ▒█░░░ ░▒█░░ ▒█░ ▒█░░▒█ ▒█▒█▒█ \n░▀▄▄▀ ▒█░░▀█ ▒█▄▄▀ ▒█▄▄▄ ▒█░▒█ 　 ▒█▄▄█ ▒█▄▄▄█ ▒█░░▀█ ▒█▄▄▄█ ░▒█░░ ▒█░▒█ ░▀▄▄▀ ▒█▄▄█ ░▒█░░ ▄█▄ ▒█▄▄▄█ ▒█░░▀█\n(Most likely wont get finished because of discouragement, sorry)\n")
    retry = input("Retry? Y/N ").upper()
    if retry == "Y":
        GameITBstart()
    else:
        Start()

def Ending():
    os.system('clsY')
    print("\n████████╗██╗░░██╗░█████╗░███╗░░██╗██╗░░██╗░██████╗  ███████╗░█████╗░██████╗░\n╚══██╔══╝██║░░██║██╔══██╗████╗░██║██║░██╔╝██╔════╝  ██╔════╝██╔══██╗██╔══██╗\n░░░██║░░░███████║███████║██╔██╗██║█████═╝░╚█████╗░  █████╗░░██║░░██║██████╔╝\n░░░██║░░░██╔══██║██╔══██║██║╚████║██╔═██╗░░╚═══██╗  ██╔══╝░░██║░░██║██╔══██╗\n░░░██║░░░██║░░██║██║░░██║██║░╚███║██║░╚██╗██████╔╝  ██║░░░░░╚█████╔╝██║░░██║\n░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚═════╝░  ╚═╝░░░░░░╚════╝░╚═╝░░╚═╝\n██████╗░██╗░░░░░░█████╗░██╗░░░██╗██╗███╗░░██╗░██████╗░██╗\n██╔══██╗██║░░░░░██╔══██╗╚██╗░██╔╝██║████╗░██║██╔════╝░██║\n██████╔╝██║░░░░░███████║░╚████╔╝░██║██╔██╗██║██║░░██╗░██║\n██╔═══╝░██║░░░░░██╔══██║░░╚██╔╝░░██║██║╚████║██║░░╚██╗╚═╝\n██║░░░░░███████╗██║░░██║░░░██║░░░██║██║░╚███║╚██████╔╝██╗\n╚═╝░░░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝\n")
    print("This game took a big crunch time and a lot of my heart, soul, and blood but I thank you so much for playing and I hope you enjoyed!\n")
    restart = input("Would you like to play again? Y/N ").upper()
    if restart == "Y":
        Start()
    else:
        exit()
def UC():
    print("██╗░░░██╗███╗░░██╗██████╗░███████╗██████╗░\n██║░░░██║████╗░██║██╔══██╗██╔════╝██╔══██╗\n██║░░░██║██╔██╗██║██║░░██║█████╗░░██████╔╝\n██║░░░██║██║╚████║██║░░██║██╔══╝░░██╔══██╗\n╚██████╔╝██║░╚███║██████╔╝███████╗██║░░██║\n░╚═════╝░╚═╝░░╚══╝╚═════╝░╚══════╝╚═╝░░╚═╝\n░█████╗░░█████╗░███╗░░██╗░██████╗████████╗██████╗░██╗░░░██╗░█████╗░████████╗██╗░█████╗░███╗░░██╗\n██╔══██╗██╔══██╗████╗░██║██╔════╝╚══██╔══╝██╔══██╗██║░░░██║██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║\n██║░░╚═╝██║░░██║██╔██╗██║╚█████╗░░░░██║░░░██████╔╝██║░░░██║██║░░╚═╝░░░██║░░░██║██║░░██║██╔██╗██║\n██║░░██╗██║░░██║██║╚████║░╚═══██╗░░░██║░░░██╔══██╗██║░░░██║██║░░██╗░░░██║░░░██║██║░░██║██║╚████║\n╚█████╔╝╚█████╔╝██║░╚███║██████╔╝░░░██║░░░██║░░██║╚██████╔╝╚█████╔╝░░░██║░░░██║╚█████╔╝██║░╚███║\n░╚════╝░░╚════╝░╚═╝░░╚══╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░╚═════╝░░╚════╝░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝\n")
    retry = input("Retry? Y/N ").upper()
    if retry == "Y":
        SnIn()
    else:
        Start()

#This sets everything in motion
Start()