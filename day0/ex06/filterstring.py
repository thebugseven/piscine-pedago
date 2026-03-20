import sys
from ft_filter import ft_filter


def main():
    """
    Return an iterator yielding those items\
    of iterable for which function(item)
    is true. If function is None, return the items that are true.
    """
    try:
        assert len(sys.argv) == 3

        S = str(sys.argv[1])
        N = int(sys.argv[2])

    except Exception:
        raise AssertionError("the arguments are bad")

    words = S.split(" ")
    result = [word for word in ft_filter(lambda x: len(x) > N, words)]
    print(result)


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
