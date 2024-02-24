MSG = """
pygame demo c: keyboard
Shows an event that responds to keyboard interaction.
Use WASD or the arrow keys to test it out.
Watch the console for info about key presses and releases.
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

# Set up app variables
app.movement = ''

# Functions

def move(event) -> None:
    """
    Move the circle using WASD or arrow keys.
    """

    # Debugging -- see console
    print(f'You just pressed key # {event.key}')

    # Check character and set app movement direction

    if event.key in [pygame.K_w, pygame.K_UP]:
        app.movement = 'N'
    elif event.key in [pygame.K_s, pygame.K_DOWN]:
        app.movement = 'S'
    elif event.key in [pygame.K_a, pygame.K_LEFT]:
        app.movement = 'W'
    elif event.key in [pygame.K_d, pygame.K_RIGHT]:
        app.movement = 'E'

def unmove() -> None:

    # Debugging -- see console
    print('You just released a key')

    # Unset app movement direction
    app.movement = ''

# Main loop
running = True
while running:

    # Check events
    for event in pygame.event.get():

        # User clicks window close button
        if event.type == pygame.QUIT:
            running = False
        
        # User presses a key down
        elif event.type == pygame.KEYDOWN:
            move(event)

        # User releases a key
        elif event.type == pygame.KEYUP:
            unmove()

    # Draw the background
    pygame.draw.rect(window, 'black', (0, 0, 400, 400))
    pygame.draw.rect(window, 'white', (175, 125, 50, 150))
    pygame.draw.rect(window, 'white', (125, 175, 150, 50))

    # Draw a little ball that responds to keyboard presses
    if app.movement == '':
        x, y = (200, 200)
    elif app.movement == 'N':
        x, y = (200, 150)
    elif app.movement == 'S':
        x, y = (200, 250)
    elif app.movement == 'W':
        x, y = (150, 200)
    elif app.movement == 'E':
        x, y = (250, 200)
    
    pygame.draw.circle(window, 'green', (x, y), 25)

    # Update the display
    pygame.display.flip()

# Quit the window
pygame.quit()
