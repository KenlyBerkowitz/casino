# Created by Kenly Berkowitz
# 06/18/2020

from TwentyOne import TwentyOne
from HighLow import HighLow
from Bank import Bank
from HighLow import clrScreen 

# funciton to play the game hiLow
def playHighLow():
  highLow = HighLow()
  highLow.run(playerAccount)

# function to play the game of twenty one
def playtwentyOne():
    twentyOne = TwentyOne()
    twentyOne.run(playerAccount)
    
# will allow you insert money to retrieve money and gamble
def bank():
    playerAccount.getAccountBalance()
    playerAccount.winningStats()
    playerAccount.addFunds()

# thanks you for playing and quits after
def quit():
    print("Thank you for playing at Kenly's Riverboat Casino\n")
    playerAccount.winningStats()
    input("Press any key to continue...")

# makes the option by  using a switch like statement and returns a function
def getOption(selection):
    switcher = {
        1:playHighLow, 
        2:playtwentyOne, 
        3:bank, 
        4:quit, 
    }
    func = switcher.get(selection)
    return func()


# implement the menu to be displayed
def displayMenu():
    print("\n*************************************")
    print("Welcome to Kenly's Riverboat Casino!!")
    print("*************************************\n\n")
    print("\nMENU")
    print("––––")
    print("1) High or Low")
    print("2) Twenty-One")
    print("3) Bank - add money to your account")
    print("4) Quit")



# main function that will control the menu and the selection that is chosen
def main():
    clrScreen()
    userInput = 0

    while userInput != 4:
        displayMenu()
        flag1 = True
        while flag1:
            userInput = int(input("\nEnter a selection from the menu: "))
            clrScreen()
            if userInput < 1 and userInput > 4:
                print("Invalid input")
            else:
                flag1 = False
        option = getOption(userInput)
        if userInput == 4:
            pass
        else:
            clrScreen()

    
# runs the main function
if __name__ == "__main__":
    playerAccount = Bank()
    playerAccount.readTextData()
    main()
    playerAccount.writeTextData()


