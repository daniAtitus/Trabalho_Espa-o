import pygame
from tkinter import Tk, simpledialog

def salvar_marcacoes(dicionario, estrelas):
    try:
        with open(dicionario, 'w') as f:
            for estrela in estrelas:
                nome = estrela['nome']
                pos = estrela['pos']
                f.write(f"{nome},{pos[0]},{pos[1]}\n")
            print("Marcações salvas com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar marcações: {e}")

def carregar_marcacoes(dicionario):
    estrelas = []
    try:
        with open(dicionario, 'r') as f:
            for linha in f:
                nome, x, y = linha.strip().split(',')
                estrelas.append({"nome": nome, "pos": (int(x), int(y))})
    except Exception as e:
        print(f"Erro ao carregar marcações: {e}")
    return estrelas

def excluir_marcacoes(dicionario):
    try:
        open(dicionario, 'w').close()
        print("Marcações excluídas com sucesso!")
    except Exception as e:
        print(f"Erro ao excluir marcações: {e}")

pygame.init()
root = Tk()
root.withdraw()

altura = 563
largura = 1000
icone = pygame.image.load("assets/nave.jpg")
estrelinha = pygame.image.load("assets/estrela.png")
pygame.display.set_icon(icone)
fundo = pygame.image.load('assets/bg.jpg')
pygame.display.set_caption("Estrelas")
tela = pygame.display.set_mode((largura, altura))
estrelas = []

desenhando = False
pos_inicial = None
pos_final = None

dicionario = "marcacoes.txt"

estrelas = carregar_marcacoes(dicionario)

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            salvar_marcacoes(dicionario, estrelas)
            pygame.quit()
            exit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_F10:
                salvar_marcacoes(dicionario, estrelas)
            elif evento.key == pygame.K_F11:
                estrelas = carregar_marcacoes(dicionario)
                print("Marcações carregadas do arquivo:")
                for estrela in estrelas:
                    print(f"Nome: {estrela['nome']}, Posição: {estrela['pos']}")
            elif evento.key == pygame.K_F12:
                excluir_marcacoes(dicionario)
                estrelas = []
            elif evento.key == pygame.K_ESCAPE:
                salvar_marcacoes(dicionario, estrelas)
                pygame.quit()
                exit()
        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            pos_inicial = pygame.mouse.get_pos()
            desenhando = True
        elif evento.type == pygame.MOUSEBUTTONUP and evento.button == 1:
            pos_final = pygame.mouse.get_pos()
            desenhando = False
            item = simpledialog.askstring("Space", "Nome da Estrela: ")
            if item is None or item == "":
                item = f"desconhecido{pos_final}"
            estrelas.append({"nome": item, "pos": pos_final})
            pos_inicial = None
            pos_final = None

    tela.blit(fundo, (0, 0))

    for i in range(1, len(estrelas)):
        pygame.draw.line(tela, (255, 255, 255), estrelas[i-1]['pos'], estrelas[i]['pos'], 3)

    for estrela in estrelas:
        nome = estrela['nome']
        pos = estrela['pos']
        pygame.draw.circle(tela, (255, 255, 255), pos, 5)
        tela.blit(estrelinha, (pos[0] - estrelinha.get_width() // 2, pos[1] - estrelinha.get_height() // 2))
        fonte = pygame.font.Font(None, 26)
        texto = fonte.render(nome, True, (255, 255, 255))
        tela.blit(texto, (pos[0] + 10, pos[1] - 10))

    if desenhando and pos_inicial:
        pos_atual = pygame.mouse.get_pos()
        pygame.draw.line(tela, (255, 255, 255), pos_inicial, pos_atual, 3)

    pygame.display.update()