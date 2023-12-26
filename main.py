import os
import sys
from random import choice
import pygame
from pygame.time import Clock


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


def game_screen():
    fon = pygame.transform.scale(load_image('coffee_bg.png'), (width, height))
    screen.blit(fon, (0, 0))
    guy = load_image('guy3.png')
    screen.blit(guy, (220, 68))
    dialog = Dialog(ordering())


def ordering():
    coffee_types = ['эспрессо', 'американо', 'капучино', 'латте', 'раф', 'моккачино', 'фраппучино']
    desserts = ['шоколадный кекс', 'ванильный кекс', 'черничный кекс',
                'торт "Наполеон"', 'торт "Медовик"', 'торт "Красный бархат"', 'торт "Птичье молоко"',
                'круассан с шоколадом', 'круассан с вареной сгущенкой', 'круассан с джемом', 'круассан классический',
                'булочка с корицей', 'булочка "Синнабон"', None, None]
    # None нужен для того, чтобы не всегда была вкусняшка
    greetings = [' - Здравствуйте! Можно мне ', ' - Здравствуйте! Мне пожалуйста ', ' - Здравствуйте! Я бы хотел ',
                 ' - Добрый день! Мне пожалуйста ', ' - Добрый день! Можно мне ', ' - Добрый день! Я бы хотел ']
    coffee = choice(coffee_types)
    dessert = choice(desserts)
    order = [choice(greetings) + coffee]
    if dessert is not None:
        order.append(f'и {dessert}')
    return order


class Button(pygame.sprite.Sprite):
    def __init__(self, text, text_coord):
        super().__init__(buttons_group, all_sprites)
        self.btn_text = text
        self.image = pygame.Surface((150, 30), pygame.SRCALPHA, 32)
        self.rect = pygame.Rect(20, text_coord, 150, 30)
        self.font = pygame.font.Font(None, 40)
        pygame.draw.rect(self.image, (247, 214, 171), (0, 0, 150, 30))
        self.text = self.font.render(self.btn_text, 0, (204, 152, 102))
        self.image.blit(self.text, (2, 2))
        screen.blit(self.image, self.rect)

    def update(self, *args):
        if self.rect.collidepoint(args[0].pos):
            if self.btn_text == 'New game':
                game_screen()
            if self.btn_text == 'Continue':
                print('game continued')
            if self.btn_text == 'Instruct':
                print('instruct is opened')


class Dialog(pygame.sprite.Sprite):
    def __init__(self, text):
        super().__init__(all_sprites)
        self.text = text[::]
        self.size = (500, 10 + 15 * len(self.text) + 10)
        self.image = pygame.Surface(self.size, pygame.SRCALPHA, 32)
        self.rect = pygame.Rect(100, 300, *self.size)
        self.font = pygame.font.Font(None, 20)
        pygame.draw.rect(self.image, (242, 151, 65), (0, 0, *self.size))
        pygame.draw.rect(self.image, (252, 199, 149), (3, 3, self.size[0] - 6, self.size[1] - 6))
        self.text_coord = 10
        for line in self.text:
            string_rendered = self.font.render(line, 1, (89, 58, 29))
            intro_rect = string_rendered.get_rect()
            intro_rect.top = self.text_coord
            intro_rect.x = 10
            self.text_coord += intro_rect.height
            self.image.blit(string_rendered, intro_rect)
            self.text_coord += 2
        screen.blit(self.image, self.rect)


if __name__ == '__main__':
    pygame.init()
    size = width, height = 720, 405
    fps = 50
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
        pygame.display.flip()
        clock.tick(fps)
