import sys

# check a right enter
if len(sys.argv) != 2:
    print('Usage: python caesar.py k')
    exit(1)
else:
    for num in sys.argv[1]:
        if not sys.argv[1].isalpha():
            print('Usage: python caesar.py k')
            exit(1)

# 2 arrays to find out indexes
alph_big = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alph_small = 'abcdefghijklmnopqrstuvwxyz'

# list of offsets
list_offsets = []
for letter in sys.argv[1]:
    if letter in alph_big:
        list_offsets.append(alph_big.index(letter))
    else:
        list_offsets.append(alph_small.index(letter))

# prepare an answer
print('plaintext: ', end='')
plaintext = input()
ciphertext = ''
index_ofsset = 0
check = len(list_offsets)

# the loop for creating of ciphertext
for letter in plaintext:
    if index_ofsset == check:
        index_ofsset = 0
    if letter.isalpha():
        if letter in alph_big:
            new_index = (alph_big.index(letter) + list_offsets[index_ofsset]) % 26
            index_ofsset += 1
            ciphertext += alph_big[new_index]
        else:
            new_index = (alph_small.index(letter) + list_offsets[index_ofsset]) % 26
            index_ofsset += 1
            ciphertext += alph_small[new_index]
    else:
        ciphertext += letter
# out our answer
print('ciphertext:', ciphertext)
