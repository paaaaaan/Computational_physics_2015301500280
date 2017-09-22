import pygame
from pygame.locals import *
import sys
pygame.init()
size = width, height = 1000, 1000
speed = [1, 1]
black = 249, 130, 57
screen = pygame.display.set_mode(size)
ball = pygame.image.load(r'C:\Users\潘\Desktop\pan.jpg')
ballrect = ball.get_rect()
while 1:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
  ballrect = ballrect.move(speed)
  if ballrect.left < 0 or ballrect.right > width:
    speed[0] = -speed[0]
  if ballrect.top < 0 or ballrect.bottom > height:
    speed[1] = - speed[1]
  screen.fill(black)
  screen.blit(ball, ballrect)
  pygame.display.flip()

  ![1](Computational_physics_2015301500280/picture1.png)
  参考源代码http://www.cnblogs.com/hongten/p/hongten_pygame_bouncing_ball.html
