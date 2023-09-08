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
pygamenumber = 1
# 화면 타이틀 설정
pygame.display.set_caption("Our Game")


##############################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
current_path = os.path.dirname(__file__) # 현재 파일의 위치 반환
image_path = os.path.join(current_path, "images") # images 폴더 위치 반환

# 배경 만들기
background = pygame.image.load(os.path.join(image_path, "background.png"))

# 캐릭터 만들기
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_speed = 10

# 주민 만들기
citizen_img_idx = pygame.image.load(os.path.join(image_path, "citizen1.png"))
citizen_size = citizen_img_idx.get_rect().size
citizen_width = citizen_size[0]
citizen_height = citizen_size[1]
citizen_x_pos = random.randint(200,(screen_width - citizen_width)/3)
citizen_y_pos = random.randint(0,screen_height)
citizen_speed = random.randint(20,30)
citizen_way = random.randint(0,1)
citizen_images =[
    pygame.image.load(os.path.join(image_path, "citizen1.png")),
    pygame.image.load(os.path.join(image_path, "citizen2.png"))]
#2
citizen1_img_idx = pygame.image.load(os.path.join(image_path, "citizen1.png"))
citizen1_size = citizen1_img_idx.get_rect().size
citizen1_width = citizen1_size[0]
citizen1_height = citizen1_size[1]
citizen1_x_pos = random.randint((screen_width - citizen_width)/3,((screen_width - citizen_width)/3)*2)
citizen1_y_pos = random.randint(0,screen_height)
citizen1_speed = random.randint(20,30)
citizen1_way = random.randint(0,1)
citizen1_images =[
    pygame.image.load(os.path.join(image_path, "citizen1.png")),
    pygame.image.load(os.path.join(image_path, "citizen2.png"))]
#3
citizen2_img_idx = pygame.image.load(os.path.join(image_path, "citizen1.png"))
citizen2_size = citizen2_img_idx.get_rect().size
citizen2_width = citizen2_size[0]
citizen2_height = citizen2_size[1]
citizen2_x_pos = random.randint(((screen_width - citizen_width)/3)*2,screen_width - citizen_width)
citizen2_y_pos = random.randint(0,screen_height)
citizen2_speed = random.randint(20,30)
citizen2_way = random.randint(0,1)
citizen2_images =[
    pygame.image.load(os.path.join(image_path, "citizen1.png")),
    pygame.image.load(os.path.join(image_path, "citizen2.png"))]


#건물
house1_width = 800
house1_height = 240 
house1_x_pos = 0
house1_y_pos = 0
# Font 정의
game_font = pygame.font.Font(None, 40)

game_result = "Game Over"

running = True

# 게임 스타팅
msg = game_font.render("Press the space to Start", True, (255, 255, 0)) # 노란색
msg_rect = msg.get_rect(center=(int(screen_width / 2), int(screen_height / 2)))
screen.blit(msg, msg_rect)
pygame.display.update()
# 클릭 시 게임 시작
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                character_x_pos, character_y_pos = (50, screen_height/2)
                running = False
            if event.key == pygame.K_ESCAPE: #esc 누르면 종료
                running = False
                screen.fill([0, 0, 0])
                msg = game_font.render("Stop Game", True, (255, 0, 0)) # 노란색
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
        if event.type == pygame.KEYDOWN:
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

    if character_x_pos < 0: # 캐릭터 안나가게 하기
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
    citizen_rect = citizen_img_idx.get_rect()
    citizen_rect.left = citizen_x_pos
    citizen_rect.top = citizen_y_pos

    citizen1_rect = citizen1_img_idx.get_rect()
    citizen1_rect.left = citizen1_x_pos
    citizen1_rect.top = citizen1_y_pos

    citizen2_rect = citizen2_img_idx.get_rect()
    citizen2_rect.left = citizen2_x_pos
    citizen2_rect.top = citizen2_y_pos
    #집 rect
    house1_rect = pygame.Rect(house1_x_pos, house1_y_pos, house1_width, house1_height)
    house1_rect_leftline = pygame.Rect(house1_x_pos, house1_y_pos, 1, house1_height)
    house1_rect_rightline = pygame.Rect(house1_width, house1_y_pos, 1, house1_height)
    house1_rect_topline = pygame.Rect(house1_x_pos, house1_y_pos, house1_width, 1)
    house1_rect_bottomline = pygame.Rect(house1_x_pos, house1_height, house1_width, 1)
    
    while (True):
        
        if character_rect.colliderect(citizen_rect):
            character_x_pos = 50
            character_y_pos = screen_height/2
        if character_rect.colliderect(citizen1_rect):
            character_x_pos = 50
            character_y_pos = screen_height/2
        if character_rect.colliderect(citizen2_rect):
            character_x_pos = 50
            character_y_pos = screen_height/2
        if character_x_pos >= screen_width*(90/100) and character_y_pos >= screen_height*(1/4) and character_y_pos <= screen_height*(1/2):
            msg = game_font.render("Clear", True, (255, 255, 0)) # 노란색
            msg_rect = msg.get_rect(center=(int(screen_width / 2), int(screen_height / 2)))
            screen.blit(msg, msg_rect)
            pygame.display.update()

        # 캐릭터 건물 충돌
        if character_rect.colliderect(house1_rect_bottomline):
            character_y_pos = house1_y_pos + house1_height + 1
        if character_rect.colliderect(house1_rect_rightline):
            character_x_pos = house1_x_pos + house1_width + 1
    
        if citizen_y_pos > 0 and citizen_y_pos < screen_height - citizen_height:
            if citizen_way == 0:
                citizen_y_pos = citizen_y_pos + citizen_speed
            if citizen_way == 1:
                citizen_y_pos = citizen_y_pos - citizen_speed

        elif citizen_y_pos <= 0 or citizen_y_pos >= screen_height - citizen_height:        
            if citizen_y_pos <= 0:
                citizen_y_pos = 0.1
                citizen_way = 0
            if citizen_y_pos >= screen_height - citizen_height:
                citizen_y_pos = screen_height - citizen_height - 0.1
                citizen_way = 1

        if citizen_rect.colliderect(house1_rect_bottomline):
            citizen_way = 0

        # 시민1
        if citizen1_y_pos > 0 and citizen1_y_pos < screen_height - citizen1_height:
            if citizen1_way == 0:
                citizen1_y_pos = citizen1_y_pos + citizen1_speed
            if citizen1_way == 1:
                citizen1_y_pos = citizen1_y_pos - citizen1_speed

        elif citizen1_y_pos <= 0 or citizen1_y_pos >= screen_height - citizen1_height:        
            if citizen1_y_pos <= 0:
                citizen1_y_pos = 0.1
                citizen1_way = 0

            if citizen1_y_pos >= screen_height - citizen1_height:
                citizen1_y_pos = screen_height - citizen1_height - 0.1
                citizen1_way = 1

        if citizen1_rect.colliderect(house1_rect_bottomline):
            citizen1_way = 0

        # 시민2
        if citizen2_y_pos > 0 and citizen2_y_pos < screen_height - citizen2_height:
            if citizen2_way == 0:
                citizen2_y_pos = citizen2_y_pos + citizen2_speed
            if citizen2_way == 1:
                citizen2_y_pos = citizen2_y_pos - citizen2_speed

        elif citizen2_y_pos <= 0 or citizen2_y_pos >= screen_height - citizen2_height:        
            if citizen2_y_pos <= 0:
                citizen2_y_pos = 0.1
                citizen2_way = 0

            if citizen2_y_pos >= screen_height - citizen2_height:
                citizen2_y_pos = screen_height - citizen2_height - 0.1
                citizen2_way = 1

        else: # 계속 게임을 진행
            continue # 안쪽 for 문 조건이 맞지 않으면 continue. 바깥 for 문 계속 수행
        break # 안쪽 for 문에서 break 를 만나면 여기로 진입 가능. 2중 for 문을 한번에 탈출

    # for 바깥조건:
    #     바깥동작
    #     for 안쪽조건:
    #         안쪽동작
    #         if 충돌하면:
    #             break
    #     else:
    #         continue
    #     break

    # 5. 화면에 그리기
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(citizen_images[not(citizen_way)], (citizen_x_pos, citizen_y_pos))
    screen.blit(citizen1_images[not(citizen1_way)], (citizen1_x_pos, citizen1_y_pos))
    screen.blit(citizen2_images[not(citizen2_way)], (citizen2_x_pos, citizen2_y_pos))
    pygame.draw.rect(screen, (0, 0, 0), house1_rect, 5)
    pygame.display.update()

# 게임 오버 메시지
msg = game_font.render(game_result, True, (255, 255, 0)) # 노란색
msg_rect = msg.get_rect(center=(int(screen_width / 2), int(screen_height / 2)))
screen.blit(msg, msg_rect)
pygame.display.update()
pygamenumber = 2
# 2초 대기
pygame.time.delay(2000)

pygame.quit()