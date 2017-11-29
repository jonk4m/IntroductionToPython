"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Jonathan Kinnard.
"""
########################################################################
# Done: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# Done: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################

import rosegraphics as rg

window = rg.TurtleWindow()

left = rg.SimpleTurtle('turtle')
left.pen = rg.Pen('midnight blue', 3)
left.speed = 60  # Fast
right = rg.SimpleTurtle('turtle')
right.pen = rg.Pen('red', 3)
right.speed = 60  # Fast
size = 300
left.right(180)
for k in range(20):
    left.draw_square(size)
    left.right(40)
    left.pen_up()
    left.forward(15)
    left.pen_down()
    left.draw_square(size)
    left.pen_up()
    left.left(45)
    left.pen_down()
    right.draw_square(size)
    right.right(40)
    right.pen_up()
    right.forward(15)
    right.pen_down()
    right.draw_square(size)
    right.pen_up()
    right.left(45)
    right.pen_down()
    size = size - 15

window.close_on_mouse_click()