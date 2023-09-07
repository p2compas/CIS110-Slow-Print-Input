#! /usr/bin/env python3

"""Methods for printing and gathering input with a delay between each character printed."""

from time import sleep
import sys

__all__ = ['slowPrint', 'slowInput']

def slowPrint(*objects: object, sep: str | None = ' ', end: str | None = '\n', delay: float | int = 0.03) -> None:
    """Print objects to the screen with a delay between characters.

    Usage is similar to the builtin print(), with the omission of file writing.

    Argument objects are the objects which string representation
    will be printed to the screen, with a delay between characters.

    Optional sep is a string which is inserted between objects, 
    defaulting to a single space character.

    Optional end is the string to be printed at the end, after all
    objects have been printed, defaulting to the newline character.

    Optional delay is a float or int specifying the delay, in seconds,
    between printing each character of output, defaulting to 0.03.

    The result is None.
    """
    s, e, first = sep, end, True
    for obj in objects:
        print(f"{s if not first else ''}", end='')
        for char in str(obj):
            print(char, end='', flush=True)
            sleep(delay)
        first = False
    print(end=e)
    return

def slowInput(prompt: str | object = '', delay: float | int = 0.03) -> str:
    """Display prompt one character at at time with delay before gathering input.

    Argument prompt is a string or object to display to the user before calling input()

    Optional delay is a float or int specifying the delay, in seconds,
    between printing each character of prompt, defaulting to 0.03

    The result is returned as a string.
    """
    for char in str(prompt):
        print(char, end='', flush=True)
        sleep(delay)
    return input()

def example() -> None:
    # print lists
    lst = ['one', 'two', 'three', 'four']
    slowPrint(lst)
    # print objects
    slowPrint(slowPrint)
    # slowInput
    name = slowInput("\nThis is a slow input prompt, What\'s your name?  ")
    num = slowInput(f"Hello, {name}! What\'s your favorite number?  ")
    # slowPrint f-string
    slowPrint(f"Your name is {name} and your favorite number is {num}.")
    # slowPrint objects
    slowPrint("Your name is", name, "and your favorite number is", num, end=".\n")
    return

if __name__ == '__main__':
    usage = """Usage: %s [message] [delay]
        message: print message with a delay between characters
        delay: delay, in seconds, between printing each character of message"""%sys.argv[0]
    match len(sys.argv):
        # Run example if no arguments specified
        case 1: example()
        # slowPrint message at default speed
        case 2: slowPrint(sys.argv[1])
        # slowPrint message at with specified delay
        case 3:
            try:
                d = float(sys.argv[2])
                slowPrint(sys.argv[1], delay=d)
            except:
                print('The delay parameter must be of type float or int.', usage, sep="\n\n")
                sys.exit(1)
        case _: print(usage)
