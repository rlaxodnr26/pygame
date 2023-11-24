import pygame, math, time, os

pygame.init()

w = 1600
h = w * (9/16)

screen = pygame.display.set_mode((w, h))

main = True
ingame = True

while main:
    while ingame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main = False
                ingame = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    print(1)
                if event.key == pygame.K_f:
                    print(2)
                if event.key == pygame.K_j:
                    print(3)
                if event.key == pygame.K_k:
                    print(4)

        screen.fill((0, 0, 0))

        pygame.draw.rect(screen, (0, 0, 0), (w / 2 - w / 8, -int(w / 100), w / 4, h + int(w / 50)))
        pygame.draw.rect(screen, (255, 255, 255), (w / 2 - w / 8, -int(w / 100), w / 4, h+ int(w / 50)), int(w / 100))
        pygame.display.flip()

            