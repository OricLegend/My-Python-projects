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
   add = num1 + num2
   print(num1, "+", num2, "=", add)

elif choice == '2':
   sub = num1 - num2
   print(num1, "-", num2, "=", sub)

elif choice == '3':
    multiply = num1 * num2
    print(num1, "*", num2, "=", multiply)

elif choice == '4':
	div = num1 / num2
	print(num1, "/", num2, "=", div)