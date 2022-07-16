import string
import random


# characters to generate password from
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_random_password():
   # No of Password you want to generate
   # length of password from the user
    number_of_passwords = int(input("How many passwords do you want to generate? "))
    length = int(input("Enter password length: "))

   # shuffling the characters
    random.shuffle(characters)
   
   # picking random characters from the list
    for password_index in range(1,number_of_passwords+1):
       password = []
       for i in range(length):
          password.append(random.choice(characters))

   # shuffling the resultant password
       random.shuffle(password)

   # converting the list to string
       password = "".join(password)

   
   # printing the list
       print(f"Password {password_index} generated : {password}")



## invoking the function
generate_random_password()