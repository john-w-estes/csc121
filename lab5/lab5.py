import random

def print_intro():
    print("Welcome to Camel!")
    print(" ")
    print("In your desperation, you have stolen a camel to make your way")
    print("across the great Mobi dessert.")
    print("The locals want their camel back and are chasing you down!")
    print("Survive your desert trek and out run the locals.")

def main():
    print_intro()

    miles = 0
    thirst = 0
    camel_tiredness = 0
    locals_travelled = -20
    canteen_drinks = 10

    done = False

    while done == False:
        print("A. Drink from your canteen.")
        print("B. Ahead at moderate speed.")
        print("C. Ahead full speed.")
        print("D. Stop for the night.")
        print("E. Status check.")
        print("Q. Quit.\n")

        user_choice = input(print("Which choice do you want? "))

        if user_choice.upper() == "Q":
            done = True
        elif user_choice.upper() == "E":
            #prints stats
            print("Miles traveled: ", miles)
            print("Drinks in canteen: ", canteen_drinks)
            print(f"The locals are {abs(miles -  locals_travelled)} miles behind you.")
        elif user_choice.upper() == "D":
            #Camel gets rest, but the locals get closer
            camel_tiredness = 0
            locals_gain = random.randrange(7,15)
            locals_travelled += locals_gain

            print("The camel is very happy and gives you his thanks.")
            print("And the locals have gained ", locals_gain, "miles.")
        elif user_choice.upper() == "C":
            #Full speed ahead
            full_speed_gain = random.randrange(10, 21)
            camel_gets_tired = random.randrange(1,3)
            locals_gain = random.randrange(7, 15)
            miles += full_speed_gain
            thirst += 1
            camel_tiredness += camel_gets_tired
            locals_travelled += locals_gain

            print("You and your camel travelled forward ", full_speed_gain, "miles.")
        elif user_choice.upper() == "B":
            #Moderate speed ahead
            mod_speed_gain = random.randrange(5, 13)
            locals_gain = random.randrange(7, 15)
            miles += mod_speed_gain
            thirst += 1
            camel_tiredness += 1
            locals_travelled += locals_gain

            print("You and your camel travelled forward ", mod_speed_gain, "miles.")
        elif user_choice.upper() == "A":
            #Drink
            if canteen_drinks > 1:
                canteen_drinks -= 1
                thirst = 0
                print("You have ", canteen_drinks, "left.")
            else:
                print("Oh no! You have no drinks left!")

        if thirst  > 6:
            print("You died of thirst!")
            done = True
        elif thirst > 4:
            print("You are thirsty.")

        if camel_tiredness > 8:
            print("You let the poor camel die!")
        elif camel_tiredness > 5:
            print("Your camel is tired.")

        if miles > 200:
            print("You escaped! You escaped!")
            done = True

        if locals_travelled > miles - 15:
            print("The locals are getting close!")
        if locals_travelled >= miles:
            print("You were caught by the locals... an unfortunate end. ")
            done = True

        oasis_attempt = random.randrange(1,21)
        if oasis_attempt == 1:
            print("You found a legendary oasis!")
            print("Fill your canteen! Let your camel rest!")
            thirst = 0
            camel_tiredness = 0

print("The end!")

if __name__ == '__main__':
    main()
