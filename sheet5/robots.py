from gasp import *          

begin_graphics()            
finished = False

place_player()

while not finished:
    move_player()

end_graphics()  

def place_player():
    print("Here I am!")

def move_player():
    print("I'm moving...")
    update_when('key_pressed')