import sys 
import time
import random
import data


def slow_print(text, delay=0.01):
    # delay = 0.018 # Correct delay. Comment to test the game quickly.
    for char in str(text):
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


class Game:
    def __init__(self, count_six=0):
        self.count_six = count_six
        return
    
    def game_help():
        slow_print('You asked for help. No problem!')
        slow_print(data.help_text)

    def quit_game():
        slow_print('Thanks for playing World of CodeCraft! See you next time!\n')
        quit()

    def six(self):
        if self.count_six == 3:
            slow_print('Oh no! You entered 666! The beast has come to get you! Better luck next time!')
            self.quit_game()
        else:
            slow_print('There is no option 6. Or is there?')
            self.count_six += 1

    def choice(self, hero, world, text=data.short_text):
        slow_print(text)
        try:
            option = input()
            if option != 6:
                self.count_six = 0
            match option:
                case '0' | 'h' | 'H':
                    self.game_help()
                case '1' | 'l' | 'L':
                    hero.look()
                case '2' | 'g' | 'G':
                    hero.go(self, world)
                case '3' | 'i' | 'I':
                    hero.interact(self, world)
                case '4' | 'a' | 'A':
                    hero.attack(hero.enemy, self)
                case '5' | 'q' | 'Q':
                    self.quit_game()
                case '6':
                    self.six()
                case _:
                    raise ValueError
        except ValueError:
            slow_print('You did not enter a valid number or letter. Please try again.')
            slow_print(text)
        self.choice(hero, world)


class Enemy:
    def __init__(self, name="Caterpie", hp=10, damage=2):
        self.name = name
        self.hp = hp
        self.damage = damage

class Location:
    def __init__(self, name, description, connections, inspectionables, visited=False):
        self.name = name
        self.description = description
        self.connections = connections
        self.inspectionables = inspectionables
        self.enemies = None
        self.visited = visited

    def appear_enemy(self, hero):
        die_roll = random.randint(0, 10)
        if die_roll < 5:
            hero.enemy = Enemy()
            slow_print(f'A wild {hero.enemy.name} appears!')
        return


class Inspec:
    def __init__(self, name, description, inspectionables=[]):
        self.name = name
        self.description = description
        self.inspectionables = inspectionables


class NPC:
    def __init__(self, name, lines):
        self.name = name
        self.lines = lines
        self.current_line = 0

    def action(self, game, hero, world):
        slow_print(f'{self.name} says:\n"{self.lines[self.current_line]}"')
        if self.current_line < len(self.lines) - 1:
            self.current_line += 1
        game.choice(hero, world)


class World:
    def __init__(self, locations=data.location_list):
        self.locations = [Location(*location) for location in locations]


class Hero:
    def __init__(self, name="Aric Dataforge", hp=100, damage=5, current_location=None):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.current_location = current_location
        self.enemy = None

    def you_are_in(self):
        slow_print(f'You are in {self.current_location.name}.')    

    def look(self):
        self.you_are_in()
        slow_print(self.current_location.description)
    
    def go(self, world):
        slow_print('Where do you want to go?')
        for i, n in enumerate(self.current_location.connections, 1):
            slow_print(f'[{i}] {world.locations[n].name}')
        print()
        try:
            number = int(input())
            if number in range(1, len(self.current_location.connections) + 1):
                self.current_location = world.locations[self.current_location.connections[i - 1]]
                if world.locations[world.locations.index(self.current_location)].visited:
                    self.you_are_in()
                else:
                    self.look()
                    world.locations[world.locations.index(self.current_location)].visited = True
                self.current_location.appear_enemy(self)
            else:
                raise ValueError
        except ValueError:
            slow_print('You did not enter a valid number.')
        

    def interact(self, game, world):
        slow_print('What do you want to interact with?')
        for n, item in enumerate(self.current_location.inspectionables, 1):
            slow_print(f'[{n}] {item.name}')
            print()
        try:
            chosen_item = self.current_location.inspectionables[int(input()) - 1]
            chosen_item.action(game, self, world)
        except (ValueError, IndexError):
            slow_print('You did not enter a valid number.')
    
    def attack(self, enemy):
        if enemy:
            print(f'You attack {enemy.name}!')
            enemy.hp -= self.damage
            if enemy.hp > 0:
                slow_print(f'{enemy.name} loses {self.damage} HP and now has {enemy.hp} HP.')
                slow_print(f'{enemy.name} attacks you.')
                self.hp -= enemy.damage
                if self.hp > 0:
                    slow_print(f'You lose {enemy.damage} HP and now have {self.hp} HP.')
                else:
                    slow_print(f'You lose your last {enemy.damage + self.hp} HP and die! Better luck next time!')
                    slow_print('\nThanks for playing World of CodeCraft! See you next time!\n')
                    quit()
            else:
                slow_print(f'{enemy.name} loses their last {self.damage - enemy.hp} HP and dies.')
                self.enemy = None
            
        else:
            slow_print('\nThere is no enemy to attack.')



class Item:
    def __init__(self, name):
        self.name = name

    def action(self):
        return
    

prisoner_lines = [
    'Wow!',
    'Hi!',
    'Bye!'
]
prisoner = Inspec('Prisoner', prisoner_lines)