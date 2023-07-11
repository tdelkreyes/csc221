from gasp import *
def draw()
    begin_graphics()
    Circle((310, 210), 100)
    Circle((275, 230), 15)
    Circle((345, 230), 15)
    Arc((310, 210), 60, 225, 315)
    Line((310, 230), (280, 180))
    Line((290, 190), (320, 180))

update_when('key_pressed')
end_graphics()
