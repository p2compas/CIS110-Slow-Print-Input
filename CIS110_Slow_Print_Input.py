# Define two functions:
# One to print one character at a time, preferrably by using formatted strings as input
# The other to display input prompts slowly and return the result from input('')

# Function prototypes:
# void slowPrint(f-string s)
# str slowInput(f-string s)

# Import dependencies
from time import sleep

# Time to wait between characters
delay = 0.075

def slowPrint(s):
    string = s
    for char in s:
        print(char, end="")
        sleep(delay)
    print()

def slowInput(s):
    string = s
    for char in s:
        print(char, end="")
        sleep(delay)
    return input()

catName = slowInput("What is the name of the best cat ever?  ")
slowPrint(f"Hello world, {catName} is the best cat!")