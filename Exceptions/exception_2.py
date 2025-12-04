  # Add error handling to the functions below. When an error occurs, return the error type.

# def divide(a, b):
#     return a / b

# divide(5, 0)
# divide(5, "0")

# def getValue(list_or_map, index_or_key):
#     return list_or_map[index_or_key]

# getValue([1, 2, 3], 5)
# getValue({"a": 1, "b": 2}, "c")


def divide(a, b):
    try:
        return a / b
    except Exception as e:
        return type(e)._name_


def getValue(list_or_map, index_or_key):
    try:
        return list_or_map[index_or_key]
    except Exception as e:
        return type(e)._name_