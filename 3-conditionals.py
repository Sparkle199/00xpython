#!/usr/bin/python3
score = int(input("enter your score: "))
if score >= 70:
    print("Distinction")
elif score >= 50:
    print("Merit")
elif score >= 40:
    print("Pass")
else:
    print("fail")
