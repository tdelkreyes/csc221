from gasp import * 
from random import randint
begin_graphics()

def place_robot():
    global T1000,navx,navy
    navx = randint(0, 63)
    navy = randint(0, 47)
    T1000 = Circle((10 * navx + 5, 10 * navy + 5), 5, color="red", filled=True)
    print("Destroy all Humans")

def safe_player_place():
    global player_shape,player_x,player_y, navx,navy
    safety = 0
    player_x = randint(0, 63)
    player_y = randint(0, 47)
    while safety == 0:
        if navx == player_x and navy == player_y:
            player_x = randint(0, 63)
            player_y = randint(0, 47)
        else:
            player_shape = Circle((10 * player_x + 5, 10 * player_y + 5), 5, filled=True)
            safety += 1

def place_player():
    global player_shape,player_x,player_y
    player_x = randint(0, 63)
    player_y = randint(0, 47)
    player_shape = Circle((10 * player_x + 5, 10 * player_y + 5), 5, filled=True)

def move_player(): 
    global player_x, player_y, player_shape

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

    move_to(player_shape, (10 * player_x + 5, 10 * player_y + 5))

def move_robot():
    global navx, navy, T1000, player_x, player_y
    if player_x > navx:
        navx += 1
    elif player_x < navx:
        navx -= 1
    elif player_y > navy:
        navy += 1
    elif player_y < navy:
        navy -= 1
    move_to(T1000, (10 * navx + 5, 10 * navy + 5))

finished = False

def check_collisions():
    global navx, navy,player_x, player_y, finished
    if navx == player_x and navy == player_y:
        finished = True
        print ("You are Terminated")
        sleep (3.00)

place_robot()
place_player()
finished = False
while not finished:
    move_player()
    move_robot()
end_graphics()    