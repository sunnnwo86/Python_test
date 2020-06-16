# thing = None
# if thing:
#     print("It's some thing")
# else:
#     print("It's no thing")

# thing = None
# if thing is None:
#     print("It's no thing")
# else:
#     print("It's some thing")

def is_none(thing):
    if thing is None:
        print("It's None")
    elif thing:
        print("It's True")
    else:
        print("It's Flase")

is_none(None)
print()
