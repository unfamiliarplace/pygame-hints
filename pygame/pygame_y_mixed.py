MSG = """
pygame demo y: mixed 2
Shows a scene with repeated actions, updating text, movement,
and multiple overlaid shapes and images.
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
window = pygame.display.set_mode([600, 600])

# Set up text module
pygame.font.init()
font = pygame.font.SysFont('Courier New', 14)

# Initialize app variables
app.n_days = 0
app.is_day = True
app.earth_x = 300
app.earth_y = 400

# Event IDs
app.e_add_day = pygame.USEREVENT + 1
app.e_toggle_day_night = pygame.USEREVENT + 2

# Set up FPS
app.fps = 30
app.fps_delay = 1_000 // 30

# Allow repeated keypressing
pygame.key.set_repeat(app.fps_delay)

# Functions

def draw_day() -> None:
    """
    Draw the day scene.
    """

    pygame.draw.rect(window, '#b1e8f2', (0, 0, 600, 600))
    pygame.draw.circle(window, 'yellow', (150, 300), 100)

def draw_night() -> None:
    """
    Draw the night scene.
    """

    pygame.draw.rect(window, 'black', (0, 0, 600, 600))
    pygame.draw.circle(window, 'white', (450, 375), 25)

def move(event) -> None:
    """
    Move the earth object using WASD.
    """

    # w = north
    if event.key == pygame.K_w:
        if app.earth_y > 0:
            app.earth_y -= 20

    # s = south
    elif event.key == pygame.K_s:
        if app.earth_y < 480:
            app.earth_y += 20

    # a = west
    elif event.key == pygame.K_a:
        if app.earth_x > 0:
            app.earth_x -= 20

    # d = east
    elif event.key == pygame.K_d:
        if app.earth_x < 480:
            app.earth_x += 20

# Initialize images
img_earth = pygame.image.load('sawczak_demo/assets/earth.png')

# Create an instructions label
instructions_1 = "A day passes every 4 seconds."
instructions_2 = "Use WASD to move the earth."
text_instructions_1 = font.render(instructions_1, True, 'white', 'black')
text_instructions_2 = font.render(instructions_2, True, 'white', 'black')

# Start event timers
pygame.time.set_timer(app.e_add_day, 4_000)
pygame.time.set_timer(app.e_toggle_day_night, 2_000)

# Main loop
running = True
while running:

    # Catch all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            move(event)

        elif event.type == app.e_add_day:
            app.n_days += 1

        elif event.type == app.e_toggle_day_night:
            app.is_day = not app.is_day

    # Draw the background
    if app.is_day:
        draw_day()
    else:
        draw_night()
    
    # Draw the earth
    window.blit(img_earth, (app.earth_x, app.earth_y))

    # Draw the days text
    text_days = font.render(f'Days: {app.n_days}', True, 'white', 'black')
    window.blit(text_days, (280, 25))

    # Draw the instructions text
    window.blit(text_instructions_1, (190, 50))
    window.blit(text_instructions_2, (200, 75))

    # Update the display
    pygame.display.flip()

# Quit the window
pygame.quit()
