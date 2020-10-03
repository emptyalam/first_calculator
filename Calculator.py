import sys
import os

os.system("cls")
# is_windows = sys.platform.startswith('win')

# Console Colors
# if is_windows:
# Windows deserves coloring too :D

G = '\033[92m'  # green
Y = '\033[93m'  # yellow
B = '\033[94m'  # blue
R = '\033[91m'  # red
W = '\033[0m'  # white


# try:
#     import win_unicode_console, colorama
#
#     win_unicode_console.enable()
#     colorama.init()
#     # Now the unicode will work ^_^
# except:
#     print("[!] Error: Coloring libraries not installed, no coloring will be used [Check the readme]")
#     G = Y = B = R = W = G = Y = B = R = W = ''

# else:
# Black: \u001b[30m
# Red: \u001b[31m
# Green: \u001b[32m
# Yellow: \u001b[33m
# Blue: \u001b[34m
# Magenta: \u001b[35m
# Cyan: \u001b[36m
# White: \u001b[37m
# Reset: \u001b[0m


def banner():
    print("""%s
    
    |.\    /|.  /\.  |.   |.|````)./``/\. |````).
    |. \  / |. /__\. |====|.|---<.|  /  |.|---<. 
    |.  \/  |./    \.|.   |.|____).\/__/. |____).%s%s
    """ % (R, G, Y))
    return "\t\u001b[36m# Coded By Mahbob Alam !!!\u001b[0m\n"


# Black: \u001b[30m
# Red: \u001b[31m
# Green: \u001b[32m
# Yellow: \u001b[33m
# Blue: \u001b[34m
# Magenta: \u001b[35m
# Cyan: \u001b[36m
# White: \u001b[37m
# Reset: \u001b[0m

print(banner())


def cal():
    print("\n\u001b[33mEnter First Number: ", end="")
    firstNumber = int(input())
    print("Enter Operator: ", end="")
    operator = input()
    print("Enter Second Number: ", end="")
    secondNumber = int(input())

    # yN = input("Try again y/n: ")
    # if firstNumber == 45 and operator == "*" and secondNumber == 3:
    #     print(f"{firstNumber} * {secondNumber} = 555")
    # elif firstNumber == 56 and operator == "+" and secondNumber == 9:
    #     print(f"{firstNumber} + {secondNumber} = 77")
    # elif firstNumber == 56 and operator == "/" and secondNumber == 6:
    #     print(f"{firstNumber} / {secondNumber} = 4")
    # while True:

    if operator == "+":
        print(f"{firstNumber} + {secondNumber} = {firstNumber + secondNumber}")
    elif operator == "-":
        print(f"{firstNumber} - {secondNumber} = {firstNumber - secondNumber}")
    elif operator == "*":
        print(f"{firstNumber} * {secondNumber} = {firstNumber * secondNumber}")
    elif operator == "/":
        print(f"{firstNumber} / {secondNumber} = {firstNumber / secondNumber}")
    else:
        print("\n\033[91mError, invalid input!")
    again()


def again():
    yN = input("\n\u001b[33mCalculate again y/n: ")
    if yN == "y":
        cal()
    elif yN == "n":
        print("\n\u001b[34mSee you later!\u001b[0m")
    else:
        again()


cal()
