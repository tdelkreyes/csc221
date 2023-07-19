from gasp import *   
from random import randint

begin_graphics()            
finished = False

player_x = randint(0, 63)
player_y = randint(0, 47)

def place_player():
    global baller

    baller = Circle((10 * player_x + 5, 10 * player_y + 5), 5, filled=True)
    print("Here I am!")
    print("I'm moving...")

def move_player():
    global player_x, player_y, baller

    key = update_when('key_pressed')

    if key == '6' and player_x < 63:
        player_x += 1

    
    

while bx < 645:
    move_to(baller, (bx + 4, by + 3))
    bx = bx + 4 
    by = by + 3
    sleep(0.02)   



place_player()

while not finished:
    move_player()

end_graphics()  