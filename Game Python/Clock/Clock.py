import pygame
import sys

pygame.init()


screen = pygame.display.set_mode((500,500))
pygame.display.set_caption ("Countdown Timer")

BLUE_GRAY= (105, 157, 196)
HARVEST_GOLD = (252, 194, 0)
BLACK = (0,0,0)
font = pygame.font.Font(None, 36)
running = True

text_1 = font.render("+", True, BLACK)
text_2 = font.render("-", True, BLACK)
text_3 = font.render("+", True, BLACK)
text_4 = font.render("-", True, BLACK)
text_5 = font.render("START", True, BLACK)
text_6 = font.render("RESET", True, BLACK)

while running :
    screen.fill(BLUE_GRAY)

    mouse_x, mouse_y = pygame.mouse.get_pos()
    
    pygame.draw.rect(screen,HARVEST_GOLD, (100, 50, 50,50))
    pygame.draw.rect(screen,HARVEST_GOLD, (100, 200, 50,50))
    pygame.draw.rect(screen,HARVEST_GOLD, (200, 50, 50,50))
    pygame.draw.rect(screen,HARVEST_GOLD, (200, 200, 50,50))
    pygame.draw.rect(screen,HARVEST_GOLD, (300, 50, 150,50))
    pygame.draw.rect(screen,HARVEST_GOLD, (300, 50, 150,50))
    pygame.draw.rect(screen,HARVEST_GOLD, (300, 150, 150,50))


    screen.blit(text_1, (117, 60))
    screen.blit(text_2, (120, 210))
    screen.blit(text_3, (217, 60))
    screen.blit(text_4, (220, 210))
    screen.blit(text_5, (330, 65))
    screen.blit(text_6, (330, 165))

    # Draw the clock center
    pygame.draw.circle(screen, BLACK, (250, 350), 72)
    pygame.draw.circle(screen, HARVEST_GOLD, (250, 350), 70)

    pygame.draw.rect(screen, BLACK, (48, 448, 404, 34))
    pygame.draw.rect(screen, HARVEST_GOLD, (50, 450, 400, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    pygame.display.flip()

pygame.quit()