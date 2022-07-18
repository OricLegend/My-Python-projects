print("select any one operator for operation : + , - , * , /")

operators = input("enter operator : ")

num1 = input("enter 1st no : ")

num2 = input("enter 2nd no : ")



num1 = num1.strip()
num2 = num2.strip()
num1 = int(num1)
num2 = int(num2)
operators = operators.strip()



if operators == "+":
   print("Ans is", num1+num2)

elif operators == "-":
   print("Ans is", num1-num2)

elif operators == "*":
   print("Ans is", num1*num2)

elif operators == "/":
   print("Ans is", num1/num2)

else:
   print("Syntex Error : Please select correct operators")