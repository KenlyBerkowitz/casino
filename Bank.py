##################
### Bank Class ###
##################

class Bank:

    def __init__(self):
        self.balance = 0  # private variable 
        self.fundsAdded = 0 # used to determine how much you made
       

    # adds money to the  account 
    def addFunds(self):
        if self.balance == 0:
            print("\nPlease add money to your account in order to gamble")
        flag = True
        while flag:
            print("Enter 0 if you would not like to buy any tokens.\n")
            try:
                money = int(input("Enter the amount of tokens you would like to buy: "))
                if money < 0:
                    print("Please enter a positive amount")
                else: 
                    flag = False
            except:
                    print("Invalid number.\n\nPlease enter a whole number")
            else:
                break
            
        self.balance += money
        self.fundsAdded += money
    
    # check to see if there  is enough money to make the bet
    def wagerBalanceCheck(self, wager):
        if wager > self.balance:
            print("\nInvalid balance. \nPlease enter more money into your account.")
            flag = True
            while flag:
                charInput = input("Would you like to enter more funds into your account? [Y/N]: ")
                charInput = charInput.upper()
                if charInput == 'Y' or charInput == 'N':
                    if charInput == 'Y':
                        self.addFunds()    # calls the addfunds function if the user wants to add funds on the spot
                        flag = False
                    else:
                        flag = False
                else:
                    print("Invalid input. Re-enter:")

    # adds wager if won
    def addWinnings(self, wager):
        self.balance += wager


    # subtract wager if lost
    def subtractFunds(self, wager):
        self.balance -= wager

    # prints account balance
    def getAccountBalance(self):
        print("Account Balance: ", self.balance)
        print("––––––––––––––––––––––\n")

    # prints winnings 
    def winningStats(self):
        print("Winnings: ", self.balance - self.fundsAdded)
        print("––––––––––––––\n")

    # outputs balance and winnings to .txt file
    def readTextData(self):
        tf = "textBalanceData.txt"
        textFile = open(tf, "r")

        textFile.seek(0)
        self.balance = int(textFile.readline())
        self.fundsAdded = int(textFile.readline())

        textFile.close()

    # inputs balance and winnings to .txt file
    def writeTextData(self):
        tf = "textBalanceData.txt"
        textFile = open(tf, "w")

        textFile.seek(0)
        textFile.write(str(self.balance) + "\n")
        textFile.write(str(self.fundsAdded) + "\n")

        textFile.close()