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

# Caique: write intro...
classes.slow_print('''
    Your eyes open to a dim, flickering light.
    You lie on your back, warm stone pressing against you.
    A headache pulses as the distant hum of machinery slowlly fills your mind.
    Memories feel scattered, like broken lines of code.
    As your vision sharpens, you see iron bars surrounding you, etched with pulsing runes.

    What is this place? Why am I here?
'''
)

# hero.look()
game.choice(hero, world)