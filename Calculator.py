oparetor = input("Enter What Do You Want (+-*/):")
num1 = float(input("Enter The Number:"))
num2 = float(input("Enter The secound number:"))

if oparetor == "+" :
    results = num1 + num2
    print(round(results, 3))
elif oparetor == "-":
    results = num1 - num2
    print(round(results, 3))
elif oparetor == "*":
    results = num1 * num2
    print(round(results, 3))
elif oparetor == "-":
    results = num1 / num2
else:
    print("Please a Valid Number")