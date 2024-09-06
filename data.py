# import classes


welcome = '''
    #####################################\n
    #   Welcome to World of CodeCraft!  #\n
    #     A text adventure game by      #\n
    #    Caique Fabris & Lou Espiral    #\n
    #####################################
'''

# xuxa: write intro
intro = '''
    Oh no! The Kingdom is in upheaval etc etc...
'''

help_text = '''Below are the commands in the game.
Press:
[0] to display this HELP
[1] to LOOK around
[2] to GO to a different area
[3] to INTERACT with people and objects
[4] to ATTACK the current enemy
[5] to QUIT the game
Then press Enter to confirm.'''

short_text = '''What do you want to do?
[0] HELP   [1] LOOK   [2] GO   [3] INTERACT   [4] ATTACK   [5] QUIT
'''


location_list = [
    ('Firewall Quarantine', 'It is dark and damp and blablabla...', [1], []),
    ('Terminal Square', '[Description of Terminal Square]', [0], []) 
    # xuxa: fill in the locations
    ]

# rooms = [classes.Room(*object) for object in room_list]

# caterpie = classes.Enemy('Caterpie', 20, 5)