# Example for factorial.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
   
# check print(factorial(5))
