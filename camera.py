import map
import math
import pygame
import settings

class Camera():
  def __init__(self):

    self.x = settings.x
    self.y = settings.y
    self.rot = 0
    self.miniMap = True
    self.scale = 0

  def draw(self, window):
    for i in range(settings.fov+1):
      #get player rotation and coordinates
      rotD = self.rot + math.radians(i - settings.fov / 2)
      x = self.x
      y = self.y
      sin = settings.precision * math.sin(rotD)
      cos = settings.precision * math.cos(rotD)
      j = 0
      #cast a ray with the directiona and coordinates
      while True:
        x += cos
        y += sin
        j += 1
        #when the ray hits a wall, save the info
        if map.map[int(x)][int(y)] != 0:
          tile = map.map[int(x)][int(y)]
          d = j
          j *= math.cos(math.radians(i-settings.fov/2))
          height = 1/j * settings.wallHeight
          break

      #draw a wall based on the info from the previous step
      d = min(d * settings.shadowStrength, 510)
      color = settings.colors[tile]
      wallColor = (max(0, color[0]-d), max(0, color[1]-d), max(0, color[2]-d))
      pygame.draw.line(window, wallColor, (i*(settings.screenWidth/settings.fov), (settings.screenHeight/2) + height), (i*(settings.screenWidth/settings.fov), (settings.screenHeight/2) - height), width=int(settings.screenWidth/settings.fov))

    #draw the minimap
    if self.miniMap:
      self.drawMiniMap(window)

  def drawMiniMap(self, window):
    #loop through the 2d map and draw it on the screen
    for i in range(len(map.map)):
      for j in range(len(map.map[0])):
        pygame.draw.rect(window, settings.colors[map.map[i][j]], (i * settings.minimapSize, j * settings.minimapSize, settings.minimapSize, settings.minimapSize))
    #draw the player on the map
    pygame.draw.circle(window, (255, 0, 0), (self.x * settings.minimapSize, self.y * settings.minimapSize), settings.minimapSize)

  def update(self, scale):
    self.scale = scale
    #check for key inputs
    keys = pygame.key.get_pressed()
    for i in range(len(keys)):
      if keys[i]:
        self.keyHeld(i)
      if keys[i] and not self.pKeys[i]:
        self.keyPressed(i)
      if not keys[i] and self.pKeys[i]:
        self.keyReleased(i)
    self.pKeys = keys

  def keyHeld(self, keyCode):
    #change player rotation and position based on key inputs
    x = self.x
    y = self.y
    sin = math.sin(self.rot)
    cos = math.cos(self.rot)
    
    if keyCode == settings.forwardKey:
      x += settings.speed*cos*self.scale
      y += settings.speed*sin*self.scale
      
    elif keyCode == settings.backwardKey:
      x -= settings.speed*cos*self.scale
      y -= settings.speed*sin*self.scale
      
    elif keyCode == settings.strafeLeftKey:
      x += settings.speed*sin*self.scale
      y += -settings.speed*cos*self.scale
      
    elif keyCode == settings.strafeRightKey:
      x += -settings.speed*sin*self.scale
      y += settings.speed*cos*self.scale
      
    elif keyCode == settings.turnLeftKey:
      self.rot -= settings.sensitivity*self.scale
      
    elif keyCode == settings.turnRightKey:
      self.rot += settings.sensitivity*self.scale
      
    if map.map[int(x)][int(y)] != 1:
      self.x = x
      self.y = y
      
  def keyPressed(self, keyCode):
    #toggle minimap
    if keyCode == settings.mapKey:
      self.miniMap = not self.miniMap

  def keyReleased(self, keyCode):
    return