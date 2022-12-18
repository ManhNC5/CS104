# we are going to generate a random password using python
import random

alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbols = "!@#&*?/()\~[]+=_-%£$"

generated_password = alphabets + number + symbols 
length_for_password = 18

password = "".join(random.sample(generated_password, length_for_password))

print(f"\nYour generated password is: {password}")