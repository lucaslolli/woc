'''
World of CodeCraft is a command line text adventure game written in Pyhton by Caique Fabris and Lou Espiral.
'''

import classes

prisoner = ('Prisoner', [
    'Wow!',
    'Hi!',
    'Bye!'
])

classes.data.location_list[0][3] = [prisoner]


# Create the world and the hero
game = classes.Game()
world = classes.World()
bestiary = None
hero = classes.Hero(current_location=world.locations[0])
world.locations[0].visited = True

# Display initial text
classes.slow_print(classes.data.welcome)
classes.slow_print(classes.data.help_text)
classes.slow_print(classes.data.intro)
hero.look()
game.choice(hero, world)