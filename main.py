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

# создали счётчик для перебора анимаций картинок персонажа
player_anim_count = 0
bg_x = 0

#создаём переменные для передвижения игрока
player_speed = 5
player_x = 100
player_y = 400

# подгружаем музыку
bg_sound = pygame.mixer.Sound('Materials/Music/ForestWalk.mp3')
bg_sound.play()    # запускаем музыку

running = True
while running:

    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x + 1200, 0))
    screen.blit(run_right[player_anim_count], (player_x, player_y))

    # создаём переменну содержащую в себе нажатую клавишу
    keys = pygame.key.get_pressed()
    # делаем проверку что если клавиша, что была нажата игроков это d, то идём вправо
    if keys[pygame.K_d]:
        player_x += player_speed
    elif keys[pygame.K_a]:
        player_x -= player_speed




    if player_anim_count == 7:
        player_anim_count = 0
    else:
        player_anim_count += 1

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