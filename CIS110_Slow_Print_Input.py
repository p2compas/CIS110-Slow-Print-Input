from time import sleep

# Print one character at a time, with objects separated by sep
# Each line ending with end, and delay seconds between characters.
def slowPrint(*objects: object, sep: str | None = ' ', end: str | None = '\n', delay: float | int = 0.05):
    s, e, first = sep, end, True
    for obj in objects:
        print(f"{s if not first else ''}", end='')
        for char in str(obj):
            print(char, end='')
            sleep(delay)
        first = False
    print(end=e)

# Display prompt one character at a time with delay seconds between characters.
# Return str from input()
def slowInput(prompt: str | object = '', delay: float | int = 0.05):
    for char in str(prompt):
        print(char, end="")
        sleep(delay)
    return input()

if __name__ == '__main__':
    # print lists example
    lst = ['one', 'two', 'three', 'four']
    slowPrint(lst)
    # print objects example
    slowPrint(slowPrint)
    slowPrint(slowInput)
    # slowInput example
    name = slowInput("\nThis is a slow input prompt, What\'s your name?  ")
    num = slowInput(f"Hello, {name}! What\'s your favorite number?  ")
    # showPrint example
    slowPrint(f"Your name is {name} and your favorite number is {num}.")
    slowPrint("Your name is", name, "and your favorite number is", num, end=1)