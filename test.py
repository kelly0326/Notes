def get_average(lst):
	total = sum(lst)
	average = total / len(lst)
	return average

# test case passed
#get_average([1,1,1])
#get_average([1,2,3])



def scope(lst):
	"""
		Calculate the distance between largest and smallest.
	"""
	largest = max(lst)
	smallest = min(lst)
	return largest - smallest

# test case passed
#scope([1,2,3])
#scope([-9, 0, 3])


# def compare(lst):
# 	"""
# 		compare the scope and average
# 	"""
# 	difference = scope(lst) - get_average(lst)
# 	#print("scope", scope(lst))
# 	#print("avg", get_average(lst))
# 	return difference

# test case passed
#compare([1,2,3])
#compare([-9, 0, -3])

def compare(lst):
	# lst = [1,2,3]
	my_average = get_average(lst)
	my_scope = scope(lst)
	#print(my_average)
	#print(my_scope)
	# if my_average > my_scope:
	# 	print("average is bigger.")
	# else:
	# 	print("scope is bigger.")
	difference = my_average - my_scope
	return difference


def main():
	difference = compare([8,8,9])
	if difference > 0:
		print("average is bigger.")
	else:
		print("scope is bigger.")


main()