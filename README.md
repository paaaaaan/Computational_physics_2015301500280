### 移动图片：
![gif](https://github.com/paaaaaan/Computational_physics_2015301500280/blob/files/gif(1).gif)

### 代码如下：
```python
import pygame
from pygame.locals import *
import sys
pygame.init()
size = width, height = 1000, 1000
speed = [5, 5]
black = 249, 130, 57
screen = pygame.display.set_mode(size)
ball = pygame.image.load(r'C:\Users\潘\Desktop\pan.png')
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
```
