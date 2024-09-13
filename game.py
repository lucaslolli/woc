'''
World of CodeCraft is a command line text adventure game written in Pyhton by Caique Fabris and Lou Espiral.
'''

import classes


# Create the world and the hero
game = classes.Game()
world = classes.World()
bestiary = None
hero = classes.Hero(current_location=world.locations[0])
world.locations[0].visited = True


classes.slow_print('''
    #####################################\n
    #   Welcome to World of CodeCraft!  #\n
    #     A text adventure game by      #\n
    #    Caique Fabris & Lou Espiral    #\n
    #####################################
''')

# Caique: write intro
classes.slow_print('''
    Oh no! The Kingdom is in upheaval etc etc...
'''
)

hero.look()

game.choice(hero, world)