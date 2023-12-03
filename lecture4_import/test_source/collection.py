#str is NOT changeble -> we are getting new str

#set is Changeble ( doesn't support index) -> all data is unique

string = "Retrospective"
print(string[2])

conver_string_to_set = set(string)
print(conver_string_to_set)

conver_string_to_set.add('A')
print(conver_string_to_set)
frozen_set = frozenset(conver_string_to_set)

cards = ['Валет', 'Король','Туз','Дата']
while cards:
    karta = cards.pop()
    print(karta)

print(list(range(6)))

slovo = 'velykeslovo'
result = [x for x in slovo]
result_upper = [x.upper() for x in slovo]
print(result)
print(result_upper)

#check all methods of the list
#[].

a = [1 , 2, 3]
b = [4, 5, 6]
a.extend(b)
print(a)
b.extend(a)
print(b)
b[4] = 100
print(b)
b.remove(3)
print(b)

#change value of the list el
list_change = list(range(8))
print(list_change)
list_ran = [7, 3, 8, 9, 2, 1 , 5, 1, 1]
target_index = list_ran.index(7)
print(target_index)
list_ran[target_index] = 4
print(list_ran)

print(list_ran.count(1))
print(list_ran.count(4))

random_list_from_list_ran = list_ran.copy()
print(random_list_from_list_ran)

carts = [0,001,01,5,6]
print(cars.sort())