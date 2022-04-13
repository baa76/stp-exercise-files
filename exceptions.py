a = input("Type a number")
b = input("Type another number")
a = float(a)
b = float(b)
try:
    print(a/b)
except ZeroDivisionError:
    print("Input cannot be zero. Try again.")