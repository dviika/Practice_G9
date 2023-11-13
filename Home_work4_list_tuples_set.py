#Home_work list, dict, set

#Task 1
'''
List (список)
Preconditions:
    Створити список міст України, наприклад: Львів, Київ, Одеса, Дніпро, Суми
    Створити список з міст, які Ви вже колись відвідали, наприклад Київ, Львів
Завдання:
    Пройтись по списку відвіданих міст, вилучити поточне місто з першого списку,
    надрукувати його в консоль.
Очікуваний результат:
    В першому списку міст залишились тільки ті міста, які Ви ще не відвідали.
'''
list_of_the_cities = ['Kyiv', 'Dnirpo', 'Sumy','Ternopil','Lviv','Odesa','Kharkiv']
cities_visited = ['Kyiv','Lviv','Odesa','Kharkiv']

for index, city in enumerate(list_of_the_cities):
    #print(city,index) - added for visibility what is shown for index and for city
    if city in cities_visited:
        print(list_of_the_cities.pop(index))

print(list_of_the_cities)

#Task 2 -> Створити кортеж елементів, наприклад 3, 'one', 2.25
'''
Завдання:
    1. Вивести в консоль всі об'єкти кортежу циклом
    2. Спробувати змінити елемент кортежу в індексі 0 (очікуємо помилку)
    3. Знайти спосіб змінити кортеж так, щоб першим елементом стало число збільшене на 2
       (підказка: можна використати кастинг (приведення до певного типу))
'''
random_tuple = (3, 'one', 2.25, 'two', 1)
for item in random_tuple:
    print(item)
random_tuple[0] = 5 #will lead to an error tuple is IMMUTABLE
transform_to_list = list(random_tuple)
transform_to_list[0] += 2
transform_to_tuple = tuple(transform_to_list)

#Task 3 -> str Створити рядок удь-який рядок українською мовою, маленькими літерами, що міститиме кілька голосних літер
'''
Завдання:
    Використовуючи list comprehension та join відтворити цей рядок таким чином,
    щоб всі голосні літери стали великими
'''
slovo = 'протистояння'
vowels = "ІЕЇАОУИЄЯЮіеїаоуиєяю"
vowels_to_upper = [char.upper() if char in vowels else char for char in slovo]
result = ''.join(vowels_to_upper)
print(f"This is an outcome of joining: {result})


#Task 4 -> Set (Множина) Створити рядок удь-який рядок українською мовою, маленькими літерами, що міститиме кілька голосних літер
'''
Завдання:
    Перетворити цей список на множину, з заміною малих голосних літер на великі
'''
base = 'прийменник'
vowels = "ІЕЇАОУИЄЯЮіеїаоуиєяю"
base_to_set = set(base)
print(type(base_to_set),base_to_set)
new_list = []

for char in base:
    if char in vowels:
        new_list.append(char.upper())

print(new_list)


#Task 5 -> Dictionary Створити рядок удь-який рядок українською мовою, маленькими літерами, що міститиме кілька голосних літер
'''
Створити 2 списки: [1, 2, 3] та ['one', 'two', 'three']
Завдання:
task 1 -> Перетворити ці 2 списки на словник, де ключами буде перший список, а значеннями -- другий
task 2 -> В словнику що утворився, поміняти місцями ключі та значення
task 3 -> Погуглити, почитати і запам'ятати які об'єкти можуть виступати ключами в словнику
       та спробувати зрозуміти чому це так
'''
list_of_int = [1,2,3]
list_of_words = ['one','two','three']
turn_into_dict = dict(zip(list_of_words, list_of_int ))
change_keys_into_value_in_dict = dict(zip(list_of_int,list_of_words ))
print(type(turn_into_dict),turn_into_dict)
print(change_keys_into_value_in_dict)