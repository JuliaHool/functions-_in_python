"""
МОДУЛЬ 2
Программа из 2-го дз
Сначала пользователь вводит год рождения Пушкина, когда отвечает верно вводит день рождения
Можно использовать свой вариант программы из предыдущего дз, мой вариант реализован ниже
Задание: переписать код используя как минимум 1 функцию
"""
def question(ask1, answer, ask2):
    year = input(ask1)
    while year != answer:
        print("Не верно")
        year = input(ask2)

question('Ввведите год рождения А.С.Пушкина:','1799','Ввведите год рождения А.С.Пушкина:')
question('Ввведите день рождения Пушкин?','6','В какой день июня родился Пушкин?' )
print('Верно')
