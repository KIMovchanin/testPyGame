import pygame
import game

def win():
    pygame.init()
    screen = pygame.display.set_mode((1200, 600))

    label = pygame.font.Font('Materials/Fonts/Quicksand-VariableFont_wght.ttf', 40)
    win_label = label.render('You win!', False, 'LightGreen')
    win_label_rect = win_label.get_rect(topleft=(500, 100))

    play_again_label = label.render('<Play again?>', False, 'Red')
    play_again_label_rect = play_again_label.get_rect(topleft=(440, 300))

    running = True
    while running:
        pygame.display.update()
        mouse = pygame.mouse.get_pos()
        game.zombie_list_in_game.clear()
        game.bullets.clear()

        screen.blit(win_label, win_label_rect)
        screen.blit(play_again_label, play_again_label_rect)

        if play_again_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            game.play()

        for event in pygame.event.get():  # за счёт метода pygame.event.get() мы получаем список из всех возможных событий
            if event.type == pygame.QUIT:  # если событие это нажатие на выход
                running = False
                pygame.quit()