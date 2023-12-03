#Task 1
'''
Створити функцію, що приймає число з консолі (використати функцію input());
    Функція повинна обробити значення таким чином: використовуючи вбудовану функцію int(),
    спробувати конвертувати рядок в число (input() завжди повертає рядок).
    Якщо конвертувати не виходить, то вивести в консоль "Entered not valid data".
'''

def accept_number():
    try:
        int(input("Enter a number here: "))
    except:
        print('Entered data is not valid')

accept_number()

#Task 2
'''
Створити функцію, що приймає 2 рядки;
    Якщо хоча б один рядок не виходить конвертувати в число, тоді робимо конкатенацію (з'єднуємо рядки),
    якщо ж обидва значення можна конвертувати в числа, то отримуємо їх суму.
    Результат друкуємо в консоль.
'''
def concatenate(line_1, line_2):
    try:
        int(line_1) or int(line_2)
        print(line_1 + line_2)
    except:
        print(str(line_1) + str(line_2))

concatenate('ty', 25)

# Task 3
'''
Створити функцію, що приймає значення з консолі. Якщо значення не можна привести до числа,
    тоді просимо користувача ввести інше значення, доки він не введе число. Згадуємо про цикл while.
   Коли користувач вводить число, дякуємо йому!
'''

def enter_int():
    while True:
        value = input("Please enter integer value: ")
        try:
            int(value)
            print('Thank you for entering correct value')
            break
        except ValueError:
            print('Entered value is not an integer')

enter_int()

# Task 4
'''
Створити ВЛАСНЕ виключення. Наприклад OnlyEvenError. Створити функцію check_digit(), яка приймає число.
    Якщо число не парне, то породжувати це своє виключення;
    Якщо парне, то повертати його (return)
'''
class OnlyEvenError(ValueError):
         pass

def check_digit(value:int):
    if value % 2:
        raise OnlyEvenError(f'Accepted value is NOT even {value}')
    else:
        return value

check_digit(8)

# Task 5
'''
Створити функцію, що буде приймати число як аргумент і викликАти в тілі функцію check_digit,
    в яку передавати це число.
   Якщо виникає помилка, то перехопити її, та збільшити вхідне число на 1;
   Якщо помилки не вникає, то помножити число на 2.
    Результат виводити в консоль.
    Також функція повинна надрукувати в консоль фразу "Я все одно завжди щось друкую".
   !!! Використовувати try-except-else-finally
'''

def update(value):
    try:
        check_digit(value)
        print(f'The value is even and doubled {value * 2}')
    except OnlyEvenError:
        print(f'The value is NOT even so we add + 1. Result = {value + 1}')
    finally:
        print('Я все одно завжди щось друкую')

update(8)