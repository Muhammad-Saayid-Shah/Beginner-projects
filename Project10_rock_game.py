# simplerock paper scissor game

import random
l1 = ["Rock","Scissor","Paper"]



while True:
    Ucount = 0
    Ccount = 0
    dcount = 0
    print("""
Play Game --> 1
Exit Game --> 2

""")
    Uch = int(input("Enter Choice (1 or 2):"))
    if Uch == 1:
        for a in range(1,6):
            print("""
1: --> Rock
2: --> Scissor
3: --> Paper                                                                    
""")
            user_input = int(input("select item  (1,2,3):"))
            if user_input == 1:
                uchoice = "Rock"
            elif user_input == 2:
                uchoice = "Scissor"
            elif user_input == 3:
                uchoice = "Paper"
            else:
                print("Invalid input select(1,2, or 3)")
            Cchoice = random.choice(l1)
            if uchoice == Cchoice:
                print(f"User Choice is: {uchoice}")
                print(f"Computer Choice is: {Cchoice}")
                print("Game Draw... \n")
                dcount += 1
                
            elif (uchoice == "Rock" and Cchoice == "Scissor") or (uchoice == "Paper" and Cchoice == "Rock") or (uchoice == "Scissor" and Cchoice == "Paper"):
                print(f"User Choice is: {uchoice}")
                print(f"Computer Choice is: {Cchoice}")
                print("You Win... \n")
                Ucount += 1
                
            else:
                print(f"User Choice is: {uchoice}")
                print(f"Computer Choice is: {Cchoice}")
                print("computer Win... \n")
                Ccount += 1
        if Ucount == Ccount:
            print(f"Final Game is Draw...,")
            print(f"computer Score: {Ccount}")
            print(f"User Score: {Ucount}")
            print(f"Total Draw Games: {dcount}")
        elif Ucount > Ccount:
            print(f"Final User win ...")
            print(f"computer Score: {Ccount}")
            print(f"User Score: {Ucount}")
            print(f"Total Draw Games: {dcount}")
        else:
            print(f"Final Computer win..")
            print(f"computer Score: {Ccount}")
            print(f"User Score: {Ucount}")
            print(f"Total Draw Games: {dcount}")



    else:       
        break


