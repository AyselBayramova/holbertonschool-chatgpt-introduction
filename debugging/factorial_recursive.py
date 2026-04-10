#!/usr/bin/python3
import sys

# Increase the recursion limit for large inputs
sys.setrecursionlimit(2000)

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            number = int(sys.argv[1])
            result = factorial(number)
            print(result)
        except ValueError:
            print("Please enter a valid integer.")
