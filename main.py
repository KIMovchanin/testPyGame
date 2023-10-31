import pygame

# обазетльный метод в начале для инициализации игры
pygame.init()
# указываем размер экрана в формате (ширина, высота)
screen = pygame.display.set_mode((600, 300))  # третий параметр говорит нам о том как запустить приложение.
                                              # Указав flags=pygame.NOFRAME не будет кнопок закрытия/сворачивания
# добавляем название для приложения
pygame.display.set_caption("PyGame Ijinerium")
# подгружаю картинку в проект
icon = pygame.image.load('Materials/inj.jpg')
# утсанавливаю картинку в качестве иконки
pygame.display.set_icon(icon)

running = True
while running:
    # меняем фон игры
    # screen.fill((50, 170, 80))   # в качестве параметра мы передаём кортеж

    # обновление экрана
    pygame.display.update()

    # чтобы закрыть экран
    for event in pygame.event.get():    # за счёт метода pygame.event.get() мы получаем список из всех возможных событий
        if event.type == pygame.QUIT:   # если событие это нажатие на выход
            running = False
            pygame.quit()               # то игры закроется. После этого действия никакие другие не должны быть
        elif event.type == pygame.KEYDOWN:  # если была нажата клавиша
            if event.key == pygame.K_SPACE: # то проверяем какая клавиша
                screen.fill((170, 50, 140)) # и меняем цвет в зависимости от нажатой клавиши
            elif event.key == pygame.K_LEFT:
                screen.fill((50, 170, 80))