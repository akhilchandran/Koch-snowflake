#!/usr/bin/python
import pygame, sys
from pygame.locals import*

fpsClock = pygame.time.Clock()

def changec(c):
  return ((c[1]+56)%233+22,(c[2]+83)%250+5,(c[0]+141)%240+15)

def newslop(s):
  return (s - 1.732)/(1+s*1.732)

def midp(p1,p2):
  return ((p1[0]+p2[0])/2,(p2[1]+p1[1])/2)

def slop(p1,p2):
  x = (p2[0]-p1[0])
  y = (p1[1]-p2[1])
  if x == 0 or y==0:
    return (y/3,x/3)
  s = float(y)/x 
  return s
  
def newp(p1,p2):
  return (p1[0]+(p2[0]-p1[0])/3,p1[1]-(p1[1]-p2[1])/3)

def newp2(p1,p2,ns,s):
  x = int((-s*(p2[1]-p1[1])+p2[0]+ns*s*p1[0])/(1+s*ns))
  y = int(-ns*(x-p1[0])+p1[1])
  return (x,y)

display = pygame.display.set_mode((1300,700))
pygame.display.set_caption('snowflack')
color = (100,20,64)
while True :
  display.fill((0,0,0))
  a =[(450,475),(850,475),(650,129),(450,475)]
  pygame.draw.polygon(display, color,(a[0],a[1],a[2]),1)
  
  pygame.display.update()
  fpsClock.tick(2)
  k = 1
  while k < 6:
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
    i = 0
    color = changec(color)
    while i < len(a)-1:
      s = slop(a[i],a[i+1])
      np1=newp(a[i],a[i+1])
      np3=newp(a[i+1],a[i])
      mp = midp(a[i],a[i+1])
      if type(s) != type(0.1):
        np2 = (mp[0]+s[0],mp[1]+s[1])
      else:
        ns = newslop(s)
        np2=newp2(np1,mp,ns,s) 
      pygame.draw.line(display, (0,0,0),np1,np3,4)
      pygame.draw.line(display, color,np1,np2,1)
      pygame.draw.line(display, color,np2,np3,1)
      a = a[:i+1]+[np1,np2,np3]+a[i+1:]
      i += 4
    pygame.display.update()
    fpsClock.tick(2)
    k +=1
