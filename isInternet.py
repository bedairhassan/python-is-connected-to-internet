import subprocess, colorama

from colorama import Fore,Back,Style
colorama.init(autoreset=True)

def isReplyInLine(array):

    for string in array:
        index = string.find('Reply')

        if index != -1:
            return True

    return False

def commandToArray(command):
    command = command.split(' ')

    output = subprocess.run(command, capture_output=True)
    output = output.stdout
    output = output.decode("utf-8") 
    output = output.split('\r\n')

    return output

def standby():
    enter = input('')

def printGREEN(string):
    print(f"{Fore.GREEN}{string}")

def printRED(string):
    print(f"{Fore.RED}{string}")

def conditionalDisplay(booleanCondition):
    if booleanCondition == True:
        printGREEN('Connected to Internet')
        return

    printRED('Not Connected To Internet Yet')

def main():

    command = "ping youtube.com"
    array = commandToArray(command)
    condition = isReplyInLine(array)
    conditionalDisplay(condition)

    standby()

main()