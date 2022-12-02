#!/usr/bin/env python3.7 
# EC2 Random Name Generator 
import random

name = input("What are your first initial and full last name? ")
department = input("What is the name of your department? ")
ec2_total = int(input("How many EC2 instances would you like to create names for? "))
for _ in range(1, ec2_total + 1):
    rand = str(random.randrange(1000,2000))
    randomUpperLetter = chr(random.randint(ord('A'), ord('Z')))
    randname = name+department+randomUpperLetter+rand
    print(randname)
