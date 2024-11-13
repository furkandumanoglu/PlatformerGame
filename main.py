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
# Fill the background
screen.fill(background_color)
    
'''Platform Class'''
class Platform:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = (0, 128, 0)  # Green color for platforms

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height)) 
    
    '''Player Class'''
class Player:
    def __init__(self):
        self.x = 50
        self.y = screen_height - 100
        self.width = 50
        self.height = 50
        self.color = (255, 0, 0)  # Red color
        self.velocity = 20
        self.is_jumping = False
        self.jump_speed = 10
        self.gravity = 0.5
        self.y_velocity = 0
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x - self.velocity > 0:
            self.x -= self.velocity
        if keys[pygame.K_RIGHT] and self.x + self.velocity < screen_width - self.width:
            self.x += self.velocity
        ''' Jumping mechanics'''
        if not self.is_jumping and keys[pygame.K_SPACE]:
            self.is_jumping = True
            self.y_velocity = -self.jump_speed

        if self.is_jumping:
            self.y += self.y_velocity
            self.y_velocity += self.gravity

            # Stop the jump when the player lands
            if self.y >= screen_height - 100:  # Assuming ground level
                self.y = screen_height - 100
                self.is_jumping = False 
    def check_collision(self, platforms):
        for platform in platforms:
            if (self.x + self.width > platform.x and self.x < platform.x + platform.width and
                    self.y + self.height >= platform.y and self.y + self.height <= platform.y + platform.height):
                    self.y = platform.y - self.height
                    self.is_jumping = False
                    return
    # If not colliding with any platform, apply gravity
            if self.y < screen_height - 100:  # Fall to the ground
                self.is_jumping = True           
               
    
    # Create Platforms
platforms = [
    Platform(100, 500, 200, 20),  # Example platform
    Platform(400, 400, 200, 20),
    Platform(600, 300, 200, 20)
]
player = Player() 
   
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
    player.check_collision(platforms)
    # Draw platforms
    for platform in platforms:
        platform.draw(screen)

    # Update the display
    pygame.display.flip()

        