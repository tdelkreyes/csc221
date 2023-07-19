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

baller = Circle((bx, by), br)

while bx < 645:
    move_to(baller, (bx + 4, by + 3))
    bx = bx + 4 
    by = by + 3
    sleep(0.02)   

def move_player():
    print("I'm moving...")
    update_when('key_pressed')

place_player()

while not finished:
    move_player()

end_graphics()  