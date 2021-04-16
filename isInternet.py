import subprocess


def searchForFind(string):
    return string.find('Reply')

def eachLineSearch(array):

    for string in array:
        index = searchForFind(string)

        if index != -1:
            return True

    return False

def commandToArray(command):
    process= subprocess.run(command.split(' '), capture_output=True)
    output = process.stdout
    output = output.decode("utf-8") 
    output = output.split('\r\n')

    return output

def standby():
    enter = input('')

def conditionalDisplay(booleanCondition):
    if booleanCondition == True:
        print('Connected to Internet')
        return

    print('Not Connected To Internet Yet')

def main():

    command = "ping youtube.com"
    array = commandToArray(command)
    condition = eachLineSearch(array)
    conditionalDisplay(condition)

    standby()

main()