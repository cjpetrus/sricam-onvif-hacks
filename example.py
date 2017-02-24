import pygame
from ptz import Camera

pygame.init()

clock = pygame.time.Clock()
#set pygame key repeat
pygame.key.set_repeat(50, 50)

#setup camera
cam = Camera()

while True:
    for event in pygame.event.get():
        print event
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # check if key is pressed
        # if you use event.key here it will give you error at runtime
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                cam.move_left()
            if event.key == pygame.K_RIGHT:
                cam.move_right()
            if event.key == pygame.K_UP:
                cam.move_up()
            if event.key == pygame.K_DOWN:
                cam.move_down()
