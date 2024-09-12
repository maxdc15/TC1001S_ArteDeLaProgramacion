import Problema_gzhg

V = Problema_gzhg.solucion_optima()
print (V)

import pygame

#imagen lago

pygame.init()
screen = pygame.display.set_mode((1103, 733))
img = pygame.image.load('lagoo.png')
done = False
bg = (127,127,127)
while not done:
   for event in pygame.event.get():
      screen.fill(bg)
      rect = img.get_rect()
      rect.center = 550, 362
      screen.blit(img, rect)
      if event.type == pygame.QUIT:
          done = True
   pygame.display.update()


#imagen zorro
pygame.init()
screen = pygame.display.set_mode((300, 480))
img = pygame.image.load('Fox.png')
done = False
bg = (127,127,127)
while not done:
   for event in pygame.event.get():
      screen.fill(bg)
      rect = img.get_rect()
      rect.center = 150, 240
      screen.blit(img, rect)
      if event.type == pygame.QUIT:
          done = True
   pygame.display.update()

#imagen harina
pygame.init()
screen = pygame.display.set_mode((400, 380))
img = pygame.image.load('Harina.png')
done = False
bg = (127,127,127)
while not done:
   for event in pygame.event.get():
      screen.fill(bg)
      rect = img.get_rect()
      rect.center = 225, 180
      screen.blit(img, rect)
      if event.type == pygame.QUIT:
          done = True
   pygame.display.update()
   
#imagen granjero

pygame.init()
screen = pygame.display.set_mode((340, 530))
img = pygame.image.load('Granjero.png')
done = False
bg = (127,127,127)
while not done:
   for event in pygame.event.get():
      screen.fill(bg)
      rect = img.get_rect()
      rect.center = 180, 265
      screen.blit(img, rect)
      if event.type == pygame.QUIT:
          done = True
   pygame.display.update()

#imagen ganso

pygame.init()
screen = pygame.display.set_mode((530, 470))
img = pygame.image.load('Ganso.png')
done = False
bg = (127,127,127)
while not done:
   for event in pygame.event.get():
      screen.fill(bg)
      rect = img.get_rect()
      rect.center = 265, 235
      screen.blit(img, rect)
      if event.type == pygame.QUIT:
          done = True
   pygame.display.update()
