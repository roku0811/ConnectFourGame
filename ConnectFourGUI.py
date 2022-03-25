
#Connect Four Game with Display

from BoardGame import *
from PlayerGame import *
import pygame 
pygame.init()

running = True


b = Board(5,6)

p1 = Player('X')
p2 = AIPlayer('O', 2)
    
# initial board
screen = pygame.display.set_mode([600, 500])
BLUE = [16, 16, 221]
screen.fill(BLUE)
for i in [50, 150, 250, 350, 450, 550]:
    pygame.draw.circle(screen, Color(0, 0, 0), (i, 450), 45, width=0)
    pygame.draw.circle(screen, Color(0, 0, 0), (i, 350), 45, width=0)
    pygame.draw.circle(screen, Color(0, 0, 0), (i, 250), 45, width=0)
    pygame.draw.circle(screen, Color(0, 0, 0), (i, 150), 45, width=0)
    pygame.draw.circle(screen, Color(0, 0, 0), (i, 50), 45, width=0)
    
pygame.display.flip()
player_column = 0

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == KEYDOWN:
                if event.key == K_1:
                    player_column = 0
                    waiting = False
                elif event.key == K_2:
                    player_column = 1
                    waiting = False
                elif event.key == K_3:
                    player_column = 2
                    waiting = False
                elif event.key == K_4:
                    player_column = 3
                    waiting = False
                elif event.key == K_5:
                    player_column = 4
                    waiting = False
                elif event.key == K_6:
                    player_column = 5
                    waiting = False
    
    p1.next_move(b, player_column)
    if b.is_win_for(p1.checker):
        print('Player', p1.checker,'has won.')
        break
    if b.all_full():
        print('It\'s a tie!')
        break
    
    table = b.slots
    for i in [0,1,2,3,4]:
        for j in [0,1,2,3,4,5]:
            if table[i][j] == 'X':
                pygame.draw.circle(screen, Color(255, 0, 0), (50+(j*100), 50+(i*100)), 45, width=0)
            elif table[i][j] == 'O':
                pygame.draw.circle(screen, Color(0, 255, 0), (50+(j*100), 50+(i*100)), 45, width=0)
    
    pygame.display.flip()
    
    p2.next_move(b)
    print(repr(b))
    if b.is_win_for(p2.checker):
        print('Player', p2.checker,'has won.')
        break
    if b.all_full():
        print('It\'s a tie!')
        break


    table = b.slots
    for i in [0,1,2,3,4]:
        for j in [0,1,2,3,4,5]:
            if table[i][j] == 'X':
                pygame.draw.circle(screen, Color(255, 0, 0), (50+(j*100), 50+(i*100)), 45, width=0)
            elif table[i][j] == 'O':
                pygame.draw.circle(screen, Color(0, 255, 0), (50+(j*100), 50+(i*100)), 45, width=0)
    
    pygame.display.flip()

pygame.quit()
    

