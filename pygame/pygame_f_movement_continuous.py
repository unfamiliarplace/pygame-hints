MSG = """
pygame demo f: movement, continuous
Shows moving an object when an event fires,
and continuing to move until another event fires.
Use WASD or the arrow keys to test it out. You do not have to hold them.
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
app.direction = ''

# Set up FPS
app.fps = 30
app.fps_delay = 1_000 // 30
fps_clock = pygame.time.Clock()

# Allow repeated keypressing every N milliseconds
pygame.key.set_repeat(app.fps_delay)

# Functions

def change_direction(event) -> None:
    """
    Change the player's movement direction using
    WASD or arrow keys.
    """

    if event.key in [pygame.K_w, pygame.K_UP]:
        app.direction = 'N'

    elif event.key in [pygame.K_s, pygame.K_DOWN]:
        app.direction = 'S'

    elif event.key in [pygame.K_a, pygame.K_LEFT]:
        app.direction = 'W'

    elif event.key in [pygame.K_d, pygame.K_RIGHT]:
        app.direction = 'E'

    print(f'Player direction changed to {app.direction}')

def move() -> None:
    """
    Move the player according to the direction it's facing.
    """

    if app.direction == 'N':
        if app.player_y > 25:
            app.player_y -= 10

    elif app.direction == 'S':
        if app.player_y < 375:
            app.player_y += 10

    elif app.direction == 'W':
        if app.player_x > 25:
            app.player_x -= 10

    elif app.direction == 'E':
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
            change_direction(event)
    
    # Move
    move()
    
    # Draw the background
    pygame.draw.rect(window, 'black', (0, 0, 400, 400))

    # Draw the player
    pygame.draw.circle(window, 'white', (app.player_x, app.player_y), 20)

    # Update the display
    pygame.display.flip()

    # Wait for next frame
    fps_clock.tick(app.fps)

# Quit the window
pygame.quit()
