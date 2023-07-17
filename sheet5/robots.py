from gasp import *   

from random import randint

player_x= randint(0, 63)

player_y= randint(0, 47)
baller=(5, 5, 5)

begin_graphics()            
finished = False

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