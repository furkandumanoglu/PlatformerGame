import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game Platform")

# Colors
background_color = (135, 206, 250)  # Light blue

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the background
    screen.fill(background_color)

    # Update the display
    pygame.display.flip()

    class Player:
     def __init__(self):
        self.x = 50
        self.y = screen_height - 100
        self.width = 50
        self.height = 50
        self.color = (255, 0, 0)  # Red color
        self.velocity = 20

     def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

     def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x - self.velocity > 0:
            self.x -= self.velocity
        if keys[pygame.K_RIGHT] and self.x + self.velocity < screen_width - self.width:
            self.x += self.velocity

    player = Player()

# Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    # Fill the background
        screen.fill(background_color)

    # Draw and move the player
        player.draw(screen)
        player.move()

    # Update the display
        pygame.display.flip()