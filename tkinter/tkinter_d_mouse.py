MSG = """
tkinter demo d: mouse
Shows an event that responds to mouse interaction.
Try clicking and holding each mouse button.
Watch the console for info about button presses and releases.
"""

print(MSG)

import tkinter

# Create an app object to store global variables
class App:
    pass
app = App()

# Set up the window
window = tkinter.Tk()
window.title('My very first tkinter GUI')
window.geometry('400x400')

# Set up app variables
app.ping = None

# Functions

def set_ping(event) -> None:
    """
    Set the ping's position to the mouse's and the colour
    as determined by which button is pressed.
    """

    x, y = event.x, event.y

    # 1 = left
    if event.num == 1:
        print('Left mouse button pressed')
        colour = 'white'
    
    # 2 = right
    elif event.num == 2:
        print('Right mouse button pressed')
        colour = 'purple'
    
    # 3 = middle
    elif event.num == 3:
        print('Middle mouse button pressed')
        colour = 'green'

    print(f'... at ({x}, {y})')

    app.ping = canvas.create_oval(x - 25, y - 25, x + 25, y + 25, fill=colour)

def clear_ping(event) -> None:
    """
    Reset / clear the ping.
    """

    print('Mouse button released')
    canvas.delete(app.ping)

# Bind mouse clicks
window.bind("<Button>", set_ping)
window.bind("<ButtonRelease>", clear_ping)

# Initialize the canvas
canvas = tkinter.Canvas(window, height=400, width=400)
canvas.pack()

# Draw the background
canvas.create_rectangle(0, 0, 400, 400, fill='black')

# Main loop
window.mainloop()
