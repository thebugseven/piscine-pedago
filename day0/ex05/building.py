import sys


def main():
    """This program counts the number of characters in a string, and
    categorizes them as upper case letters, lower case letters,
    punctuation marks, spaces, and digits. The string can be provided
    as a command-line argument or entered by the user when prompted."""
    if len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided")

    if len(sys.argv) == 1:
        print("What is the text to count?")
        x = sys.stdin.read()
    else:
        x = str(sys.argv[1])

    nbrUpper = sum(1 for c in x if c.isupper())
    nbrLower = sum(1 for c in x if c.islower())
    nbrPunct = sum(1 for c in x if not c.isalnum() and not c.isspace())
    nbrSpace = sum(1 for c in x if c.isspace())
    nbrDigit = sum(1 for c in x if c.isdigit())

    print(f"The text contains {len(x)} characters:")
    print(f"{nbrUpper} upper letters")
    print(f"{nbrLower} lower letters")
    print(f"{nbrPunct} punctuation marks")
    print(f"{nbrSpace} spaces")
    print(f"{nbrDigit} digits")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
