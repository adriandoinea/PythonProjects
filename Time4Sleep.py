"""This is a program that shuts down the PC after a certain time that is
set by the user."""

import os
import time

print("The pc will shut down in:")
h=int(input("Hours: "))
m=int(input("Minutes: "))
s=int(input("Seconds: "))

run=input("Press ENTER to start ")
while run=="":
    s = s - 1
    if s < 0:
        s = 59
        m = m- 1
    if m < 0:
        m = 59
        h = h - 1

    os.system("cls")

    print("The system will shut down. Time remaining: ",h,":",m,":",s)

    time.sleep(1)
    if h==0 and m==0 and s==0:
        os.system("shutdown /s /t 1")
        break