"""It is a program that generates a password using letters, numbers and
symbols."""

import random
caract="abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*_"
leng=int(input("How many characters?\n"))
passw=""
if leng>=6:
    for i in range(leng):
        passw+=random.choice(caract)
    print(passw)
else:
    print("The password must be at least 6 characters long if you want a strong one!")