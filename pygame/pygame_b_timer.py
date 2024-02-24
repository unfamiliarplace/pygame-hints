MSG = """
pygame demo b: timer
Shows an event that repeats on a loop.
No interaction possible.
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
font = pygame.font.SysFont('Courier New', 24)

# Set app variables
app.showing_text = False
app.text = font.render('Watch me blink', True, 'black', 'white')

# Create event ID
e_toggle_text = pygame.USEREVENT + 1

# Start timer running
pygame.time.set_timer(e_toggle_text, 1_500)

# Associated function(s)
def toggle_text() -> None:
    if app.showing_text:
        print('Toggling text off')
        app.showing_text = False
    
    else:
        print('Toggling text on')
        app.showing_text = True

# Main loop
running = True
while running:

    # Check events
    for event in pygame.event.get():

        # User clicks window close button
        if event.type == pygame.QUIT:
            running = False

        # Timed event
        elif event.type == e_toggle_text:
            toggle_text()
    
    # Draw background
    pygame.draw.rect(window, 'blue', (0, 0, 400, 400))

    # Draw text
    if app.showing_text:
        window.blit(app.text, (100, 150))

    # Update the display
    pygame.display.flip()

# Quit the window
pygame.quit()
