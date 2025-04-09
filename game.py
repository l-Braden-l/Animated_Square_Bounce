# -- Pygame Game Template -- #
import random
import pygame
import sys
import config # Import the config module 
import time
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

# -- Draw Counter -- #
def draw_counter(screen, counter):
    font = pygame.font.Font(None, 30)  # Set font and size
    counter_text = font.render(f"Wall Hits: {counter}", True, (0, 0, 0)) # counter color
    screen.blit(counter_text, (10, 10))  # Stamp text at the top-left corner

# -- Draw Speed -- #
def draw_speed(screen, speed):
    font = pygame.font.Font(None, 30)  # Set font and size
    speed_text = font.render(f"Speed: {speed:.1f}", True, (0, 0, 0)) # speed color
    screen.blit(speed_text, (10, 40))  # Stamp text at the top-left corner

def draw_text(screen):
    font = pygame.font.Font(None, 30)  # Set font and size
    img_textI = font.render(f"Press \"I\" to increase", True, (0, 0, 0)) # speed color
    img_textD = font.render(f"Press \"D\" to increase", True, (0, 0, 0)) # speed color
    screen.blit(img_textI, (10, 70))  # Stamp text at the top-left corner
    screen.blit(img_textD, (10, 100))  # Stamp text at the top-left corner


def main():
   screen = init_game()
   clock = pygame.time.Clock() # Initialize the clock here

   # -- Set Counter -- #
   counter = 0
   speed = 0
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
         speed_x = speed_x * -1
         counter += 1
         # -- Y -- #
      if y + height > config.WINDOW_HEIGHT - 1 or y < 0:
         speed_y = speed_y * -1
         counter += 1

      # -- Speed Change if I Press -- #
      key = pygame.key.get_pressed()
      if key[pygame.K_i]:

         if speed < 50: 
            speed_x += 0.05
            speed_y += 0.05
            speed += 0.1
         else: 
            speed_x = speed_x
            speed_y = speed_y
            speed = speed

      # -- Speed Change if D Press -- #
      if key[pygame.K_d]: 

         if speed > 50: 
            speed_x -= 0.05
            speed_y -= 0.05
            speed -= 0.1

         else: 
            speed_x = speed_x
            speed_y = speed_y
            speed = speed


      # -- Draw Rectangle -- #
      draw_rectangle(screen, x, y, width, height)
      
      # -- Draw Counter -- #
      draw_counter(screen, counter)

      # -- Draw speed -- #
      draw_speed(screen, speed)

      draw_text(screen)
      pygame.display.flip()

      # -- Limit the frame rate to the specified frames per second (FPS) -- #
      clock.tick(config.FPS) # Use the clock to control the frame rate

   pygame.quit()
   sys.exit()

if __name__ == "__main__":
   main()