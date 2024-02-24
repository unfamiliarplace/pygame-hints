MSG = """
tkinter demo y: mixed 2
Shows a scene with repeated actions, updating text, movement,
and multiple overlaid shapes and images.
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
window.geometry('600x600')

# Initialize app variables
app.objects = {}
app.n_days = 0
app.is_day = True
app.earth_x = 300
app.earth_y = 400

# Set up FPS
app.fps = 30
app.fps_delay = 1_000 // 30

# Functions

def clear_canvas() -> None:
    """
    Clear the parts of the canvas that need to be cleared.
    """

    for key in ['background', 'moon', 'sun']:
        if (key in app.objects) and (app.objects[key] is not None):
            canvas.delete(app.objects[key])
            app.objects[key] = None

def draw_day() -> None:
    """
    Draw the day scene.
    """
    clear_canvas()

    background = canvas.create_rectangle(0, 0, 600, 600, fill='#b1e8f2')
    app.objects['background'] = background

    sun = canvas.create_oval(50, 200, 250, 400, fill='yellow')
    app.objects['sun'] = sun

    # Move earth above the background too
    canvas.tag_raise(earth)


def draw_night() -> None:
    """
    Draw the night scene.
    """

    clear_canvas()

    background = canvas.create_rectangle(0, 0, 600, 800, fill='black')
    app.objects['background'] = background

    moon = canvas.create_oval(425, 350, 475, 400, fill='white')
    app.objects['moon'] = moon

    # Move earth above the background too
    canvas.tag_raise(earth)


def add_day() -> None:
    """
    Add a day to the counter and schedule the next one.
    """
    app.n_days += 1
    text_days.set(f'Days: {app.n_days}')
    window.after(4_000, add_day)

def toggle_day_night() -> None:
    """
    Toggle whether to draw day or night.
    """
    app.is_day = not app.is_day

    if app.is_day:
        draw_day()
    else:
        draw_night()

    window.after(2_000, toggle_day_night)

def move(event) -> None:
    """
    Move the earth object using WASD.
    """

    # w = north
    if event.keysym.lower() in ['w', 'up']:
        if app.earth_y > 0:
            canvas.move(app.objects['earth'], 0, -20)
            app.earth_y -= 20

    # s = south
    elif event.keysym.lower() in ['s', 'down']:
        if app.earth_y < 480:
            canvas.move(app.objects['earth'], 0, 20)
            app.earth_y += 20

    # a = west
    elif event.keysym.lower() in ['a', 'left']:
        if app.earth_x > 0:
            canvas.move(app.objects['earth'], -20, 0)
            app.earth_x -= 20

    # d = east
    elif event.keysym.lower() in ['d', 'right']:
        if app.earth_x < 480:
            canvas.move(app.objects['earth'], 20, 0)
            app.earth_x += 20


# Initialize the canvas
canvas = tkinter.Canvas(window, height=600, width=600)
canvas.pack()

# Add a label to track the days
text_days = tkinter.StringVar()
text_days.set('Days: 0')
label_days = tkinter.Label(canvas, textvariable=text_days, fg='white', bg='black', font=("Courier", 16))
label_days.pack()
canvas.create_window(300, 20, window=label_days)

# Add a label with instructions
text_instructions = "A day passes every 4 seconds.\n"
text_instructions += "Use WASD to move the earth."
label_instructions = tkinter.Label(canvas, text=text_instructions, fg='white', bg='black', font=("Courier", 11))
label_instructions.pack()
canvas.create_window(300, 80, window=label_instructions)

# Initialize and show images
img_earth = tkinter.PhotoImage(file='sawczak_demo/assets/earth.png')
earth = canvas.create_image(app.earth_x, app.earth_y, anchor=tkinter.NW, image=img_earth)
app.objects['earth'] = earth

# Bind keypresses
window.bind("<KeyPress>", move)

# Draw the initial scene
draw_day()
    
# Start the day cycle
window.after(4_000, add_day)
window.after(2_000, toggle_day_night)

# Main loop
window.mainloop()
