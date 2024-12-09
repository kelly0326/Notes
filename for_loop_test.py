# see python_nested_.ipynb


import time
from pprint import pprint

def clock():
	for minute in range(60):
		for second in range(60):
			print(f"{str(minute).zfill(2)}: {str(second).zfill(2)}")
			time.sleep(1)
# clock()


single_list = [1,2,3,3,5]
count = 0
for num in single_list:
	if num == 3:
		count = count + 1
# print(count)


# How many 3 in nested_list?
nested_list = [[5, 1, 2, 4, 1, 2, 5, 5, 2, 2, 3, 4, 1, 3, 5, 5, 5, 3, 4, 5], [5, 3, 2, 4, 5, 1, 3, 2, 1, 2, 3, 2, 2, 1, 1, 1, 5, 5, 1, 1], [1, 5, 3, 1, 3, 5, 1, 3, 2, 1, 4, 5, 3, 3, 1, 5, 1, 2, 2, 5], [2, 5, 2, 5, 1, 2, 1, 3, 3, 5, 1, 4, 5, 3, 1, 1, 5, 3, 3, 3], [3, 1, 3, 2, 4, 5, 2, 1, 4, 1, 5, 1, 4, 3, 1, 4, 4, 5, 1, 3], [5, 4, 4, 5, 3, 2, 4, 2, 3, 5, 5, 2, 4, 5, 5, 1, 3, 1, 3, 2], [1, 1, 5, 2, 4, 2, 3, 1, 1, 4, 5, 2, 2, 5, 1, 5, 3, 4, 4, 2], [5, 2, 1, 4, 1, 4, 2, 2, 1, 4, 5, 5, 1, 1, 3, 3, 5, 3, 5, 2], [2, 5, 2, 5, 4, 4, 4, 1, 3, 5, 2, 1, 3, 5, 3, 2, 1, 5, 2, 1], [2, 1, 2, 1, 1, 3, 5, 2, 3, 4, 3, 5, 5, 4, 4, 4, 2, 2, 3, 2], [2, 5, 5, 4, 1, 2, 5, 1, 5, 5, 5, 3, 1, 4, 1, 4, 1, 4, 2, 2], [3, 2, 4, 2, 4, 5, 5, 4, 2, 2, 1, 1, 1, 4, 4, 4, 5, 2, 1, 1], [2, 5, 3, 5, 1, 1, 5, 3, 4, 4, 1, 5, 1, 4, 5, 4, 4, 2, 4, 1], [2, 3, 4, 2, 1, 1, 5, 2, 1, 5, 3, 3, 5, 3, 2, 3, 1, 1, 2, 2], [3, 1, 3, 3, 1, 5, 5, 4, 1, 5, 1, 1, 2, 2, 1, 1, 2, 4, 4, 1]]
# pprint(nested_list)

counter = []
for inner in nested_list: # take out every list inside the nested_list
	count = 0
	for number in inner: # take out 3 from every list
		if number == 3:
			count = count + 1
	counter.append(count)
# print(counter)


# 12/8/2024
my_nested_list = [
                    [1,2,3],
                    [2,2,3],
                    [3,3,1]
                                ]
# pprint(my_nested_list)

# how many 3 in my_nested_list?

counter = []
for inner in my_nested_list:
	sum = 0
	for number in inner:
		if number == 3:
			sum = sum + 1
	counter.append(sum)
# print(counter)


# total amount of 3

sum = 0
for inner in my_nested_list:
	for number in inner:
		if number == 3:
			sum = sum + 1
# print(sum)



# nested_list

pprint(nested_list)

