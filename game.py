# -- Pygame Game Template -- #
import random
import pygame
import sys
import config # Import the config module 
def init_game (): 
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT)) # Use constants from config
    pygame.display.set_caption(config.TITLE)
    return screen


def handle_events ():
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
          return False
       elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
             return False
    return True

# -- Draw Rectangle -- # 
def draw_rectangle(screen, x, y, width, height): 
   pygame.draw.rect(screen, config.GREEN, (x, y, width, height))




def main():
   screen = init_game()
   clock = pygame.time.Clock() # Initialize the clock here

   # -- Set Starting X,Y For Square -- # 
   x = 0
   y = 0
   # -- Square Properties -- #
   width = 50
   height = 50
   speed_x = 2
   speed_y = 2

   running = True
   while running:
      running = handle_events()
      
      screen.fill(config.SKY_BLUE) # Use color from config

      # -- Update Position of Square -- # 
      x += speed_x
      y += speed_y

      # -- If Touch Border -- # 
         # -- X -- #
      if x + width > config.WINDOW_WIDTH - 1 or x < 0:
         speed_x = speed_x * -1.15
         height += 1
         width += 1
         # -- Y -- #
      if y + height > config.WINDOW_HEIGHT - 1 or y < 0:
         speed_y = speed_y * -1.15
         height += 1
         width += 1

      # -- Draw Rectangle -- #
      draw_rectangle(screen, x, y, width, height)

      pygame.display.flip()

      # -- Limit the frame rate to the specified frames per second (FPS) -- #
      clock.tick(config.FPS) # Use the clock to control the frame rate

   pygame.quit()
   sys.exit()

if __name__ == "__main__":
   main()