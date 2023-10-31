import pygame

pygame.init()
pygame.display.set_mode((1200, 600))
run_right = [
    pygame.image.load('Materials/Images/Anim/run_r/1.png').convert_alpha(),
    pygame.image.load('Materials/Images/Anim/run_r/2.png').convert_alpha(),
    pygame.image.load('Materials/Images/Anim/run_r/3.png').convert_alpha(),
    pygame.image.load('Materials/Images/Anim/run_r/4.png').convert_alpha(),
    pygame.image.load('Materials/Images/Anim/run_r/5.png').convert_alpha(),
    pygame.image.load('Materials/Images/Anim/run_r/6.png').convert_alpha(),
    pygame.image.load('Materials/Images/Anim/run_r/7.png').convert_alpha(),
    pygame.image.load('Materials/Images/Anim/run_r/8.png').convert_alpha()
]
run_left = [
    pygame.image.load('Materials/Images/Anim/run_l/1.png').convert_alpha(),
    pygame.image.load('Materials/Images/Anim/run_l/2.png').convert_alpha(),
    pygame.image.load('Materials/Images/Anim/run_l/3.png').convert_alpha(),
    pygame.image.load('Materials/Images/Anim/run_l/4.png').convert_alpha(),
    pygame.image.load('Materials/Images/Anim/run_l/5.png').convert_alpha(),
    pygame.image.load('Materials/Images/Anim/run_l/6.png').convert_alpha(),
    pygame.image.load('Materials/Images/Anim/run_l/7.png').convert_alpha(),
    pygame.image.load('Materials/Images/Anim/run_l/8.png').convert_alpha()
]
idle = [
    pygame.image.load('Materials/Images/Anim/idle/1.png').convert_alpha(),
    pygame.image.load('Materials/Images/Anim/idle/2.png').convert_alpha(),
    pygame.image.load('Materials/Images/Anim/idle/3.png').convert_alpha(),
    pygame.image.load('Materials/Images/Anim/idle/4.png').convert_alpha(),
    pygame.image.load('Materials/Images/Anim/idle/5.png').convert_alpha(),
    pygame.image.load('Materials/Images/Anim/idle/6.png').convert_alpha()
]
