MSG = """
tkinter demo b: timer
Shows an event that repeats on a loop.
No interaction possible.
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

# Set app variables
app.showing_text = False
app.label = None

# Function that will repeat on a timer
# It does this by invoking itself after N milliseconds
def toggle_text() -> None:
    if app.showing_text:
        print('Toggling text off')
        app.showing_text = False

        app.label.destroy()

    else:
        print('Toggling text on')
        app.showing_text = True

        app.label = tkinter.Label(canvas, text='Watch me blink', fg='black', bg='white', font=("Courier New", 24))
        app.label.pack()
        canvas.create_window(200, 200, window=app.label)

    # Schedule the next occurrence of myself
    window.after(1_500, toggle_text)

# Start self-invoking function going after N milliseconds
window.after(1_500, toggle_text)

# Create a canvas
canvas = tkinter.Canvas(window, height=400, width=400)
canvas.pack()

# Create a background
canvas.create_rectangle(0, 0, 400, 400, fill='blue')

# Main loop
window.mainloop()
