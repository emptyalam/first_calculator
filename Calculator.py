import sys
import os

os.system("cls")
# is_windows = sys.platform.startswith('win')


G = '\033[92m'  # green
Y = '\033[93m'  # yellow
B = '\033[94m'  # blue
R = '\033[91m'  # red
W = '\033[0m'  # white


def banner():
    print("""%s
    
    |.\    /|.  /\.  |.   |.|````)./``/\. |````).
    |. \  / |. /__\. |====|.|---<.|  /  |.|---<. 
    |.  \/  |./    \.|.   |.|____).\/__/. |____).%s%s
    """ % (R, G, Y))
    return "\t\u001b[36m# Coded By Mahbob Alam !!!\u001b[0m\n"


print(banner())


def cal():
    print("\n\u001b[33mEnter First Number: ", end="")
    firstNumber = int(input())
    print("Enter Operator (e.g. + - * /): ", end="")
    operator = input()
    print("Enter Second Number: ", end="")
    secondNumber = int(input())


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
