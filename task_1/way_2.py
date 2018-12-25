#подход тот же, что и в way_1 но импользуем срезы. 
string_with_dates = "e1452-25-16ntriesareduebyJan1452-25-16uary4440-15-254th201at8:00pmreated2005-10-15byACMEInc.andassoci1425-12-15ates2345-14-12"
scrolls = []
n = 0
n_2 = 9
numbers = '1234567890'
x = '-'

for i in string_with_dates:
    i = string_with_dates[n:n_2 + 1]
    if i[4] == i[7] == x and i[0] in numbers and i[1] in numbers and i[2] in numbers \
    and i[3] in numbers and i[5] in numbers and i[6] in numbers and i[8] in numbers and i[9] in numbers:
        scrolls.append(i)
    n += 1
    n_2 += 1
    if n_2 == len(string_with_dates):
	      break
print(scrolls)
