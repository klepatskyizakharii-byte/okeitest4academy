try:
    print("Start")
    print(10/0)
    print("No errors")


except (NameError, ZeroDivisionError):
    print("we have an error")


print("code after capsule")
