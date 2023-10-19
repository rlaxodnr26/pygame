import os
import pygame
import random
##############################################################
# 기본 초기화 (반드시 해야 하는 것들)
pygame.init()

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

# 배경 만들기
background = pygame.image.load(os.path.join(image_path, "background.png"))

# 캐릭터 만들기
character = pygame.image.load(os.path.join(image_path, "charcter_strate.png"))
character_img_idx = pygame.image.load(os.path.join(image_path, "charcter_strate.png"))
character_image = pygame.image.load(os.path.join(image_path, "charcter_strate.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_speed = 10

# 주민 만들기

spdm = 10 # 주민 속도 최소
spdM = 15 # 최대
popul = 6 # 주민 수
pop = popul + 1
for cm in range(1,pop):
    globals()[f'citizen{cm}_img_idx'] = pygame.image.load(os.path.join(image_path, "citizen1.png"))
    globals()[f'citizen{cm}_size'] = globals()[f'citizen{cm}_img_idx'].get_rect().size
    globals()[f'citizen{cm}_width'] = globals()[f'citizen{cm}_size'][0]
    globals()[f'citizen{cm}_height'] = globals()[f'citizen{cm}_size'][1]
    if cm == 1:
        globals()[f'citizen{cm}_x_pos'] = random.randint(200, ((screen_width - globals()[f'citizen{1}_width'])/popul))
    else:
        globals()[f'citizen{cm}_x_pos'] = random.randint(((screen_width - globals()[f'citizen{1}_width'])/popul)*(cm-1), ((screen_width - globals()[f'citizen{1}_width'])/popul)*cm)
    globals()[f'citizen{cm}_y_pos'] = random.randint(0,screen_height)
    globals()[f'citizen{cm}_speed'] = random.randint(spdm, spdM)
    globals()[f'citizen{cm}_way'] = random.randint(0,1)
    globals()[f'citizen{cm}_images'] = [
        pygame.image.load(os.path.join(image_path, "citizen1.png")),
        pygame.image.load(os.path.join(image_path, "citizen2.png"))]
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
                pygame.time.delay(2000)
                pygame.quit()
to_x = 0
to_y = 0
running = True
while running:
    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        if event.type == pygame.KEYDOWN: # 방향키로 이동
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            if event.key == pygame.K_RIGHT:
                to_x += character_speed
            if event.key == pygame.K_UP:
                to_y -= character_speed
            if event.key == pygame.K_DOWN:
                to_y += character_speed

            if event.key == pygame.K_ESCAPE: #esc 누르면 종료
                running = False
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
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

    #주민 rect 정보 업데이트
    for cm1 in range(1,pop):
        globals()[f'citizen{cm1}_rect'] = globals()[f'citizen{cm1}_img_idx'].get_rect()
        globals()[f'citizen{cm1}_rect'].left =  globals()[f'citizen{cm1}_x_pos']
        globals()[f'citizen{cm1}_rect'].top =  globals()[f'citizen{cm1}_y_pos']

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
        if score <= 0:
            score = 0
        elif score >= 5:
            score = 5
            if character_x_pos >= screen_width*(90/100) and character_y_pos >= screen_height*(1/4) and character_y_pos <= screen_height*(1/2):
                screen.fill([0, 0, 0])
                msg = game_font.render("Clear", True, (255, 255, 0))
                msg_rect = msg.get_rect(center=(int(screen_width / 2), int(screen_height / 2)))
                screen.blit(msg, msg_rect)
                pygame.display.update()
                pygame.time.delay(2000)
                pygame.quit()
                
        #별 충돌
        if score <= 5:
            if character_rect.colliderect(point_rect):
                point_rd = random.randint(0,1)
                score += 1
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

        # 시민1 충돌
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
            # 시민1 벽 충돌
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
        
                
        else:
            continue
        break

    # 5. 화면에 그리기
    screen.blit(background, (0, 0))
    screen.blit(character_image, (character_x_pos, character_y_pos))
    for cm1 in range(1,pop):
        screen.blit(globals()[f'citizen{cm1}_images'][not(globals()[f'citizen{cm1}_way'])], (globals()[f'citizen{cm1}_x_pos'], globals()[f'citizen{cm1}_y_pos']))
    screen.blit(point, (point_x_pos, point_y_pos))
    pygame.display.update()

# 게임 오버 메시지
msg = game_font.render("Game_over", True, (255, 255, 0)) # 노란색
msg_rect = msg.get_rect(center=(int(screen_width / 2), int(screen_height / 2)))
screen.blit(msg, msg_rect)
pygame.display.update()

# 2초 대기
pygame.time.delay(2000)

pygame.quit()