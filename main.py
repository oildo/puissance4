import pygame
from pygame.locals import *

from field import *

#---------------------------------------------------------------

# initialisation des variables
""""dimentions"""
dim_fenetre = [800, 650]  # 0 --> x / 1 --> y
"""couleurs"""
gris = (161, 161, 161)
"""Strings"""
red_win = "Rouge a gagné!"
yellow_win = "Jaune a gagné!"
"""other"""
turn = True  # True = red turn
BREAK = 1000

# initialisation de pygame
pygame.init()

# initialisation de la fenetre
fenetre = pygame.display.set_mode((dim_fenetre[0], dim_fenetre[1]))
pygame.display.set_caption("puissance 4")  # nom de la fenetre

# fond bleu
fenetre.fill(gris)

# font initialisation
font=pygame.font.Font(None, 100)

# rafraichissement de la fenetre
pygame.display.flip()

# initialisation of the field
m_field = Field(fenetre, 0, 0, dim_fenetre[0], dim_fenetre[1])
m_field.draw()

# boucle infinie
continuer = True  # si continuer vaut False, alors la boucle (et le programme) s'arrete(nt)
while continuer:

    # parcourir les evenements
    for event in pygame.event.get():

        # quitte l'app si on appuie sur la croix
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            continuer = False

        if event.type == KEYDOWN and event.key == K_e:
            m_field.init()
            turn = True

        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            if turn:
                if m_field.add_token(m_field.which_column(event.pos), 1):
                    turn = not turn
            else:
                if m_field.add_token(m_field.which_column(event.pos), 2):
                    turn = not turn
    who_won = m_field.is_win_def()
    if not who_won == 0:
        m_field.init()           # initialisation sequence
        turn = True              # -----------------------

        if who_won == 1:
            fenetre.fill(m_field.get_color(3))  # fill the display with the color red
            text_win = font.render(red_win,1,(255,255,255))
        else:
            fenetre.fill(m_field.get_color(2))  # fill the display with the color yellow
            text_win = font.render(yellow_win,1,(255,255,255))
        
        fenetre.blit(text_win, (int(dim_fenetre[0]/2 - text_win.get_width()/2), 200))
        pygame.display.flip()    # refresh the display
        # pygame.time.delay(BREAK)  # wait for 1 sec
        br = True
        while br : 
            for e in pygame.event.get():
                if e.type == KEYDOWN or (e.type == MOUSEBUTTONDOWN) and (e.button == 1 or e.button == 3): 
                    br = False
            
    m_field.draw()
    # rafraichissement de la fenetre
    pygame.display.flip()
