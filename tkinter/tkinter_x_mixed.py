MSG = """
tkinter demo x: mixed 1
Shows a button that, when clicked, begins a repeated action.
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
app.objects = {}
app.movement = 'N'
app.earth_y = 200

# Set up FPS
app.fps = 30
app.fps_delay = 1_000 // 30

# Functions

def show_earth():
    """
    Respond to a click on the show earth button.
    """

    # Draw the earth and add it to the shapes registry
    earth = canvas.create_image(200, app.earth_y, anchor=tkinter.N, image=img_earth)
    app.objects['earth'] = earth

    # Remove the start button
    start_button.destroy()

    # Start moving the earth
    move_earth()

def move_earth():
    """
    Move the earth up till it reaches the top of the screen.
    Then move it down till it reaches the bottom of the screen.
    Repeat.
    """

    # Moving north?
    if app.movement == 'N':
        if app.earth_y > 0:
            canvas.move(app.objects['earth'], 0, -10)
            app.earth_y -= 10
        else:
            app.movement = 'S'

    # Moving south?
    elif app.movement == 'S':
        if app.earth_y < 290:
            canvas.move(app.objects['earth'], 0, 10)
            app.earth_y += 10
        else:
            app.movement = 'N'
    
    # Schedule the next move
    window.after(app.fps_delay, move_earth)

# Create a canvas
canvas = tkinter.Canvas(window, height=400, width=400)
canvas.pack()

# Create a background
background = canvas.create_rectangle(0, 0, 400, 400, fill='black', outline='black')

# Initialize images
img_earth = tkinter.PhotoImage(file='sawczak_demo/assets/earth.png')

# Create a button
start_button = tkinter.Button(window, text='Show Earth', command=show_earth)
start_window = canvas.create_window(200, 100, window=start_button)

# Main loop
window.mainloop()
