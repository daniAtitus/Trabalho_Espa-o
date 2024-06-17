import pygame 
import os,time
from tkinter import simpledialog, messagebox

pygame.init()
altura = 563
largura = 1000
icone  = pygame.image.load("assets/nave.jpg")
estrelinha  = pygame.image.load("assets/estrela.png")
pygame.display.set_icon(icone)
fundo = pygame.image.load('assets/bg.jpg')
pygame.display.set_caption("Estrelas")
tela = pygame.display.set_mode((largura,altura))
estrelas = []
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
        elif evento.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                item = simpledialog.askstring("Space", "Nome da Estrela: ")
                print(item)
                if item is None or item == "":
                    item = f"desconhecido{pos}"
                estrelas.append((item, pos))
    tela.blit(fundo, (0, 0))
    for estrela in estrelas:
        nome, pos = estrela
        pygame.draw.circle(tela, (255, 255, 255), pos, 5)
        tela.blit(estrelinha, (pos))
        fonte = pygame.font.Font(None, 26)
        texto = fonte.render(nome, True, (255, 255, 255))
        tela.blit(texto, (pos[0] + 10, pos[1] - 10))
    pygame.display.update()
pygame.quit()