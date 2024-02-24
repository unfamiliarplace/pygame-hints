MSG = """
pygame demo a: basics
Shows making a window with shapes, text, and images.
No interaction possible.
"""

print(MSG)

import pygame

# Set up the window
pygame.init()
pygame.display.set_caption('My very first pygame GUI')
window = pygame.display.set_mode([400, 400])

# Set up text module
pygame.font.init()
font = pygame.font.SysFont('Courier New', 24)

# Define text
text = font.render('Windows 95', True, 'white', 'black')

# Set up images
img_earth = pygame.image.load('sawczak_demo/assets/earth.png')

# Main loop
running = True
while running:

    # Check events
    for event in pygame.event.get():

        # User clicks window close button
        if event.type == pygame.QUIT:
            running = False

    # Draw shapes
    pygame.draw.rect(window, 'red', (0, 0, 200, 200))
    pygame.draw.rect(window, 'green', (200, 0, 400, 200))
    pygame.draw.rect(window, 'yellow', (200, 200, 400, 400))
    pygame.draw.rect(window, 'blue', (0, 200, 200, 400))

    # Draw image
    window.blit(img_earth, (250, 50))

    # Draw text
    window.blit(text, (130, 185))

    # Update the display
    pygame.display.flip()

# Quit the window
pygame.quit()
