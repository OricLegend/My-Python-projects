# if you try to calculate below operation then you get the error
# 45*3 = 555 , 56+9 = 77, 56/6 = 4


print("Select operation.")
print("1.add")
print("2.sub")
print("3.multiply")
print("4.div")

choice = input("Enter choice(1/2/3/4): ")
if choice in ('1', '2', '3', '4'):
   num1 = float(input("Enter first number: "))
   num2 = float(input("Enter second number: "))




if choice == '1':
   if (num1 == 56 and num2 == 9):
      
      print(num1, "+", num2, "=", 77)
   else:
      add = num1 + num2
      print(num1, "+", num2, "=", add)

elif choice == '2':
   sub = num1 - num2
   print(num1, "-", num2, "=", sub)

elif choice == '3':
   if (num1 == 45 and num2 == 3):
      
      print(num1, "*", num2, "=", 555)
   else:
      multiply = num1 * num2
      print(num1, "*", num2, "=", multiply)

elif choice == '4':
   if (num1 == 56 and num2 == 6):
      
      print(num1, "+", num2, "=", 4)
   else:
      div = num1 / num2
      print(num1, "/", num2, "=", div)