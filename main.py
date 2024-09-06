import pygame
pygame.init()

import settings

#initiate pygame
display = pygame.display
window = pygame.display.set_mode((settings.screenWidth, settings.screenHeight))
pygame.display.set_caption(settings.name)
pygame.event.get()
clock = pygame.time.Clock()

import map
import camera
import player
won = False

player = player.Player(settings.x, settings.y, 0)
camera = camera.Camera(settings.x, settings.y, 0, settings.fov)
player.addChild(camera)
gameObjects = [player, camera]

pKeys = pygame.key.get_pressed()

def drawText(text, color, size, x, y):  
  #draw a text with the given settings
  font = pygame.font.SysFont('Monospace Regular', size)
  textSurface = font.render(str(text), False, color)
  window.blit(textSurface, (x - font.size(text)[0] / 2, y - font.size(text)[1] / 2))

def updateKeyHeld(keyCode):
    for i in gameObjects:
        i.keyHeld(keyCode)

def updateKeyPressed(keyCode):
    for i in gameObjects:
        i.keyPressed(keyCode)

def updateKeyReleased(keyCode):
    for i in gameObjects:
        i.keyReleased(keyCode)

def drawGameObjects(window):
    for i in gameObjects:
        i.draw(window)

def updateGameObjects(scale):
    for i in gameObjects:
        i.update(scale)

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

    #check for key inputs
    keys = pygame.key.get_pressed()
    for i in range(len(keys)):
        if keys[i]:
            updateKeyHeld(i)
        if keys[i] and not pKeys[i]:
            updateKeyPressed(i)
        if not keys[i] and pKeys[i]:
            updateKeyReleased(i)
    pKeys = keys

    if map.map[int(player.x)][int(player.y)] == 2:
      won = True

    #display the win screen if won, else draw and update the player
    if won:
        pygame.draw.rect(window, (175, 175, 175), (0, 0, settings.screenWidth, settings.screenHeight))
        drawText("YOU WON!", (0, 255, 0), 45, settings.screenWidth/2, settings.screenHeight/2)
    else:
        drawGameObjects(window)
        updateGameObjects(scale)

  #display the fps
    drawText("FPS: " + str(round(fps, 2)), (255, 0, 0), 35, settings.screenWidth/2, 25)
  
    pygame.display.flip()
    clock.tick(settings.targetFps)

