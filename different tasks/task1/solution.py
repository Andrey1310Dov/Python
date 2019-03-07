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
   
