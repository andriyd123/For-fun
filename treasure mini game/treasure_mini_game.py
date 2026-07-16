from ast import If


print('''
    .-------.--------.
   /_______/|\______/ \
   \                \  )
    \oOo__   __o_o___\.'     
   .- 88 <-o-> ) ) .- |        
   |-8-8--\|/--o-o-|.'|
|\/| <*>   '   ( ( |  _($)
@@@'-----------O-O-'(@)=
     O-m   |\/\/|
           '----'             ldb
------------------------------------------------
''')

print("Welcome to the Treasure Mini Game! Your goal is to find the treasure. Good luck!")

choice1 = input("You are at a crossroad. Choose to go 'left' or 'right'.").lower()

if choice1 == "left":
    choice2 = input("You come to a lake. There is an island in the middle of the lake." " Type 'wait' to wait for a boat or 'swim' to swim across.").lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?").lower()
        if choice3 == "red":
            print("You found the treasure! You win!")
        else:
            print("You chose the wrong door. Game Over.")
    else:
        print("You get attacked by an angry shark. Game Over.")
else:
    print("You fell into a hole. Game Over.")

