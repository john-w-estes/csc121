'''
Random Number: Guessing Game
'''
import random

def main():

    print("Hi! I'm thinking of a random number between 1 and 100.")

    #Create a secret numbers
    secret_number = random.randrange(1, 101)

    #Attempt count
    user_attempt_number = 1

    #Set user number to something impossible
    user_guess = 0

    #Let user guess and loop until user gets it right or
    #user runs out of chances
    while user_guess != secret_number and user_attempt_number < 8:

        #Tell what attempt numbers
        print("---- Attempt ", user_attempt_number)
        user_input_text = input("Guess what number I am thinking of: ")
        user_guess = int(user_input_text)

        #print whether too high or too low
        if user_guess > secret_number:
            print("Too high.")
        elif user_guess < secret_number:
            print("Too low.")
        else:
            print("You got it!")

        #Add to the attempt count
        user_attempt_number += 1

    #Here check to see if the user ran out of tries.
    if user_guess != secret_number:
        print("Aw, you ran out of tries. The number was " + str(secret_number) + ".")

#Call the main function
main()

'''
This is  a simple text-only game that demonstrates the use of functions.
The game is called 'mudball' and the players take turns lobbing mudballs
at each other until someone gets hit.
'''
import math

def print_instructions():
    ''' This function prints the instructions '''

    #You can use the triple-quote string in a print statement to
    #print multiples lines.
    print("""Welcome to Mudball!!! The idea is to hit the other player with a mudball.
    Enter you angle (in degrees) and the amount of PSI to charge your gun with.
     """)

def calculate_distance(psi, angle_in_degrees):
    ''' Calculate the distance the mudball flies'''
    angle_in_radians = math.radians(angle_in_degrees)
    distance = .5 * psi ** 2 * math.sin(angle_in_radians) * math.cos(angle_in_radians)
    return distance

def get_user_input(name):
    '''Get the user input for psi and angle. Return a list of two numbers.'''
    #We wil learn more sophisticated tools later on.
    psi = float(input(name + " charge the gun with how much psi? "))
    angle = float(input(name + " move the gun at what angle? "))
    return psi, angle

def get_player_names():
    '''Get a list of players' names'''
    print("Enter players names. Enter as many as you'd like.")
    done = False
    players = []
    while not done:
        player = input("Enter player (hit enter to quit): ")
        if len(player) > 0:
            players.append(player)
        else:
            done = True

    print()
    return players

def process_player_turn(player_name, distance_apart):
    ''' The code runs the turn for each player.
    If it returns False, keep going with the game.
    If it reutrns True, someone has won, so stop.'''
    psi, angle = get_user_input(player_name)

    distance_mudball = calculate_distance(psi, angle)
    difference = distance_mudball - distance_apart

    if difference > 1:
        print("You went ", difference, " yards too far!")
    elif difference < 1:
        print("You went ", difference * -1, " yards too short!")
    else:
        print("Hit!", player_name, "wins!")
        return True

    print()
    return False

def main():
    """Main program."""

    "Get the game started."
    print_instructions()
    player_names = get_player_names()
    distance_apart = random.randrange(50, 150)

    #Keep looking until someone wins
    done = False
    while not done:
        #Loop for each player
        for player_name in player_names:
            #process their turns
            done = process_player_turn(player_name, distance_apart)
            #If someone won, 'break' out of this loop.
            if done:
                break

if __name__ == "__main__":
    main()
