MSG = """
tkinter demo c: keyboard
Shows an event that responds to keyboard interaction.
Use WASD or the arrow keys to test it out.
Watch the console for info about key presses and releases.
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
app.circle = None

# Functions

def move(event) -> None:
    """
    Move the circle using WASD or arrow keys.
    """

    # Debugging -- see console
    print(f'You just pressed key: {event.keysym}')

    # Check character and set app movement direction

# w = north
    if event.keysym.lower() in ['w', 'up']:
        canvas.moveto(app.circle, 175, 125)

    # s = south
    elif event.keysym.lower() in ['s', 'down']:
        canvas.moveto(app.circle, 175, 225)

    # a = west
    elif event.keysym.lower() in ['a', 'left']:
        canvas.moveto(app.circle, 125, 175)

    # d = east
    elif event.keysym.lower() in ['d', 'right']:
        canvas.moveto(app.circle, 225, 175)

def unmove(event) -> None:

    # Debugging -- see console
    print('You just released a key')

    # Move the earth back
    canvas.moveto(app.circle, 175, 175)
    

# Bind keypresses
window.bind("<KeyPress>", move)
window.bind("<KeyRelease>", unmove)

# Initialize the canvas
canvas = tkinter.Canvas(window, height=400, width=400)
canvas.pack()

# Draw the background
canvas.create_rectangle(0, 0, 400, 400, fill='black')
canvas.create_rectangle(175, 125, 225, 275, fill='white')
canvas.create_rectangle(125, 175, 275, 225, fill='white')

# Draw the circle
app.circle = canvas.create_oval(175, 175, 225, 225, fill='green')

# Main loop
window.mainloop()
