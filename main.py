import pygame
from tkinter import simpledialog

pygame.init()

altura = 563
largura = 1000
icone = pygame.image.load("assets/nave.jpg")
estrelinha = pygame.image.load("assets/estrela.png")
pygame.display.set_icon(icone)
fundo = pygame.image.load('assets/bg.jpg')
pygame.display.set_caption("Estrelas")
tela = pygame.display.set_mode((largura, altura))
estrelas = []
linhas = []  

desenhando = False  
pos_inicial = None  
pos_final = None    

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1: 
            pos_inicial = pygame.mouse.get_pos()
            desenhando = True
        elif evento.type == pygame.MOUSEBUTTONUP and evento.button == 1:
            pos_final = pygame.mouse.get_pos()
            desenhando = False
            item = simpledialog.askstring("Space", "Nome da Estrela: ")
            if item is None or item == "":
                item = f"desconhecido{pos_final}"
            estrelas.append((item, pos_final))
            linhas.append((pos_inicial, pos_final))  
            pos_inicial = None
            pos_final = None
            
    tela.blit(fundo, (0, 0))
    
    for estrela in estrelas:
        nome, pos = estrela
        pygame.draw.circle(tela, (255, 255, 255), pos, 5)
        tela.blit(estrelinha, (pos[0] - estrelinha.get_width() // 2, pos[1] - estrelinha.get_height() // 2))
        fonte = pygame.font.Font(None, 26)
        texto = fonte.render(nome, True, (255, 255, 255))
        tela.blit(texto, (pos[0] + 10, pos[1] - 10))
    
    for linha in linhas:
        pygame.draw.line(tela, (255, 255, 255), linha[0], linha[1], 3)
    
    if desenhando and pos_inicial:
        pos_atual = pygame.mouse.get_pos()
        pygame.draw.line(tela, (255, 255, 255), pos_inicial, pos_atual, 3)
    
    pygame.display.update()

pygame.quit()
