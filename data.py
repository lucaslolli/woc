welcome = '''
    #####################################\n
    #   Welcome to World of CodeCraft!  #\n
    #     A text adventure game by      #\n
    #    Caique Fabris & Lou Espiral    #\n
    #####################################
'''

# Caique: write intro
intro = '''
    Oh no! The Kingdom is in upheaval etc etc...
'''

help_text = '''Below are the commands in the game.
Press:
[0] or [H] to display this HELP
[1] or [L] to LOOK around
[2] or [G] to GO to a different area
[3] or [I] to INTERACT with people and objects
[4] or [A] to ATTACK the current enemy
[5] or [Q] to QUIT the game
Then press Enter to confirm.'''

short_text = '''What do you want to do?
[0] HELP   [1] LOOK   [2] GO   [3] INTERACT   [4] ATTACK   [5] QUIT
'''
# alternative:
#  0 [H]ELP   1 [L]OOK   2 [G]O   3 [I]NTERACT   4 [A]TTACK   5 [Q]UIT

location_list = [
    ('Firewall Quarantine', 'It is hot in here.', [1], []),
    ('Terminal Square', 'It is square and terminal.', [0], []) 
    # Caique: fill in the locations
    ]