#basic calculator program
name= input("Whats your name?? :")
print("Hello", name ,"welcome to the Basic Calculator")

#asking the user for the input
num1=float(input("Enter your first number :"))
operator=input("Enter your Ooerator (either +,-,* or /) :")
num2=float(input("Enter your Second number :"))

#the calculator operation
if operator == "+":
    result= num1 +num2
    print(f"{num1}+{num2}= {result}")
elif operator == "-":
    result= num1-num2
    print(f"{num1}-{num2}= {result}")
elif operator== "*":
    result= num1 * num2
    print(f"{num1}* {num2}= {result}")
elif operator == "/":
    if num2 != 0:
        result= num1 / num2
        print(f"{num1} / {num2} = {result}")
else:
    print("INVALID OPERATOR!!! Please input one of the operators providedkk:")
