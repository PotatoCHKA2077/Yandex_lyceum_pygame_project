import os
import sys

import pygame
from pygame.time import Clock

FPS = 50


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = ['New game', 'Continue', 'Instruct']  #

    fon = pygame.transform.scale(load_image('coffee_fon.jpg'), (width, height))
    screen.blit(fon, (0, 0))
    text_coord = 110
    for line in intro_text:
        Button(line, text_coord)
        text_coord += 50


class Button(pygame.sprite.Sprite):
    def __init__(self, text, text_coord):
        super().__init__(buttons_group, all_sprites)
        self.btn_text = text
        self.image = pygame.Surface((150, 30), pygame.SRCALPHA, 32)
        self.rect = pygame.Rect(20, text_coord, 150, 30)
        self.font = pygame.font.Font(None, 40)
        pygame.draw.rect(self.image, (247, 214, 171), (0, 0, 150, 30))
        self.text = self.font.render(text, 0, (245, 190, 118))
        self.image.blit(self.text, (2, 2))
        screen.blit(self.image, self.rect)

    def update(self, *args):
        if self.rect.collidepoint(args[0].pos):
            if self.btn_text == 'New game':
                print('game started')
            if self.btn_text == 'Continue':
                print('game continued')
            if self.btn_text == 'Instruct':
                print('instruct is opened')


if __name__ == '__main__':
    pygame.init()
    size = width, height = 720, 405
    screen = pygame.display.set_mode(size)
    clock = Clock()
    all_sprites = pygame.sprite.Group()
    buttons_group = pygame.sprite.Group()
    running = True
    start_screen()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                buttons_group.update(event)
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
