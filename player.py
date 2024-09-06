import map
import math
import pygame
import settings
from gameObject import GameObject
    

class Player(GameObject):
  def __init__(self, x, y, rot):
    super().__init__(x, y, rot)

  def draw(self, window):
    self.drawMiniMap(window)

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

  def drawMiniMap(self, window):
    #loop through the 2d map and draw it on the screen
    for i in range(len(map.map)):
      for j in range(len(map.map[0])):
        pygame.draw.rect(window, settings.colors[map.map[i][j]], (i * settings.minimapSize, j * settings.minimapSize, settings.minimapSize, settings.minimapSize))
    #draw the player on the map
    pygame.draw.circle(window, (255, 0, 0), (self.x * settings.minimapSize, self.y * settings.minimapSize), settings.minimapSize)