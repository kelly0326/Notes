'''
Author: Shu Liu
Date: 2024/12/20
Version: 1.0.0
License: MIT
'''

# read the raw data
def read_data(path):
  file = open(path)
  data = file.read()
  # print("data type:", type(data)) # string
  # print(repr(data)) # string (raw data)

  # convert data (string) to data1 (list)
  data1 = data.split("\n")
  # print(data1)
  # print("data1 type:", type(data1)) # list

  # convert data1 (list) to a nested list: data2.
  data2 = []
  for temp in data1:
    temp = temp.split(",")
    data2.append(temp)
  # print(type(data2)) # list
  # print("data2", data2) # nested list: data2 (inside the list: strings)
  # print("data2 length:", len(data2)) # 6
  return data2





# get all the columns from data2 to see the type of the lst 
# (lst is now a list with string elements)
def get_column(data, column_number):
    list_string = []
    for row in data:
      list_string.append(row[column_number])
    return list_string



# convert the column (my_column) to float
def float_column(my_column):
  count = []
  for number in range(len(my_column)):
    if number != 0:
      my_column[number] = float(my_column[number])
      count.append(my_column[number])
  # print("in line 51", count)
  return count


# get the largest number from each float_column
def largest(my_float_column):
    largest = max(my_float_column)
    # print("largest=", largest)
    return largest

# get the smallest number from each float_column
def smallest(my_float_column):
  smallest = min(my_float_column)
  # print("smallest=", smallest)
  return smallest





# write a new file with largest number from each col. as the last row
def write_file(data, smallest, largest):
  # large_num_list = ["largest="]
  # for i in range(1, 6):
  #   temp = get_column(data, i)
  #   temp = float_column(temp)
  #   get_largest = largest(temp)
  #   large_num_list.append(str(get_largest))
  # data.append(large_num_list)
  # print(data) # the largest number list added to data2
 # for row in data:
  #  print(row)

  file = open("my_new_amd.csv", "w") # establish a new file
  for row in data:
    file.write(",".join(row))
    file.write("\n")
  file.write(",".join(smallest))
  file.write("\n")
  file.write(",".join(largest))
  file.write("\n")

def get_smallest_and_largest(data2):
  largest_list = []
  smallest_list = []
  for i in range(1, 6):
    list_string = get_column(data2, i)
    print(list_string)
    my_float_column = float_column(list_string)
    print(my_float_column)
    get_largest = largest(my_float_column)
    get_smallest = smallest(my_float_column)
    largest_list.append(get_largest)
    smallest_list.append(get_smallest)
  print("largest", largest_list)
  print("smallest", smallest_list)
  smallest_final = ["smallest="]
  largest_final = ["largest="]
  for number in smallest_list:
    smallest_final.append(str(number))
  for number in largest_list:
    largest_final.append(str(number))
  print("small final", smallest_final)
  print("large final", largest_final)
  return smallest_final, largest_final




def main():
  # call read_data() to return data2 (a nested list)
  data2 = read_data("amd.csv")


  smallest_final, largest_final = get_smallest_and_largest(data2)

  # write the max number and add it to a new file
  write_file(data2, smallest_final, largest_final)
  


main()

  # get each column (with strings inside) from data2
  # list_string1 = get_column(data2, 1)
  # print("line 96", list_string1)
  # list_string2 = get_column(data2, 2)
  # print(list_string2)
  # list_string3 = get_column(data2, 3)
  # print(list_string3)
  # list_string4 = get_column(data2, 4)
  # print(list_string4)
  # list_string5 = get_column(data2, 5)
  # print(list_string5)


  # convert data2 type from string to float

  # my_float_column1 = float_column(list_string1)
  # my_float_column2 = float_column(list_string2)
  # my_float_column3 = float_column(list_string3)
  # my_float_column4 = float_column(list_string4)
  # my_float_column5 = float_column(list_string5)



  # get largest number from each column
  # get_largest = largest(my_float_column1)
  # get_largest = largest(my_float_column2)
  # get_largest = largest(my_float_column3)
  # get_largest = largest(my_float_column4)
  # get_largest = largest(my_float_column5)


  # # get smallest number from each column
  # get_smallest = smallest(my_float_column1)
  # get_smallest = smallest(my_float_column2)
  # get_smallest = smallest(my_float_column3)
  # get_smallest = smallest(my_float_column4)
  # get_smallest = smallest(my_float_column5)