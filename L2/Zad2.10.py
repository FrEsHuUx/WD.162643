try:
    a = int(input("Enter a number: "))
    print("Your number:", a)
except ValueError:
    print("Please input a number, not a symbol")