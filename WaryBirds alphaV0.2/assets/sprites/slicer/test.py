import pygame
import os
import time
r=[
pygame.image.load(os.path.join("D:\\","OIP.jpeg"))
]

win = pygame.display.set_mode((2000,1000))
picture = pygame.transform.scale(r[0], (3000, 1000))
while True:
    win.fill((200,200,200))
    win.blit(picture,(0,0))
    pygame.event.get()
    pygame.display.update()