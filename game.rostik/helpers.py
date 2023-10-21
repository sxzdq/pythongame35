from random import *
from time import *
from data import *

def fight(current_enemy):
        round = randint(1, 2)
        enemy = enemies[current_enemy]
        enemy_hp = enemies[current_enemy]['hp']
        print(f'Противник - {enemy["name"]}: {enemy["script"]}')
        input('Enter чтобы продолжить')
        print()

        while  player['hp'] > 0 and enemy_hp > 0:
            if round % 2 == 1:
                print(f'{player["name"]} атакует {enemy["name"]}')
                crit = randint(1, 100)
                if crit < player['luck']:
                    enemy_hp -= player['attack'] * 3
                else: 
                    enemy_hp -= player['attack']
                sleep(1)
                print(f'''{player["name"]} - {player["hp"]}
        {enemy["name"]} - {enemy["hp"]}''')
                print()
                sleep(1)
            
            else:
                print(f'{enemy["name"]} атакует {player["name"]}')
                player['hp'] -= enemy['attack'] * player['armor']
                sleep(1)
                print(f''' {player["name"]} - {player["hp"]}
        {enemy["name"]} - {enemy_hp}''')
                print()
                sleep(1)

            round += 1
        if player['hp'] > 0:
            print(f'Противник - {enemy["name"]} - {enemy["win"]}')
        else:
            print(f'Противник - {enemy["name"]} - {enemy["loss"]}')
        player['hp'] = 100
        return current_enemy

def training(training_type):
        skip = '2'
        if items['2']['name'] in player['inventory']:
             skip = input('''Желаете пропустить тренировку?
1 - да
2 - нет
''')
        if skip == '2':
            for i in range(0, 101, 20):
                print(f'Тренировка завершенна на {i}%')
                sleep(1.5)
        if training_type == '1':
            player['attack'] += 2
            print(f'Вы завершили тренироваться! Ваша атака равна - {player["attack"]}')
        elif training_type == '2':
            player['armor'] -= 0.9
            print(f'Вы завершили тренироваться! Ваша атака равна - {player["armor"]}')
        print()

def display_player():
    print(f'Игрок - {player["name"]}')
    print(f'Величина атаки - {player["attack"]}. Шанс критического урона ({player["attack"]}ед.) равен {player["luck"]}')
    print(f'Броня поглощает {(1 - player["armor"]) * 100}% урона')
    print()

def display_enemy(current_enemy):
    enemy = enemies[current_enemy]
    print(f'Противник - {enemy["name"]}')
    print(f'Величина атаки - {enemy["attack"]}')
    print(f'Здоровье - {enemy["hp"]}')
    print()

def earn():
    print('''Добро пожаловать на фабрику! У тебя есть шанс 66.66% заработать 500 монет. 
          И 33.33% потерять их''')
    result = randint(1, 100)
    sleep(1.5)
    print('Результат...')
    sleep(1.5)
    print('К моему сожалению..')
    sleep(1.5)
    if result < 67:
        print('Вы выйграли 500 монет')
        player['money'] +=500
    else:
        print('Голда не на балике. Вы проиграли 500 монет')
        player['money'] -=500
    print()
    print(f'Текущий баланс - {player["money"]}')
    print()

def shop():
    print('Привет путник')
    print(f'У тебя есть {player["money"]} монет')
    for key, value in items.items():
        print(f'{key} - {value["name"]}: {value["price"]}')
    item = input()
    if item in player['inventory']:
        print('У тебя уже есть такой предмет')
    elif player['money'] >= items[item]['price']:
        print('ты купил шляпу полную')
        player['inventory'].append(items[item]["name"])
        player['money'] -= items[item]["price"]
    else:
        print('Не хватает деняк')
    print()
    print('Буду ждать тебя снова, путник')
    print()

def display_inventory():
    print('У вас есть:')
    for value in player['inventory']:
        print(value)
    print(f'{player["money"]} монет в кармане.')
    print()
    if 'Зелье удачи' in player['inventory']:
        potion = input('''Желаешь выпить Зелье удачи?
1 - да
2 - нет
''')
        if potion == '1':
            player['luck'] += 7
            print(f'Вы были благославлены, удача повысилась на: {player["luck"]}%')
            player['inventory'].remove('Линчик')