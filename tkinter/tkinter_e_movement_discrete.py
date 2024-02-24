MSG = """
tkinter demo e: movement, discrete
Shows moving an object when an event fires.
Use WASD or the arrow keys to test it out. Hold them to keep moving.
Watch the console for info about the object's X and Y positions.
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

# Initialize app variables
app.player = None
app.player_x = 200
app.player_y = 200

# Functions

def move(event) -> None:
    """
    Move the earth object using WASD or arrow keys.
    """

    # w = north
    if event.keysym.lower() in ['w', 'up']:
        if app.player_y > 0:
            canvas.move(app.player, 0, -20)
            app.player_y -= 25

    # s = south
    elif event.keysym.lower() in ['s', 'down']:
        if app.player_y < 400:
            canvas.move(app.player, 0, 20)
            app.player_y += 25

    # a = west
    elif event.keysym.lower() in ['a', 'left']:
        if app.player_x > 0:
            canvas.move(app.player, -20, 0)
            app.player_x -= 25

    # d = east
    elif event.keysym.lower() in ['d', 'right']:
        if app.player_x < 400:
            canvas.move(app.player, 20, 0)
            app.player_x += 25

    print(f'Moved to ({app.player_x}, {app.player_y})')

# Bind keypresses
window.bind("<KeyPress>", move)

# Initialize the canvas
canvas = tkinter.Canvas(window, height=400, width=400)
canvas.pack()

# Draw the background
canvas.create_rectangle(0, 0, 400, 400, fill='black')

# Draw the player
app.player = canvas.create_oval(180, 180, 220, 220, fill='white')

# Main loop
window.mainloop()
