def even_odd(num):
    if num % 2 == 0:
        return (f"{num} is a even number")
    else:
        return (f"{num} is a odd number")


num = int(input("enter a number to check even or odd : "))

print(even_odd(num))