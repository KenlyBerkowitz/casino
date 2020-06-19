import random
import time
import os



##################
### Dice Class ###
##################

class Dice: 

    def __init__(self):
        self.die1 = 1
        self.die2 = 1
        self.timeUnit = 0.0
        self.total = 0

    # will return values
    def playerRollDice(self):
        self.timeUnit = .02

        # loop to simulate dice rolls
        for x in range(25):
            clrScreen()
            print("Good Luck", end = "")
            if x % 3 == 2:
                print("...")
            elif x % 3 == 1:
                print("..")
            else:
                print(".")

            # assigns dice random numbers and prints them
            self.die1 = random.randint(1,6)
            print("Die 1: ", self.die1)
            self.die2 = random.randint(1,6)
            print("Die 2: ", self.die2)
            time.sleep(self.timeUnit)
            self.timeUnit += .02

    # computer dice roll
    def compRollDice(self):
        self.die1 = random.randint(1,6)
        self.die2 = random.randint(1,6)
    
    # prints the total of dice
    def getDiceTotalStr(self):
        self.total = self.die1 + self.die2
        print("Total: ", self.total)

    # tallies and returns dice totals
    def getDiceTotal(self):
        self.total = self.die1 + self.die2
        return self.total



#####################
### HighLow Class ###
#####################

class HighLow:

    def __init__(self):
        self.dice = Dice()
        self.wager = 0

    #displays welcome and rules of the game    
    def welcome(self):
        print("Welcome to the game of Hi Low. ")
        print("––––––––––––––––––––––––––––––\n")
        print("RULES: \n-------")
        print("This game is played with two dice that will be rolled.")
        print("Make a wager and define your bet if it will be high or low.")
        print("Low consists of of numbers 1-6 and high consists of 7-12.")
        print("House wins on dice showing 3 and 4.")
        print("Player wins automatically on snake eyes (1,1)")
        print("Pays 1 : 1")
        print("Good Luck!!\n")

    # determines winner to add or subtract to balance in players account
    def resultPayout(self, playerAccount, diceTotal, userChoice):

        if self.dice.die1 == 1 and self.dice.die2 == 1:
            print("You win!!!")
            playerAccount.addWinnings(self.wager)

        elif self.dice.die1 == 3 and self.dice.die2 == 4:
            print("You Lose...")
            playerAccount.subtractFunds(self.wager)

        elif self.dice.die1 == 4 and self.dice.die2 == 3:
            print("You Lose...")
            playerAccount.subtractFunds(self.wager)

        elif diceTotal >= 1 and diceTotal <= 6:
            if userChoice == 'L':
                print("You win!!!")
                playerAccount.addWinnings(self.wager)
            else:
                print("You Lose...")
                playerAccount.subtractFunds(self.wager)
        
        elif diceTotal >= 7 and diceTotal <= 12:
            if userChoice == 'H':
                print("You win!!!")
                playerAccount.addWinnings(self.wager)
            else:
                print("You Lose...")
                playerAccount.subtractFunds(self.wager)

        playerAccount.getAccountBalance()    #displays account balance

    # runs main game
    def run(self, playerAccount):
        self.welcome()

        flag1 = True
        while flag1:
            while True:
                try:
                    self.wager = int(input("How much would you like to bet? \nEnter a whole number: "))
                except:
                    print("Invalid number. Please enter a whole number")
                else:
                    break

            playerAccount.wagerBalanceCheck(self.wager)    # checks whether or not the acct balance is greater than the wager
            # if the player enter 0 as bet, and has zero money, the game is ended
            if playerAccount.balance == 0:    
                break
            print("Your bet: ", self.wager, "\n")

            # user input and input validation
            flag2 = True
            while flag2:
                userChoice = input("High or Low? Enter [H/L]: ")
                userChoice = userChoice.upper()
                if userChoice == 'H' or userChoice == 'L':
                    flag2 = False
                else:
                    print("Invalid choice...")

            # rolls dice and tallies dice 
            self.dice.playerRollDice()
            diceTotal = self.dice.getDiceTotal()
            self.resultPayout(playerAccount, diceTotal, userChoice)    # determines is player won or lost

            flag3 = True
            while flag3:
                charInput = input("Would you like to play again? [Y/N]: ")
                charInput = charInput.upper()
                if charInput == 'Y' or charInput == 'N':
                    if charInput == 'N':
                        flag1 = False
                        print("\nThank you for playing High or Low")
                        input("Press any key to continue...")
                    flag3 = False



# needed to put this function outside of main due to import loop
# clearscreen function
def clrScreen():
    
    #for mac/linux
    if os.name == 'posix':
      _ = os.system('clear')
    # for windows 
    else:
      _ = os.system('cls')
    print("\n\n")



