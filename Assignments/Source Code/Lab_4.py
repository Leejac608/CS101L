########################################################################
##
## CS 101 Lab
## Program #4
## Name: Jacob Lee
## Email: jllw4v@umsystem.edu
##
## PROBLEM : The need for a slot machine
##
## ALGORITHM : 
##      1. Creating the play again function to make it so the user has the option of playing again or breaking out of the program
##      2. Creating the wager option to allow the player to wager what they would like in chips
##      3. Creating the bank option to allow the player to keep track of their bank and how much they would like to spend to spin
##      4. Reels function to allow for random integers to appear to give the game mechanic in 
##      5. Payout function to allow for the user to get paid in their bank
##      6. Creating the __main__ function allowing the previous functions to be used in the main 
##      7. Applying extra variables to keep track of certain elements such as spins, bank, max bank,etc.
## ERROR HANDLING:
##      Cannot wager 0 or negative chips or larger than current bank
##      Cannot input an integer or anything other than Y/YES or NO/N
##      Cannot start with chips less than or equal to 0 and not larger than 100 
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

import random

def play_again() -> bool:
    user_input = input("Do you want to play again?\n")
    user_input= user_input.upper()
    while (user_input != 'YES') and (user_input != 'Y') and (user_input != 'N') and (user_input != 'NO'):
        print('The value entered is not valid.')
        user_input = input("Would you like to play again? Y/YES or N/NO: \n")
        user_input = user_input.upper()
    if (user_input == 'NO') or (user_input == 'N'):
        return False
    else:
        return True

def get_wager(bank : int) -> int:
    user_wager = int(input("How many chips do you want to wager?"))
    while(user_wager > bank) or (user_wager < 1):
        print("The value must be above zero and less than your total chips.")
        user_wager = int(input("How much would you like to wager?: "))
    return user_wager

def get_slot_results() -> tuple:
    reel1 = random.randint(1,10)
    reel2 = random.randint(1,10)
    reel3 = random.randint(1,10)
    return reel1, reel2, reel3
def get_matches(reela, reelb, reelc) -> int:
    if reela == reelb == reelc:
        return 3
    elif (reela == reelb) or (reela == reelc) or (reelb == reelc):
        return 2
    else:
        return 0
def get_bank():
    user_bank = int(input("How many chips do you want to start with? \n"))
    if user_bank < 0:
        print("Too low a value, you can only choose 1 - 100 chips ")
        user_bank = int(input("How many chips do you want to start with? \n"))
    elif user_bank > 100:
        print("Too high a value, you can only choose 1 - 100 chips ")
        user_bank = int(input("How many chips do you want to start with? \n"))
    return user_bank
def get_payout(user_wager, user_matches):
    if user_matches == 3:
        return user_wager * 10
    elif user_matches == 2:
        return user_wager * 3
    else:
        return user_wager * -1

if __name__ == "__main__":
    user_playing = True
    while user_playing:
        user_bank = get_bank()
        beginning_bank = user_bank
        bank_max = 0
        final_max = user_bank
        user_spins = 0

        while user_bank > 0:
            user_wager = get_wager(user_bank)

            reel1,reel2,reel3 = get_slot_results()

            user_matches = get_matches(reel1,reel2,reel3)
            user_payout = get_payout (user_wager, user_matches)
            user_bank = user_bank + user_payout
            user_spins += 1

            if user_bank > final_max:
                final_max = user_bank
            print("Your spin", reel1, reel2, reel3)
            print("You matched", user_matches, "reels")
            print("You won/lost", user_payout)
            print("Current bank", user_bank)
            print()
        print("You lost all", beginning_bank, "in", user_spins, "spins")
        print("The most chips you had was", final_max)
        user_playing = play_again()






