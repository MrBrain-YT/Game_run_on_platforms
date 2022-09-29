import pygame
import random
pygame.init()

sc = pygame.display.set_mode((500, 700))
pygame.display.set_caption('run on platforms')
clock = pygame.time.Clock()
counter = 0
grass = pygame.image.load("sprites/Start_grass.bmp")
ground = pygame.image.load("sprites/Start_earth.bmp")
background = pygame.image.load("sprites/Back.bmp")

open_jump = True
hero_jump_y = 450
jump_fors = -35
move = jump_fors + 1
jump = 1
# restart
restart = 1
# game score
heart_score = 3
score = 0
score_for_speed_up = 0
# platforms list
space_platforms = 20
oll_delit_platforms = 0
platforms = ['mini', 'normal']
# speed platforms
speed_platforms = 1
old_speed_platforms = 1
old_speed = 1
max_speed = 5
speed = 5
speed_x_platform_start = -25
speed_x_platforms_random = 225
speed_x_platforms_random_two = 225
speed_x_platforms_random_three = 225
speed_x_platforms_mini_two = 410
speed_x_platforms_mini_three = 410
speed_x_platforms_mini = 410
x_text = 442
# x platforms
x_hero = 150
x_up = 400
x_tutorial_text_and = 357
x_space = 40
x_tutorial_text = 150
x_score = 20
x_enter = 500
x_enter2 = 500
x_restart = 500
cord_x_start = -25
cord_x_normal = 225
cord_x_mini = 410
x_platforms_start = 0
x_platforms_random = 500
x_platforms_random_two = 500
x_platforms_random_three = 500
x_platforms_mini_two = 500
x_platforms_mini_three = 500
x_platforms_mini = 500
# y platforms
y_tutorial_text_and = 635
y_space = 635
y_score = 20
y_enter = 700
y_enter2 = 700
y_restart = 700
y_heart = 10
y_text = 33
y_platforms = 0
y_platforms_start = 500
y_oll_platforms_old = y_platforms_start
y_platforms_random = 500
y_platforms_random_two = 500
y_platforms_random_three = 500
y_platforms_mini_two = 500
y_platforms_mini_three = 500
y_platforms_mini = 500
# delite platforms
delite_platforms = -500
delite_mini_platforms = -68
delite_normal_platforms = -250
delite_platforms_start = 600
# load fonts
score_font = pygame.font.Font('fonts/minecraft.ttf', 40)
score_text = score_font.render(str(score), 1, (255, 255, 255))
heart_font = pygame.font.Font('fonts/minecraft.ttf', 40)
heart_text = heart_font.render(str(heart_score), 1, (0, 0, 0))
restart_font = pygame.font.Font('fonts/minecraft.ttf', 40)
restart_text = restart_font.render("restart", 1, (255, 69, 0), (105, 105, 105))
pos = restart_text.get_rect()
tutorial_font = pygame.font.Font('fonts/minecraft.ttf', 45)
tutorial_text = tutorial_font.render("Jump to", 1, (218, 165, 32))
tutorial_text_3d = tutorial_font.render("Jump to", 1, (184, 134, 11))
tutorial_text_and = tutorial_font.render("&", 1, (218, 165, 32))
tutorial_text_and_3d = tutorial_font.render("&", 1, (184, 134, 11))
# load animations
runing = True
run1 = pygame.image.load("sprites/animation/Run.bmp")
run1.set_colorkey((255, 255, 255))
run2 = pygame.image.load("sprites/animation/Run2.bmp")
run2.set_colorkey((255, 255, 255))
run3 = pygame.image.load("sprites/animation/Run3.bmp")
run3.set_colorkey((255, 255, 255))
run4 = pygame.image.load("sprites/animation/Run4.bmp")
run4.set_colorkey((255, 255, 255))
run5 = pygame.image.load("sprites/animation/Run5.bmp")
run5.set_colorkey((255, 255, 255))
anim_run = [run1, run2, run3, run4, run5]
frame = 1
while_frame = 0
jump_frame = 0
jumping = False
j_frame = 0
jump1 = pygame.image.load("sprites/animation/jump/jump.bmp")
jump1.set_colorkey((255, 255, 255))
jump2 = pygame.image.load("sprites/animation/jump/jump2.bmp")
jump2.set_colorkey((255, 255, 255))
jump3 = pygame.image.load("sprites/animation/jump/jump3.bmp")
jump3.set_colorkey((255, 255, 255))
jump4 = pygame.image.load("sprites/animation/jump/jump4.bmp")
jump4.set_colorkey((255, 255, 255))
jump5 = pygame.image.load("sprites/animation/jump/jump5.bmp")
jump5.set_colorkey((255, 255, 255))
jump6 = pygame.image.load("sprites/animation/jump/jump6.bmp")
jump6.set_colorkey((255, 255, 255))
anim_jump = [jump1, jump2, jump3, jump4, jump5, jump6]
anim_fall = jump5
# load music
jump_music = pygame.mixer.Sound("Music/jump.wav")
fon_music = pygame.mixer.Sound("Music/fon music.wav")
fon_music.play(-1)
while_jump_music = True
# load images
heart = pygame.image.load("sprites/heart.bmp")
heart.set_colorkey((255, 255, 255))
enter = pygame.image.load("sprites/Enter.png").convert_alpha()
enter2 = pygame.image.load("sprites/Enter2.png").convert_alpha()
space = pygame.image.load("sprites/space.png").convert_alpha()
up = pygame.image.load("sprites/up.png").convert_alpha()
mini_random_platforms = pygame.image.load("sprites/Mini_ground.bmp")
mini_random_platforms_two = pygame.image.load("sprites/Mini_ground.bmp")
mini_random_platforms_three = pygame.image.load("sprites/Mini_ground.bmp")
normal_random_platforms = pygame.image.load("sprites/ground.bmp")
normal_random_platforms_two = pygame.image.load("sprites/ground.bmp")
normal_random_platforms_three = pygame.image.load("sprites/ground.bmp")
normal_random_platforms_grass = pygame.image.load("sprites/grass.bmp")
normal_random_platforms_grass_two = pygame.image.load("sprites/grass.bmp")
mini_random_platforms_grass = pygame.image.load("sprites/mini_grass.bmp")
normal_random_platforms_grass_three = pygame.image.load("sprites/grass.bmp")
mini_random_platforms_grass_two = pygame.image.load("sprites/mini_grass.bmp")
mini_random_platforms_grass_three = pygame.image.load("sprites/mini_grass.bmp")
# moving platforms
while_normal_random_platforms = False
while_normal_random_platforms2 = False
while_mini_random_platforms = False
while_normal_random_platforms3 = False
while_mini_random_platforms2 = False
while_mini_random_platforms3 = False


def speed_up(speed_platforms, max_speed, speed, oll_delit_platforms, old_speed):
    if speed_platforms == max_speed:
        pass
    elif oll_delit_platforms >= speed * 2:
        if old_speed == speed_platforms:
            speed_platforms += 1
            return speed_platforms


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            try:
                if event.key == pygame.K_SPACE:
                    jump = 0
                    if while_jump_music:
                        while_jump_music = False
                        jump_music.play(0)
                elif event.key == pygame.K_UP:
                    jump = 0
                    if while_jump_music:
                        while_jump_music = False
                        jump_music.play(0)
                elif event.key == pygame.K_ENTER:
                    restart = 0
                elif event.key == pygame.K_KP_ENTER:
                    restart = 0
            except:
                restart = 0

    if restart == 0:
        if y_restart == 200:
            y_restart = 700
            # return variables
            while_normal_random_platforms = False
            while_normal_random_platforms2 = False
            while_mini_random_platforms = False
            while_normal_random_platforms3 = False
            while_mini_random_platforms2 = False
            while_mini_random_platforms3 = False
            heart_score = 3
            space_platforms = 20
            heart_font = pygame.font.Font('fonts/minecraft.ttf', 40)
            heart_text = heart_font.render(str(heart_score), 1, (0, 0, 0))
            jump_fors = -35
            move = jump_fors + 1
            jump = 1
            restart = 1
            heart_score = 3
            score = 0
            score_for_speed_up = 0
            oll_delit_platforms = 0
            platforms = ['mini', 'normal']
            speed_platforms = 1
            old_speed_platforms = 1
            old_speed = 1
            max_speed = 5
            speed = 5
            speed_x_platform_start = -25
            speed_x_platforms_random = 225
            speed_x_platforms_random_two = 225
            speed_x_platforms_random_three = 225
            speed_x_platforms_mini_two = 410
            speed_x_platforms_mini_three = 410
            speed_x_platforms_mini = 410
            x_text = 442
            x_restart = 500
            cord_x_start = -25
            cord_x_normal = 225
            cord_x_mini = 410
            x_platforms_start = 0
            x_platforms_random = 500
            x_platforms_random_two = 500
            x_platforms_random_three = 500
            x_platforms_mini_two = 500
            x_platforms_mini_three = 500
            x_platforms_mini = 500
            y_restart = 700
            y_heart = 10
            y_text = 33
            y_platforms = 0
            y_platforms_start = 500
            y_oll_platforms_old = y_platforms_start
            y_platforms_random = 500
            y_platforms_random_two = 500
            y_platforms_random_three = 500
            y_platforms_mini_two = 500
            y_platforms_mini_three = 500
            y_platforms_mini = 500
            delite_platforms = -500
            delite_mini_platforms = -68
            delite_normal_platforms = -250
            delite_platforms_start = 600
            y_enter = 700
            y_enter2 = 700
            restart = 1
            counter = 0
            x_hero = 150
            hero_jump_y = 450
        else:
            restart = 1

    if hero_jump_y >= 750:
        if heart_score != 0:
            heart_score -= 1
        if heart_score == 0:
            heart_font = pygame.font.Font('fonts/minecraft.ttf', 50)
            heart_text = heart_font.render('game over', 1, (225, 0, 0))
            x_text = 107
            y_text = 100
            speed_platforms = 0
            y_heart = 700
            x_restart = 165
            y_restart = 200
            y_enter = 190
            y_enter2 = 190
            x_enter = 56
            x_enter2 = 362
            x_hero = 500
            runing = True
            jumping = False
            pygame.mixer.music.stop()

        else:
            heart_text = heart_font.render(str(heart_score), 1, (0, 0, 0))
            hero_jump_y = 50
            jump = 1

            if x_platforms_random <= 150:
                if x_platforms_random <= -100:
                    pass
                elif x_platforms_random <= 150:
                    hero_jump_y = y_platforms_random - 50
            if x_platforms_random_two <= 150:
                if x_platforms_random_two <= -100:
                    pass
                elif x_platforms_random_two <= 150:
                    hero_jump_y = y_platforms_random_two - 50
            if x_platforms_random_three <= 150:
                if x_platforms_random_three <= -100:
                    pass
                elif x_platforms_random_three <= 150:
                    hero_jump_y = y_platforms_random_three - 50
            if x_platforms_mini <= 170:
                if x_platforms_mini <= 82:
                    pass
                elif x_platforms_mini <= 170:
                    hero_jump_y = y_platforms_mini - 50
            if x_platforms_mini_two <= 170:
                if x_platforms_mini_two <= 82:
                    pass
                elif x_platforms_mini_two <= 170:
                    hero_jump_y = y_platforms_mini_two - 50
            if x_platforms_mini_three <= 170:
                if x_platforms_mini_three <= 82:
                    pass
                elif x_platforms_mini_three <= 170:
                    hero_jump_y = y_platforms_mini_three - 50

    if jump == 0:
        if jump_fors < 0:
            jump_frame += 1
            runing = False
            jumping = True

            if jump_frame <= 5:
                j_frame = 0
            elif 5 < jump_frame < 10:
                j_frame = 0
            elif 10 < jump_frame < 15:
                j_frame = 2
            elif 15 < jump_frame < 20:
                j_frame = 3
            elif 25 < jump_frame < 50:
                j_frame = 4

            hero_jump_y -= 10
            jump_fors = jump_fors + 1
        elif jump_fors == 0:
            runing = False
            jump = 1

    if x_platforms_random <= 150:
        if x_platforms_random <= -100:
            pass
        elif x_platforms_random <= 150:
            if hero_jump_y + 50 >= y_platforms_random:
                if hero_jump_y + 50 >= y_platforms_random + 10:
                    jump = 1
                    jumping = True
                    runing = False
                    j_frame = 4
                elif hero_jump_y + 50 >= y_platforms_random:
                    if open_jump:
                        runing = True
                        jumping = False
                        hero_jump_y = y_platforms_random - 50
                        jump_fors = -35
                        while_jump_music = True

    if x_platforms_start <= 150:
        if x_platforms_start <= -350:
            pass
        elif x_platforms_start <= 150:
            if hero_jump_y + 50 >= y_platforms_start:
                if hero_jump_y + 50 >= y_platforms_start + 10:
                    jump = 1
                    jumping = True
                    runing = False
                    j_frame = 4
                elif hero_jump_y + 50 >= y_platforms_start:
                    if open_jump:
                        runing = True
                        jumping = False
                        hero_jump_y = y_platforms_start - 50
                        jump_fors = -35
                        while_jump_music = True

    if x_platforms_random_two <= 170:
        if x_platforms_random_two <= -100:
            pass
        elif x_platforms_random_two <= 170:
            if hero_jump_y + 50 >= y_platforms_random_two:
                if hero_jump_y + 50 >= y_platforms_random_two + 10:
                    jump = 1
                    jumping = True
                    runing = False
                    j_frame = 4
                elif hero_jump_y + 50 >= y_platforms_random_two:
                    if open_jump:
                        runing = True
                        jumping = False
                        hero_jump_y = y_platforms_random_two - 50
                        jump_fors = -35
                        while_jump_music = True

    if x_platforms_random_three <= 170:
        if x_platforms_random_three <= -100:
            pass
        elif x_platforms_random_three <= 170:
            if hero_jump_y + 50 >= y_platforms_random_three:
                if hero_jump_y + 50 >= y_platforms_random_three + 10:
                    jump = 1
                    jumping = True
                    runing = False
                    j_frame = 4
                elif hero_jump_y + 50 >= y_platforms_random_three:
                    if open_jump:
                        runing = True
                        jumping = False
                        hero_jump_y = y_platforms_random_three - 50
                        jump_fors = -35
                        while_jump_music = True

    if x_platforms_mini <= 170:
        if x_platforms_mini <= 82:
            pass
        elif x_platforms_mini <= 170:
            if hero_jump_y + 50 >= y_platforms_mini:
                if hero_jump_y + 50 >= y_platforms_mini + 10:
                    jump = 1
                    jumping = True
                    runing = False
                    j_frame = 4
                elif hero_jump_y + 50 >= y_platforms_mini:
                    if open_jump:
                        runing = True
                        jumping = False
                        hero_jump_y = y_platforms_mini - 50
                        jump_fors = -35
                        while_jump_music = True

    if x_platforms_mini_two <= 170:
        if x_platforms_mini_two <= 82:
            pass
        elif x_platforms_mini_two <= 170:
            if hero_jump_y + 50 >= y_platforms_mini_two:
                if hero_jump_y + 50 >= y_platforms_mini_two + 10:
                    jump = 1
                    jumping = True
                    runing = False
                    j_frame = 4
                elif hero_jump_y + 50 >= y_platforms_mini_two:
                    if open_jump:
                        runing = True
                        jumping = False
                        hero_jump_y = y_platforms_mini_two - 50
                        jump_fors = -35
                        while_jump_music = True

    if x_platforms_mini_three <= 170:
        if x_platforms_mini_three <= 82:
            pass
        elif x_platforms_mini_three <= 170:
            if hero_jump_y + 50 >= y_platforms_mini_three:
                if hero_jump_y + 50 >= y_platforms_mini_three + 10:
                    jump = 1
                    jumping = True
                    runing = False
                    j_frame = 4
                elif hero_jump_y + 50 >= y_platforms_mini_three:
                    if open_jump:
                        runing = True
                        jumping = False
                        hero_jump_y = y_platforms_mini_three - 50
                        jump_fors = -35
                        while_jump_music = True

    if x_platforms_start == delite_platforms:
        oll_delit_platforms += 1
        pass

    elif x_platforms_random <= delite_normal_platforms:
        while_normal_random_platforms = False
        x_platforms_random = 500
        oll_delit_platforms += 1

    elif x_platforms_random_three <= delite_normal_platforms:
        while_normal_random_platforms3 = False
        x_platforms_random_three = 500
        oll_delit_platforms += 1

    elif x_platforms_random_two <= delite_normal_platforms:
        while_normal_random_platforms2 = False
        x_platforms_random_two = 500
        oll_delit_platforms += 1

    elif x_platforms_mini <= delite_mini_platforms:
        while_mini_random_platforms = False
        x_platforms_mini = 500
        oll_delit_platforms += 1

    elif x_platforms_mini_two <= delite_mini_platforms:
        while_mini_random_platforms2 = False
        x_platforms_mini_two = 500
        oll_delit_platforms += 1

    elif x_platforms_mini_three <= delite_mini_platforms:
        while_normal_random_platforms3 = False
        x_platforms_mini_three = 500
        oll_delit_platforms += 1

    if x_platforms_start == cord_x_start - space_platforms:
        plat = random.choice(platforms)
        if plat == 'mini':
            if x_platforms_mini == 500:
                one = y_oll_platforms_old - 75
                two = y_oll_platforms_old + 75
                y_platforms = random.randint(one, two)
                y_platforms_mini = y_platforms
                y_oll_platforms_old = y_platforms
                while_mini_random_platforms = True
            elif x_platforms_mini_two == 500:
                one = y_oll_platforms_old - 75
                two = y_oll_platforms_old + 75
                y_platforms = random.randint(one, two)
                y_platforms_mini_two = y_platforms
                y_oll_platforms_old = y_platforms
                while_mini_random_platforms2 = True
            elif x_platforms_mini_three == 500:
                one = y_oll_platforms_old - 75
                two = y_oll_platforms_old + 75
                y_platforms = random.randint(one, two)
                y_platforms_mini_three = y_platforms
                y_oll_platforms_old = y_platforms
                while_mini_random_platforms3 = True
        elif plat == 'normal':
            if x_platforms_random == 500:
                one = y_oll_platforms_old - 75
                two = y_oll_platforms_old + 75
                y_platforms = random.randint(one, two)
                y_platforms_random = y_platforms
                y_oll_platforms_old = y_platforms
                while_normal_random_platforms = True
            elif x_platforms_random_two == 500:
                one = y_oll_platforms_old - 75
                two = y_oll_platforms_old + 75
                y_platforms = random.randint(one, two)
                y_platforms_random_two = y_platforms
                y_oll_platforms_old = y_platforms
                while_normal_random_platforms2 = True
            elif x_platforms_random_three == 500:
                one = y_oll_platforms_old - 75
                two = y_oll_platforms_old + 75
                y_platforms = random.randint(one, two)
                y_platforms_random_three = y_platforms
                y_oll_platforms_old = y_platforms
                while_normal_random_platforms3 = True

    elif cord_x_normal == x_platforms_random + space_platforms:
        plat = random.choice(platforms)
        if plat == 'mini':
            if x_platforms_mini == 500:
                one = y_oll_platforms_old - 75
                two = y_oll_platforms_old + 75
                if two > 650:
                    two = 650
                if one < 100:
                    one = 650
                try:
                    y_platforms = random.randint(one, two)
                except:
                    y_platforms = random.randint(two, one)

                y_platforms_mini = y_platforms
                y_oll_platforms_old = y_platforms
                spd = speed_up(speed_platforms, max_speed, speed, oll_delit_platforms, old_speed_platforms)
                speed_platforms = spd
                while_mini_random_platforms = True
            elif x_platforms_mini_two == 500:
                one = y_oll_platforms_old - 75
                two = y_oll_platforms_old + 75
                if two > 650:
                    two = 600
                if one < 100:
                    one = 650
                try:
                    y_platforms = random.randint(one, two)
                except:
                    y_platforms = random.randint(two, one)
                y_platforms_mini_two = y_platforms
                y_oll_platforms_old = y_platforms
                spd = speed_up(speed_platforms, max_speed, speed, oll_delit_platforms, old_speed_platforms)
                speed_platforms = spd
                while_mini_random_platforms2 = True
            elif x_platforms_mini_three == 500:
                one = y_oll_platforms_old - 75
                two = y_oll_platforms_old + 75
                if two > 650:
                    two = y_oll_platforms_old
                if one < 100:
                    one = 650
                try:
                    y_platforms = random.randint(one, two)
                except:
                    y_platforms = random.randint(two, one)
                y_platforms_mini_three = y_platforms
                y_oll_platforms_old = y_platforms
                spd = speed_up(speed_platforms, max_speed, speed, oll_delit_platforms, old_speed_platforms)
                speed_platforms = spd
                while_mini_random_platforms3 = True
        elif plat == 'normal':
            if x_platforms_random == 500:
                one = y_oll_platforms_old - 75
                two = y_oll_platforms_old + 75
                if two > 650:
                    two = 600
                if one < 100:
                    one = 650
                try:
                    y_platforms = random.randint(one, two)
                except:
                    y_platforms = random.randint(two, one)
                y_platforms_random = y_platforms
                y_oll_platforms_old = y_platforms
                spd = speed_up(speed_platforms, max_speed, speed, oll_delit_platforms, old_speed_platforms)
                speed_platforms = spd
                while_normal_random_platforms = True
            elif x_platforms_random_two == 500:
                one = y_oll_platforms_old - 75
                two = y_oll_platforms_old + 75
                if two > 650:
                    two = 600
                if one < 100:
                    one = 650
                try:
                    y_platforms = random.randint(one, two)
                except:
                    y_platforms = random.randint(two, one)
                y_platforms_random_two = y_platforms
                y_oll_platforms_old = y_platforms
                spd = speed_up(speed_platforms, max_speed, speed, oll_delit_platforms, old_speed_platforms)
                speed_platforms = spd
                while_normal_random_platforms2 = True
            elif x_platforms_random_three == 500:
                one = y_oll_platforms_old - 75
                two = y_oll_platforms_old + 75
                if two > 650:
                    two = 600
                if one < 100:
                    one = 650
                try:
                    y_platforms = random.randint(one, two)
                except:
                    y_platforms = random.randint(two, one)
                y_platforms_random_three = y_platforms
                y_oll_platforms_old = y_platforms
                spd = speed_up(speed_platforms, max_speed, speed, oll_delit_platforms, old_speed_platforms)
                speed_platforms = spd
                while_normal_random_platforms3 = True
        else:
            if x_platforms_mini == 500:
                one = y_oll_platforms_old - 75
                two = y_oll_platforms_old + 75
                if two > 650:
                    two = 600
                if one < 100:
                    one = 650
                try:
                    y_platforms = random.randint(one, two)
                except:
                    y_platforms = random.randint(two, one)
                y_platforms_mini = y_platforms
                y_oll_platforms_old = y_platforms
                spd = speed_up(speed_platforms, max_speed, speed, oll_delit_platforms, old_speed_platforms)
                speed_platforms = spd
                while_mini_random_platforms = True
            elif x_platforms_mini_two == 500:
                one = y_oll_platforms_old - 75
                two = y_oll_platforms_old + 75
                if two > 650:
                    two = 600
                if one < 100:
                    one = 650
                try:
                    y_platforms = random.randint(one, two)
                except:
                    y_platforms = random.randint(two, one)
                y_platforms_mini_two = y_platforms
                y_oll_platforms_old = y_platforms
                spd = speed_up(speed_platforms, max_speed, speed, oll_delit_platforms, old_speed_platforms)
                speed_platforms = spd
                while_mini_random_platforms2 = True
            elif x_platforms_mini_three == 500:
                one = y_oll_platforms_old - 75
                two = y_oll_platforms_old + 75
                if two > 650:
                    two = 600
                if one < 100:
                    one = 650
                try:
                    y_platforms = random.randint(one, two)
                except:
                    y_platforms = random.randint(two, one)
                y_platforms_mini_three = y_platforms
                y_oll_platforms_old = y_platforms
                spd = speed_up(speed_platforms, max_speed, speed, oll_delit_platforms, old_speed_platforms)
                speed_platforms = spd
                while_mini_random_platforms3 = True


    elif cord_x_normal == x_platforms_random_two + space_platforms:
        plat = random.choice(platforms)
        if plat == 'mini':
            if x_platforms_mini == 500:
                one = y_oll_platforms_old - 75
                two = y_oll_platforms_old + 75
                if two > 650:
                    two = 600
                if one < 100:
                    one = 650
                try:
                    y_platforms = random.randint(one, two)
                except:
                    y_platforms = random.randint(two, one)
                y_platforms_mini = y_platforms
                y_oll_platforms_old = y_platforms
                spd = speed_up(speed_platforms, max_speed, speed, oll_delit_platforms, old_speed_platforms)
                speed_platforms = spd
                while_mini_random_platforms = True
            elif x_platforms_mini_two == 500:
                one = y_oll_platforms_old - 75
                two = y_oll_platforms_old + 75
                if two > 650:
                    two = 600
                if one < 100:
                    one = 650
                try:
                    y_platforms = random.randint(one, two)
                except:
                    y_platforms = random.randint(two, one)
                y_platforms_mini_two = y_platforms
                y_oll_platforms_old = y_platforms
                spd = speed_up(speed_platforms, max_speed, speed, oll_delit_platforms, old_speed_platforms)
                speed_platforms = spd
                while_mini_random_platforms2 = True
            elif x_platforms_mini_three == 500:
                one = y_oll_platforms_old - 75
                two = y_oll_platforms_old + 75
                if two > 650:
                    two = 600
                if one < 100:
                    one = 650
                try:
                    y_platforms = random.randint(one, two)
                except:
                    y_platforms = random.randint(two, one)
                y_platforms_mini_three = y_platforms
                y_oll_platforms_old = y_platforms
                spd = speed_up(speed_platforms, max_speed, speed, oll_delit_platforms, old_speed_platforms)
                speed_platforms = spd
                while_mini_random_platforms3 = True
        elif plat == 'normal':
            if x_platforms_random == 500:
                one = y_oll_platforms_old - 75
                two = y_oll_platforms_old + 75
                if two > 650:
                    two = 600
                if one < 100:
                    one = 650
                try:
                    y_platforms = random.randint(one, two)
                except:
                    y_platforms = random.randint(two, one)
                y_platforms_random = y_platforms
                y_oll_platforms_old = y_platforms
                spd = speed_up(speed_platforms, max_speed, speed, oll_delit_platforms, old_speed_platforms)
                speed_platforms = spd
                while_normal_random_platforms = True
            elif x_platforms_random_two == 500:
                one = y_oll_platforms_old - 75
                two = y_oll_platforms_old + 75
                if two > 650:
                    two = 600
                if one < 100:
                    one = 650
                try:
                    y_platforms = random.randint(one, two)
                except:
                    y_platforms = random.randint(two, one)
                y_platforms_random_two = y_platforms
                y_oll_platforms_old = y_platforms
                spd = speed_up(speed_platforms, max_speed, speed, oll_delit_platforms, old_speed_platforms)
                speed_platforms = spd
                while_normal_random_platforms2 = True
            elif x_platforms_random_three == 500:
                one = y_oll_platforms_old - 75
                two = y_oll_platforms_old + 75
                if two > 650:
                    two = 600
                if one < 100:
                    one = 650
                try:
                    y_platforms = random.randint(one, two)
                except:
                    y_platforms = random.randint(two, one)
                y_platforms_random_three = y_platforms
                y_oll_platforms_old = y_platforms
                spd = speed_up(speed_platforms, max_speed, speed, oll_delit_platforms, old_speed_platforms)
                speed_platforms = spd
                while_normal_random_platforms3 = True
        else:
            if x_platforms_mini == 500:
                one = y_oll_platforms_old - 75
                two = y_oll_platforms_old + 75
                if two > 650:
                    two = 600
                if one < 100:
                    one = 650
                try:
                    y_platforms = random.randint(one, two)
                except:
                    y_platforms = random.randint(two, one)
                y_platforms_mini = y_platforms
                y_oll_platforms_old = y_platforms
                spd = speed_up(speed_platforms, max_speed, speed, oll_delit_platforms, old_speed_platforms)
                speed_platforms = spd
                while_mini_random_platforms = True
            elif x_platforms_mini_two == 500:
                one = y_oll_platforms_old - 75
                two = y_oll_platforms_old + 75
                if two > 650:
                    two = 600
                if one < 100:
                    one = 650
                try:
                    y_platforms = random.randint(one, two)
                except:
                    y_platforms = random.randint(two, one)
                y_platforms_mini_two = y_platforms
                y_oll_platforms_old = y_platforms
                spd = speed_up(speed_platforms, max_speed, speed, oll_delit_platforms, old_speed_platforms)
                speed_platforms = spd
                while_mini_random_platforms2 = True
            elif x_platforms_mini_three == 500:
                one = y_oll_platforms_old - 75
                two = y_oll_platforms_old + 75
                if two > 650:
                    two = 600
                if one < 100:
                    one = 650
                try:
                    y_platforms = random.randint(one, two)
                except:
                    y_platforms = random.randint(two, one)
                y_platforms_mini_three = y_platforms
                y_oll_platforms_old = y_platforms
                spd = speed_up(speed_platforms, max_speed, speed, oll_delit_platforms, old_speed_platforms)
                speed_platforms = spd
                while_mini_random_platforms3 = True



    elif cord_x_mini == x_platforms_mini + space_platforms:
        plat = random.choice(platforms)
        if plat == 'mini':
            if x_platforms_random == 500:
                one = y_oll_platforms_old - 75
                two = y_oll_platforms_old + 75
                if two > 650:
                    two = 600
                if one < 100:
                    one = 650
                try:
                    y_platforms = random.randint(one, two)
                except:
                    y_platforms = random.randint(two, one)
                y_platforms_random = y_platforms
                y_oll_platforms_old = y_platforms
                spd = speed_up(speed_platforms, max_speed, speed, oll_delit_platforms, old_speed_platforms)
                speed_platforms = spd
                while_normal_random_platforms = True
            elif x_platforms_random_two == 500:
                one = y_oll_platforms_old - 75
                two = y_oll_platforms_old + 75
                if two > 650:
                    two = 600
                if one < 100:
                    one = 650
                try:
                    y_platforms = random.randint(one, two)
                except:
                    y_platforms = random.randint(two, one)
                y_platforms_random_two = y_platforms
                y_oll_platforms_old = y_platforms
                spd = speed_up(speed_platforms, max_speed, speed, oll_delit_platforms, old_speed_platforms)
                speed_platforms = spd
                while_normal_random_platforms2 = True
            elif x_platforms_random_three == 500:
                one = y_oll_platforms_old - 75
                two = y_oll_platforms_old + 75
                if two > 650:
                    two = 600
                if one < 100:
                    one = 650
                try:
                    y_platforms = random.randint(one, two)
                except:
                    y_platforms = random.randint(two, one)
                y_platforms_random_three = y_platforms
                y_oll_platforms_old = y_platforms
                spd = speed_up(speed_platforms, max_speed, speed, oll_delit_platforms, old_speed_platforms)
                speed_platforms = spd
                while_normal_random_platforms3 = True
        elif plat == 'normal':
            if x_platforms_random == 500:
                one = y_oll_platforms_old - 75
                two = y_oll_platforms_old + 75
                if two > 650:
                    two = 600
                if one < 100:
                    one = 650
                try:
                    y_platforms = random.randint(one, two)
                except:
                    y_platforms = random.randint(two, one)
                y_platforms_random = y_platforms
                y_oll_platforms_old = y_platforms
                spd = speed_up(speed_platforms, max_speed, speed, oll_delit_platforms, old_speed_platforms)
                speed_platforms = spd
                while_normal_random_platforms = True
            elif x_platforms_random_two == 500:
                one = y_oll_platforms_old - 75
                two = y_oll_platforms_old + 75
                if two > 650:
                    two = 600
                if one < 100:
                    one = 650
                try:
                    y_platforms = random.randint(one, two)
                except:
                    y_platforms = random.randint(two, one)
                y_platforms_random_two = y_platforms
                y_oll_platforms_old = y_platforms
                spd = speed_up(speed_platforms, max_speed, speed, oll_delit_platforms, old_speed_platforms)
                speed_platforms = spd
                while_normal_random_platforms2 = True
            elif x_platforms_random_three == 500:
                one = y_oll_platforms_old - 75
                two = y_oll_platforms_old + 75
                if two > 650:
                    two = 600
                if one < 100:
                    one = 650
                try:
                    y_platforms = random.randint(one, two)
                except:
                    y_platforms = random.randint(two, one)
                y_platforms_random_three = y_platforms
                y_oll_platforms_old = y_platforms
                spd = speed_up(speed_platforms, max_speed, speed, oll_delit_platforms, old_speed_platforms)
                speed_platforms = spd
                while_normal_random_platforms3 = True
        else:
            if x_platforms_mini == 500:
                one = y_oll_platforms_old - 75
                two = y_oll_platforms_old + 75
                if two > 650:
                    two = 600
                if one < 100:
                    one = 650
                try:
                    y_platforms = random.randint(one, two)
                except:
                    y_platforms = random.randint(two, one)
                y_platforms_mini = y_platforms
                y_oll_platforms_old = y_platforms
                spd = speed_up(speed_platforms, max_speed, speed, oll_delit_platforms, old_speed_platforms)
                speed_platforms = spd
                while_mini_random_platforms = True
            elif x_platforms_mini_two == 500:
                one = y_oll_platforms_old - 75
                two = y_oll_platforms_old + 75
                if two > 650:
                    two = 600
                if one < 100:
                    one = 650
                try:
                    y_platforms = random.randint(one, two)
                except:
                    y_platforms = random.randint(two, one)
                y_platforms_mini_two = y_platforms
                y_oll_platforms_old = y_platforms
                spd = speed_up(speed_platforms, max_speed, speed, oll_delit_platforms, old_speed_platforms)
                speed_platforms = spd
                while_mini_random_platforms2 = True
            elif x_platforms_mini_three == 500:
                one = y_oll_platforms_old - 75
                two = y_oll_platforms_old + 75
                if two > 650:
                    two = 600
                if one < 100:
                    one = 650
                try:
                    y_platforms = random.randint(one, two)
                except:
                    y_platforms = random.randint(two, one)
                y_platforms_mini_three = y_platforms
                y_oll_platforms_old = y_platforms
                spd = speed_up(speed_platforms, max_speed, speed, oll_delit_platforms, old_speed_platforms)
                speed_platforms = spd
                while_mini_random_platforms3 = True


    elif cord_x_normal == x_platforms_random_three + space_platforms:
        plat = random.choice(platforms)
        if plat == 'mini':
            if x_platforms_mini == 500:
                one = y_oll_platforms_old - 75
                two = y_oll_platforms_old + 75
                if two > 650:
                    two = 600
                if one < 100:
                    one = 650
                try:
                    y_platforms = random.randint(one, two)
                except:
                    y_platforms = random.randint(two, one)
                y_platforms_mini = y_platforms
                y_oll_platforms_old = y_platforms
                spd = speed_up(speed_platforms, max_speed, speed, oll_delit_platforms, old_speed_platforms)
                speed_platforms = spd
                while_mini_random_platforms = True
            elif x_platforms_mini_two == 500:
                one = y_oll_platforms_old - 75
                two = y_oll_platforms_old + 75
                if two > 650:
                    two = 600
                if one < 100:
                    one = 650
                try:
                    y_platforms = random.randint(one, two)
                except:
                    y_platforms = random.randint(two, one)
                y_platforms_mini_two = y_platforms
                y_oll_platforms_old = y_platforms
                spd = speed_up(speed_platforms, max_speed, speed, oll_delit_platforms, old_speed_platforms)
                speed_platforms = spd
                while_mini_random_platforms2 = True
            elif x_platforms_mini_three == 500:
                one = y_oll_platforms_old - 75
                two = y_oll_platforms_old + 75
                if two > 650:
                    two = 600
                if one < 100:
                    one = 650
                try:
                    y_platforms = random.randint(one, two)
                except:
                    y_platforms = random.randint(two, one)
                y_platforms_mini_three = y_platforms
                y_oll_platforms_old = y_platforms
                spd = speed_up(speed_platforms, max_speed, speed, oll_delit_platforms, old_speed_platforms)
                speed_platforms = spd
                while_mini_random_platforms3 = True
        elif plat == 'normal':
            if x_platforms_random == 500:
                one = y_oll_platforms_old - 75
                two = y_oll_platforms_old + 75
                if two > 650:
                    two = 600
                if one < 100:
                    one = 650
                try:
                    y_platforms = random.randint(one, two)
                except:
                    y_platforms = random.randint(two, one)
                y_platforms_random = y_platforms
                y_oll_platforms_old = y_platforms
                spd = speed_up(speed_platforms, max_speed, speed, oll_delit_platforms, old_speed_platforms)
                speed_platforms = spd
                while_normal_random_platforms = True
            elif x_platforms_random_two == 500:
                one = y_oll_platforms_old - 75
                two = y_oll_platforms_old + 75
                if two > 650:
                    two = 600
                if one < 100:
                    one = 650
                try:
                    y_platforms = random.randint(one, two)
                except:
                    y_platforms = random.randint(two, one)
                y_platforms_random_two = y_platforms
                y_oll_platforms_old = y_platforms
                spd = speed_up(speed_platforms, max_speed, speed, oll_delit_platforms, old_speed_platforms)
                speed_platforms = spd
                while_normal_random_platforms2 = True
            elif x_platforms_random_three == 500:
                one = y_oll_platforms_old - 75
                two = y_oll_platforms_old + 75
                if two > 650:
                    two = 600
                if one < 100:
                    one = 650
                try:
                    y_platforms = random.randint(one, two)
                except:
                    y_platforms = random.randint(two, one)
                y_platforms_random_three = y_platforms
                y_oll_platforms_old = y_platforms
                spd = speed_up(speed_platforms, max_speed, speed, oll_delit_platforms, old_speed_platforms)
                speed_platforms = spd
                while_normal_random_platforms3 = True
        else:
            if x_platforms_mini == 500:
                one = y_oll_platforms_old - 75
                two = y_oll_platforms_old + 75
                if two > 650:
                    two = 600
                if one < 100:
                    one = 650
                try:
                    y_platforms = random.randint(one, two)
                except:
                    y_platforms = random.randint(two, one)
                y_platforms_mini = y_platforms
                y_oll_platforms_old = y_platforms
                spd = speed_up(speed_platforms, max_speed, speed, oll_delit_platforms, old_speed_platforms)
                speed_platforms = spd
                while_mini_random_platforms = True
            elif x_platforms_mini_two == 500:
                one = y_oll_platforms_old - 75
                two = y_oll_platforms_old + 75
                if two > 650:
                    two = 600
                if one < 100:
                    one = 650
                try:
                    y_platforms = random.randint(one, two)
                except:
                    y_platforms = random.randint(two, one)
                y_platforms_mini_two = y_platforms
                y_oll_platforms_old = y_platforms
                spd = speed_up(speed_platforms, max_speed, speed, oll_delit_platforms, old_speed_platforms)
                speed_platforms = spd
                while_mini_random_platforms2 = True
            elif x_platforms_mini_three == 500:
                one = y_oll_platforms_old - 75
                two = y_oll_platforms_old + 75
                if two > 650:
                    two = 600
                if one < 100:
                    one = 650
                try:
                    y_platforms = random.randint(one, two)
                except:
                    y_platforms = random.randint(two, one)
                y_platforms_mini_three = y_platforms
                y_oll_platforms_old = y_platforms
                spd = speed_up(speed_platforms, max_speed, speed, oll_delit_platforms, old_speed_platforms)
                speed_platforms = spd
                while_mini_random_platforms3 = True


    elif cord_x_mini == x_platforms_mini_two + space_platforms:
        plat = random.choice(platforms)
        if plat == 'mini':
            if x_platforms_random == 500:
                one = y_oll_platforms_old - 75
                two = y_oll_platforms_old + 75
                if two > 650:
                    two = 600
                if one < 100:
                    one = 650
                try:
                    y_platforms = random.randint(one, two)
                except:
                    y_platforms = random.randint(two, one)
                y_platforms_random = y_platforms
                y_oll_platforms_old = y_platforms
                spd = speed_up(speed_platforms, max_speed, speed, oll_delit_platforms, old_speed_platforms)
                speed_platforms = spd
                while_normal_random_platforms = True
            elif x_platforms_random_two == 500:
                one = y_oll_platforms_old - 75
                two = y_oll_platforms_old + 75
                if two > 650:
                    two = 600
                if one < 100:
                    one = 650
                try:
                    y_platforms = random.randint(one, two)
                except:
                    y_platforms = random.randint(two, one)
                y_platforms_random_two = y_platforms
                y_oll_platforms_old = y_platforms
                spd = speed_up(speed_platforms, max_speed, speed, oll_delit_platforms, old_speed_platforms)
                speed_platforms = spd
                while_normal_random_platforms2 = True
            elif x_platforms_random_three == 500:
                one = y_oll_platforms_old - 75
                two = y_oll_platforms_old + 75
                if two > 650:
                    two = 600
                if one < 100:
                    one = 650
                try:
                    y_platforms = random.randint(one, two)
                except:
                    y_platforms = random.randint(two, one)
                y_platforms_random_three = y_platforms
                y_oll_platforms_old = y_platforms
                spd = speed_up(speed_platforms, max_speed, speed, oll_delit_platforms, old_speed_platforms)
                speed_platforms = spd
                while_normal_random_platforms3 = True
        elif plat == 'normal':
            if x_platforms_random == 500:
                one = y_oll_platforms_old - 75
                two = y_oll_platforms_old + 75
                if two > 650:
                    two = 600
                if one < 100:
                    one = 650
                try:
                    y_platforms = random.randint(one, two)
                except:
                    y_platforms = random.randint(two, one)
                y_platforms_random = y_platforms
                y_oll_platforms_old = y_platforms
                spd = speed_up(speed_platforms, max_speed, speed, oll_delit_platforms, old_speed_platforms)
                speed_platforms = spd
                while_normal_random_platforms = True
            elif x_platforms_random_two == 500:
                one = y_oll_platforms_old - 75
                two = y_oll_platforms_old + 75
                if two > 650:
                    two = 600
                if one < 100:
                    one = 650
                try:
                    y_platforms = random.randint(one, two)
                except:
                    y_platforms = random.randint(two, one)
                y_platforms_random_two = y_platforms
                y_oll_platforms_old = y_platforms
                spd = speed_up(speed_platforms, max_speed, speed, oll_delit_platforms, old_speed_platforms)
                speed_platforms = spd
                while_normal_random_platforms2 = True
            elif x_platforms_random_three == 500:
                one = y_oll_platforms_old - 75
                two = y_oll_platforms_old + 75
                if two > 650:
                    two = 600
                if one < 100:
                    one = 650
                try:
                    y_platforms = random.randint(one, two)
                except:
                    y_platforms = random.randint(two, one)
                y_platforms_random_three = y_platforms
                y_oll_platforms_old = y_platforms
                spd = speed_up(speed_platforms, max_speed, speed, oll_delit_platforms, old_speed_platforms)
                speed_platforms = spd
                while_normal_random_platforms3 = True
        else:
            if x_platforms_mini == 500:
                one = y_oll_platforms_old - 75
                two = y_oll_platforms_old + 75
                if two > 650:
                    two = 600
                if one < 100:
                    one = 650
                try:
                    y_platforms = random.randint(one, two)
                except:
                    y_platforms = random.randint(two, one)
                y_platforms_mini = y_platforms
                y_oll_platforms_old = y_platforms
                spd = speed_up(speed_platforms, max_speed, speed, oll_delit_platforms, old_speed_platforms)
                speed_platforms = spd
                while_mini_random_platforms = True
            elif x_platforms_mini_two == 500:
                one = y_oll_platforms_old - 75
                two = y_oll_platforms_old + 75
                if two > 650:
                    two = 600
                if one < 100:
                    one = 650
                try:
                    y_platforms = random.randint(one, two)
                except:
                    y_platforms = random.randint(two, one)
                y_platforms_mini_two = y_platforms
                y_oll_platforms_old = y_platforms
                spd = speed_up(speed_platforms, max_speed, speed, oll_delit_platforms, old_speed_platforms)
                speed_platforms = spd
                while_mini_random_platforms2 = True
            elif x_platforms_mini_three == 500:
                one = y_oll_platforms_old - 75
                two = y_oll_platforms_old + 75
                if two > 650:
                    two = 600
                if one < 100:
                    one = 650
                try:
                    y_platforms = random.randint(one, two)
                except:
                    y_platforms = random.randint(two, one)
                y_platforms_mini_three = y_platforms
                y_oll_platforms_old = y_platforms
                spd = speed_up(speed_platforms, max_speed, speed, oll_delit_platforms, old_speed_platforms)
                speed_platforms = spd
                while_mini_random_platforms3 = True


    elif cord_x_mini == x_platforms_mini_three + space_platforms:
        plat = random.choice(platforms)
        if plat == 'mini':
            if x_platforms_random == 500:
                one = y_oll_platforms_old - 75
                two = y_oll_platforms_old + 75
                if two > 650:
                    two = 600
                if one < 100:
                    one = 650
                try:
                    y_platforms = random.randint(one, two)
                except:
                    y_platforms = random.randint(two, one)
                y_platforms_random = y_platforms
                y_oll_platforms_old = y_platforms
                spd = speed_up(speed_platforms, max_speed, speed, oll_delit_platforms, old_speed_platforms)
                speed_platforms = spd
                while_normal_random_platforms = True
            elif x_platforms_random_two == 500:
                one = y_oll_platforms_old - 75
                two = y_oll_platforms_old + 75
                if two > 650:
                    two = 600
                if one < 100:
                    one = 650
                try:
                    y_platforms = random.randint(one, two)
                except:
                    y_platforms = random.randint(two, one)
                y_platforms_random_two = y_platforms
                y_oll_platforms_old = y_platforms
                spd = speed_up(speed_platforms, max_speed, speed, oll_delit_platforms, old_speed_platforms)
                speed_platforms = spd
                while_normal_random_platforms2 = True
            elif x_platforms_random_three == 500:
                one = y_oll_platforms_old - 75
                two = y_oll_platforms_old + 75
                if two > 650:
                    two = 600
                if one < 100:
                    one = 650
                try:
                    y_platforms = random.randint(one, two)
                except:
                    y_platforms = random.randint(two, one)
                y_platforms_random_three = y_platforms
                y_oll_platforms_old = y_platforms
                spd = speed_up(speed_platforms, max_speed, speed, oll_delit_platforms, old_speed_platforms)
                speed_platforms = spd
                while_normal_random_platforms3 = True
        elif plat == 'normal':
            if x_platforms_random == 500:
                one = y_oll_platforms_old - 75
                two = y_oll_platforms_old + 75
                if two > 650:
                    two = 600
                if one < 100:
                    one = 650
                try:
                    y_platforms = random.randint(one, two)
                except:
                    y_platforms = random.randint(two, one)
                y_platforms_random = y_platforms
                y_oll_platforms_old = y_platforms
                spd = speed_up(speed_platforms, max_speed, speed, oll_delit_platforms, old_speed_platforms)
                speed_platforms = spd
                while_normal_random_platforms = True
            elif x_platforms_random_two == 500:
                one = y_oll_platforms_old - 75
                two = y_oll_platforms_old + 75
                if two > 650:
                    two = 600
                if one < 100:
                    one = 650
                try:
                    y_platforms = random.randint(one, two)
                except:
                    y_platforms = random.randint(two, one)
                y_platforms_random_two = y_platforms
                y_oll_platforms_old = y_platforms
                spd = speed_up(speed_platforms, max_speed, speed, oll_delit_platforms, old_speed_platforms)
                speed_platforms = spd
                while_normal_random_platforms2 = True
            elif x_platforms_random_three == 500:
                one = y_oll_platforms_old - 75
                two = y_oll_platforms_old + 75
                if two > 650:
                    two = 600
                if one < 100:
                    one = 650
                try:
                    y_platforms = random.randint(one, two)
                except:
                    y_platforms = random.randint(two, one)
                y_platforms_random_three = y_platforms
                y_oll_platforms_old = y_platforms
                spd = speed_up(speed_platforms, max_speed, speed, oll_delit_platforms, old_speed_platforms)
                speed_platforms = spd
                while_normal_random_platforms3 = True
        else:
            if x_platforms_mini == 500:
                one = y_oll_platforms_old - 75
                two = y_oll_platforms_old + 75
                if two > 650:
                    two = 600
                if one < 100:
                    one = 650
                try:
                    y_platforms = random.randint(one, two)
                except:
                    y_platforms = random.randint(two, one)
                y_platforms_mini = y_platforms
                y_oll_platforms_old = y_platforms
                spd = speed_up(speed_platforms, max_speed, speed, oll_delit_platforms, old_speed_platforms)
                speed_platforms = spd
                while_mini_random_platforms = True
            elif x_platforms_mini_two == 500:
                one = y_oll_platforms_old - 75
                two = y_oll_platforms_old + 75
                if two > 650:
                    two = 600
                if one < 100:
                    one = 650
                try:
                    y_platforms = random.randint(one, two)
                except:
                    y_platforms = random.randint(two, one)
                y_platforms_mini_two = y_platforms
                y_oll_platforms_old = y_platforms
                spd = speed_up(speed_platforms, max_speed, speed, oll_delit_platforms, old_speed_platforms)
                speed_platforms = spd
                while_mini_random_platforms2 = True
            elif x_platforms_mini_three == 500:
                one = y_oll_platforms_old - 75
                two = y_oll_platforms_old + 75
                if two > 650:
                    two = 600
                if one < 100:
                    one = 650
                try:
                    y_platforms = random.randint(one, two)
                except:
                    y_platforms = random.randint(two, one)
                y_platforms = random.randint(one, two)
                y_platforms_mini_three = y_platforms
                y_oll_platforms_old = y_platforms
                spd = speed_up(speed_platforms, max_speed, speed, oll_delit_platforms, old_speed_platforms)
                speed_platforms = spd
                while_mini_random_platforms3 = True

    if speed_platforms == None:
        speed_platforms = old_speed_platforms
        old_speed = speed_platforms - 1
    elif speed_platforms == 2:
        space_platforms = 30
        old_speed_platforms = 2
        speed = 10
        speed_platforms = old_speed_platforms
        old_speed = speed_platforms - 1
        cord_x_normal = 226
        cord_x_mini = 410
        cord_x_start = -26
    elif speed_platforms == 3:
        space_platforms = 45
        old_speed_platforms = 3
        speed = 20
        speed_platforms = old_speed_platforms
        old_speed = speed_platforms - 1
        cord_x_normal = 227
        cord_x_mini = 407
        cord_x_start = -27
    elif speed_platforms == 4:
        space_platforms = 60
        old_speed_platforms = 4
        speed = 40
        speed_platforms = old_speed_platforms
        old_speed = speed_platforms - 1
        cord_x_normal = 224
        cord_x_mini = 408
        cord_x_start = -24
    elif speed_platforms == 5:
        space_platforms = 75
        speed = 100
        old_speed_platforms = 5
        speed_platforms = old_speed_platforms
        old_speed = speed_platforms - 1
        cord_x_normal = 225
        cord_x_mini = 410
        cord_x_start = -25

    if while_normal_random_platforms:
        x_platforms_random = x_platforms_random - speed_platforms

    if while_normal_random_platforms2:
        x_platforms_random_two = x_platforms_random_two - speed_platforms

    if while_mini_random_platforms:
        x_platforms_mini = x_platforms_mini - speed_platforms

    if while_normal_random_platforms3:
        x_platforms_random_three = x_platforms_random_three - speed_platforms

    if while_mini_random_platforms2:
        x_platforms_mini_two = x_platforms_mini_two - speed_platforms

    if while_mini_random_platforms3:
        x_platforms_mini_three = x_platforms_mini_three - speed_platforms

    if oll_delit_platforms == speed * 2:
        old_speed += 1

    sc.blit(background, (0, 0))
    sc.blit(score_text, (x_score, y_score))
    sc.blit(restart_text, (x_restart, y_restart))
    sc.blit(heart, (405, y_heart))
    sc.blit(heart_text, (x_text, y_text))
    sc.blit(ground, (x_platforms_start, y_platforms_start))
    sc.blit(grass, (x_platforms_start, y_platforms_start))
    sc.blit(tutorial_text_3d, (x_tutorial_text + 3, 558))
    sc.blit(tutorial_text, (x_tutorial_text, 560))
    sc.blit(tutorial_text_and_3d, (x_tutorial_text_and + 3, 633))
    sc.blit(tutorial_text_and, (x_tutorial_text_and, 635))
    sc.blit(up, (x_up, 635))
    sc.blit(space, (x_space, y_space))
    sc.blit(normal_random_platforms, (x_platforms_random, y_platforms_random))
    sc.blit(normal_random_platforms_two, (x_platforms_random_two, y_platforms_random_two))
    sc.blit(normal_random_platforms_grass, (x_platforms_random, y_platforms_random))
    sc.blit(normal_random_platforms_grass_two, (x_platforms_random_two, y_platforms_random_two))
    sc.blit(mini_random_platforms, (x_platforms_mini, y_platforms_mini))
    sc.blit(mini_random_platforms_grass, (x_platforms_mini, y_platforms_mini))
    sc.blit(normal_random_platforms_three, (x_platforms_random_three, y_platforms_random_three))
    sc.blit(normal_random_platforms_grass_three, (x_platforms_random_three, y_platforms_random_three))
    sc.blit(mini_random_platforms_two, (x_platforms_mini_two, y_platforms_mini_two))
    sc.blit(mini_random_platforms_grass_two, (x_platforms_mini_two, y_platforms_mini_two))
    sc.blit(mini_random_platforms_three, (x_platforms_mini_three, y_platforms_mini_three))
    sc.blit(mini_random_platforms_grass_three, (x_platforms_mini_three, y_platforms_mini_three))
    sc.blit(enter, (x_enter, y_enter))
    sc.blit(enter2, (x_enter2, y_enter2))

    if while_frame <= 12:
        frame = 0
    elif while_frame > 12 and while_frame < 24:
        frame = 1
    elif while_frame > 24 and while_frame < 36:
        frame = 2
    elif while_frame > 36 and while_frame < 48:
        frame = 3
    elif while_frame > 48 and while_frame < 60:
        frame = 4
        while_frame = 0

    if runing:
        sc.blit(anim_run[frame], (x_hero, hero_jump_y))

    if jumping:
        sc.blit(anim_jump[j_frame], (x_hero, hero_jump_y))
    else:
        jump_frame = 0

    counter += 1
    if speed_platforms == 1:
        if counter >= 15:
            score += 1
            counter = 0
    elif speed_platforms == 2:
        if counter >= 13:
            score += 1
            counter = 0
    elif speed_platforms == 3:
        if counter >= 10:
            score += 1
            counter = 0
    elif speed_platforms == 4:
        if counter >= 8:
            score += 1
            counter = 0
    elif speed_platforms == 5:
        if counter >= 5:
            score += 1
            counter = 0

    score_text = score_font.render(str(score), 1, (255, 255, 255))
    x_platforms_start = x_platforms_start - speed_platforms
    x_tutorial_text_and -= speed_platforms
    x_tutorial_text -= speed_platforms
    x_up -= speed_platforms
    x_space -= speed_platforms
    hero_jump_y += 5
    while_frame += 1
    pygame.display.update()
    clock.tick(60)
