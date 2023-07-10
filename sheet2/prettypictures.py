Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from gasp import *
>>> begin_graphics()
>>> Circle((300, 200), 100)
<Circle object centered at (300, 200) with a radius of 100>
>>> Circle((265, 220), 15)
<Circle object centered at (265, 220) with a radius of 15>
>>> Circle((335, 220), 15)
<Circle object centered at (335, 220) with a radius of 15>
>>> Arc((300, 200), 60, 225, 315)
<Arc object centered at (300, 200) with a radius of 60. Its arc goes from 225º to 315º>
>>> Line((300, 220), (280, 180))
<Line segment object from (300, 220) to (280, 180)>
>>> Line((280, 180), (320, 180))
<Line segment object from (280, 180) to (320, 180)>
