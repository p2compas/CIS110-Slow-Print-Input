# Define two functions:
# One to print one character at a time, preferrably by using formatted strings as input
# The other to display input prompts slowly and return the result from input('')

# Function prototypes:
# void slowPrint(f-string s)
# str slowInput(f-string s)

# Import dependencies
from time import sleep

# Time to wait between characters
delay = 0.05

def slowPrint(s):
    for char in str(s):
        print(char, end="")
        sleep(delay)
    print()

def slowInput(s):
    for char in str(s):
        print(char, end="")
        sleep(delay)
    return input()

# print lists
lst = ['one', 'two', 'three', 'four']
slowPrint(lst)

# print objects
slowPrint(slowPrint)
slowPrint(slowInput)

# input
name = slowInput("\nThis is a slow input prompt, What\'s your name?  ")

num = slowInput(f"Hello, {name}! What\'s your favorite number?  ")

# output
slowPrint(f"Your name is {name} and your favorite number is {num}.")
