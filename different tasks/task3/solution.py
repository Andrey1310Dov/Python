def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
def get_zeros(n):
    num = str(factorial(n))
    zeros = 0
    for i in num[::-1]:
        if int(i) == 0:
            zeros += 1
        else:
            break
    return zeros
        
print(get_zeros(1))
print(get_zeros(5))
print(get_zeros(12))
print(get_zeros(56))
print(get_zeros(15))
print(get_zeros(27))
print(get_zeros(75))


# Сложность O(n)
