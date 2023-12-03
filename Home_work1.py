######################################################################################
# Task 1 - create a list  with number and print sum of all his elements
list_of_numbers = [6, 45, 6, 3, 1]
sum_of_all = 0
for element in list_of_numbers:
    sum_of_all = sum_of_all + element
print("Task #1. Sum of all elements:", sum_of_all)

######################################################################################
# Task 2 - create a list with duplicate number and print sum of all Unique elements
elList = [7, 1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 8, 9, 9]

uniqueList = []
duplicateList = []
sum_of_unique = 0

for element in elList:
    if element not in uniqueList:
        uniqueList.append(element)
        sum_of_unique = sum_of_unique + element
    elif element not in duplicateList:
        duplicateList.append(element)
print("Task #2. Sum of all Unique elements:", sum_of_unique)

######################################################################################
# Task 3 - create dictionary with initial salary and change initial value to 1,5%
my_dict = { 'employeeID': 101,'position': 'copywriter','salary': 400}
# Key and percentage you want to apply
key_to_update = 'salary'
percentage = 1.5  # 1.5% from initial (you can change this to your desired percentage)

# 1. Access the initial value
initial_value = my_dict['salary']

# 2. Calculate the new value by taking a percentage of the initial value
new_value = initial_value * percentage / 100

# 3. Update the dictionary with the new value
my_dict['salary'] = new_value

# Print the updated dictionary
print("Task #3. Dictionary with updated salary:", my_dict)
