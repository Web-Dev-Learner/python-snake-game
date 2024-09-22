# build a screen and a moving block

import pygame
# from pygame.locals import *
from pygame.locals import KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN, K_ESCAPE, QUIT


def draw_block():
    surface.fill((110,110,5))

    # blit -> one of the methods to 
    # place an image onto the screens of pygame applications

    surface.blit(block,(block_x,block_y))

    # flip update the display surface to screen
     
    pygame.display.flip()


if __name__ == '__main__':
    pygame.init()

    # pygame.display.set_mode() -> initialize a window or screen for display


    surface = pygame.display.set_mode((500,500))
    surface.fill((110,110,5))

    block = pygame.image.load("resources/block.jpg").convert()

    block_x,block_y = 100,100

    surface.blit(block,(block_x,block_y))
    
    pygame.display.flip()



# event loop
# x - right+ ,- left  ,, y - top - , + down
    running = True

    while running:
        for event in pygame.event.get():
            
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if event.key == K_LEFT:
                    block_x -= 10
                    draw_block()
                if event.key == K_RIGHT:
                    block_x += 10
                    draw_block()
                if event.key == K_UP:
                    block_y -= 10
                    draw_block()
                if event.key == K_DOWN:
                    block_y += 10
                    draw_block()

            elif event.type == QUIT:
                running = False
       



