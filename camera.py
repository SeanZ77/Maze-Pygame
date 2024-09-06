import map
import math
import pygame
import settings
from gameObject import GameObject

class Camera(GameObject):
  def __init__(self, x, y, rot, fov):
    super().__init__(x, y, rot)
    self.fov = fov

  def draw(self, window):
    for i in range(settings.fov+1):
      #get rotation and coordinates
      rotD = self.rot + math.radians(i - self.fov / 2)
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
          j *= math.cos(math.radians(i-self.fov/2))
          height = 1/j * settings.wallHeight
          break

      #draw a wall based on the info from the previous step
      d = min(d * settings.shadowStrength, 510)
      color = settings.colors[tile]
      wallColor = (max(0, color[0]-d), max(0, color[1]-d), max(0, color[2]-d))
      pygame.draw.line(window, wallColor, (i*(settings.screenWidth/self.fov), (settings.screenHeight/2) + height), (i*(settings.screenWidth/self.fov), (settings.screenHeight/2) - height), width=int(settings.screenWidth/self.fov))