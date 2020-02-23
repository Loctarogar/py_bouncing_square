import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
class Square():
    def __init__ (self):
        self.x = 390
        self.y = 580
        self.width = 20
        self.hight = 20
        
    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.y, self.x, self.width, self.hight))
        
    
class Stick():
    def __init__ (self):
        self.x = 200
        self.y = 200
        self.width = 200
        self.hight = 35
        
    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.y, self.x, self.width, self.hight))
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (800, 600)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

square = Square()
stick = Stick()

# create background
background = pygame.Surface(screen.get_size());
background = background.convert();
background.fill((0, 0, 0));

def redrawGameWindow():
    screen.blit(background, (0, 0))
    square.draw(screen)
    stick.draw(screen)
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and stick.y >= 0:
        stick.y -= 4
    if keys[pygame.K_RIGHT] and stick.y <= size[0] - stick.width:
        stick.y += 4
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
 
    # --- Drawing code should go here
    redrawGameWindow()
    
    square
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()