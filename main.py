import pygame

# добавили класс Clock в игру, чтобы в конце программы сделать "тик" в игре медленнее
clock = pygame.time.Clock()



# обазетльный метод в начале для инициализации игры
pygame.init()
# указываем размер экрана в формате (ширина, высота)
screen = pygame.display.set_mode((1200, 600))  # третий параметр говорит нам о том как запустить приложение.
                                              # Указав flags=pygame.NOFRAME не будет кнопок закрытия/сворачивания
# добавляем название для приложения
pygame.display.set_caption("PyGame Ijinerium")
# подгружаю картинку в проект
icon = pygame.image.load('Materials/Images/inj.jpg')
# утсанавливаю картинку в качестве иконки
pygame.display.set_icon(icon)
bg = pygame.image.load('Materials/Images/back.jpg')
player = pygame.image.load('Materials/Images/Anim/run_r/1.png')

# создаём список для анимации
run_right = [
    pygame.image.load('Materials/Images/Anim/run_r/1.png'),
    pygame.image.load('Materials/Images/Anim/run_r/2.png'),
    pygame.image.load('Materials/Images/Anim/run_r/3.png'),
    pygame.image.load('Materials/Images/Anim/run_r/4.png'),
    pygame.image.load('Materials/Images/Anim/run_r/5.png'),
    pygame.image.load('Materials/Images/Anim/run_r/6.png'),
    pygame.image.load('Materials/Images/Anim/run_r/7.png'),
    pygame.image.load('Materials/Images/Anim/run_r/8.png')
]

run_left = [
    pygame.image.load('Materials/Images/Anim/run_l/1.png'),
    pygame.image.load('Materials/Images/Anim/run_l/2.png'),
    pygame.image.load('Materials/Images/Anim/run_l/3.png'),
    pygame.image.load('Materials/Images/Anim/run_l/4.png'),
    pygame.image.load('Materials/Images/Anim/run_l/5.png'),
    pygame.image.load('Materials/Images/Anim/run_l/6.png'),
    pygame.image.load('Materials/Images/Anim/run_l/7.png'),
    pygame.image.load('Materials/Images/Anim/run_l/8.png')
]
idle = [
    pygame.image.load('Materials/Images/Anim/idle/1.png'),
    pygame.image.load('Materials/Images/Anim/idle/2.png'),
    pygame.image.load('Materials/Images/Anim/idle/3.png'),
    pygame.image.load('Materials/Images/Anim/idle/4.png'),
    pygame.image.load('Materials/Images/Anim/idle/5.png'),
    pygame.image.load('Materials/Images/Anim/idle/6.png')
]

# создали счётчик для перебора анимаций картинок персонажа
player_anim_count_run = 0
player_anim_count_idle = 0
bg_x = 0

#создаём переменные для передвижения игрока
player_speed = 8
Jump_force = 25
jump_count = Jump_force
is_jump = False
player_x = 100
player_y = 400

# подгружаем музыку
bg_sound = pygame.mixer.Sound('Materials/Music/ForestWalk.mp3')
bg_sound.play()    # запускаем музыку

running = True
while running:

    keys = pygame.key.get_pressed()

    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x + 1200, 0))
    if keys[pygame.K_d]:
        screen.blit(run_right[player_anim_count_run], (player_x, player_y))
    elif keys[pygame.K_a]:
        screen.blit(run_left[player_anim_count_run], (player_x, player_y))
    else:
        screen.blit(idle[player_anim_count_idle], (player_x, player_y))

    # создаём переменну содержащую в себе нажатую клавишу
    # делаем проверку что если клавиша, что была нажата игроков это d, то идём вправо
    if keys[pygame.K_d] and player_x < 1100:
        player_x += player_speed
    elif keys[pygame.K_a] and player_x > 0:
        player_x -= player_speed

# как работает прыжок. Мы создали переменную, что хранит в себе False. Пока она False мы не прыграем.
# Как только мы нажимаешь пробел она становится True и из-за этого скрипт ниже срабатывает в "else".
# Далее мы говорим "если счётчик больше отрицательной силы, то" и выполняется в зависимости от условия дальнейшее:
# Либо мы вычитаем из player_y счётчик, что равен изначально силе, из-за чего персонаж поднимается, так как 0x и 0y это
# верхний левый угол приложения. И в момент, когда счётчик становится меньше или равен нулю, то теперь он прибавляет
# из-за чего игрок опускается. После каждого из этих двух действий (поднятия или опускания) счётчик уменьшается, из-за
# чего и получается эффект прыжка, так как с каждым тиком счётчик уменьшается, в итоге уходя в отрицательное значение
# После всего этого, можно сказать, счётчик перезаряжается и возвращает False для is_jump, чтобы программа ждала, пока
# Мы нажмём пробел и превратила is_jump в True после нажатия пробела.

    if not is_jump:
        if keys[pygame.K_SPACE]:
            is_jump = True
    else:
        if jump_count >= -Jump_force:
            if jump_count > 0:
                player_y -= jump_count
            else:
                player_y += abs(jump_count)
            jump_count -= 5
        else:
            is_jump = False
            jump_count = Jump_force

    # меняем "фрейм" к которому мы обращаемся
    if player_anim_count_run == len(run_right) - 1:
        player_anim_count_run = 0
    else:
        player_anim_count_run += 1

    if player_anim_count_idle == len(idle) - 1:
        player_anim_count_idle = 0
    else:
        player_anim_count_idle += 1

    # эта перемення указана там, где мы доболвяем фон на экран и сделали её чтобы сдвигать фон влево
    bg_x -= 7
    if bg_x <= -1200:
        bg_x = 0

    # обновление экрана
    pygame.display.update()

    # чтобы закрыть экран
    for event in pygame.event.get():    # за счёт метода pygame.event.get() мы получаем список из всех возможных событий
        if event.type == pygame.QUIT:   # если событие это нажатие на выход
            running = False
            pygame.quit()               # то игры закроется. После этого действия никакие другие не должны быть

    clock.tick(14)