import pygame, math, time, os, random

pygame.init()

w = 1600
h = w * (9/16)

screen = pygame.display.set_mode((w, h))

clock = pygame.time.Clock()

main = True
ingame = True

keys =  [0, 0, 0, 0]
keyset = [0, 0, 0, 0]

maxframe = 60
fps = 0

gst = time.time()
Time = time.time() - gst

ty = 0
tst = Time

t1 = []
t2 = []
t3 = []
t4 = []

Cpath = os.path.dirname(__file__)
Fpath = os.path.join(Cpath, "font")

rate = "PERFECT"

ingame_font_rate = pygame.font.Font(None, int(w / 23))
rate_text = ingame_font_rate.render(str(rate), False, (255, 255, 255))

def sum_note(n):
    if n == 1:
        ty = 0
        tst = Time + 2
        t1.append([ty, tst])
    if n == 2:
        ty = 0
        tst = Time + 2
        t2.append([ty, tst])
    if n == 3:
        ty = 0
        tst = Time + 2
        t3.append([ty, tst])
    if n == 4:
        ty = 0
        tst = Time + 2
        t4.append([ty, tst])

speed = 1

notesumt = 0

a = 0
aa = 00



while main:
    while ingame:

        if Time > 0.2 * notesumt:
            notesumt += 1
            while a == aa:
                a = random.randint(1,4)
            sum_note(a)
            aa = a

        Time = time.time() - gst

        fps = clock.get_fps()

        ingame_font_combo = pygame.font.Font(None, int((w / 38) * combo_effect2))
        combo_text = ingame_font_combo.render(str(combo), False, (255, 255, 255))

        rate_text = ingame_font_rate.render(str(rate), alse, (255, 255, 255))

        if fps == 0:
            fps = maxframe
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    keyset[0] = 1
                    if len(t1) > 0:
                      if t1[0][0] > h / 2:
                        del t1[0]
                if event.key == pygame.K_f:
                    keyset[1] = 1
                    if len(t2) > 0:
                      if t2[0][0] > h / 2:
                        del t2[0]
                if event.key == pygame.K_j:
                    keyset[2] = 1
                    if len(t3) > 0:
                       if t3[0][0] > h / 2:
                        del t3[0]
                if event.key == pygame.K_k:
                    keyset[3] = 1
                    if len(t4) > 0:
                      if t4[0][0] > h / 2:
                        del t4[0]
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    keyset[0] = 0
                if event.key == pygame.K_f:
                    keyset[1] = 0
                if event.key == pygame.K_j:
                    keyset[2] = 0
                if event.key == pygame.K_k:
                    keyset[3] = 0
                    

        screen.fill((0, 0, 0))

        keys[0] += (keyset[0] - keys[0]) / (3 * (maxframe / fps))
        keys[1] += (keyset[1] - keys[1]) / (3 * (maxframe / fps))
        keys[2] += (keyset[2] - keys[2]) / (3 * (maxframe / fps))
        keys[3] += (keyset[3] - keys[3]) / (3 * (maxframe / fps))

        pygame.draw.rect(screen, (0, 0, 0), (w / 2 - w / 8, -int(w / 100), w / 4, h + int(w / 50)))

        for i in range(7):
            i += 1
            pygame.draw.rect(screen, (200 - ((200 / 7) * i), 200 -((200 / 7) * i), 200 - ((200 / 7) * i)), (w / 2 - w / 8 + w / 32 - (w / 32) * keys[0], (h / 12) * 9 - (h / 30) * keys[0] * i, w / 16 * keys[0], (h / 35) / i))
        for i in range(7):
            i += 1
            pygame.draw.rect(screen, (200 - ((200 / 7) * i), 200 -((200 / 7) * i), 200 - ((200 / 7) * i)), (w / 2 - w / 16 + w / 32 - (w / 32) * keys[1], (h / 12) * 9 - (h / 30) * keys[1] * i, w / 16 * keys[1], (h / 35) / i))
        for i in range(7):
            i += 1
            pygame.draw.rect(screen, (200 - ((200 / 7) * i), 200 -((200 / 7) * i), 200 - ((200 / 7) * i)), (w / 2 + w / 32 - (w / 32) * keys[2], (h / 12) * 9 - (h / 30) * keys[2] * i, w / 16 * keys[2], (h / 35) / i))
        for i in range(7):
            i += 1
            pygame.draw.rect(screen, (200 - ((200 / 7) * i), 200 -((200 / 7) * i), 200 - ((200 / 7) * i)), (w / 2 + w / 16 + w / 32 - (w / 32) * keys[3], (h / 12) * 9 - (h / 30) * keys[3] * i, w / 16 * keys[3], (h / 35) / i))


        pygame.draw.rect(screen, (255, 255, 255), (w / 2 - w / 8, -int(w / 100), w / 4, h+ int(w / 50)), int(w / 100))

        #note========================================================================================================
        for tile_data in t1:
            tile_data[0] = (h / 12) * 9 + (Time - tile_data[1]) * 350 * speed * (h / 900)
            pygame.draw.rect(screen, (255, 255, 255), (w / 2 - w / 8, tile_data[0] - h / 100, w / 16, h / 50))
            if tile_data[0] > h - (h / 9):
                t1.remove(tile_data)

        for tile_data in t2:
            tile_data[0] = (h / 12) * 9 + (Time - tile_data[1]) * 350 * speed * (h / 900)
            pygame.draw.rect(screen, (255, 255, 255), (w / 2 - w / 16, tile_data[0] - h / 100, w / 16, h / 50))
            if tile_data[0] > h - (h / 9):
                t2.remove(tile_data)

        for tile_data in t3:
            tile_data[0] = (h / 12) * 9 + (Time - tile_data[1]) * 350 * speed * (h / 900)
            pygame.draw.rect(screen, (255, 255, 255), (w / 2, tile_data[0] - h / 100, w / 16, h / 50))
            if tile_data[0] > h - (h / 9):
                t3.remove(tile_data)

        for tile_data in t4:
            tile_data[0] = (h / 12) * 9 + (Time - tile_data[1]) * 350 * speed * (h / 900)
            pygame.draw.rect(screen, (255, 255, 255), (w / 2 + w / 16, tile_data[0] - h / 100, w / 16, h / 50))
            if tile_data[0] > h - (h / 9):
                t4.remove(tile_data)
        #note=========================================================================================================

        pygame.draw.rect(screen, (0, 0, 0), (w / 2 - w / 8, (h / 12) * 9, w / 4, h / 2))
        pygame.draw.rect(screen, (255, 255, 255), (w / 2 - w / 8, (h / 12) * 9, w / 4, h / 2), int(h / 100))
        
        screen.blit(rate_text, (w / 2 - rate_text.get_width() / 2, (h / 3) * 2 - rate_text.get_height() / 2))
        
        pygame.display.flip()

        clock.tick(maxframe)

            