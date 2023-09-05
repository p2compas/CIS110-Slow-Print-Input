# Define two functions:
# One to print one character at a time, using arbitrary arguments like the builtin print
# The other to display input prompts slowly and return the result from input('')

# Function prototypes:
# void slowPrint(*objects: object, sep: str | None = ' ', end: str | None = '\n')
# str slowInput(prompt: str | object)

# Import dependencies
from time import sleep

# Time to wait between characters
delay = 0.025

def slowPrint(*objects, sep=' ', end='\n'):
    if not type(sep) in [str, None]:
        raise TypeError(f'sep must be None or a string, not {type(sep).__name__}')
    if not type(end) in [str, None]:
        raise TypeError(f'end must be None or a string, not {type(end).__name__}')
    s, e, first = sep, end, True
    for obj in objects:
        print(f"{s if not first else ''}", end='')
        for char in str(obj):
            print(char, end='')
            sleep(delay)
        first = False
    print(end=e)

def slowInput(prompt):
    for char in str(prompt):
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
slowPrint("Your name is", name, "and your favorite number is", num, end=".\n")