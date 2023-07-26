from gasp import * 
from random import randint
begin_graphics()

class Player:
    pass

class Robot:
    pass

def place_robot():
    global robot
    robot = Robot
    robot.x = randint(0, 63)
    robot.y = randint(0, 47)
    robot.form = Circle((10 * robot.x + 5, 10 * robot.y + 5), 5, color="red", filled=True)

def safe_player_place():
    global player
    player = Player()
    safety = 0
    player_x = randint(0, 63)
    player_y = randint(0, 47)
    while safety == 0:
        if robot.x == player_x and robot.y == player_y:
            player_x = randint(0, 63)
            player_y = randint(0, 47)
        else:
            player_shape = Circle((10 * player_x + 5, 10 * player_y + 5), 5, filled=True)
            safety += 1

def move_player(): 
    global player

    key = update_when('key_pressed')

    while key == '5':
        remove_from_screen(player_shape)
        safe_player_place()
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
    global player
    if player_x > robot.x:
        robot.x += 1
    elif player_x < robot.x:
        robot.x -= 1
    elif player_y > robot.y:
        robot.y += 1
    elif player_y < robot.y:
        robot.y -= 1
    move_to(robot, (10 * robot.x + 5, 10 * robot.y + 5))

finished = False

def crash():
    global finished
    if robot.x == player_x and robot.y == player_y:
        finished = True
    else:
        finished = False

def check_collisions():
    global finished
    crash()
    if finished == True:
        key_text = Text("You are Terminated", (320, 240), size=48)
        sleep (3.00)

place_robot()
safe_player_place()

finished = False
key_text = Text("Run for your Life!", (320, 240), size=48)
sleep(1)
remove_from_screen(key_text)
while not finished:
    move_player()
    move_robot()
    check_collisions()
end_graphics()   