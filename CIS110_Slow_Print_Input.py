# Define two functions:
# One to print one character at a time, preferrably by using formatted strings as input
# The other to display input prompts slowly and return the result from input('')

# Function prototypes:
# void slowPrint(f-string s)
# str slowInput(f-string s)

# Import dependencies
from time import sleep

def slowPrint(s):
    delay = 0.1
    string = s
    for char in s:
        print(char, end="")
        sleep(delay)
    print()

catName = 'Garfield'
slowPrint(f"Hello world, {catName} is the best cat!")