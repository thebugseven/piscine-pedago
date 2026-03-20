def all_thing_is_obj(object: any) -> int:
    if type(object) is list:
        print(f"{type(object).__name__}: {str(type(object))}")
    elif type(object) is tuple:
        print(f"{type(object).__name__}: {str(type(object))}")
    elif type(object) is set:
        print(f"{type(object).__name__}: {str(type(object))}")
    elif type(object) is dict:
        print(f"{type(object).__name__}: {str(type(object))}")
    elif type(object) is str:
        print(f"{object} is in the kitchen : {str(type(object))}")
    else:
        print("Type not found")
    return 42
