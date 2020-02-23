import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
    
class Stick():
    def __init__ (self):
        self.x = 200
        self.y = 120
        self.width = 200
        self.height = 15
        
    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.x, self.y, self.width, self.height))
        
stick = Stick()

class Square():
    def __init__ (self):
        self.x = 390
        self.y = 480
        self.width = 20
        self.height = 20
        self.y_vel = 2
        self.x_vel = 2
        
    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.x, self.y, self.width, self.height))
        self.y += self.y_vel
        self.x += self.x_vel
        # bouncing from display borders
        if self.y + self.height >= size[1] or self.y <= 1:
            self.y_vel = self.y_vel * -1
        if self.x + self.width >= size[0] or self.x <= 1:
            self.x_vel = self.x_vel * -1
        #bouncing from stick
        if self.y <= stick.y + stick.height:
            if self.x >= stick.x and self.x + self.width <= stick.x + stick.width and self.y + self.height > stick.y:
                self.y_vel *= -1
        
    def hit_box(self, box):
        if self.y + self.height > box.y:
            if self.x + self.width > box.x and self.x + self.width < box.x + box.width:
                return True
            return False
                
class Box():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 30
        self.height = 30
        
    def draw(self, screen):
        pygame.draw.rect(screen, GREEN,(self.x, self.y, self.width, self.height))
        
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (800, 600)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Bouncing square")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

square = Square()


# create background
background = pygame.Surface(screen.get_size());
background = background.convert();
background.fill((0, 0, 0));

def redrawGameWindow():
    screen.blit(background, (0, 0))
    square.draw(screen)
    stick.draw(screen)
    for box in boxes:
        box.draw(screen)

step = 50
boxes = [];
for box in range(0, 20):
    boxes.append(Box(step,570))
    step += 35
for box in boxes:
    print (box.x)    
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and stick.x >= 0:
        stick.x -= 4
    if keys[pygame.K_RIGHT] and stick.x <= size[0] - stick.width:
        stick.x += 4
 
    # --- Game logic should go here
    for box in boxes:
        if square.hit_box(box):
            boxes.pop(boxes.index(box))
 
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