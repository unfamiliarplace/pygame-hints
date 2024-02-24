MSG = """
pygame demo e: movement, discrete
Shows moving an object when an event fires.
Use WASD or the arrow keys to test it out. Hold them to keep moving.
Watch the console for info about the object's X and Y positions.
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

# Initialize app variables
app.player_x = 200
app.player_y = 200

# Allow repeated keypressing every N milliseconds
pygame.key.set_repeat(33)

# Functions

def move(event) -> None:
    """
    Move the player using WASD or arrow keys.
    """

    if event.key in [pygame.K_w, pygame.K_UP]:
        if app.player_y > 25:
            app.player_y -= 10

    elif event.key in [pygame.K_s, pygame.K_DOWN]:
        if app.player_y < 375:
            app.player_y += 10

    elif event.key in [pygame.K_a, pygame.K_LEFT]:
        if app.player_x > 25:
            app.player_x -= 10

    elif event.key in [pygame.K_d, pygame.K_RIGHT]:
        if app.player_x < 375:
            app.player_x += 10

    print(f'Player moved to ({app.player_x}, {app.player_y})')

# Main loop
running = True
while running:

    # Catch all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            move(event)
    
    # Draw the background
    pygame.draw.rect(window, 'black', (0, 0, 400, 400))

    # Draw the player
    pygame.draw.circle(window, 'white', (app.player_x, app.player_y), 20)

    # Update the display
    pygame.display.flip()

# Quit the window
pygame.quit()
