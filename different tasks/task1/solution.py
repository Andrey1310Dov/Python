from itertools import product

def search_pairs(array, k):
    out = set()
    check = set()
    for i, j in product(array, array):
        if i + j == k and i not in check and j not in check:
            out.add((i, j))
            check.add(i)
            check.add(j)
    return list(out)
   
print(search_pairs([1, 2, 6, 5, 3, 4, 7, 8, 3, 2], 5))

# Сложность алгоритма O(n^2)

def search_pairs(array, k):
    check_second_digit = set(array)
    check_pairs = set()
    out = []
    for i in array:
        j = k - i
        if j in check_second_digit:
            if j not in check_pairs:
                out.append((i, j))
                check_pairs.add(i)
                check_pairs.add(j)
    return list(out)
   
print(search_pairs([1, 2, 6, 5, 3, 4, 7, 8, 3, 2, 8, 3, 4, 7, 5, 2, 7, 8, 0], 6))
print(search_pairs([1, 2, 6, 5, 3, 4, 7, 8, 3, 2], 5))
print(search_pairs([1, 2, 6, 5, 3, 4, 7, 8, 3, 2, 8, 3, 4, 7, 5, 2, 7, 8, 0], 3))
print(search_pairs([4, 4, 4, 2, 4, 2, 6, 7, 6, 2], 8))

# Сложность алгоритма O(n)
   
