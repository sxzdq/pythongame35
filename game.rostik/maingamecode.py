from random import *
from time import *
from data import *
from helpers import *

name = input('''Ты попал на земли утопии. 
Здесь разные герои с уголков вселенной встретились, 
чтобы получить власть древнего, и стать сильнейшим.
Введи свои имя, герой: ''')
player['name'] = name
current_enemy = 0

while True:
    action = input('''Выбери действие:
1 - В бой
2 - Тренировка
3 - Магазин
4 - Как поднять бабла?
5 - Показать инвентарь
6 - Информация об игроке
7 - Информация о враге              
''')
    if action == '1':
        current_enemy = fight(current_enemy)
        if current_enemy == 4:
            break


    elif action == '2':
        training_type = input('''1 тренировать атаку
2 тренировать защиту
''')
        training(training_type)
    elif action == '3':
        shop()
    elif action == '4':
        earn()
    elif action == '5':
        display_inventory
    elif action == '6':
        display_player()
        print()
    elif action == '7':
        display_enemy(current_enemy)
        print()
    print()
        


