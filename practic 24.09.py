#  ЗАДАНИЕ 0
"""
Написать программу которая проверяет что в строке есть хотя бы один пробел, число, буква нижнего и верхнего регистра.
Если это так, то вывести 'YES', иначе 'NO'
1. isspace
2. islower
3. isupper
4. isdigit


test_string = 'Hello world123'

for symbol in test_string:
    print(symbol)
    print(symbol.isspace())
    print(symbol.islower())
    print(symbol.isupper())
    print(symbol.isdigit())
    print('======================')
"""

test_string = 'Hell%o world123'

for symbol in test_string:
    if symbol.isspace() or symbol.islower() or symbol.isupper() or symbol.isdigit():
        print('YES')
    else:
        print('NO')

"""
"""
1. Напишите программу где пользователь вводит число symbol_len, а программа генерирует пароль длинной symbol_len.
Чем выше будет сложность пароля, тем лучше.
2. Напишите программу где пользователь вводит пароль, а программа проверяет сложность пароля и выводит свой результат
в оценочной шкале от 1 до 5.
3. Напишите программу где пользователь вводит число - count, а программа выводит count чисел фибоначчи.


# ЗАДАНИЕ 1
import random

ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""

all = ascii_lowercase + ascii_uppercase + digits + punctuation
k = 5
symbols = random.choices(ascii_lowercase, k)  # Сгенерировали 5 рандомных символов из букв ascii_lowercase
done_str = ''.join(symbols)(all,k)
print(done_str)

# ЗАДАНИЕ 4

count = int(input('Веди число'))
f1 = f2 = 1
print(f1 , f2 ,end = ' ' )
i = 2
while i < count:
    f1,f2=f2,f1+f2
    print(f2,end = ' ' )
    i+=1
print()




