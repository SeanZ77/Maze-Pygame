import pygame
pygame.init()

import settings

#initiate pygame
display = pygame.display
window = pygame.display.set_mode((settings.screenWidth, settings.screenHeight))
pygame.display.set_caption(settings.name)
pygame.event.get()
clock = pygame.time.Clock()

import map, player

won = False

player = player.Player()

def drawText(text, color, size, x, y):
  #draw a text with the given settings
  font = pygame.font.SysFont('Monospace Regular', size)
  textSurface = font.render(str(text), False, color)
  window.blit(textSurface, (x - font.size(text)[0] / 2, y - font.size(text)[1] / 2))

pKeys = pygame.key.get_pressed()

#main loop
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      quit()

  #draw the ceiling and floor
  pygame.draw.rect(window, settings.colors[3], (0, 0, settings.screenWidth, settings.screenHeight / 2))
  pygame.draw.rect(window, settings.colors[0], (0, settings.screenHeight / 2, settings.screenWidth, settings.screenHeight / 2))

  #get the fps and adjust the game speed according to it
  fps = clock.get_fps()
  try:
    scale = settings.targetFps/fps
  except:
    scale = 0

  #display the win screen if won, else draw and update the player
  if won:
    pygame.draw.rect(window, (175, 175, 175), (0, 0, settings.screenWidth, settings.screenHeight))
    drawText("YOU WON!", (0, 255, 0), 45, settings.screenWidth/2, settings.screenHeight/2)
  else:
    player.draw(window)
    player.update(scale)
    if map.map[int(player.x)][int(player.y)] == 2:
      won = True

  #display the fps
  drawText("FPS: " + str(round(fps, 2)), (255, 0, 0), 35, settings.screenWidth/2, 25)
  
  pygame.display.flip()
  clock.tick(settings.targetFps)