# Notes
import time
lst = [2,2,2,3,3,3,3,7]
len(lst)
# 8

count = 0
for num in lst:
	count = count + 1
print(count)
# 8


lst = [2,2,2,3,3,3,3,7]
odd_count = 0
even_count = 0
for num in lst:
    if num % 2 == 1:
        odd_count = odd_count + 1
    else:
        even_count = even_count + 1
print(odd_count)
print(even_count)
# 5
# 3

count = 0
for num in lst:
    time.sleep(1)
    count += 1
    print(f"{num=}, {count=}")
    print(count)