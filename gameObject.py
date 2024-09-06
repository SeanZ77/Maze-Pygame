import camera
import map
import math
import pygame
import settings

class GameObject():
  def __init__(self, x, y, rot):
    self.x = x
    self.y = y
    self.rot = rot
    self.scale = 0
    self.children = []
    self.pKeys = pygame.key.get_pressed()

  def draw(self, window):
      return
 
  def update(self, scale):
    self.scale = scale
    for i in self.children:
        i.x = self.x
        i.y = self.y
        i.rot = self.rot

  def keyHeld(self, keyCode):
   return
      
  def keyPressed(self, keyCode):
    return

  def keyReleased(self, keyCode):
    return

  def addChild(self, child):
    self.children.append(child)