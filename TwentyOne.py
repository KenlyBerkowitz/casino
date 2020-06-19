from HighLow import Dice
from HighLow import clrScreen 



########################
### Twenty-One Class ###
########################

class TwentyOne:
    # initializes a TwentyOne object
    def __init__(self):
        self.dice = Dice()
        self.wager = 0

    # displays welcome to game and rules
    def welcome(self):
        print("Welcome to the game of Twenty One!")
        print("––––––––––––––––––––––––––––––––––\n")
        print("This game is played with a two - six sided dice.\n")
        print("Roll to get as close as you can to 21 without going over.\n")
        print("If the computer gets closer to 21 than you, the computer wins. Otherwise, you win. \n")
        print("If you and the computer goes over 21, you tie.\n")
        print("If you get the same number as the computer without going over, the computer wins.\n")
        print("The computer rolls the same amount of times as you.\n")
        print("You are forced to roll a minimum of two times\n")
        print("Have fun! Good Luck!\n")
        print("Pays 1 : 1")

    # main running program to play the game
    def run(self, playerAccount):
        self.welcome()

        flag1 = True
        while flag1:
            playerTotal = 0
            computerTotal = 0
            flag2 = True        # flag for while loops
            flag3 = True        # flag for while loops

            # Input and input validation for type and value
            while True:
                try:
                    self.wager = int(input("How much would you like to bet? \nEnter a whole number: "))
                except:
                    print("Invalid number.\n\n Please enter a whole number")
                else:
                    break

            playerAccount.wagerBalanceCheck(self.wager)     # checks whether the balance is greater than wager
            # if the player enter 0 as bet, and has zero money, the game is ended
            if playerAccount.balance == 0:
                break
            print("Your bet: ", self.wager, "\n")

        
            while flag3:
                # checks if it is the first roll, if it is, the program will not execute next while loop
                if playerTotal == 0:
                    flag4 = False
                else:
                    flag4 = True
                input("Press any key to roll...")

                # rolls players dice
                self.dice.playerRollDice()
                playerTotal += self.dice.getDiceTotal()
                print("Player Total: ", playerTotal)

                # rolls computers dice
                self.dice.compRollDice()
                computerTotal += self.dice.getDiceTotal()

                #if player goes over 21, the game is over
                if playerTotal > 21:
                    flag3 = False
                    flag4 = False

                # user input and validation to roll again
                while flag4:
                    charInput = input("Would you like to roll again? [Y/N]: ")
                    charInput = charInput.upper()
                    if charInput == 'Y' or charInput == 'N':
                        if charInput == 'N':
                            flag3 = False
                        flag4 = False
            
            # displays scores
            print("\n\nPlayer Total: ", playerTotal)
            print("Computer Total: ", computerTotal)

            # determines winner
            if playerTotal > 21 and computerTotal > 21:
                print("Its a tie!")
            elif playerTotal > 21 and computerTotal <= 21:
                print("You Lost...")
            elif playerTotal <= 21 and computerTotal > 21:
                print("You Won!!")
                playerAccount.addWinnings(self.wager)
            elif playerTotal <= 21 and computerTotal <= 21:
                if(playerTotal > computerTotal): 
                    print("You won!")
                    playerAccount.addWinnings(self.wager)
                else:
                    print("You Lost...")
                    playerAccount.subtractFunds(self.wager)
            elif playerTotal == computerTotal:
                print("Computer Won...")
                playerAccount.subtractFunds(self.wager)
            elif playerTotal <= 21 and computerTotal > 21:
                print("You Won!!")
                playerAccount.addWinnings(self.wager)

            playerAccount.getAccountBalance()    # prints account balance
            
            # user input and validation to play again
            flag5 = True
            while flag5:
                charInput1 = input("Would you like to play again? [Y/N]: ")
                charInput1 = charInput1.upper()
                if charInput1 == 'Y' or charInput1 == 'N':
                    if charInput1 == 'N':
                        flag1 = False
                        print("\nThank you for playing Twenty-One")
                        input("Press any key to continue...")
                    flag5 = False

            clrScreen()
            