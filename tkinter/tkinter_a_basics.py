MSG = """
tkinter demo a: basics
Shows making a window with shapes, text, and images.
No interaction possible.
"""

print(MSG)

import tkinter

# Set up the window
window = tkinter.Tk()
window.title('My very first tkinter GUI')
window.geometry('400x400')

# Create a canvas
canvas = tkinter.Canvas(window, height=400, width=400)
canvas.pack()

# Create a background
canvas.create_rectangle(0, 0, 200, 200, fill='red')
canvas.create_rectangle(200, 0, 400, 200, fill='green')
canvas.create_rectangle(200, 200, 400, 400, fill='yellow')
canvas.create_rectangle(0, 200, 200, 400, fill='blue')

# Create some text
label = tkinter.Label(canvas, text='Windows 95', fg='white', bg='black', font=("Courier New", 24))
label.pack()
canvas.create_window(200, 200, window=label)

# Create an image
img_earth = tkinter.PhotoImage(file='sawczak_demo/assets/earth.png')
earth = canvas.create_image(300, 50, anchor=tkinter.N, image=img_earth)

# Main loop
window.mainloop()
