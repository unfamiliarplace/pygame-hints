MSG = """
pygame demo d: mouse
Shows an event that responds to mouse interaction.
Try clicking and holding each mouse button.
Watch the console for info about button presses and releases.
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
app.ping_pos = []
app.ping_colour = ''

# Functions

def set_ping(event) -> None:
    """
    Set the ping's position to the mouse's and the colour
    as determined by which button is pressed.
    """

    app.ping_pos = pygame.mouse.get_pos()    

    # 0 = left
    if pygame.mouse.get_pressed()[0]:
        print('Left mouse button pressed')
        app.ping_colour = 'white'
    
    # 1 = middle
    elif pygame.mouse.get_pressed()[1]:
        print('Middle mouse button pressed')
        app.ping_colour = 'green'
    
    # 2 = right
    elif pygame.mouse.get_pressed()[2]:
        print('Right mouse button pressed')
        app.ping_colour = 'purple'

    print(f'... at {app.ping_pos}')

def clear_ping() -> None:
    """
    Reset / clear the ping.
    """

    print('Mouse button released')
    app.ping_pos = []
    app.ping_colour = ''

# Main loop
running = True
while running:

    # Draw the background
    # We do this first because we want to draw a circle over it...
    # There are other ways to organize this but for simplicity
    pygame.draw.rect(window, 'black', (0, 0, 400, 400))

    # Check events
    for event in pygame.event.get():

        # User clicks window close button
        if event.type == pygame.QUIT:
            running = False
        
        # A mouse button is pressed down
        elif event.type == pygame.MOUSEBUTTONDOWN:
            set_ping(event)

        # A mouse button is released
        elif event.type == pygame.MOUSEBUTTONUP:
            clear_ping()

    # Draw the ping
    if app.ping_pos != []:
        pygame.draw.circle(window, app.ping_colour, app.ping_pos, 25)

    # Update the display
    pygame.display.flip()

# Quit the window
pygame.quit()
