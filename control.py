from pynput.mouse import Controller
from pynput.keyboard import Controller

def controlMouse() :
    mouse = Controller()
    mouse.position = (500,200) # left to right, top to bottom , from
                             # from top-left of the screen you can imagine the top-left to be (0,0)
def controlKeyboard():
    keyboard = Controller()
    keyboard.type("I am awesome")
controlKeyboard()



