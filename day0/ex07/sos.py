import sys


NESTED_MORSE = {
    'a': ".-",
    'b': "-...",
    'c': "-.-.",
    'd': "-..",
    'e': ".",
    'f': "..-.",
    'g': "--.",
    'h': "....",
    'i': "..",
    'j': ".---",
    'k': "-.-",
    'l': ".-..",
    'm': "--",
    'n': "-.",
    'o': "---",
    'p': ".--.",
    'q': "--.-",
    'r': ".-.",
    's': "...",
    't': "-",
    'u': "..-",
    'v': "...-",
    'w': ".--",
    'x': "-..-",
    'y': "-.--",
    'z': "--..",
    ' ': "/ ",
    '1': ".----",
    '2': "..---",
    '3': "...--",
    '4': "....-",
    '5': ".....",
    '6': "-....",
    '7': "--...",
    '8': "---..",
    '9': "----.",
    '0': "-----"
}


def main():
    try:
        assert len(sys.argv) == 2

        S = str(sys.argv[1])

        if not all(char.isalnum() or char.isspace() for char in S):
            raise AssertionError("the arguments are bad")

        result = [NESTED_MORSE[char] + " " for char in S.lower()]
        print("".join(result))
    except Exception:
        raise AssertionError("the arguments are bad")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
