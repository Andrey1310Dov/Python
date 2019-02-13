# Example for factorial.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Example for sum

def sum(ls):
    if len(ls) == 1:
        return ls[0]
    else:
        return ls[0] + sum(ls[1:])
 
# Count indexes in a list

def num_index(ls):
    if len(ls) == 1:
        return 1
    else:
        return 1 + num_index(ls[1:])
    
# Search a max index of a list

def max(ls):
    if len(ls) == 2:
        return ls[0] if ls[0] > ls[1] else ls[1]
    else:
        sub_ls = ls[1:]
        return ls[0] if ls[0] > max(sub_ls) else max(sub_ls)

    
# Algorithm QUICKSORT with recursion

def quicksort(ls):
    if len(ls) < 2:
        return ls
    else:
        basis = ls[0]
        less = [i for i in ls[1:] if i <= basis]
        more = [i for i in ls[1:] if i > basis]
        return quicksort(less) + [basis] + quicksort(more)
