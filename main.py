import pygame, random, animzombie, animplayer, animbat
# добавили класс Clock в игру, чтобы в конце программы сделать "тик" в игре медленнее
clock = pygame.time.Clock()

ap = animplayer
ab = animbat
az = animzombie


# обазетльный метод в начале для инициализации игры
pygame.init()
# указываем размер экрана в формате (ширина, высота)
screen = pygame.display.set_mode((1200, 600))  # третий параметр говорит нам о том как запустить приложение.
                                              # Указав flags=pygame.NOFRAME не будет кнопок закрытия/сворачивания
# добавляем название для приложения
pygame.display.set_caption("PyGame Injinerium")
# подгружаю картинку в проект
icon = pygame.image.load('Materials/Images/inj.jpg').convert()
# утсанавливаю картинку в качестве иконки
pygame.display.set_icon(icon)
bg = pygame.image.load('Materials/Images/back.jpg').convert()
#player = ap.run_right[0]           # pygame.image.load('Materials/Images/Anim/run_r/1.png')
zombie = az.zombie_walk_l[0]


# создали счётчик для перебора анимаций картинок персонажа
player_anim_count_run = 0
player_anim_count_idle = 0
zombie_anim_count_walk = 0
bg_x = 0

#создаём переменные для передвижения игрока
player_speed = 10
Jump_force = 30
jump_count = Jump_force
is_jump = False
player_x = 100
player_y = 400
zombie_list_in_game = []
# подгружаем музыку
bg_sound = pygame.mixer.Sound('Materials/Music/ForestWalk.mp3')
bg_sound.play()    # запускаем музыку

#  создали таймер для спавна зомби
zombie_timer = pygame.USEREVENT + 1
pygame.time.set_timer(zombie_timer, random.randint(700, 5000))

running = True
while running:

    keys = pygame.key.get_pressed()

    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x + 1200, 0))

    # создаём хитбоксы игрока и зомби
    player_rect = ap.run_right[0].get_rect(topleft=(player_x, player_y))

    # когда у нас срабатывает USEREVENT (мы сами указываем когда он срабатывает) в конце цикла срабатывает условие и в
    # наш список добавляется коллайдер за границами экрана. А в скрипте под этим комментарием мы это считываем и если
    # в списке что то появляется то мы перебираем это и рисуем на экране картинку по координатам того колайдера, что мы
    # добавляем в конце, затем изменяем x для этого элемента постоянно на - 10 и проверяем касается ли коллайдер игрока
    # коллайдера зомби и в случае соприкосновения мы теряем хп
    if zombie_list_in_game:
        for el in zombie_list_in_game:
            screen.blit(az.zombie_walk_l[zombie_anim_count_walk], el)
            el.x -= 10
            # а теперь прописываем что происходит при соприкосновении игрока с зомби
            if player_rect.colliderect(el):
                print('-1 hp')

    if keys[pygame.K_RIGHT]:
        screen.blit(ap.run_right[player_anim_count_run], (player_x, player_y))
    elif keys[pygame.K_LEFT]:
        screen.blit(ap.run_left[player_anim_count_run], (player_x, player_y))
    else:
        screen.blit(ap.idle[player_anim_count_idle], (player_x, player_y))

    # создаём переменну содержащую в себе нажатую клавишу
    # делаем проверку что если клавиша, что была нажата игроков это d, то идём вправо
    if keys[pygame.K_RIGHT] and player_x < 1100:
        player_x += player_speed
    elif keys[pygame.K_LEFT] and player_x > 0:
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
        if keys[pygame.K_UP]:
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
    if player_anim_count_run == len(ap.run_right) - 1:
        player_anim_count_run = 0
    else:
        player_anim_count_run += 1

    if player_anim_count_idle == len(ap.idle) - 1:
        player_anim_count_idle = 0
    else:
        player_anim_count_idle += 1

    if zombie_anim_count_walk == len(az.zombie_walk_l) - 1:
        zombie_anim_count_walk = 0
    else:
        zombie_anim_count_walk += 1

    # эта перемення указана там, где мы доболвяем фон на экран и сделали её чтобы сдвигать фон влево
    # bg_x -= 7
    # if bg_x <= -1200:
    #     bg_x = 0

    # обновление экрана
    pygame.display.update()

    # чтобы закрыть экран
    for event in pygame.event.get():    # за счёт метода pygame.event.get() мы получаем список из всех возможных событий
        if event.type == pygame.QUIT:   # если событие это нажатие на выход
            running = False
            pygame.quit()               # то игры закроется. После этого действия никакие другие не должны быть
        # при срабатывании USEREVENT добавляем в список коллайдер от зомби, по координатам которого мы будем рисовать на
        # экране самого зомби
        if event.type == zombie_timer:
            zombie_list_in_game.append(zombie.get_rect(topleft=(1220, 430)))

    clock.tick(14)