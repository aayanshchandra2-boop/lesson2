import pygame
def main():
    pygame.init()
    screen_width, screen_height = 400, 500
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption(" Colour changing sprite")


    colors = {
        "red": (255, 0, 0),
         "green": (0, 255, 0),
         "blue": (0, 0, 255),
         "yellow": (255, 255, 0),
        "purple": (128, 0, 128),
        "orange": (255, 165, 0)
}

    current_color = colors['white']
    x,y = 30,30
    sprite_width, sprite_height = 60, 60
    clock= pygame.time.Clock()
    done = False
    while not done:     
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
           done = True
      pressed= pygame.key.get_pressed()
      if pressed[pygame.K_left]:x-=3
      if pressed[pygame.K_RIGHT]:x+=3
      if pressed[pygame.K_UP]:y-=3
      if pressed[pygame.K_DOWN]:y+=3
      x= min(max(x,0),sprite_width-sprite_width)
      y= min(max(y,0),sprite_height-sprite_height)
      if x == 0:current_color = colors['red']
      if x == sprite_width-sprite_width:current_color = colors['green']
      else:current_color = colors['white']

      screen.fill((0, 0, 0))
      pygame.draw.rect(sprite, current_color, (x, y, sprite_width, sprite_height))
      pygame.display.flip()
      clock.tick(90)  
    pygame.quit()  
if __name__ == "__main__":