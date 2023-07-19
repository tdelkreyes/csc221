from gasp import *   
from random import randint

begin_graphics()            
finished = False

player_x = randint(0, 63)
player_y = randint(0, 47)
navx = randint(0, 63)
navy = randint(0, 47)

def place_robot():
    global T1000

    T1000 = Box((10 * navx + 5, 10 * navy + 5), 5, color="red", filled=True)
    print("destroy all Humans")

def place_player():
    global baller

    baller = Circle((10 * player_x + 5, 10 * player_y + 5), 5, filled=True)
    print("Here I am!")

def move_player():
    global player_x, player_y, baller

    key = update_when('key_pressed')

    if key == '6' and player_x < 63:
        player_x += 1

    elif key == '3':
        if player_x < 63:
            player_x += 1
        if player_y > 0:
            player_y -= 1

    elif key == '2' and player_y > 0:
        player_y -= 1

    elif key == '1':
        if player_x > 0:
            player_x -= 1
        if player_y > 0:
            player_y -= 1

    elif key == '4' and player_x > 0:
        player_x -= 1
    
    elif key == '7':
        if player_x > 0:
            player_x -= 1
        if player_y < 47:
            player_y += 1
    
    elif key == '8' and player_y < 47:
        player_y += 1

    elif key == '9':
        if player_x < 63:
            player_x += 1
        if player_y < 47:
            player_y += 1
    move_to(baller, (10 * player_x + 5, 10 * player_y + 5))

def move_robot():
    global navx, navy, T1000, player_x, player_y

    if player_x > navx:
        navx =+ 1
    elif player_x < navx:
        navx -= 1
    elif player_y > navy:
        navy += navy
    elif player_y < navy:
        navy -= navy
    move_to(T1000, (10 * navx + 5, 10 * navy + 5))

place_robot()

place_player()

while not finished:
    move_player()

def check_collisions():
    finished = True
    print("You've been caught!")
    sleep(3)

end_graphics()  