try1 = input("enter +,-,*,/ ")
trynum1 = float(input("Enter the first NO:   "))
trynum2 = float(input("Enter the second NO:  "))


if try1 == "+":
    result = trynum1+trynum2
    print(result)
elif try1 == "-":
    result = trynum1-trynum2
    print(result)
elif try1 == "*":
    result = trynum1*trynum2
    print(result)
elif try1 == "/":
    result = trynum1/trynum2
    print(result)
else:
    print(f"{try1}")