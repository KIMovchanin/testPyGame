import pygame

# обазетльный метод в начале для инициализации игры
pygame.init()
# указываем размер экрана в формате (ширина, высота)
screen = pygame.display.set_mode((1000, 700))  # третий параметр говорит нам о том как запустить приложение.
                                              # Указав flags=pygame.NOFRAME не будет кнопок закрытия/сворачивания
# добавляем название для приложения
pygame.display.set_caption("PyGame Ijinerium")
# подгружаю картинку в проект
icon = pygame.image.load('Materials/inj.jpg')
# утсанавливаю картинку в качестве иконки
pygame.display.set_icon(icon)

# создаём объект square рисуя через класс Surface() квадрат
square = pygame.Surface((50, 170))   # принимает в качестве параметра кортеж со значениями ширины и высоты
square.fill((50, 170, 80))

# создаём надпись
myfont = pygame.font.Font('Materials/Fonts/Agbalumo-Regular.ttf', 40)  # первым параметром получает шрифт, вторым - размер шрифта
# дополнительные характеристики
text_surface = myfont.render('Injinerium', False, 'Yellow')    # мы можем указать здесь сам текст, что будет отображён, цвет, задний фон и тд
# подгружаю картинку
image = pygame.image.load('C:/Users/kondr/OneDrive/Рабочий стол/Арты/hThxjaFdCbQ.jpg')

running = True
while running:

    # рисуем на экране наш квадрат с помощью метода blit
    screen.blit(square, (0, 0))    # принимает два параметра, первый - сам объект. Второй - координаты спавна
    screen.blit(text_surface, (200, 200))
    # другой способ рисования в 1 строку кода
    # рисуем объект круг на поверхности "screen", выбираю цвет, кортежем передаю координаты и задаю радиус круга
    pygame.draw.circle(screen, 'Red', (100, 40), 30)
    screen.blit(image, (400, 0))
    # обновление экрана
    pygame.display.update()

    # чтобы закрыть экран
    for event in pygame.event.get():    # за счёт метода pygame.event.get() мы получаем список из всех возможных событий
        if event.type == pygame.QUIT:   # если событие это нажатие на выход
            running = False
            pygame.quit()               # то игры закроется. После этого действия никакие другие не должны быть



