from time import sleep

# Print one character at a time, with objects separated by sep
# Each line ending with end, and delay seconds between characters.
def slowPrint(*objects: object, sep: str | None = ' ', end: str | None = '\n', delay: float | int = 0.05) -> None:
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
def slowInput(prompt: str | object = '', delay: float | int = 0.05) -> str:
    for char in str(prompt):
        print(char, end="")
        sleep(delay)
    return input()

# If ran as script, show examples
if __name__ == '__main__':
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