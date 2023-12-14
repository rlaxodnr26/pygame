import os
import pygame
import random
import time
##############################################################
# 기본 초기화 (반드시 해야 하는 것들)
pygame.init()
clock = pygame.time.Clock()

# 화면 크기 설정
screen_width = 1280 # 가로 크기
screen_height = 960 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Our Game")


############################################################## 

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
current_path = os.path.dirname(__file__) # 현재 파일의 위치 반환
image_path = os.path.join(current_path, "images") # images 폴더 위치 반환
totaltime = pygame.time.get_ticks()
# 배경 만들기
background = [0,
    pygame.image.load(os.path.join(image_path, "background1.png")),
    pygame.image.load(os.path.join(image_path, "background2.png")),
    pygame.image.load(os.path.join(image_path, "background3.png")),
    pygame.image.load(os.path.join(image_path, "background4.png")),
    pygame.image.load(os.path.join(image_path, "background5.png")),
    pygame.image.load(os.path.join(image_path, "background6.png"))]
backgroundnumber = 1
chapter = 1

# 캐릭터 만들기
character = pygame.image.load(os.path.join(image_path, "charcter_strate.png"))
character_img_idx = pygame.image.load(os.path.join(image_path, "charcter_strate.png"))

character_image = [
    pygame.image.load(os.path.join(image_path, "charcter_strate.png")),
    pygame.image.load(os.path.join(image_path, "charcter_strate1.png")),
    pygame.image.load(os.path.join(image_path, "charcter_strate2.png"))]

character_image_sword = [
    pygame.image.load(os.path.join(image_path, "charcter_strate_sword.png")),
    pygame.image.load(os.path.join(image_path, "charcter_strate1_sword.png")),
    pygame.image.load(os.path.join(image_path, "charcter_strate2_sword.png"))]

character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_speed = 30
cha_num = 0
deadcount1 = 0
deadcount2 = 0

############################################  챕터 1  ######################################

# 주민 만들기
spdm = 10 # 주민 속도 최소
spdM = 15 # 최대
popul = 4 # 주민 수
pop = popul + 1
for cm in range(1,pop):
    globals()[f'citizen{cm}_img_idx'] = pygame.image.load(os.path.join(image_path, "citizen_forward_1.png"))
    globals()[f'citizen{cm}_size'] = globals()[f'citizen{cm}_img_idx'].get_rect().size
    globals()[f'citizen{cm}_width'] = globals()[f'citizen{cm}_size'][0]
    globals()[f'citizen{cm}_height'] = globals()[f'citizen{cm}_size'][1]
    if cm == 1:
        globals()[f'citizen{cm}_x_pos'] = random.randint(200, int((screen_width - globals()[f'citizen{1}_width'])/popul))
    else:
        globals()[f'citizen{cm}_x_pos'] = random.randint(int((screen_width - globals()[f'citizen{1}_width'])/popul)*(cm-1), int((screen_width - globals()[f'citizen{1}_width'])/popul)*cm)
    globals()[f'citizen{cm}_y_pos'] = random.randint(0,screen_height)
    globals()[f'citizen{cm}_speed'] = random.randint(spdm, spdM)
    globals()[f'citizen{cm}_way'] = random.randint(0,1)
    globals()[f'citizen{cm}_forward_images'] = [
        pygame.image.load(os.path.join(image_path, "citizen_forward_1.png")),
        pygame.image.load(os.path.join(image_path, "citizen_forward_2.png"))]

#건물
house1_width = 800
house1_height = 240 
house1_x_pos = 0
house1_y_pos = 0

house2_width = 550
house2_height = 230
house2_x_pos = screen_width - house2_width
house2_y_pos = screen_height - house2_height

#포인트
point = pygame.image.load(os.path.join(image_path, "point.png"))
point_size = citizen1_img_idx.get_rect().size
point_width = citizen1_size[0]
point_height = citizen1_size[1]
point_rd = random.randint(0,1)
if point_rd == 0:
    point_rd_x = random.randint(point_width, house1_width - point_width)
    point_rd_y = random.randint(house1_height + point_width, screen_height - point_width)
if point_rd == 1:
    point_rd_x = random.randint(house1_width + point_width, screen_width - point_width)
    point_rd_y = random.randint(point_height, screen_height - house2_height - point_height)
point_x_pos = point_rd_x
point_y_pos = point_rd_y
score = 0

##########################################  챕터 2  #################################################

#잔디 만들기
gras = 24 # 주민 수
gra = gras + 1
grasspot = [random.randint(1, 24), random.randint(1, 24), random.randint(1, 24), random.randint(1, 24), random.randint(1, 24), random.randint(1, 24)]
for gp in range(0,6):
    if grasspot[gp] == 18 or grasspot[gp] == 23 or grasspot[gp] == 24:
        grasspot[gp] = int(grasspot[gp]) - random.randint(2,3)
for gm in range(1,gra):
    globals()[f'grass{gm}_img_idx'] = pygame.image.load(os.path.join(image_path, "grass1.png"))
    globals()[f'grass{gm}_size'] = globals()[f'grass{gm}_img_idx'].get_rect().size
    globals()[f'grass{gm}_width'] = globals()[f'grass{gm}_size'][0]
    globals()[f'grass{gm}_height'] = globals()[f'grass{gm}_size'][1]
    if gm > 0 and gm <= 6:
        globals()[f'grass{gm}_x_pos'] = (screen_width/6)*(gm - 1) + 18
        globals()[f'grass{gm}_y_pos'] = 120
    if gm > 6 and gm <= 12: 
        globals()[f'grass{gm}_x_pos'] = (screen_width/6)*(gm - 7) + 18
        globals()[f'grass{gm}_y_pos'] = 120 + (18 + globals()[f'grass{gm}_height'])
    if gm > 12 and gm <= 18:
        globals()[f'grass{gm}_x_pos'] = (screen_width/6)*(gm - 13) + 18
        globals()[f'grass{gm}_y_pos'] = 120 + (18 + globals()[f'grass{gm}_height'])*2
    if gm > 18 and gm <= 24:
        globals()[f'grass{gm}_x_pos'] = (screen_width/6)*(gm - 19) + 18
        globals()[f'grass{gm}_y_pos'] = 120 + (18 + globals()[f'grass{gm}_height'])*3
    globals()[f'grass{gm}_images'] = [
        pygame.image.load(os.path.join(image_path, "grass1.png")),
        pygame.image.load(os.path.join(image_path, "grass2.png")),
        pygame.image.load(os.path.join(image_path, "grass3.png"))]
    globals()[f'grass{gm}_images_number'] = 0

#####################################  챕터 3  ###########################################

sword = pygame.image.load(os.path.join(image_path, "sword.png"))
rock = pygame.image.load(os.path.join(image_path, "rock.png"))
swordkey_1 = [
    pygame.image.load(os.path.join(image_path, "up.png")),
    pygame.image.load(os.path.join(image_path, "down.png")),
    pygame.image.load(os.path.join(image_path, "left.png")),
    pygame.image.load(os.path.join(image_path, "right.png"))]
swordkey_2 = [
    pygame.image.load(os.path.join(image_path, "up.png")),
    pygame.image.load(os.path.join(image_path, "down.png")),
    pygame.image.load(os.path.join(image_path, "left.png")),
    pygame.image.load(os.path.join(image_path, "right.png"))]
swordkey_3 = [
    pygame.image.load(os.path.join(image_path, "up.png")),
    pygame.image.load(os.path.join(image_path, "down.png")),
    pygame.image.load(os.path.join(image_path, "left.png")),
    pygame.image.load(os.path.join(image_path, "right.png"))]
swordkey_4 = [
    pygame.image.load(os.path.join(image_path, "up.png")),
    pygame.image.load(os.path.join(image_path, "down.png")),
    pygame.image.load(os.path.join(image_path, "left.png")),
    pygame.image.load(os.path.join(image_path, "right.png"))]
key_num = [0,1,2,3]

sword_x_pos = 550
sword_y_pos = 500
rock_x_pos = 300
rock_y_pos = 600

barrier1_width = 525
barrier1_height = 625
barrier1_x_pos = 0
barrier1_y_pos = 0

barrier2_width = 1280 - 810
barrier2_height = 625
barrier2_x_pos = 810
barrier2_y_pos = 0

barrier1_rect = pygame.Rect(barrier1_x_pos, barrier1_y_pos, barrier1_width, barrier1_height)
barrier1_rect_leftline = pygame.Rect(barrier1_x_pos, barrier1_y_pos, 1, barrier1_height)
barrier1_rect_rightline = pygame.Rect(barrier1_width, barrier1_y_pos, 1, barrier1_height)
barrier1_rect_topline = pygame.Rect(barrier1_x_pos, barrier1_y_pos, barrier1_width, 1)
barrier1_rect_bottomline = pygame.Rect(barrier1_x_pos, barrier1_height, barrier1_width, 1)

barrier2_rect = pygame.Rect(barrier2_x_pos, barrier2_y_pos, barrier2_width, barrier2_height)
barrier2_rect_leftline = pygame.Rect(barrier2_x_pos, barrier2_y_pos, 1, barrier2_height)
barrier2_rect_rightline = pygame.Rect(barrier2_width, barrier2_y_pos, 1, barrier2_height)
barrier2_rect_topline = pygame.Rect(barrier2_x_pos, barrier2_y_pos, barrier2_width, 1)
barrier2_rect_bottomline = pygame.Rect(barrier2_x_pos, barrier2_height, barrier2_width, 1)

swordwin = 0

###############################################챕터 4##########################################

total_score = 0
level_control = 10
total_level = 0
total_level_list = [10, 13, 16, 19, 21, 24]

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



###########################################################################################################
# Font 정의
game_font = pygame.font.Font(None, 40)

running = True

# 게임 스타팅
msg = game_font.render("Press the space to Start", True, (255, 255, 0)) # 시작 화면
msg_rect = msg.get_rect(center=(int(screen_width / 2), int(screen_height / 2)))
screen.blit(msg, msg_rect)
pygame.display.update()
# 클릭 시 게임 시작
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: # 스페이스를 누르면 시작
                character_x_pos, character_y_pos = (50, screen_height/2)
                running = False

            if event.key == pygame.K_ESCAPE: #esc 누르면 종료
                running = False
                screen.fill([0, 0, 0])
                msg = game_font.render("Stop Game", True, (255, 0, 0))
                msg_rect = msg.get_rect(center=(int(screen_width / 2), int(screen_height / 2)))
                screen.blit(msg, msg_rect)
                pygame.display.update()
                pygame.time.delay(800)
                pygame.quit()
to_x = 0
to_y = 0
running = True
walking = False
delay = 100
interval = 500
pygame.key.set_repeat(delay, interval)

while running:
    dt = clock.tick(60)
    # 이벤트
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.time.delay(800)
            pygame.quit()
        if event.type == pygame.KEYDOWN: # 방향키로 이동
            if event.key == pygame.K_LEFT:
                to_x = 0 - character_speed
                walking = True
                key_press = 2
            if event.key == pygame.K_RIGHT:
                to_x = character_speed
                walking = True
                key_press = 3
            if event.key == pygame.K_UP:
                to_y = 0 - character_speed
                walking = True
                key_press = 0
            if event.key == pygame.K_DOWN:
                to_y = character_speed
                walking = True
                key_press = 1
            if event.key == pygame.K_SPACE:
                if chapter == 3:
                    sword_y_pos -= 10
                key_press = 4
            

            if event.key == pygame.K_ESCAPE: #esc 누르면 종료
                running = False
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
                walking = False
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
                walking = False

        if walking == True:
            cha_num += 1
            if cha_num > 2:
                cha_num = 1
        elif walking == False:
            cha_num = 0
    character_x_pos += to_x
    character_y_pos += to_y 
    #캐릭터 안나가게 하기
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # 캐릭터 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    if chapter == 1:
        #주민 rect 정보 업데이트
        for cm1 in range(1,pop):
            globals()[f'citizen{cm1}_rect'] = globals()[f'citizen{cm1}_img_idx'].get_rect()
            globals()[f'citizen{cm1}_rect'].left =  globals()[f'citizen{cm1}_x_pos']
            globals()[f'citizen{cm1}_rect'].top =  globals()[f'citizen{cm1}_y_pos']    
        #별 rect
        point_rect = point.get_rect()
        point_rect.left = point_x_pos
        point_rect.top = point_y_pos

        #집 rect
        house1_rect = pygame.Rect(house1_x_pos, house1_y_pos, house1_width, house1_height)
        house1_rect_leftline = pygame.Rect(house1_x_pos, house1_y_pos, 1, house1_height)
        house1_rect_rightline = pygame.Rect(house1_width, house1_y_pos, 1, house1_height)
        house1_rect_topline = pygame.Rect(house1_x_pos, house1_y_pos, house1_width, 1)
        house1_rect_bottomline = pygame.Rect(house1_x_pos, house1_height, house1_width, 1)

        house2_rect = pygame.Rect(house2_x_pos, house2_y_pos, house2_width, house2_height)
        house2_rect_leftline = pygame.Rect(house2_x_pos, house2_y_pos, 1, house2_height)
        house2_rect_rightline = pygame.Rect(house2_width, house2_y_pos, 1, house2_height)
        house2_rect_topline = pygame.Rect(house2_x_pos, house2_y_pos, house2_width, 1)
        house2_rect_bottomline = pygame.Rect(house2_x_pos, house2_height, house2_width, 1)

    while (True):
######################################################### 챕터 1 ####################################################################
        totaltime = pygame.time.get_ticks()
        if chapter == 1: 
        # 점수 표시
            msg = game_font.render(str(score)+" / 5", True, (255, 255, 0))
            screen.blit(msg, ((screen_width/20)*18 , screen_height / 25))
            pygame.display.update()

        # 캐릭터와 주민이 닿았을 때 캐릭터 위치 & 점수 감소
            for cm2 in range(1,pop):
                if character_rect.colliderect(globals()[f'citizen{cm2}_rect']):
                    character_x_pos = 50
                    character_y_pos = screen_height/2
                    if score < 5:
                        score -= 1
                        deadcount1 += 1 
            if score <= 0:
                score = 0
            elif score >= 5:
                score = 5
                if character_x_pos >= screen_width*(90/100) and character_y_pos >= screen_height*(1/4) and character_y_pos <= screen_height*(1/2):
                    character_x_pos = 0
                    character_y_pos = 0
                    chapter = 2
                    screen.fill((0,0,0))
                    msg = pygame.font.Font(None, 50).render("Clear!     Clear Time : " + str(totaltime/1000), True, (255, 255, 0))
                    msg_rect = msg.get_rect(center=(int(screen_width / 2), int(screen_height / 2)))
                    screen.blit(msg, msg_rect)
                    pygame.display.update()
                    pygame.time.delay(1500)
                    
            #별 충돌
            if score <= 5:
                if character_rect.colliderect(point_rect):
                    point_rd = random.randint(0,1)
                    score += 5
                    if point_rd == 0:
                        point_rd_x = random.randint(point_width, house1_width - point_width)
                        point_rd_y = random.randint(house1_height + point_width, screen_height - point_width)
                    if point_rd == 1:
                        point_rd_x = random.randint(house1_width + point_width, screen_width - point_width)
                        point_rd_y = random.randint(point_height, screen_height - house2_height - point_height)
                    point_x_pos = point_rd_x
                    point_y_pos = point_rd_y
            if score >= 5:
                point_x_pos = screen_width * 2
                point_y_pos = screen_height * 2

            # 캐릭터 건물 충돌
            if character_rect.colliderect(house1_rect_bottomline):
                character_y_pos = house1_y_pos + house1_height + 1
            if character_rect.colliderect(house1_rect_rightline):
                character_x_pos = house1_x_pos + house1_width + 1

            if character_rect.colliderect(house2_rect_topline):
                character_y_pos = house2_y_pos - character_height - 1
            if character_rect.colliderect(house2_rect_leftline):
                character_x_pos = house2_x_pos - character_width - 1

            # 시민 충돌
            cm3 = 1
            while cm3 < pop:
                if globals()[f'citizen{cm3}_y_pos'] > 0 and globals()[f'citizen{cm3}_y_pos'] < screen_height - globals()[f'citizen{cm3}_height']:
                    if globals()[f'citizen{cm3}_way'] == 0:
                        globals()[f'citizen{cm3}_y_pos'] = globals()[f'citizen{cm3}_y_pos'] + globals()[f'citizen{cm3}_speed']
                    if globals()[f'citizen{cm3}_way'] == 1:
                        globals()[f'citizen{cm3}_y_pos'] = globals()[f'citizen{cm3}_y_pos'] - globals()[f'citizen{cm3}_speed']
                    if globals()[f'citizen{cm3}_rect'].colliderect(house1_rect_bottomline):
                        globals()[f'citizen{cm3}_way'] = 0
                    elif globals()[f'citizen{cm3}_rect'].colliderect(house2_rect_topline):
                        globals()[f'citizen{cm3}_way'] = 1
                # 시민 벽 충돌
                elif globals()[f'citizen{cm3}_y_pos'] <= 0 or globals()[f'citizen{cm3}_y_pos'] >= screen_height - globals()[f'citizen{cm3}_height']:        
                    if globals()[f'citizen{cm3}_y_pos'] <= 0:
                        globals()[f'citizen{cm3}_y_pos'] = 0.1
                        globals()[f'citizen{cm3}_way'] = 0

                    if globals()[f'citizen{cm3}_y_pos'] >= screen_height - globals()[f'citizen{cm3}_height']:
                        globals()[f'citizen{cm3}_y_pos'] = screen_height - globals()[f'citizen{cm3}_height'] - 0.1
                        globals()[f'citizen{cm3}_way'] = 1
                cm3 += 1
                if cm3 == pop:
                    break
######################################################### 챕터 2 ########################################################################################        
        elif chapter == 2:
            pygame.display.update()
            backgroundnumber = 2
            #잔디 rect
            for gm1 in range(1,gra):
                globals()[f'grass{gm1}_rect'] = globals()[f'grass{gm1}_img_idx'].get_rect()
                globals()[f'grass{gm1}_rect'].left =  globals()[f'grass{gm1}_x_pos']
                globals()[f'grass{gm1}_rect'].top =  globals()[f'grass{gm1}_y_pos']

            #잔디 충돌
            for gm2 in range(1,gra):
                if character_rect.colliderect(globals()[f'grass{gm2}_rect']):
                    if gm2 in grasspot:
                        globals()[f'grass{gm2}_images_number'] = 1
                        screen.blit(globals()[f'grass{gm2}_images'][int(globals()[f'grass{gm2}_images_number'])], (globals()[f'grass{gm2}_x_pos'], globals()[f'grass{gm2}_y_pos']))
                        pygame.display.update()
                        pygame.time.delay(850)
                        character_x_pos = character_width
                        character_y_pos = 20
                        deadcount2 += 1
                        for gm3 in range(1,gra):
                            globals()[f'grass{gm3}_images_number'] = 0
                            if gm3 > 0 and gm3 <= 6:
                                globals()[f'grass{gm3}_x_pos'] = (screen_width/6)*(gm3 - 1) + 18
                                globals()[f'grass{gm3}_y_pos'] = 120
                            if gm3 > 6 and gm3 <= 12: 
                                globals()[f'grass{gm3}_x_pos'] = (screen_width/6)*(gm3 - 7) + 18
                                globals()[f'grass{gm3}_y_pos'] = 120 + (18 + globals()[f'grass{gm3}_height'])
                            if gm3 > 12 and gm3 <= 18:
                                globals()[f'grass{gm3}_x_pos'] = (screen_width/6)*(gm3 - 13) + 18
                                globals()[f'grass{gm3}_y_pos'] = 120 + (18 + globals()[f'grass{gm3}_height'])*2
                            if gm3 > 18 and gm3 <= 24:
                                globals()[f'grass{gm3}_x_pos'] = (screen_width/6)*(gm3 - 19) + 18
                                globals()[f'grass{gm3}_y_pos'] = 120 + (18 + globals()[f'grass{gm3}_height'])*3
                    else:
                        globals()[f'grass{gm2}_images_number'] = 2
                        globals()[f'grass{gm2}_x_pos'] = -100
                        globals()[f'grass{gm2}_y_pos'] = -100
            if event.type == pygame.KEYDOWN:
                if deadcount2 >= 3:
                    if event.key == pygame.K_r:
                            grasspot = [random.randint(1, 24), random.randint(1, 24), random.randint(1, 24), random.randint(1, 24), random.randint(1, 24), random.randint(1, 24)]
                            for gp in range(0,6):
                                if grasspot[gp] == 18 or grasspot[gp] == 23 or grasspot[gp] == 24:
                                    grasspot[gp] = int(grasspot[gp]) - random.randint(2,3)
            if character_x_pos >= 1150 and character_y_pos >= 850:
                screen.fill((0,0,0))
                msg = pygame.font.Font(None, 50).render("Clear!     Clear Time : " + str(totaltime/1000), True, (255, 255, 0))
                msg_rect = msg.get_rect(center=(int(screen_width / 2), int(screen_height / 2)))
                screen.blit(msg, msg_rect)
                pygame.display.update()
                pygame.time.delay(1000)
                backgroundnumber = 3
                character_x_pos = 0
                character_y_pos = 715
                chapter = 3
################################################## 챕터 3 ###################################################################   
        elif chapter == 3:  #칼 뽑기
            swordscore = 0
            if character_rect.colliderect(barrier1_rect_bottomline):
                character_y_pos = barrier1_y_pos + barrier1_height + 1
            if character_rect.colliderect(barrier1_rect_rightline):
                character_x_pos = barrier1_x_pos + barrier1_width + 1
            if character_rect.colliderect(barrier2_rect_bottomline):
                character_y_pos = barrier2_y_pos + barrier2_height + 1
            if character_rect.colliderect(barrier2_rect_leftline):
                character_x_pos = barrier2_x_pos - 1
            if character_y_pos >= 775:
                character_y_pos = 775
                
            if character_x_pos >= 510 and character_x_pos <= 740 and character_y_pos >= 520 and character_y_pos <= 560:
                screen.fill((0, 0, 0))
                msg = pygame.font.Font(None, 70).render("Entering...", True, (255, 255, 0))
                msg_rect = msg.get_rect(center=(int(screen_width / 2), int(screen_height / 2)))
                screen.blit(msg, msg_rect)
                pygame.display.update()
                pygame.time.delay(800)
                backgroundnumber = 4

            if backgroundnumber == 4:
                character_x_pos = 0
                character_y_pos = 1200
                if event.type == pygame.KEYDOWN:
                    if key_press == key_num[0]:
                        pygame.time.delay(150)
                        key_num[0] = key_num[1]
                        key_num[1] = key_num[2]
                        key_num[2] = key_num[3]
                        key_num[3] = random.randint(0,3)

                        sword_y_pos -= 200
                    elif key_press != key_num[0]:
                        sword_y_pos += 5
                    if sword_y_pos >= 380:
                        sword_y_pos = 380
                    if sword_y_pos <= -220:
                        swordscore = 100
                        sword_y_pos = -220
                        swordwin = 1
                        backgroundnumber = 5
                        character_image = character_image_sword
                        pygame.time.delay(100)
                        msg = pygame.font.Font(None, 100).render("Clear!", True, (255, 255, 0))
                        msg_rect = msg.get_rect(center=(int(screen_width / 2), int(screen_height / 2)))
                        screen.blit(msg, msg_rect)
                        pygame.display.update()
                        pygame.time.delay(900)
                        character_x_pos = 630
                        character_y_pos = 695
                else:
                    sword_y_pos += 1
                    if sword_y_pos >= 380:
                        sword_y_pos = 380
                swordscore = ((sword_y_pos - 380)/600) * 10

            if sword_y_pos <= 300:
                if character_y_pos <= 635:
                    character_y_pos = 635
            if character_x_pos >= 1230:
                if backgroundnumber == 5:
                    msg = pygame.font.Font(None, 50).render("Clear!    clear time : " + str(totaltime/1000), True, (255, 255, 0))
                    msg_rect = msg.get_rect(center=(int(screen_width / 2), int(screen_height / 2)))
                    screen.blit(msg, msg_rect)
                    pygame.display.update()
                    pygame.time.delay(900)
                    character_x_pos, character_y_pos = (screen_width/2, screen_height/2)
                    chapter = 4
                else:
                    msg = pygame.font.Font(None, 50).render("You need weapon!", True, (255, 255, 0))
                    msg_rect = msg.get_rect(center=(int(screen_width / 2), int(screen_height / 2)))
                    screen.blit(msg, msg_rect)
                    pygame.display.update()
            pygame.display.update()

        ############### 챕터 4 #############   
        elif chapter == 4:
            backgroundnumber = 6
            character_speed = 10

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
                if character_rect.colliderect(i.enemy_rect):
                    character_x_pos = (screen_width / 2) - (character_width / 2)
                    character_y_pos = (screen_height / 2) - (character_height / 2)
                    total_score = 0

            if total_score >= total_level_list[total_level]:
                total_level += 1

            if total_level + level_control >= len(enemy_list):
                enemy_list.append(enemy_class())
            pygame.display.update()

        else:
            continue
        break

##############################################출력#####################################################################################
    screen.blit(background[backgroundnumber], (0, 0))
    if chapter == 1:
        if score >= 5:
            pygame.draw.rect(screen, (255,255,0), (1120, 290, 300, 165))
        for cm1 in range(1,pop):
            screen.blit(globals()[f'citizen{cm1}_forward_images'][not(globals()[f'citizen{cm1}_way'])], (globals()[f'citizen{cm1}_x_pos'], globals()[f'citizen{cm1}_y_pos']))
        screen.blit(point, (point_x_pos, point_y_pos))
        msg = game_font.render(str(score)+" / 5", True, (255, 255, 0))
        screen.blit(msg, ((screen_width/20)*18 , screen_height / 25))
        screen.blit(character_image[cha_num], (character_x_pos, character_y_pos))
        pygame.display.update()

    if chapter == 2:
        for gm4 in range(1,gra):
            screen.blit(globals()[f'grass{gm4}_images'][int(globals()[f'grass{gm4}_images_number'])], (globals()[f'grass{gm4}_x_pos'], globals()[f'grass{gm4}_y_pos']))

    if backgroundnumber  ==  4:
        screen.blit(sword, (sword_x_pos, sword_y_pos))
        screen.blit(rock, (rock_x_pos, rock_y_pos))
        screen.blit(swordkey_1[key_num[0]], (300, 780))
        screen.blit(swordkey_2[key_num[1]], (520, 780))
        screen.blit(swordkey_3[key_num[2]], (700, 780))
        screen.blit(swordkey_4[key_num[3]], (880, 780))
        msg = pygame.font.Font(None, 80).render(str(int(-swordscore))+"%", True, (0, 0, 0))
        screen.blit(msg, ((screen_width/20)*15 , screen_height / 20))
        pygame.display.update()

    if backgroundnumber == 6:
    
            if total_score == 0:
                screen.blit(dragon_front, (dragon_front_x_pos, dragon_front_y_pos))
            if key_press == 4:
                if character_rect.colliderect(dragon_front_rect):
                    total_score = 3
                if character_rect.colliderect(dragon_back_rect):
                    total_score = 6
                if character_rect.colliderect(dragon_left_rect):
                    total_score = 9
                if character_rect.colliderect(dragon_right_rect):
                    total_score = 12
               

            if total_score == 3:
                screen.blit(dragon_back, (dragon_back_x_pos, dragon_back_y_pos))

            if total_score == 6:
                screen.blit(dragon_left, (dragon_left_x_pos, dragon_left_y_pos))

            if total_score == 9:
                screen.blit(dragon_right, (dragon_right_x_pos, dragon_right_y_pos))
            enemy_count = game_font.render(str(len(enemy_list)), True, (255, 255, 255))
            screen.blit(enemy_count, (10, 10))

            for i in enemy_list:
                i.enemy_move()
                screen.blit(i.enemy_image, (i.enemy_x_pos, i.enemy_y_pos))
            if total_score >= 12:
                msg = pygame.font.Font(None, 50).render("Clear!    clear time : " + str(totaltime/1000), True, (255, 255, 0))
                msg_rect = msg.get_rect(center=(int(screen_width / 2), int(screen_height / 2)))
                screen.blit(msg, msg_rect)
                print(totaltime)
                pygame.display.update()
                pygame.time.delay(2000)
                pygame.quit()
            score = game_font.render(str(int(total_score)), True, (255, 255, 255))
            screen.blit(score, (screen_width - 50, 10))


    if chapter == 1:
        msg = game_font.render(str(totaltime/1000), True, (255, 255, 0))
        screen.blit(msg, ((screen_width/20)*2 , screen_height / 25))
    else:
        msg = game_font.render(str(totaltime/1000), True, (255, 255, 0))
        screen.blit(msg, ((screen_width/20)*18 , screen_height / 25))
 

    screen.blit(character_image[cha_num], (character_x_pos, character_y_pos))
    pygame.display.update()

# 게임 오버 메시지
msg = game_font.render("Game_over", True, (255, 255, 0)) # 노란색
msg_rect = msg.get_rect(center=(int(screen_width / 2), int(screen_height / 2)))
screen.blit(msg, msg_rect)
pygame.display.update()
# 2초 대기
pygame.time.delay(2000)

pygame.quit()