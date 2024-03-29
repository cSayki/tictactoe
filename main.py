import pygame
import time
    
pygame.init()

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("TicTacToe tu connais")

# Décor du jeu
line_width = 5
background = "antiquewhite"
grid = "black"

# Nombre de coup dans la partie et switch entre tour joueur 1 et joueur 2
coup = 0
tour = 1

# Ajout des polices
font = pygame.font.SysFont(None, 40)

# Position des croix et cercles
T = set()

def draw_background():
    screen.fill(background)
    for x in range(3):
        pygame.draw.line(screen, grid, (0, x * 100), (SCREEN_WIDTH, x * 100), line_width) #line(surface, color, start_pos, end_pos, width)
        pygame.draw.line(screen, grid, (x * 100, 0), (x * 100, SCREEN_HEIGHT), line_width)

def croix():
    x = col * 100 + 50
    y = row * 100 + 50
    pygame.draw.line(screen, "red", (x - 40, y - 40), (x + 40, y + 40), line_width)
    pygame.draw.line(screen, "red", (x - 40, y + 40), (x + 40, y - 40), line_width)
    return x, y

def rond():
    x = col * 100 + 50
    y = row * 100 + 50
    pygame.draw.circle(screen, "blue", (x, y), 40, line_width)
    return x, y

def position_jouee():
    global coup, tour
    x, y = row, col
    coord = (x, y, tour)
    if coord not in T:
        T.add(coord)
        coup += 1
        print(T)

def check_victoire():
    for ligne in range(0, 3): # joueur 1
        if (ligne, 0, 1) in T and (ligne, 1, 1) in T and (ligne, 2, 1) in T:
            return True
    for colonne in range(0, 3):
        if (0, colonne, 1) in T and (1, colonne, 1) in T and (2, colonne, 1) in T:
            return True
    if (0, 0, 1) in T and (1, 1, 1) in T and (2, 2, 1) in T:
        return True
    if (0, 2, 1) in T and (1, 1, 1) in T and (2, 0, 1) in T:
        return True
    
    for ligne in range(0, 3): # joueur 2
        if (ligne, 0, 0) in T and (ligne, 1, 0) in T and (ligne, 2, 0) in T:
            return True
    for colonne in range(0, 3):
        if (0, colonne, 0) in T and (1, colonne, 0) in T and (2, colonne, 0) in T:
            return True
    if (0, 0, 0) in T and (1, 1, 0) in T and (2, 2, 0) in T:
        return True
    if (0, 2, 0) in T and (1, 1, 0) in T and (2, 0, 0) in T:
        return True
    return False

def afficher_message_victoire(joueur):
    message = font.render(f"Victoire du joueur {joueur} !", True, "black")
    screen.blit(message, (10, SCREEN_HEIGHT // 2))

def victoire(joueur):
    global run
    print(f"Victoire du joueur 1 ! \nNombre de coup : {coup}")
    afficher_message_victoire(joueur)
    pygame.display.update()
    time.sleep(3)
    run = False

def egalite():
    global coup, run
    if coup == 9 and check_victoire() == False:
        message_match_nul = font.render(f"Match nul !", True, "black")
        screen.blit(message_match_nul, (70, SCREEN_HEIGHT // 2))
        pygame.display.update()
        time.sleep(3)
        run = False


run = True

draw_background()

while run == True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # 1 c'est clique gauche
                col = event.pos[0] // 100 #event.pos[O] c'est pour réccupérer la position x de la souris
                row = event.pos[1] // 100 #event.pos[1] c'est pour réccupérer la position y de la souris
                if tour == 1:
                    if (row, col, 1) not in T and (row, col, 0) not in T:
                        croix()
                        position_jouee()
                        if check_victoire() == True:
                            victoire(1)
                        egalite()
                        tour -= 1
                        #print(tour, coup)
                else:
                    if (row, col, 1) not in T and (row, col, 0) not in T:
                        rond()
                        position_jouee()
                        if check_victoire() == True:
                            victoire(2)
                        egalite()
                        tour += 1
                        #print(tour, coup)
    
    pygame.display.update()

pygame.quit()
