import math


def NULL_not_found(obj: any) -> int:
    if obj is None:
        print(f"Nothing: {obj} {type(obj)}")
        return 0

    if isinstance(obj, float) and math.isnan(obj):
        print(f"Cheese: {obj} {type(obj)}")
        return 0

    if isinstance(obj, bool) and obj is False:
        print(f"Fake: {obj} {type(obj)}")
        return 0

    if isinstance(obj, int) and obj == 0:
        print(f"Zero: {obj} {type(obj)}")
        return 0

    if isinstance(obj, str) and obj == "":
        print(f"Empty: {type(obj)}")
        return 0

    print("Type not Found")
    return 1
