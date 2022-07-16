# name = input("enter your name : ")

# temp = " "

# for i in range(len(name)):
#     if name[i] not in temp:
#         print(f"{name[i]}:{name.count(name[i])}")

#         temp += name[i]



name = input("enter your name : ")

temp = " "

for i in name:
    if i not in temp:
        print(f"{i}:{name.count(i)}")

        temp += i
