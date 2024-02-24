MSG = """
pygame demo z: mouse movement tracking
Shows the tracking of mouse motion.
Try moving the mouse.
Watch the console for info about angles.
"""

print(MSG)

import pygame
import math

# Create an app object to store global variables
class App:
    pass
app = App()

# Set up the window
pygame.init()
pygame.display.set_caption('My very first pygame GUI')

# Dimensions
w = 1200
w2 = w // 2  # half

h = 800
h2 = h // 2  # half

p = (w * h) // 12_000
p2 = p // 2  # half
p25 = p2 + 5 # half + tiny bit of padding for bounds checking

bg_a = '#198935'
bg_b = '#12689a'

# Make window
window = pygame.display.set_mode([w, h])

# Set up text module
pygame.font.init()
font = pygame.font.SysFont('Courier New', 24)

# Set up fps
app.fps = 60
app.fps_delay = 1_000 // app.fps
fps_clock = pygame.time.Clock()

# Player position and rotation
app.player_x = w2
app.player_y = h2
app.player_angle = 0

# Speeds
app.player_speed = 1 # Percentage of the distance to your cursor it will move each frame
app.max_speed_x = (0.01 * app.player_speed) * (w * 0.45)
app.max_speed_y = (0.01 * app.player_speed) * (h * 0.45)

# App states
app.look_away = False
app.follow = False

# Set up images
app.bg_img = pygame.image.load('sawczak_demo/assets/underwater.jpg').convert()
app.bg_img = pygame.transform.scale(app.bg_img, (w * 1.65, w * 1.35))

app.player_img_normal = pygame.image.load('sawczak_demo/assets/player_normal.png').convert_alpha()
app.player_img_follow = pygame.image.load('sawczak_demo/assets/player_follow.png').convert_alpha()
app.player_img_avoid = pygame.image.load('sawczak_demo/assets/player_avoid.png').convert_alpha()

app.player_img_normal = pygame.transform.scale(app.player_img_normal, (p, p))
app.player_img_follow = pygame.transform.scale(app.player_img_follow, (p, p))
app.player_img_avoid = pygame.transform.scale(app.player_img_avoid, (p, p))

app.player_img = app.player_img_normal

app.player_rect = app.player_img.get_rect(center=(app.player_x, app.player_y))
app.player_rotated_img = app.player_img
app.player_rotated_rect = app.player_rotated_img.get_rect(center=app.player_rect.center)

# Functions

def update_rotation() -> None:
    """
    Set the ping's position to the mouse's and the colour
    as determined by which button is pressed.
    """

    mouse_x, mouse_y = pygame.mouse.get_pos()

    d_x = mouse_x - app.player_x
    d_y = mouse_y - app.player_y
    app.player_angle = math.degrees(math.atan2(d_y, d_x))

    # The rotation is counter-clockwise by default
    app.player_angle += 450
    app.player_angle %= 360
    app.player_angle = 360 - app.player_angle

    if app.look_away:
        app.player_angle += 180
    
    app.player_img = app.player_img_normal
    if app.follow:
        if app.look_away:
            app.player_img = app.player_img_avoid
        else:
            app.player_img = app.player_img_follow    

    app.player_rect = app.player_img.get_rect(center=(app.player_x, app.player_y))
    app.player_rotated_img = pygame.transform.rotate(app.player_img, app.player_angle)
    app.player_rotated_rect = app.player_rotated_img.get_rect(center=app.player_rect.center)

    # print(f'... at ({mouse_x}, {mouse_y})')

def move() -> None:
    """
    Move the player.
    """

    # Get distance
    mouse_x, mouse_y = pygame.mouse.get_pos()

    d_x = (mouse_x - (app.player_x - p2))
    d_y = (mouse_y - (app.player_y - p2))

    d_x *= (0.01 * app.player_speed)
    d_y *= (0.01 * app.player_speed)

    # If looking away, go away from mouse
    if app.look_away:

        # Get proportion of maximum speed
        prop_x = abs(d_x / 2) / app.max_speed_x
        prop_y = abs(d_y / 2) / app.max_speed_y
        i_prop_x = (1 - prop_x)
        i_prop_y = (1 - prop_y)

        # Reverse direction
        if d_x < 0:
            d_x_mod = 1
        else:
            d_x_mod = -1
        
        if d_y < 0:
            d_y_mod = 1
        else:
            d_y_mod = -1
        
        # Invert scale
        d_x = i_prop_x * d_x_mod * app.max_speed_x
        d_y = i_prop_y * d_y_mod * app.max_speed_y

        # Just feels like it needs to scale
        d_x *= 0.75
        d_y *= 0.75    

    # Modify the player's coordinates
    app.player_x += d_x
    app.player_y += d_y

    # Prevent out of bounds
    if app.player_x > (w - p25):
        app.player_x = (w - p25) - (app.player_x - (w - p25))

    if app.player_x < p25:
        app.player_x = p25 + abs(p25 - app.player_x)

    if app.player_y > (h - p25):
        app.player_y = (h - p25) - (app.player_y - (h - p25))

    if app.player_y < p25:
        app.player_y = p25 + abs(p25 - app.player_y)

    # Updating rotation also does the actual movement so we might as well do it here
    update_rotation()


def keydown(event) -> None:
    """
    Respond to a keydown event.
    """

    if event.key in [pygame.K_x]:
        app.look_away = not app.look_away

    elif event.key in [pygame.K_f]:
        app.follow = not app.follow

# Main loop
running = True
while running:

    # Check events
    for event in pygame.event.get():

        # User clicks window close button
        if event.type == pygame.QUIT:
            running = False
        
        # A keyboard button is pressed down
        elif event.type == pygame.KEYDOWN:
            keydown(event)
            update_rotation() # Because the rotation mode might have changed

        # The mouse moves
        elif event.type == pygame.MOUSEMOTION:
            update_rotation()

    # Draw the background
    if app.look_away:
        bg_colour = bg_b
        msg_look = 'Looking away from mouse'
    else:
        bg_colour = bg_a
        msg_look = 'Looking towards mouse'
    
    if app.follow:
        msg_go = 'Player moving'
        move()
    else:
        msg_go = 'Player stationary'

    pygame.draw.rect(window, bg_colour, (0, 0, w, h))

    window.blit(app.bg_img, (0, -(1 * h)))

    # Draw the text
    text_look = font.render(f'{msg_look}. Press X to toggle.', True, 'white')
    text_look_rect = text_look.get_rect(center=(w // 2, h * 0.9))
    window.blit(text_look, text_look_rect)

    text_go = font.render(f'{msg_go}. Press F to toggle.', True, 'white')
    text_go_rect = text_go.get_rect(center=(w // 2, h * 0.95))
    window.blit(text_go, text_go_rect)

    # Draw the player
    window.blit(app.player_rotated_img, app.player_rotated_rect.topleft)
   
    # Update the display
    pygame.display.flip()

    # Wait for next frame
    fps_clock.tick(app.fps)

# Quit the window
pygame.quit()
