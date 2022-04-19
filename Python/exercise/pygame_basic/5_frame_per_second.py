import pygame

pygame.init() # 초기화 (반드시 필요)

#화면 크기 설정
screen_width = 480 #가로 크기
screen_hight = 640 #세로 크기
screen = pygame.display.set_mode((screen_width, screen_hight))

#화면 타이틀 설정
pygame.display.set_caption("Nado Game") #게임 이름

#FPS
clock = pygame.time.Clock()

#배경 이미지 불러오기
background = pygame.image.load("C:\\Users\\skxog\\Desktop\\PythonWorkSpace\\pygame_basic\\background.png")

#캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:\\Users\\skxog\\Desktop\\PythonWorkSpace\\pygame_basic\\character.png")
character_size = character.get_rect().size #이미지 크기를 구해옴
character_width = character_size[0] #캐릭터의 가로 크기
character_height = character_size[1] #캐릭터의 세로 크기
character_x_pos = screen_width / 2 - (character_width / 2) # 화면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos = screen_hight - character_height #화면 세로 크기 가장 아래에 해당하는 곳에 위치

#이동할 좌표
to_x = 0
to_y = 0

#이동 속도
character_speed = 0.6

#이벤트 루프
running = True #게임이 진행중인가 확인
while running:
    dt = clock.tick(10) #게임화면의 초당 프레임 수를 설정

    #캐릭터가 100만큼 이동을 해야함
    #10 fps : 1초 동안에 10번 동작 - > 1번에 몇 만큼 이동? 10만큼! 10 * 10 = 100
    #20 fps : 1초 동안에 20번 동작 - > 1번에 몇 만큼 이동? 5만큼! 5 * 20 = 100
    
    for event in pygame.event.get(): #어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생하였는가?
            running = False #게임이 진행중이 아님

        if event.type == pygame.KEYDOWN: #키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed

        if event.type == pygame.KEYUP: #방향키를 뗴면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    #세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_hight - character_height:
        character_y_pos = screen_hight - character_height

    screen.blit(background, (0,0))

    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update() #게임화면을 다시 그리기

#pygame 종료
pygame.quit()