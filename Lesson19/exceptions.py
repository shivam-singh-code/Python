class JustNotCoolError(Exception):
    pass

x = 2
try:
    raise JustNotCoolError("Not cool man")
    # raise Exception("Custom exception")
    # print(x/0)
    # if not type(x) is str:
    #     raise TypeError("only String are allowed")
except NameError:
    print(f'Name erro something is undefined')
except ZeroDivisionError:
    print("Please do not divide by 0")
except Exception as error:
    print(error)
else:
    print("No error")
finally:
    print("I AM going to print with or without an error")