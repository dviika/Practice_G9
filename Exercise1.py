#numbers
# random_list = [1,2,3,4,5,6]
# result = sum(random_list)
# print(result)
#
# # strings
# random_list_of_strings = ["Artem", "Dmytro", "Sveta"]
# result1 = ' '.join(random_list_of_strings)
# print(result1)
#
# for name in random_list_of_strings:
#     print(name)
#
# mixed_elements = ["Artem", 1, 2, 3]  #sum works only for int / join for string
#
# result_for_mixed_elements = ''
# for name in mixed_elements:
#     result_for_mixed_elements += str(element) #making it str
#
# print(result_for_mixed_elements)
#
# for sym in 'Artem':
#     print(sym)

#dictionaly pair key and value
human = {
    'first_name': 'Sasha',
    'second_name': 'Malina',
    'age': 35,
    'salary': 1000
}


print(human['first_name']) #straight acess
human['salary'] = 1500
print(human['salary'])

human['salary'] = human['salary'] * 1.5
# #human['salary'] *= 1.5
# print(human['salary'])
#
# print(human.keys())
# print(human.values())
#
# keys = ['one', [213],'three']
# keys = ['one', 'two','three']
# values = [1, 2, 3]
# result = dict(zip(keys, values))
# result = dict(zip(values, keys)) #error [213] can't be a key

for pair in human.items():
    print(pair)

pairs = []
for pair in human.items():
    pairs.append(pair)
print(pair)

