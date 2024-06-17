import pygame 
import os,time
from tkinter import simpledialog, messagebox

pygame.init()
altura = 563
largura = 1000
fundo = pygame.image.load('assets/bg.jpg')
pygame.display.set_caption("Estrelas")
tela = pygame.display.set_mode((largura,altura))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    tela.blit(fundo,(0,0))
    pygame.display.update()


pygame.quit()


