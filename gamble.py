import random
import re
import sys
import os


def clear():
    if sys.platform == "linux" or sys.platform == "linux2":
        os.system("clear")
    elif sys.platform == "win32":
        os.system("cls")


def create_file():
    opnr = open("wallet.txt", "w+")
    opnr.write("1")
    opnr.close()


def file_writer(data):
    opnr = open("wallet.txt", "w")
    opnr.write(str(data))
    opnr.close()


def file_reader():
    opnr = open("wallet.txt", "r")
    data = opnr.read()
    opnr.close()
    
    return data


def gamble(bets):
    global randnum
    
    if randnum <= bets:
        return 0
    else:
        return 1


if __name__ == "__main__":
    try:
        clear()
        pattern_bet = r"bet"
        pattern_wallet = r"wallet"
        pattern_beg = r"beg"
        level = 3
        #wallet = int(file_reader())
        while True:
            if int(file_reader()) < 100 and int(file_reader()) > 30:
                randnum = random.randint(23, int(file_reader()))
            elif level > 3:
                randnum = random.randint(level+int(file_reader())-20, int(file_reader())+30)
            else:
                randnum = random.randint(int(file_reader())-30, int(file_reader())+60)
            

            user_input = input("> ")
            
            if re.search(pattern_bet, user_input):
                bets = int(user_input.lstrip("bet"))
                if bets <= int(file_reader()):
                    if gamble(bets) == 0:
                        file_writer(str(int(file_reader())+randnum))
                        #wallet += randnum
                        file_writer(int(file_reader()))
                        print("__________________")
                        print("|You Won: {0}     |".format(randnum))
                        print("|Wallet: {0}      |".format(int(file_reader())))
                        print("|_________________|")
                        level += 9
                    else:
                        file_writer(str(int(file_reader())-bets))
                        if int(file_reader()) < 0:
                            file_writer("0")
                        
                        #file_writer(str(int(file_reader())))
                        print("__________________")
                        print("|You Lost: {0}   |".format(bets))
                        print("|Wallet: {0}     |".format(int(file_reader())))
                        print("|________________|")
                        level -= 3
                else:
                    print ("You Don't enough Coins")
            elif re.search(pattern_wallet, user_input):
                print("Wallet: {0}".format(int(file_reader())))
            elif user_input.strip() == "beg":
                bot = random.randint(0, 1)
                if bot == 1:
                    if int(file_reader()) == 0:
                        randints = random.randint(1, 50)
                        coins = str(int(file_reader()) + randints)
                        file_writer(coins)
                        print("You Got: ", randints)
                    else:
                        randints = random.randint(1, int(file_reader())+3)
                        coins = str(int(file_reader()) + randints)
                        file_writer(coins)
                        print("You Got: ", randints)
                else:
                    print("You Got 0 Coins")
            
            elif user_input.strip() == "exit":
                exit()
            elif user_input.strip() == "commands":
                print("commands ->   shows all the Commands")
                print("bet [You're amount]  ->   Puts a bet ")
                print("wallet ->   Shows You're Wallet")
                print("beg ->   beg for coins")
                print("exit ->   Exit Game")
            else:
                print("Invalid Input")
    except FileNotFoundError as error:
        create_file()
    except KeyboardInterrupt:
        print("Type exit To Exit")
    except Exception as error:
        print(error)

