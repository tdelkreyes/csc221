from gasp import *   

from random import randint

begin_graphics()            
finished = False

player_x = randint(0, 63)
player_y = randint(0, 47)
bx = 5
by = 5
br = 5
baller = Circle((bx, by), br)

while bx < 645:
    move_to(baller, (bx + 4, by + 3))
    sleep(0.02)

def place_player():
    print("Here I am!")
    Circle((10 * player_x + 5, 10 * player_y + 5), 5, filled=True)

def move_player():
    print("I'm moving...")
    update_when('key_pressed')

place_player()

while not finished:
    move_player()

end_graphics()  