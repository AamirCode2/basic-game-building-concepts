import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill((255, 255, 255)) 
    centre_rect = pygame.draw.rect(screen, (0,0, 0), pygame.Rect(260, 180, 60, 60))
    pygame.display.set_caption("MY FIRST GAME SCREEN")
    text = pygame.font.Font(None, 36).render("MY FIRST GAME SCREEN!", True, pygame.Color("Black"))
    

    screen.blit(text, (100, 100))
    pygame.display.flip()