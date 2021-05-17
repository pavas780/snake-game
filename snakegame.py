import pygame
import random
import os
pygame.mixer.init()


x=pygame.init()
screenwidth=900
screenheight=600
window=pygame.display.set_mode((screenwidth,screenheight))
pygame.display.set_caption('GTA 6')
pygame.display.update()
bg=pygame.image.load('2167042.jpg')
bg=pygame.transform.scale(bg,(screenwidth,screenheight)).convert_alpha()
bg1=pygame.image.load('1262596.jpg')
bg1=pygame.transform.scale(bg1,(screenwidth,screenheight)).convert_alpha()
bg2=pygame.image.load('216.png')
bg2=pygame.transform.scale(bg2,(screenwidth,screenheight)).convert_alpha()
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)
grey=(122,122,122)
def textscreen(text,color,x,y):
    screen_text=font.render(text,True,color)
    window.blit(screen_text,[x,y])

def plotsnake(window,black,snake_list,size):
    for x,y in snake_list:
        pygame.draw.rect(window,black,[x,y,snake_size,snake_size])
clock = pygame.time.Clock()
snake_size = 20
font = pygame.font.SysFont(str(None), 55)
def welcome():
    exit_game=False
    pygame.mixer.music.load('GTA V - Welcome to Los Santos Soundtrack - Intro_Theme song(MP3_160K).mp3')
    pygame.mixer.music.play()

    while not exit_game:
        window.fill((220,220,220))
        window.blit(bg,(0,0))
        textscreen("WELCOME TO WHITE SNAKE",white,200,100)
        textscreen("PRESS ENTER TO PLAY!!",white, 200, 300)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:

                    gameloop()
        pygame.display.update()
        clock.tick(60)


def gameloop():
    snake_list = []
    snakelength = 1
    #
    exit_game = False
    game_over = False

    #

    velocity_x = 0
    velocity_y = 0

    snake_x = 100
    snake_y = 100
    in_velocity = 5
    snake_size = 20
    score = 0
    food_x = random.randint(20, 900 / 1.5)
    food_y = random.randint(20, 600 / 1.5)
    fps = 60
    if(not os.path.exists("hiscore.txt")):
        with open('hiscore.txt', 'w') as f:
            f.write('0')

    with open('hiscore.txt', 'r') as f:
        hiscore = f.read()
    while not exit_game:
        if game_over==True:
            pygame.mixer.music.load('beep-03.mp3')
            pygame.mixer.music.play()

            with open('hiscore.txt', 'w') as f:
                f.write(str(hiscore))
            window.fill(white)
            window.blit(bg2,(0,0))
            textscreen("GAME-OVER!!",red,300,0)
            textscreen('PRESS ENTER TO CONTINUE..', black, 200, 100)
            textscreen(f'SCORE: {score}',black, 350, 400)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True

                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        welcome()
        else:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        velocity_x=in_velocity
                        velocity_y=0

                    if event.key==pygame.K_LEFT:
                        velocity_x-=in_velocity
                        velocity_y = 0
                    if event.key==pygame.K_UP:
                        velocity_y-=in_velocity
                        velocity_x = 0
                    if event.key==pygame.K_DOWN:
                        velocity_y=in_velocity
                        velocity_x = 0
                    if event.key==pygame.K_q:
                        score+=10

            snake_x+=velocity_x
            snake_y+=velocity_y
            if abs(snake_x-food_x)<20 and abs(snake_y-food_y)<20:
                pygame.mixer.music.load('beep-07.mp3')
                pygame.mixer.music.play()
                score+=10
                food_x = random.randint(20, 900 / 1.5)
                food_y = random.randint(20, 600 / 1.5)
                snakelength+=2
                if score>int(hiscore):
                    hiscore=score

            window.fill(grey)
            textscreen("SCORE: "+ str(score)+'    HISCORE: '+str(hiscore),white,250,5)
            pygame.draw.rect(window,red, [food_x,food_y ,snake_size, snake_size])

            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append((head))
            if len(snake_list)>snakelength:
                del snake_list[0]
            if head in snake_list[:-1]:
                game_over=True
                pygame.mixer.music.load('beep-03.mp3')
                pygame.mixer.music.play()
            if snake_x<0 or snake_x>screenwidth or snake_y<0 or snake_y>screenheight:
                pygame.mixer.music.load('beep-03.mp3')
                pygame.mixer.music.play()
                game_over=True
            plotsnake(window,white,snake_list,snake_size)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()
welcome()
