scrolls = []
date_every = ''
numbers = '1234567890'
x = '-'

string_with_dates = "entriesareduebyJan1452-25-16uary4440-15-254th201at8:00pmreated2005-10-15byACMEInc.andassoci1425-12-15ates"
for i in string_with_dates:
    if i in numbers or i == x:
        date_every += i
    else:
        date_every = ''
    if len(date_every) == 10 and date_every[4] == date_every[7] == x \
    and date_every[0] in numbers and date_every[1] in numbers and date_every[2] in numbers \
    and date_every[3] in numbers and date_every[5] in numbers and date_every[6] in numbers \
    and date_every[8] in numbers and date_every[9] in numbers:
            scrolls.append(date_every)
            date_every = ''
print(scrolls)
