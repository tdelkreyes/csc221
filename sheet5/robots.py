from gasp import * 
from random import randint
class Player:
    pass
class Robot:
    pass
begin_graphics()
numbots = 10
def place_robots():
    global terminators
    terminators = []
    while len(terminators) < numbots:
        t1000 = Robot()
        t1000.x = randint(0, 47)
        t1000.y = randint(0, 47)
        if not crash(t1000,terminators):
            t1000.form = Box((10 * t1000.x + 5, 10 * t1000.y + 5), 10, 10, color="red", filled=True)
            terminators.append(t1000)
def safe_player_place():
    global player
    player = Player()
    player.x = randint(0, 63)
    player.y = randint(0, 47)
    player.shape = Circle((10 * player.x + 5, 10 * player.y + 5), 5, filled=True)
    if crash(player, terminators):
        player.x = randint(0, 63)
        player.y = randint(0, 47)
        player.shape = Circle((10 * player.x + 5, 10 * player.y + 5), 5, filled=True)

def move_player(): 
    global player
    key = update_when('key_pressed')
    while key == '5':
        remove_from_screen(player.shape)
        safe_player_place()
        key = update_when('key_pressed')
    if key == '6' and player.x < 63:
        player.x += 1
    elif key == '3':
        if player.x < 63:
            player.x += 1
        if player.y > 0:
            player.y -= 1
    elif key == '2' and player.y > 0:
        player.y -= 1
    elif key == '1':
        if player.x > 0:
            player.x -= 1
        if player.y > 0:
            player.y -= 1
    elif key == '4' and player.x > 0:
        player.x -= 1
    
    elif key == '7':
        if player.x > 0:
            player.x -= 1
        if player.y < 47:
            player.y += 1
    
    elif key == '8' and player.y < 47:
        player.y += 1
    elif key == '9':
        if player.x < 63:
            player.x += 1
        if player.y < 47:
            player.y += 1
    move_to(player.shape, (10 * player.x + 5, 10 * player.y + 5))
def move_robots():
    global terminators
    for t1000 in terminators:
        if player.x > t1000.x:
            t1000.x += 1
        elif player.x < t1000.x:
            t1000.x -= 1
        if player.y > t1000.y:
            t1000.y += 1
        elif player.y < t1000.y:
            t1000.y -= 1
        move_to(t1000.form, (10 * t1000.x, 10 * t1000.y))

finished = False

def crash(player,terminators):
    for t1000 in terminators:
        if t1000.x == player.x and t1000.y == player.y:
            return True
        else:
            return False
def check_collisions():
    global finished
    crash(player, terminators)
    if crash == True:
        key_text = Text("You are Terminated", (320, 240), size=48, color="red")
        sleep (3.00)
        finished == True

place_robots()

safe_player_place()
key_text = Text("Run for your Life!", (320, 240), size=48)
sleep(1)
remove_from_screen(key_text)
while not finished:
    move_player()
    move_robots()
    check_collisions()
end_graphics()      