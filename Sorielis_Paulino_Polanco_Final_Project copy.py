# Sorielis Paulino Polanco
# Comp 112-03

import turtle
import os
import time
import random 

os.chdir("/Users/sorielispaulinopolanco/Documents")
screen = turtle.Screen()
move_speed = 10
turn_speed = 10





def forward():
    turtle.forward(move_speed)
def backward():
    turtle.backward(move_speed)
def left():
    turtle.left(turn_speed)
def right():
    turtle.right(turn_speed)


# making dictionary for the questions
questions = {"Should Sorielis get up to go to class?(Write Yes or No)":"yes" ,
             "Should Sorielis go to spanish class?(Write Yes or No)":"yes" ,
             "\nSorielis has free time to study in Olin for the up coming tests! Should Sorielis go to study?(Write yes or no)": "yes" ,
             "Sorielis is hungry should she go to Usdan \n or go to her room to make a mini sandwich(write usdan or room)":"usdan" }



score = 0
inventory = []
def points(question, valid_answers=None):
    
    """
With using the dictionary and values
if user adds the correct answer will gain 5 points.
if user adds invalid answer -1
if incorrect -2
By putting the .lower() function it will make it that if User puts Yes or yes will anyways give the user 5 points

Str and then returns if user gains 5 points or not.

    """
  
    
    global score
    
    correct_answer = questions[question].lower()      
    while True:
        answer = input(question).lower()  
        if valid_answers and answer not in valid_answers:
            print("Invalid input!")
            score -= 1  
            print("You have lost 1 point "+str(score)+" points.\n")
        elif answer == correct_answer:
            score += 5 
            print("Correct! You gained 5 points.")
            print("Your current score is "+str(score)+" points.\n")
            break
        else:
            score -= 2  
            print("Incorrect! You lost 2 points.")
            print("Your current score is "+str(score)+" points.\n")
            break

    
    

def sorielis_life():
    
    """
if statements for users inputs
outputs will show at the end if user lost points or gain points.

no signature.
    """
 

    screen.bgcolor("lightblue")
        
    print("WELCOME TO SORIELIS'S LIFE")
    print("Try to get over 10 points!AND COLLECT OBJECTS!")
    user = input("Write 'start' to start:")

    if user == 'start':
        print("Story Time: \nSorielis wake up in her cozy room. Then\n 'BEEP BEEP'. Wake up and then the day begins!! ")
        
        user1 = points("Should Sorielis get up to go to class?(Write Yes or No)")
        print("\n")
        
        
        pick1 = input("Next? (Write Yes or No): ").lower()
            

        if pick1 == 'yes':
            print("\n Sorielis turn off the alarm, and get out from bed. Sorielis is getting ready for class.")
            
            points("Should Sorielis go to spanish class?(Write Yes or No)")
            print("You find the Spanish Book on the table. Do you want to collect it? (Write Yes or No)")
            # this collects objects 
            collect_book = input().lower()
            
            if collect_book == 'yes':
                inventory.append("Book") 
                print("You have collected the Spanish Book!")
            
            print("\n")
            
            pick2 = input("Next?(Write Yes or No)").lower()

            if pick2 == "yes":
                print(" 'Well is time for me to go to class... sigh...'\n You go to class")
                
                image1=("SorielisP.gif")
                screen.register_shape(image1)
                turtle.shape(image1)
                turtle.width()

                turtle.penup()
                turtle.speed(5)
                turtle.home()
                turtle.home()
                turtle.back(400)

                print("I'm in class !")
                turtle.clearscreen()
                screen.bgcolor("pink")

                print("\nClass ends!")
                points("\nSorielis has free time to study in Olin for the up coming tests! Should Sorielis go to study?(Write yes or no)")
               
                print("You find a magic pencil. Do you want to collect it? (Write Yes or No)")
                collect_book = input().lower()
                # this collects objects 
                if collect_book == 'yes':
                    inventory.append("Magic Pencil") 
                    print("You have collected a Magic Pencil!")
                    
                    print("\n")
                
                
                        
                pick3 = input("Next!(Write Yes or No)").lower()

                if pick3 == 'yes':
                    print("\n")
                    print("Time to study for an hour!")
                    points("Sorielis is hungry should she go to Usdan \n or go to her room to make a mini sandwich(write usdan or room)")
                  

                
                    print("Let's go back to my room! I have my drawing 1 class I need to get my materials ")
                    image2 = ("SorielisP.gif")
                    screen.register_shape(image2)
                    turtle.shape(image2)
                    turtle.width()

                    turtle.penup()
                    turtle.speed(5)
                    turtle.home()
                    turtle.home()
                    turtle.back(500)
                    screen.clear()

                    
                    

                    
                        


                        #while user plays if user gets more than 10 they have won the game
                        #but if they did not it will say try again
                        #
                    if score > 10:
                        
                        
                        print("YOU WON!")
                        turtle.write('You won!\nThe End.',align = "center", font = ("Arial", 50 , "normal"))
                        screen.bgcolor("pink")
                        print("Your final score = " + str(score) + " points. This is your invantory:" +str(inventory))
                    else:
                        print("Try again:(")
                        turtle.write('Try again:(',align = "center", font = ("Arial", 50 , "normal"))
                        screen.bgcolor("red")
                        print("Your final score = " + str(score) + " points. This is your inventory:"+str(inventory))
                    
                            
                            
                       

            
                 
sorielis_life()



