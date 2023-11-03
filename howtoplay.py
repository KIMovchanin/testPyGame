import pygame
import menu

def howtoplay():
    pygame.init()

    screen = pygame.display.set_mode((1067, 600))

    label = pygame.font.Font('Materials/Fonts/Quicksand-VariableFont_wght.ttf', 20)

    text_label1 = label.render('You need to survive 30 seconds and you will win, but you have only 7 bullets.', False, 'White')
    text_label2 = label.render('Kill 1 zombie = +100 points.', False, 'White')
    text_label3 = label.render('Survive 1 second = +10 points.', False, 'White')

    move_label = label.render('For move use arrows (<- and ->).', False, 'White')

    jump_label = label.render('For jump use space.', False, 'White')

    shoot_label = label.render('For shooting use key "f".', False, 'White')

    back_button = label.render('<- Back to menu.', False, 'Red')
    back_button_rect = back_button.get_rect(topleft=(30, 550))

    running = True
    while running:
        pygame.display.update()

        screen.blit(text_label1, (200, 200))
        screen.blit(text_label2, (440, 225))
        screen.blit(text_label3, (415, 250))

        screen.blit(move_label, (390, 400))
        screen.blit(jump_label, (450, 425))
        screen.blit(shoot_label, (430, 450))
        screen.blit(back_button, back_button_rect)

        mouse = pygame.mouse.get_pos()
        if back_button_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            menu.startmenu()

        for event in pygame.event.get():  # за счёт метода pygame.event.get() мы получаем список из всех возможных
            # событий
            if event.type == pygame.QUIT:  # если событие это нажатие на выход
                running = False

    pygame.quit()