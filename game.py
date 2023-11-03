import animplayer as ap
import animzombie as az
import pygame
import bdconnect as db
import bullet as bl

def play():
    # добавили класс Clock в игру, чтобы в конце программы сделать "тик" в игре медленнее
    clock = pygame.time.Clock()

    # обаятельный метод в начале для инициализации игры
    pygame.init()
    # указываем размер экрана в формате (ширина, высота)
    screen = pygame.display.set_mode((1200, 600))  # третий параметр говорит нам о том как запустить приложение.
    # Указав flags=pygame.NOFRAME не будет кнопок закрытия/сворачивания
    # добавляем название для приложения
    pygame.display.set_caption("PyGame Injinerium")
    # подгружаю картинку в проект
    icon = pygame.image.load('Materials/Images/inj.jpg').convert()
    # устанавливаю картинку в качестве иконки
    pygame.display.set_icon(icon)
    bg = pygame.image.load('Materials/Images/back.jpg').convert()

    zombie = az.zombie_walk_l[0]

    # создали счётчик для перебора анимаций картинок персонажа
    player_anim_count_run = 0
    player_anim_count_idle = 0
    zombie_anim_count_walk = 0
    bg_x = 0

    # создаём переменные для передвижения игрока
    player_speed = 10
    Jump_force = 30
    jump_count = Jump_force
    is_jump = False
    player_x = 100
    player_y = 400
    player_hp = 3
    zombie_list_in_game = []
    # подгружаем музыку
    bg_sound = pygame.mixer.Sound('Materials/Music/ForestWalk.mp3')
    bg_sound.play()  # запускаем музыку

    #  создали таймер для спавна зомби
    zombie_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(zombie_timer, 2500)

    label = pygame.font.Font('Materials/Fonts/Quicksand-VariableFont_wght.ttf', 40)
    lose_label = label.render('You lose!', False, 'DarkRed')
    restart_label = label.render('Play again', False, 'DarkGreen')
    restart_label_rect = restart_label.get_rect(topleft=(500, 350))

    ammo_max = 7
    ammo = ammo_max
    # db.addindb()
    bullets = []
    score = 0
    # создаём переменную для понимания проиграл игрок или нет
    gameplay = True

    running = True
    while running:
        keys = pygame.key.get_pressed()

        screen.blit(bg, (bg_x, 0))
        screen.blit(bg, (bg_x + 1200, 0))

        # грубо говоря всё работает, пока игрок жив
        if gameplay:

            # создаём хитбоксы игрока и зомби
            player_rect = ap.run_right[0].get_rect(topleft=(player_x, player_y))

            # Когда у нас срабатывает USER EVENT (мы сами указываем когда он срабатывает) в конце цикла срабатывает
            # условие и в наш список добавляется коллайдер за границами экрана. А в скрипте под этим комментарием мы
            # это считываем и если в списке что-то появляется, то мы перебираем это и рисуем на экране картинку по
            # координатам того колайдера, что мы добавляем в конце, затем изменяем x для этого элемента постоянно на
            # - 10 и проверяем касается ли коллайдер игрока коллайдера зомби и в случае соприкосновения мы теряем хп
            if zombie_list_in_game:
                # функция enumerate позволяет не только получить функцию, но и индекс этого элемента
                for (i, el) in enumerate(zombie_list_in_game):
                    screen.blit(az.zombie_walk_l[zombie_anim_count_walk], el)
                    el.x -= 10

                    if el.x < -70:
                        zombie_list_in_game.pop(i)

                    # а теперь прописываем что происходит при соприкосновении игрока с зомби
                    if player_rect.colliderect(el):
                        player_hp -= 1
                        if player_hp == 0 or player_hp < 0:
                            bg_sound.stop()
                            gameplay = False

            if keys[pygame.K_RIGHT]:
                screen.blit(ap.run_right[player_anim_count_run], (player_x, player_y))
            elif keys[pygame.K_LEFT]:
                screen.blit(ap.run_left[player_anim_count_run], (player_x, player_y))
            else:
                screen.blit(ap.idle[player_anim_count_idle], (player_x, player_y))

            # создаём переменную содержащую в себе нажатую клавишу
            # делаем проверку что если клавиша, что была нажата игроков это d, то идём вправо
            if keys[pygame.K_RIGHT] and player_x < 1100:
                player_x += player_speed
            elif keys[pygame.K_LEFT] and player_x > 0:
                player_x -= player_speed

            # Как работает прыжок. Мы создали переменную, что хранит в себе False. Пока она False мы не прыграем. Как
            # только мы нажимаешь пробел она становится True и из-за этого скрипт ниже срабатывает в "else". Далее мы
            # говорим "если счётчик больше отрицательной силы, то" и выполняется в зависимости от условия дальнейшее:
            # Либо мы вычитаем из player_y счётчик, что равен изначально силе, из-за чего персонаж поднимается,
            # так как 0x и 0y это верхний левый угол приложения. И в момент, когда счётчик становится меньше или равен
            # нулю, то теперь он прибавляет из-за чего игрок опускается. После каждого из этих двух действий (поднятия
            # или опускания) счётчик уменьшается, из-за чего и получается эффект прыжка, так как с каждым тиком счётчик
            # уменьшается, в итоге уходя в отрицательное значение После всего этого, можно сказать,
            # счётчик перезаряжается и возвращает False для is_jump, чтобы программа ждала, пока Мы нажмём пробел и
            # превратила is_jump в True после нажатия пробела.

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
            if player_anim_count_run == len(ap.run_right) - 1:
                player_anim_count_run = 0
            else:
                player_anim_count_run += 1

            if player_anim_count_idle == len(ap.idle) - 1:
                player_anim_count_idle = 0
            else:
                player_anim_count_idle += 1

            # if zombie_anim_count_walk == len(az.zombie_walk_l) - 1:
            #     zombie_anim_count_walk = 0
            # else:
            #     zombie_anim_count_walk += 1

            # эта переменная указана там, где мы добавляем фон на экран и сделали её, чтобы сдвигать фон влево
            # bg_x -= 7
            # if bg_x <= -1200:
            #     bg_x = 0

            if bullets:
                for (i, el) in enumerate(bullets):
                    screen.blit(bl.bullet_r[0], (el.x, el.y))
                    el.x += 70

                    if el.x > 1220:
                        bullets.pop(i)

                    if zombie_list_in_game:
                        for (index, enemy) in enumerate(zombie_list_in_game):
                            if el.colliderect(enemy):
                                zombie_list_in_game.pop(index)
                                bullets.pop(i)
                                score += 10

        else:
            # заполняем экран таким цветом при проигрыше
            screen.fill('Black')
            screen.blit(lose_label, (520, 260))
            screen.blit(restart_label, restart_label_rect)

            mouse = pygame.mouse.get_pos()
            # Collidepoint позволяет проверить соприкасается ли квадрат с мышкой
            # мы проверяем находится ли мышка в координатах надписи и нажата ли она
            # В get_pressed мы в конце написали [0], так как данный метод содержит в себе 3 значения, каждый из которых
            # может быть True или False. Первый из-за нажатия левой кнопки, второй из-за правой, а третий из-за колёсика
            if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                gameplay = True
                player_x = 100
                zombie_list_in_game.clear()
                bg_sound.play()
                bullets.clear()
                ammo = ammo_max

        # обновление экрана
        pygame.display.update()

        # чтобы закрыть экран
        for event in pygame.event.get():  # за счёт метода pygame.event.get() мы получаем список из всех возможных
            # событий
            if event.type == pygame.QUIT:  # если событие это нажатие на выход
                running = False
                print(score)
                db.addindb('vika', score)  # записываю всё в бд
                pygame.quit()  # То игры закроется. После этого действия никакие другие не должны быть
            # при срабатывании USEREVENT добавляем в список коллайдер от зомби, по координатам которого мы будем
            # рисовать на экране самого зомби
            if event.type == zombie_timer:
                zombie_list_in_game.append(zombie.get_rect(topleft=(1220, 430)))
            if gameplay and event.type == pygame.KEYUP and event.key == pygame.K_f and ammo > 0:
                bullets.append(bl.bullet_r[0].get_rect(topleft=(player_x + 20, player_y + 35)))
                ammo -= 1
        clock.tick(14)
