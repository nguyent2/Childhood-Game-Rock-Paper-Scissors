#################################################################################
# Author(s): Thy H. Nguyen
# Username: nguyent2
#
# Assignment: A07: Rock-Paper-Scissors
# Purpose: Practice solving a problem more independently (without much/any starter code).
# More practice breaking a problem into pieces using functions.
# Even more practice with key concepts so far: loops, conditionals, and more!
#################################################################################
# Acknowledgements: Berea College
#
#
#################################################################################

import random
def computer_choice():
    """
    This function randomly prints the computer's choice
    :param: None
    :return: computer_turn, the choice that the computer randomly chooses
    """
    choices = ("scissors", "paper", "rock", "lizard", "spock") #A tuple of choices to save space for the randomly chooses one
    computer_turn = random.choice(choices) #The choice of the computer
    print("Computer chooses ", computer_turn, ".")
    return  computer_turn

def check_user_choice(user_choice):
    """
    This function checks to see if the user's input is compatible for this game or not.
    If the user puts in an incompatible word, require the user to redo it until it is compatible.
    :param user_choice: the input user enters in
    :return: user_choice (all lower cases), and inform ready for the next step
    """

    choices = ["scissors", "paper", "rock", "lizard", "spock"] #List of choices to check compatibility
    user_choice = user_choice.lower() #lower case all of the inputs
    while user_choice not in choices: #If the input is incompatible
        user_choice = input("Enter a choice: ").lower() #requires the user to put in one of the choices in the list
    print("You are ready for this game!") #announce that the user is ready for the next step
    return user_choice

def check_winner(user_choice):
    """
    This functions check to see the user is win or lose
    :param user_choice: This takes the user's input (which is compatible with this game)
    :return: result, whether the user loses, wins, or draws in the game.
    """
    choices = (("rock", "spock", "scissors", "paper",  "lizard"),("scissors", "lizard", "paper", "rock", "spock"),
               ("spock", "paper", "rock", "scissors", "lizard"), ("scissors", "rock", "lizard", "paper", "spock"),
              ("paper",  "lizard", "spock", "rock","scissors"))
    #Since the list of choices are fixed, used tuples to save the space of this program. Each case is inside one tuple.
    #The order is that to the left of the center is lose, to the right is win, at the center is draw
    computer_turn = computer_choice()
    #Take the computer's choice
    for i in range(5): #Since there are only 5 cases
        if user_choice == (choices[i])[2]: #Check through all of the tuples to find the case
            if computer_turn == (choices[i])[0] or computer_turn == (choices[i])[1]:
                #The options to the left of the center is lose
                result = "Computer wins"
            elif computer_turn == (choices[i])[2]:
                #The options to the right is win
                result = "This is a draw. No one wins."
            else: #This is the center position
                result = "User wins."
    print(result) #print result so the user knows it.
    return result

def points(result):
    """
    This function calculates the points of each round
    :param result: this is the result from the previous (whether the user wins, loses or draws)
    :return: Computer_point: the points of computer, User_point: the point of the user
    """
    if result == "Computer wins":
        #Make a tuple to save the result of each round
        (Computer_point,User_point)=(1,0)
        print("Computer: ", Computer_point, "User: ",User_point)
    elif result == "User wins.":
        (Computer_point,User_point)=(0,1)
        print("Computer: ", Computer_point, "User: ", User_point)
    else:
        (Computer_point,User_point) = (0,0)
        print("Computer: ",Computer_point, "User: ", User_point)
    return (Computer_point,User_point)
    #return a tuple so that we can calculate the sum of points easier.

def sum(list_of_result):
    """
    This function sums the score of the game
    :param list_of_result: the list of the result after each round
    :return: computer_total_point, and user_total_point (the total points of each opponent)
    """

    computer_total_point=0
    user_total_point=0
    for i in range(int(len(list_of_result))):
        (points_added_for_computer,points_added_for_user)=list_of_result[i]
        computer_total_point += points_added_for_computer
        user_total_point +=points_added_for_user
    print("Computer total point is: ", computer_total_point, " User total point is: ", user_total_point)
    return computer_total_point, user_total_point

def main():
    """
    This function is the main function
    :param: None
    :return: The points of the game
    """

    list_of_result = [] #Create an empty list for saving the result
    while True: #This game will run forever
        user_choice = input("Enter a choice: ")
        result = check_winner(check_user_choice(user_choice))
        list_of_result.append(points(result))
        sum(list_of_result)

main()
