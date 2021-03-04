from math import *
a = input(u"Wprowadź pierwszą liczbę ")
a = int(a)
operator = input(u"Wprowadź operator działania (+, -, , *, /, //, %)")

b = input(u"Wprowadź drugą liczbę ")
b = int(b)
if operator == '+':
    print(a + b)
elif operator == '-':
    print(a - b)
elif operator == '*':
    print(a * b)
elif operator == '*':
    print(a * b)
elif operator == '**':
    print(a ** b)
elif operator == '/':
    print(a / b)
elif operator == '//':
    print(a // b)
elif operator == '%':
    print(a % b)
else:
    print(u"Błędny operator")
