# def what_returns():
#     try:
#         return "from try"
#     finally:
#         return "from finally"
# print(what_returns())


def read_number(text):
    try:
        value = int(text)
    except ValueError:
        print("Not a valid integer")
        return None
    else:
        print(f"Successfully parsed: {value}")
        return value
read_number("42")
read_number("abc")