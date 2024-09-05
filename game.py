'''
World of CodeCraft is a command line text adventure game the written in Pyhton by Caique Fabris and Lou Espiral.
'''

import sys 
import time
import random
import data


hp = 100
damage = 10
current_room = data.rooms[0]
enemy = None
count_six = 0


def slow_print(text, delay = 0.018):
    for char in str(text):
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()
    

def appear_enemy():
    die_roll = random.randint(0, 10)
    if die_roll > -1:
        slow_print(f'A wild {data.caterpie.name} appears!')
        global enemy
        enemy = data.caterpie
    return

# Each function below executes one of the options available for the player
def game_help(text=data.help_text):
    slow_print('\nYou asked for help. No problem!')
    slow_print(text)

def look(room=current_room):
    slow_print(f'\nYou are in {room.name}. {room.description}')

def go(room=current_room):
    slow_print('\nWhere do you want to go?')
    pairs = enumerate(room.connections, 1)
    for i, n in pairs:
        slow_print(i, data.rooms[n].name)
    try:
        number = int(input())
        if number in range(1, len(room.connections) + 1):
            global current_room
            current_room = data.rooms[room.connections[i - 1]]
            look(current_room)
            appear_enemy()
        else:
            raise ValueError
    except ValueError:
        slow_print('\nYou did not enter a valid number.')
        
def interact(room=current_room):
    slow_print('\nWhat do you want to interact with?')
    for n, obj in room.objects:
        slow_print(n, obj)
    try:
        chosen_object = room.objects[int(input())]
        chosen_object.interact()
    except (ValueError, IndexError):
        slow_print('\nYou did not enter a valid number.')

def attack(enemy=data.caterpie):
    if enemy:
        enemy.hp -= damage
        slow_print(f'\n {enemy.name} loses {damage} HP and has now {enemy.hp} HP.')
        slow_print(f'{enemy.name} attacks you.')
        global hp
        hp -= enemy.damage
        if hp > 0:
            slow_print(f'\n You lose {damage} HP and now have {hp} HP.')
        else:
            slow_print(f'\n You lose your last {enemy.damage + hp} HP and are now dead! Better luck next time!')
            slow_print('\nThanks for playing World of CodeCraft! See you next time!\n')
            quit()
    else:
        slow_print('\nThere is no enemy to attack.')
    
def exit():
    slow_print('\nThanks for playing World of CodeCraft! See you next time!\n')
    quit()

def six():
    if count_six == 3:
        slow_print('\nOh no! You entered 666! The beast has come to get you! Better luck next time!')
        quit()
    else:
        slow_print('\nThere is no option 6. Or is there?')
        count_six += 1

# Exibts the prompt for the player and calls the function selected 
def choice(text=data.short_text):
    print(text)
    try:
        option = int(input())
        if option != 6:
            count_six = 0
        match option:
            case 0:
                game_help()
            case 1:
                look(current_room)
            case 2:
                go(current_room)
            case 3:
                interact(current_room)
            case 4:
                attack(enemy)
            case 5:
                exit()
            case 6:
                six()
    except ValueError:
        print('\nYou did not enter a valid number. Please try again.')
        print(text)
    choice(text)

# Displays initial text
slow_print(data.welcome)
slow_print(data.help_text)
slow_print(data.intro)
look()
choice()