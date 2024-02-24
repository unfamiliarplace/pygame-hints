MSG = """
tkinter demo f: movement, continuous
Shows moving an object when an event fires,
and continuing to move until another event fires.
Use WASD or the arrow keys to test it out. You do not have to hold them.
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
app.direction = ''

# Set up FPS
app.fps = 30
app.fps_delay = 1_000 // 30

# Functions

def change_direction(event) -> None:
    """
    Change the player's movement direction using
    WASD or arrow keys.
    """

    # w = north
    if event.keysym.lower() in ['w', 'up']:
        app.direction = 'N'

    # s = south
    elif event.keysym.lower() in ['s', 'down']:
        app.direction = 'S'

    # a = west
    elif event.keysym.lower() in ['a', 'left']:
        app.direction = 'W'

    # d = east
    elif event.keysym.lower() in ['d', 'right']:
        app.direction = 'E'

    print(f'Changed direction to {app.direction}')

def move() -> None:
    """
    Move the player according to the direction it's facing.
    """

    if app.direction == 'N':
        if app.player_y > 30:
            canvas.move(app.player, 0, -10)
            app.player_y -= 10

    elif app.direction == 'S':
        if app.player_y < 370:
            canvas.move(app.player, 0, 10)
            app.player_y += 10

    elif app.direction == 'W':
        if app.player_x > 30:
            canvas.move(app.player, -10, 0)
            app.player_x -= 10

    elif app.direction == 'E':
        if app.player_x < 370:
            canvas.move(app.player, 10, 0)
            app.player_x += 10

    print(f'Moved to ({app.player_x}, {app.player_y})')

    # Schedule next invocation of self
    window.after(app.fps_delay, move)

# Bind keypresses
window.bind("<KeyPress>", change_direction)

# Start self-invoking function going after N milliseconds
window.after(app.fps_delay, move)

# Initialize the canvas
canvas = tkinter.Canvas(window, height=400, width=400)
canvas.pack()

# Draw the background
canvas.create_rectangle(0, 0, 400, 400, fill='black')

# Draw the player
app.player = canvas.create_oval(180, 180, 220, 220, fill='white')

# Main loop
window.mainloop()
