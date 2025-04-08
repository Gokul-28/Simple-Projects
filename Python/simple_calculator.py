# Simple Calculator 

operator = str(input("Enter the operator that is going to be used (+,-,*,/) : "))
number_1 = float(input("Enter the first value: "))
number_2 = float(input("Enter the second value: "))

if operator == "+":
    answer = number_1 + number_2
    print(f"The addiction of two values is {answer}")
    print('Calculation is done')
elif operator == '-':
    answer = number_2 -  number_1
    print(f"The subtraction of two values is {answer}")
    print('Calculation is done')
elif operator == "*":
    answer = number_1 * number_2
    print(f"The multiplication of two values is {answer}")
    print('Calculation is done')
elif operator == '/':
    answer = number_1 / number_2
    print(f"The division of two values is {answer}")
    print('Calculation is done')
else :
    print("You have entered a wrong number or made an error in the operator. Try again")

