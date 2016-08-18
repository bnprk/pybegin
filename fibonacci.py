#!/usr/bin/env python3 

num = int(input("Enter the number upto which you want to have the series: "))
print(" ")

def fibonacci():

    a, b = 0, 1

    while b < num:

        print(b, end = " ")

        a, b = b, a + b

fibonacci()
print('\n')


