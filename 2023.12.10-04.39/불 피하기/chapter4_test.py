import pygame
import random
import os
import time
######
pygame.init()

screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))

current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "images")

pygame.display.set_caption("Our game")

clock = pygame.time.Clock()
#####
total_score = 0
level_control = 10
total_level = 0
total_level_list = [10, 13, 16, 19, 21, 24]
#####
game_font = pygame.font.Font(None, 40)

background = pygame.image.load(os.path.join(image_path, "back.png"))
#####
player = pygame.image.load(os.path.join(image_path, "player_small.png"))
player_size = player.get_rect().size
player_width = player_size[0]
player_height = player_size[1]
player_x_pos = (screen_width / 2) - (player_width / 2)
player_y_pos = (screen_height / 2) - (player_height / 2)

player_to_x = 0
player_to_y = 0

player_speed = 0.4
#####
enemy_list = list()
class enemy_class:
    enemy_image = pygame.image.load(os.path.join(image_path, "enemy_small.png"))
    enemy_size = enemy_image.get_rect().size
    enemy_width = enemy_size[0]
    enemy_height = enemy_size[1]
    enemy_spawnPoint = None
    enemy_speed = 0
    enemy_x_pos = 0
    enemy_y_pos = 0
    enemy_rad = 0

    enemy_rect = enemy_image.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    def __init__(self):
        self.enemy_speed = random.choice([1.0, 1.5, 2.0, 2.5, 3.0])
        self.enemy_spawnPoint = random.choice(['UP', 'DOWN', 'LEFT', 'RIGHT'])

        # 스폰 지점 설정
        if self.enemy_spawnPoint == 'LEFT':
            self.enemy_x_pos = - self.enemy_width
            self.enemy_y_pos = random.randint(0, screen_height - self.enemy_height)
            self.enemy_rad = random.choice([(1, 3), (1, 2), (2, 2), (2, 1), (3, 1), (3, 0), (1, -3), (1, -2), (2, -2), (2, -1), (3, -1)])
        elif self.enemy_spawnPoint == 'RIGHT':
            self.enemy_x_pos = screen_width
            self.enemy_y_pos = random.randint(0, screen_height - self.enemy_height)
            self.enemy_rad = random.choice([(-1, 3), (-1, 2), (-2, 2), (-2, 1), (-3, 1), (-3, 0), (-1, -3), (-1, -2), (-2, -2), (-2, -1), (-3, -1)])
        elif self.enemy_spawnPoint == 'UP':
            self.enemy_x_pos = random.randint(0, screen_width - self.enemy_width)
            self.enemy_y_pos = - self.enemy_height
            self.enemy_rad = random.choice([(3, 1), (2, 1), (2, 2), (1, 2), (1, 3), (0, 3), (-3, 1), (-2, 1), (-2, 2), (-1, 2), (-1, 3)])
        elif self.enemy_spawnPoint == 'DOWN':
            self.enemy_x_pos = random.randint(0, screen_width - self.enemy_width)
            self.enemy_y_pos = screen_height
            self.enemy_rad = random.choice([(3, -1), (2, -1), (2, -2), (1, -2), (1, -3), (0, -3), (-3, -1), (-2, -1), (-2, -2), (-1, -2), (-1, -3)])


    def enemy_move(self):
        self.enemy_x_pos += self.enemy_speed * self.enemy_rad[0]
        self.enemy_y_pos += self.enemy_speed * self.enemy_rad[1]
        global total_score
        
        def boundary_UP():
            if self.enemy_y_pos < -self.enemy_height:
                return True
        
        def boundary_DOWN():
            if self.enemy_y_pos > screen_height:
                return True
        
        def boundary_LEFT():
            if self.enemy_x_pos < -self.enemy_width:
                return True
        
        def boundary_RIGHT():
            if self.enemy_x_pos > screen_width:
                return True

        if self.enemy_spawnPoint == 'UP':
            if boundary_LEFT() or boundary_RIGHT() or boundary_DOWN():
                enemy_list.remove(self)

        if self.enemy_spawnPoint == 'DOWN':
            if boundary_LEFT() or boundary_RIGHT() or boundary_UP():
                enemy_list.remove(self)

        if self.enemy_spawnPoint == 'LEFT':
            if boundary_UP() or boundary_DOWN() or boundary_RIGHT():
                enemy_list.remove(self)

        if self.enemy_spawnPoint == 'RIGHT':
            if boundary_UP() or boundary_DOWN() or boundary_LEFT():
                enemy_list.remove(self)

    def enemy_coll(self):
        self.enemy_rect = self.enemy_image.get_rect()
        self.enemy_rect.left = self.enemy_x_pos
        self.enemy_rect.top = self.enemy_y_pos
#####
dragon_front = pygame.image.load(os.path.join(image_path, "dragon_front.png"))
dragon_front_size = dragon_front.get_rect().size
dragon_front_width = dragon_front_size[0]
dragon_front_height = dragon_front_size[1]
dragon_front_x_pos = (screen_width/2) - (dragon_front_width/2)
dragon_front_y_pos = 0

dragon_back = pygame.image.load(os.path.join(image_path, "dragon_back.png"))
dragon_back_size = dragon_back.get_rect().size
dragon_back_width = dragon_back_size[0]
dragon_back_height = dragon_back_size[1]
dragon_back_x_pos = (screen_width/2) - (dragon_back_width/2)
dragon_back_y_pos = (screen_height) - (dragon_back_height)

dragon_left = pygame.image.load(os.path.join(image_path, "dragon_left.png"))
dragon_left_size = dragon_left.get_rect().size
dragon_left_width = dragon_left_size[0]
dragon_left_height = dragon_left_size[1]
dragon_left_x_pos = 0
dragon_left_y_pos = (screen_height/2) - (dragon_left_height/2)

dragon_right = pygame.image.load(os.path.join(image_path, "dragon_right.png"))
dragon_right_size = dragon_right.get_rect().size
dragon_right_width = dragon_right_size[0]
dragon_right_height = dragon_right_size[1]
dragon_right_x_pos = (screen_width) - (dragon_right_width)
dragon_right_y_pos = (screen_height/2) - (dragon_right_height/2)
#####
running = True

while running:
    dt = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_to_x -= player_speed
            if event.key == pygame.K_RIGHT:
                player_to_x += player_speed
            if event.key == pygame.K_UP:
                player_to_y -= player_speed
            if event.key == pygame.K_DOWN:
                player_to_y += player_speed
            
        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                player_to_x = 0
            if event.key in [pygame.K_UP, pygame.K_DOWN]:
                player_to_y = 0
        
    player_x_pos += player_to_x * dt
    player_y_pos += player_to_y * dt


    # 플레이어 경계값
    if player_x_pos < 0:
        player_x_pos = 0
    elif player_x_pos > screen_width - player_width:
        player_x_pos = screen_width - player_width
    if player_y_pos < 0:
        player_y_pos = 0
    elif player_y_pos > screen_height - player_height:
        player_y_pos = screen_height - player_height

    # 적 생성

    if total_score + level_control >= len(enemy_list):
        enemy_list.append(enemy_class())

    # 충돌 처리
    player_rect = player.get_rect()
    player_rect.left = player_x_pos
    player_rect.top = player_y_pos

    dragon_front_rect = dragon_front.get_rect()
    dragon_front_rect.left = dragon_front_x_pos
    dragon_front_rect.top = dragon_front_y_pos

    dragon_back_rect = dragon_back.get_rect()
    dragon_back_rect.left = dragon_back_x_pos
    dragon_back_rect.top = dragon_back_y_pos
    
    dragon_left_rect = dragon_left.get_rect()
    dragon_left_rect.left = dragon_left_x_pos
    dragon_left_rect.top = dragon_left_y_pos
    
    dragon_right_rect = dragon_right.get_rect()
    dragon_right_rect.left = dragon_right_x_pos
    dragon_right_rect.top = dragon_right_y_pos

    for i in enemy_list:
        i.enemy_coll()
        if player_rect.colliderect(i.enemy_rect):
            player_x_pos = (screen_width / 2) - (player_width / 2)
            player_y_pos = (screen_height / 2) - (player_height / 2)
            total_score = 0



    # 화면에 그리기

    screen.blit(background, (0, 0))
    screen.blit(player, (player_x_pos, player_y_pos))

    for i in enemy_list:
        i.enemy_move()
        screen.blit(i.enemy_image, (i.enemy_x_pos, i.enemy_y_pos))
    
    if total_score == 0:
        screen.blit(dragon_front, (dragon_front_x_pos, dragon_front_y_pos))
    
    if player_rect.colliderect(dragon_front_rect):
        total_score = 3

    if total_score == 3:
        screen.blit(dragon_back, (dragon_back_x_pos, dragon_back_y_pos))

    if player_rect.colliderect(dragon_back_rect):
        total_score = 6

    if total_score == 6:
        screen.blit(dragon_left, (dragon_left_x_pos, dragon_left_y_pos))

    if player_rect.colliderect(dragon_left_rect):
        total_score = 9
    
    if total_score == 9:
        screen.blit(dragon_right, (dragon_right_x_pos, dragon_right_y_pos))

    if player_rect.colliderect(dragon_right_rect):
        total_score = 12

    score = game_font.render(str(total_score//3)+" / 4", True, (255, 255, 255))
    screen.blit(score, ((screen_width/20)*18 , screen_height / 25))

    pygame.display.update()