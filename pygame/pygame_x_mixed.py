MSG = """
pygame demo x: mixed 1
Shows a button that, when clicked, begins a repeated action.
"""

print(MSG)

import pygame

# Create an app object to store global variables
class App:
    pass
app = App()

# Set up the window
pygame.init()
pygame.display.set_caption('My very first pygame GUI')
window = pygame.display.set_mode([400, 400])

# Set up text module
pygame.font.init()
font = pygame.font.SysFont('Courier New', 18)

# A decent way to pass around "global" variables
class App:
    pass
app = App()

# Set up app variables
app.clicked = False
app.movement = 'N'
app.earth_y = 200

# Set up images
img_earth = pygame.image.load('sawczak_demo/assets/earth.png')

# Create a button
btn_start_text = font.render('Show Earth', True, 'black', 'white')
btn_start_rect = pygame.Rect(130, 150, 200, 50)

# Event IDs
app.e_move = pygame.USEREVENT + 1

# Set up FPS
app.fps = 30
app.fps_delay = 1_000 // 30

# Functions

def move_earth():
    """
    Move the earth up till it reaches the top of the screen.
    Then move it down till it reaches the bottom of the screen.
    Repeat.
    """

    # Moving north?
    if app.movement == 'N':
        if app.earth_y > 0:
            app.earth_y -= 10
        else:
            app.movement = 'S'

    # Moving south?
    elif app.movement == 'S':
        if app.earth_y < 290:
            app.earth_y += 10
        else:
            app.movement = 'N'

# Main loop
running = True
while running:

    # Check events
    for event in pygame.event.get():

        # User clicks window close button
        if event.type == pygame.QUIT:
            running = False
        
        # The move event fires
        elif event.type == app.e_move:
            move_earth()

    # Draw the background
    pygame.draw.rect(window, 'black', (0, 0, 400, 400))

    # Draw the button
    if not app.clicked:
        window.blit(btn_start_text, (130, 150))

    # Draw the earth
    if app.clicked:
        window.blit(img_earth, (200, app.earth_y))

    # Check for button press

    if btn_start_rect.collidepoint(pygame.mouse.get_pos()):
        if pygame.mouse.get_pressed()[0] and (not app.clicked):
            app.clicked = True
            pygame.time.set_timer(app.e_move, app.fps_delay)

    # Update the display
    pygame.display.flip()

# Quit the window
pygame.quit()
