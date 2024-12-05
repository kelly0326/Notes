def flag0():
	for i in range(13):
		print("|", end = "")
		for j in range(39):
			if i % 2 == 0:
				print("0", end = "")
			else:
				print("1", end = "")
		print("|", end = "")
		print()
# flag0()



def flag1():
	for i in range(13):
		print("|", end = "")
		for j in range(39):
			if i < 9 and j < 13:
				print("*", end = "")
			elif i % 2 == 0:
				print("0", end = "")
			else:
				print("1", end = "")
		print("|", end = "")
		print()
# flag1()


# mine
def flag2():
	for i in range(13):
		print("|", end = "")
		for j in range(39):
			if i < 9 and j < 12:
				if i % 2 == 0 and j % 2 == 0:
					print("*", end = "")
				elif i % 2 == 1 and j % 2 == 1 and j != 11: # means when j=11 it'll go to the next 'else'
					print("*", end = "")
				else:
					print(" ", end = "")
			else:
				if i % 2 == 0:
					print("0", end = "")
				else:
					print("1", end = "")
		print("|")
flag2()


# standard
def flag4():
	for i in range(13):
		print("|", end = "")
		for j in range(39):
			# this is * area
			if i < 9 and j < 12:
				# this is the even row
				if i % 2 == 0 and j % 2 == 0:
					print("*", end = "")
				# this is odd row determined by i
				elif i % 2 == 1 and j % 2 == 1 and j != 12:
					print("*", end = "")
				else: # this is all spaces
					print(" ", end = "")
			# this is stripe area
			else:
				if i % 2 == 0:
					print("0", end = "")
				else:
					print("1", end = "")
		print("|") # the row ending
# flag4()