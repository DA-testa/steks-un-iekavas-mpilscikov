# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(next)

        if next in ")]}":
            last_opening = opening_brackets_stack.pop()
            if not are_matching(last_opening, next):
                return i + 1

    return -1
            


def main():
    
    text = input()

    # For GitHub tests
    if 'I' in text[0]:
        text = input()

    mismatch = find_mismatch(text)
    
    if mismatch == -1:
        print('Success')

    else:
        print(mismatch)


if __name__ == "__main__":
    main()
