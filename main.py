import os
import sys
from random import choice, randrange
import pygame
from pygame.time import Clock
from recipes import *
mango_counter = 0
chery_counter = 0
milk_counter = 0
cream_counter = 0
coffee_counter = 0


def load_image(name):
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
    global fon, screen_is
    screen_is = 'start'
    intro_text = ['New game', 'Continue', 'Instruct']
    fon = pygame.transform.scale(load_image('coffee_fon.jpg'), (width, height))
    screen.blit(fon, (0, 0))
    text_coord = [20, 110]
    for line in intro_text:
        Button(line, text_coord)
        text_coord[-1] += 50


def order_screen():
    global fon, screen_is
    screen_is = 'order'
    buttons_group.empty()
    fon = load_image('coffee_bg.png')
    screen.blit(fon, (0, 0))
    ordering()
    buttons = ['Принять', 'Отказаться']
    text_coord = [150, 340]
    for text in buttons:
        Button(text, text_coord)
        text_coord[0] += 130


def cooking_screen():
    global screen_is, fon, coffe_machine, cream, milk, mango_syrup, cherry_syrup, cup, add_zone, coffee_order
    screen_is = 'cook'
    buttons_group.empty()
    fon = pygame.transform.scale(load_image('table_fon.png'), (width, height))
    screen.blit(fon, (0, 0))
    coffe_machine = CoffeMachine()
    cream = Cream()
    milk = Milk()
    mango_syrup = MangoSyrup()
    cherry_syrup = CherrySyrup()
    cup = Cup()
    add_zone = AddZone()
    buttons = ["Готово", "Сбросить"]
    text_coord = [200, 375]
    for text in buttons:
        Button(text, text_coord)
        text_coord[0] += 130
    print(coffee_order)


def result_screen():
    global screen_is, fon, coffee_order


def ordering():
    coffee_types = ['эспрессо', 'капучино', 'латте', 'раф']
    greetings = [' - Здравствуйте! Можно мне ', ' - Здравствуйте! Мне пожалуйста ', ' - Здравствуйте! Я бы хотел ',
                 ' - Добрый день! Мне пожалуйста ', ' - Добрый день! Можно мне ', ' - Добрый день! Я бы хотел ']
    global coffee_order
    coffee_order = choice(coffee_types)
    order = [choice(greetings) + coffee_order]
    Dialog(order)


def coffee_falling():
    global coffee_counter
    for _ in range(4):
        Liquid((choice([randrange(coffe_machine.rect.x + 80, coffe_machine.rect.x + 84),
                        randrange(coffe_machine.rect.x+102, coffe_machine.rect.x+106)]),
                coffe_machine.rect.y + 149), (99, 52, 1))
    if coffee_counter < 100:
        coffee_counter += 0.5


def cream_falling():
    global cream_counter
    for _ in range(3):
        Liquid((randrange(cream.rect.x + 37, cream.rect.x + 43), cream.rect.y+115), (255, 255, 255))
    if cream_counter < 100:
        cream_counter += 0.5


def milk_falling():
    global milk_counter
    for _ in range(3):
        Liquid((randrange(milk.rect.x + 7, milk.rect.x + 13), milk.rect.y+83), (255, 255, 255))
    if milk_counter < 100:
        milk_counter += 0.5


def mango_syrup_falling():
    global mango_counter
    for _ in range(3):
        Liquid((randrange(mango_syrup.rect.x + 22, mango_syrup.rect.x + 28), mango_syrup.rect.y+40), (255, 220, 28))
    if mango_counter < 100:
        mango_counter += 0.5


def cherry_syrup_falling():
    global chery_counter
    for _ in range(3):
        Liquid((randrange(cherry_syrup.rect.x + 22, cherry_syrup.rect.x + 28), cherry_syrup.rect.y+40), (125, 1, 1))
    if chery_counter < 100:
        chery_counter += 0.5


def count_viz(s):
    global mango_counter
    global chery_counter
    global milk_counter
    global cream_counter
    global coffee_counter
    image = load_image('book.png')
    rect = image.get_rect()
    rect.x = 632
    rect.y = 10
    screen.blit(image, rect)
    pygame.draw.rect(s, (131, 104, 0), (645, 28, 38, 10))
    font = pygame.font.Font(None, 14)
    text = font.render('recipes', True, (77, 61, 2))
    screen.blit(text, (647, 28))
    pygame.draw.rect(s, (255, 180, 0), (10, 10, 10, mango_counter))
    pygame.draw.rect(s, (150, 0, 0), (25, 10, 10, chery_counter))
    pygame.draw.rect(s, (255, 255, 255), (40, 10, 10, milk_counter))
    pygame.draw.rect(s, (200, 200, 200), (55, 10, 10, cream_counter))
    pygame.draw.rect(s, (100, 60, 0), (70, 10, 10, coffee_counter))
    pygame.draw.rect(s, (255, 255, 255), (10, 10, 10, 102), 2)
    pygame.draw.rect(s, (255, 255, 255), (25, 10, 10, 102), 2)
    pygame.draw.rect(s, (255, 255, 255), (40, 10, 10, 102), 2)
    pygame.draw.rect(s, (255, 255, 255), (55, 10, 10, 102), 2)
    pygame.draw.rect(s, (255, 255, 255), (70, 10, 10, 102), 2)


def draw_book():
    n = 80
    k = 240
    m = 400
    c = 25
    v = 155
    b = 280
    if is_open:
        pygame.draw.rect(screen, (160, 120, 90), (10, 0, 560, 405))
        # ---------------------------------------------------------------------------------------------------
        pygame.draw.rect(screen, (255, 180, 0), (10 + n, c, 10, recipes_lvl1['капучино'][0]))
        pygame.draw.rect(screen, (150, 0, 0), (25 + n, c, 10, recipes_lvl1['капучино'][1]))
        pygame.draw.rect(screen, (255, 255, 255), (40 + n, c, 10, recipes_lvl1['капучино'][2]))
        pygame.draw.rect(screen, (200, 200, 200), (55 + n, c, 10, recipes_lvl1['капучино'][3]))
        pygame.draw.rect(screen, (100, 60, 0), (70 + n, c, 10, recipes_lvl1['капучино'][4]))
        pygame.draw.rect(screen, (255, 255, 255), (10 + n, c, 10, 102), 2)
        pygame.draw.rect(screen, (255, 255, 255), (25 + n, c, 10, 102), 2)
        pygame.draw.rect(screen, (255, 255, 255), (40 + n, c, 10, 102), 2)
        pygame.draw.rect(screen, (255, 255, 255), (55 + n, c, 10, 102), 2)
        pygame.draw.rect(screen, (255, 255, 255), (70 + n, c, 10, 102), 2)
        pygame.draw.rect(screen, (255, 180, 0), (10 + k, c, 10, recipes_lvl1['латте'][0]))
        pygame.draw.rect(screen, (150, 0, 0), (25 + k, c, 10, recipes_lvl1['латте'][1]))
        pygame.draw.rect(screen, (255, 255, 255), (40 + k, c, 10, recipes_lvl1['латте'][2]))
        pygame.draw.rect(screen, (200, 200, 200), (55 + k, c, 10, recipes_lvl1['латте'][3]))
        pygame.draw.rect(screen, (100, 60, 0), (70 + k, c, 10, recipes_lvl1['латте'][4]))
        pygame.draw.rect(screen, (255, 255, 255), (10 + k, c, 10, 102), 2)
        pygame.draw.rect(screen, (255, 255, 255), (25 + k, c, 10, 102), 2)
        pygame.draw.rect(screen, (255, 255, 255), (40 + k, c, 10, 102), 2)
        pygame.draw.rect(screen, (255, 255, 255), (55 + k, c, 10, 102), 2)
        pygame.draw.rect(screen, (255, 255, 255), (70 + k, c, 10, 102), 2)
        pygame.draw.rect(screen, (255, 180, 0), (10 + m, c, 10, recipes_lvl1['эспрессо'][0]))
        pygame.draw.rect(screen, (150, 0, 0), (25 + m, c, 10, recipes_lvl1['эспрессо'][1]))
        pygame.draw.rect(screen, (255, 255, 255), (40 + m, c, 10, recipes_lvl1['эспрессо'][2]))
        pygame.draw.rect(screen, (200, 200, 200), (55 + m, c, 10, recipes_lvl1['эспрессо'][3]))
        pygame.draw.rect(screen, (100, 60, 0), (70 + m, c, 10, recipes_lvl1['эспрессо'][4]))
        pygame.draw.rect(screen, (255, 255, 255), (10 + m, c, 10, 102), 2)
        pygame.draw.rect(screen, (255, 255, 255), (25 + m, c, 10, 102), 2)
        pygame.draw.rect(screen, (255, 255, 255), (40 + m, c, 10, 102), 2)
        pygame.draw.rect(screen, (255, 255, 255), (55 + m, c, 10, 102), 2)
        pygame.draw.rect(screen, (255, 255, 255), (70 + m, c, 10, 102), 2)
        # -------------------------------------------------------------------------------------
        pygame.draw.rect(screen, (255, 180, 0), (10 + n, v, 10, recipes_lvl2['капучино с вишней'][0]))
        pygame.draw.rect(screen, (150, 0, 0), (25 + n, v, 10, recipes_lvl2['капучино с вишней'][1]))
        pygame.draw.rect(screen, (255, 255, 255), (40 + n, v, 10, recipes_lvl2['капучино с вишней'][2]))
        pygame.draw.rect(screen, (200, 200, 200), (55 + n, v, 10, recipes_lvl2['капучино с вишней'][3]))
        pygame.draw.rect(screen, (100, 60, 0), (70 + n, v, 10, recipes_lvl2['капучино с вишней'][4]))
        pygame.draw.rect(screen, (255, 255, 255), (10 + n, v, 10, 102), 2)
        pygame.draw.rect(screen, (255, 255, 255), (25 + n, v, 10, 102), 2)
        pygame.draw.rect(screen, (255, 255, 255), (40 + n, v, 10, 102), 2)
        pygame.draw.rect(screen, (255, 255, 255), (55 + n, v, 10, 102), 2)
        pygame.draw.rect(screen, (255, 255, 255), (70 + n, v, 10, 102), 2)
        pygame.draw.rect(screen, (255, 180, 0), (10 + k, v, 10, recipes_lvl2['латте с вишней'][0]))
        pygame.draw.rect(screen, (150, 0, 0), (25 + k, v, 10, recipes_lvl2['латте с вишней'][1]))
        pygame.draw.rect(screen, (255, 255, 255), (40 + k, v, 10, recipes_lvl2['латте с вишней'][2]))
        pygame.draw.rect(screen, (200, 200, 200), (55 + k, v, 10, recipes_lvl2['латте с вишней'][3]))
        pygame.draw.rect(screen, (100, 60, 0), (70 + k, v, 10, recipes_lvl2['латте с вишней'][4]))
        pygame.draw.rect(screen, (255, 255, 255), (10 + k, v, 10, 102), 2)
        pygame.draw.rect(screen, (255, 255, 255), (25 + k, v, 10, 102), 2)
        pygame.draw.rect(screen, (255, 255, 255), (40 + k, v, 10, 102), 2)
        pygame.draw.rect(screen, (255, 255, 255), (55 + k, v, 10, 102), 2)
        pygame.draw.rect(screen, (255, 255, 255), (70 + k, v, 10, 102), 2)
        pygame.draw.rect(screen, (255, 180, 0), (10 + m, v, 10, recipes_lvl2['раф'][0]))
        pygame.draw.rect(screen, (150, 0, 0), (25 + m, v, 10, recipes_lvl2['раф'][1]))
        pygame.draw.rect(screen, (255, 255, 255), (40 + m, v, 10, recipes_lvl2['раф'][2]))
        pygame.draw.rect(screen, (200, 200, 200), (55 + m, v, 10, recipes_lvl2['раф'][3]))
        pygame.draw.rect(screen, (100, 60, 0), (70 + m, v, 10, recipes_lvl2['раф'][4]))
        pygame.draw.rect(screen, (255, 255, 255), (10 + m, v, 10, 102), 2)
        pygame.draw.rect(screen, (255, 255, 255), (25 + m, v, 10, 102), 2)
        pygame.draw.rect(screen, (255, 255, 255), (40 + m, v, 10, 102), 2)
        pygame.draw.rect(screen, (255, 255, 255), (55 + m, v, 10, 102), 2)
        pygame.draw.rect(screen, (255, 255, 255), (70 + m, v, 10, 102), 2)
        # -------------------------------------------------------------------------------------
        pygame.draw.rect(screen, (255, 180, 0), (10 + n, b, 10, recipes_lvl3['раф с вишней'][0]))
        pygame.draw.rect(screen, (150, 0, 0), (25 + n, b, 10, recipes_lvl3['раф с вишней'][1]))
        pygame.draw.rect(screen, (255, 255, 255), (40 + n, b, 10, recipes_lvl3['раф с вишней'][2]))
        pygame.draw.rect(screen, (200, 200, 200), (55 + n, b, 10, recipes_lvl3['раф с вишней'][3]))
        pygame.draw.rect(screen, (100, 60, 0), (70 + n, b, 10, recipes_lvl3['раф с вишней'][4]))
        pygame.draw.rect(screen, (255, 255, 255), (10 + n, b, 10, 102), 2)
        pygame.draw.rect(screen, (255, 255, 255), (25 + n, b, 10, 102), 2)
        pygame.draw.rect(screen, (255, 255, 255), (40 + n, b, 10, 102), 2)
        pygame.draw.rect(screen, (255, 255, 255), (55 + n, b, 10, 102), 2)
        pygame.draw.rect(screen, (255, 255, 255), (70 + n, b, 10, 102), 2)
        pygame.draw.rect(screen, (255, 180, 0), (10 + k, b, 10, recipes_lvl3['раф с манго'][0]))
        pygame.draw.rect(screen, (150, 0, 0), (25 + k, b, 10, recipes_lvl3['раф с манго'][1]))
        pygame.draw.rect(screen, (255, 255, 255), (40 + k, b, 10, recipes_lvl3['раф с манго'][2]))
        pygame.draw.rect(screen, (200, 200, 200), (55 + k, b, 10, recipes_lvl3['раф с манго'][3]))
        pygame.draw.rect(screen, (100, 60, 0), (70 + k, b, 10, recipes_lvl3['раф с манго'][4]))
        pygame.draw.rect(screen, (255, 255, 255), (10 + k, b, 10, 102), 2)
        pygame.draw.rect(screen, (255, 255, 255), (25 + k, b, 10, 102), 2)
        pygame.draw.rect(screen, (255, 255, 255), (40 + k, b, 10, 102), 2)
        pygame.draw.rect(screen, (255, 255, 255), (55 + k, b, 10, 102), 2)
        pygame.draw.rect(screen, (255, 255, 255), (70 + k, b, 10, 102), 2)
        pygame.draw.rect(screen, (255, 180, 0), (10 + m, b, 10, recipes_lvl3['раф манго и вишня'][0]))
        pygame.draw.rect(screen, (150, 0, 0), (25 + m, b, 10, recipes_lvl3['раф манго и вишня'][1]))
        pygame.draw.rect(screen, (255, 255, 255), (40 + m, b, 10, recipes_lvl3['раф манго и вишня'][2]))
        pygame.draw.rect(screen, (200, 200, 200), (55 + m, b, 10, recipes_lvl3['раф манго и вишня'][3]))
        pygame.draw.rect(screen, (100, 60, 0), (70 + m, b, 10, recipes_lvl3['раф манго и вишня'][4]))
        pygame.draw.rect(screen, (255, 255, 255), (10 + m, b, 10, 102), 2)
        pygame.draw.rect(screen, (255, 255, 255), (25 + m, b, 10, 102), 2)
        pygame.draw.rect(screen, (255, 255, 255), (40 + m, b, 10, 102), 2)
        pygame.draw.rect(screen, (255, 255, 255), (55 + m, b, 10, 102), 2)
        pygame.draw.rect(screen, (255, 255, 255), (70 + m, b, 10, 102), 2)
        font = pygame.font.Font(None, 20)
        lvl1 = font.render(" капучино                            латте                             эспрессо", True,
                           (255, 255, 255))
        lvl1_x = 90
        lvl1_y = 10
        screen.blit(lvl1, (lvl1_x, lvl1_y))

        lvl2 = font.render(" капучино с вишней           латте с вишней                        раф ", True,
                           (255, 255, 255))
        lvl2_x = 60
        lvl2_y = 140
        screen.blit(lvl2, (lvl2_x, lvl2_y))

        lvl3 = font.render("   раф с вишней                  раф с манго                раф манго и вишня", True,
                           (255, 255, 255))
        lvl3_x = 70
        lvl3_y = 263
        screen.blit(lvl3, (lvl3_x, lvl3_y))
        pygame.display.flip()


def recipes_book(*args):
    global is_open
    is_open = False
    if args[0].type == pygame.MOUSEBUTTONDOWN and 631 < args[0].pos[0] < 689 and 9 < args[0].pos[1] < 76:
        if not is_open:
            is_open = True
        else:
            is_open = False


class Button(pygame.sprite.Sprite):
    def __init__(self, text, text_coord):
        super().__init__(buttons_group, all_sprites)
        self.btn_text = text
        self.size = (120, 25)
        self.image = pygame.Surface((150, 30), pygame.SRCALPHA, 32)
        self.rect = pygame.Rect(*text_coord, *self.size)
        self.font = pygame.font.Font(None, 25)
        pygame.draw.rect(self.image, (242, 151, 65), (0, 0, *self.size))
        pygame.draw.rect(self.image, (252, 199, 149), (3, 3, self.size[0] - 6, self.size[1] - 6))
        self.text = self.font.render(self.btn_text, 1, (89, 58, 29))
        self.image.blit(self.text, (4, 4))
        screen.blit(self.image, self.rect)

    def update(self, *args):
        if self.rect.collidepoint(args[0].pos):
            if self.btn_text == 'New game':
                order_screen()
            if self.btn_text == 'Continue':
                print('game continued')
            if self.btn_text == 'Instruct':
                print('instruct is opened')
            if self.btn_text == 'Отказаться':
                ordering()
            if self.btn_text == 'Принять':
                cooking_screen()
            if self.btn_text == "Сбросить":
                global mango_counter
                global chery_counter
                global milk_counter
                global cream_counter
                global coffee_counter
                mango_counter = 0
                chery_counter = 0
                milk_counter = 0
                cream_counter = 0
                coffee_counter = 0


class Dialog(pygame.sprite.Sprite):
    def __init__(self, text):
        super().__init__(all_sprites, dialog_group)
        self.text = text[::]
        self.size = (500, 10 + 15 * len(self.text) + 10)
        self.image = pygame.Surface(self.size, pygame.SRCALPHA, 32)
        self.rect = pygame.Rect(100, 300, *self.size)
        self.font = pygame.font.Font(None, 25)
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


class CoffeMachine(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites, things_group)
        self.image = self.image = load_image("coffee_machine.png")
        self.rect = self.image.get_rect()
        self.rect.x = width // 2 - self.rect.width
        self.rect.y = 70
        screen.blit(self.image, self.rect)


class Cream(pygame.sprite.Sprite):
    image = load_image("cream_pitcher.png")

    def __init__(self):
        super().__init__(all_sprites, things_group)
        self.image = Cream.image
        self.rect = self.image.get_rect()
        self.rect.x = 20
        self.rect.y = 140
        self.true_pos = (self.rect.x, self.rect.y)
        self.is_moving = False
        self.is_adding = False
        screen.blit(self.image, self.rect)

    def update(self, *args):
        if args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            if args[0].button == 1:
                if not self.is_moving:
                    self.rect = self.image.get_rect()
                    self.rect.x = args[0].pos[0] - 15
                    self.rect.y = args[0].pos[1] - self.rect.height // 2 + 30
                    self.is_moving = True
                    pygame.mouse.set_visible(False)
                else:
                    if not self.is_adding and add_zone.rect.collidepoint(args[0].pos):
                        self.is_adding = True
                        self.image = pygame.transform.rotate(self.image, 30)
                        self.rect = self.image.get_rect()
                        self.rect.x = args[0].pos[0] - 40
                        self.rect.y = args[0].pos[1] - self.rect.height // 2
                    else:
                        self.is_adding = False
                        self.image = Cream.image
                        self.rect = self.image.get_rect()
                        self.rect.x = args[0].pos[0] - 15
                        self.rect.y = args[0].pos[1] - self.rect.height // 2 + 30
            elif args[0].button == 3 and self.is_moving:
                self.image = Cream.image
                self.rect = self.image.get_rect()
                self.rect.x = self.true_pos[0]
                self.rect.y = self.true_pos[-1]
                self.is_moving = False
                self.is_adding = False
                pygame.mouse.set_visible(True)
        if self.is_moving and args[0].type == pygame.MOUSEMOTION:
            if not self.is_adding:
                self.rect.x = args[0].pos[0] - 15
                self.rect.y = args[0].pos[1] - self.rect.height // 2 + 30
            else:
                self.rect.x = args[0].pos[0] - 40
                self.rect.y = args[0].pos[1] - self.rect.height // 2
                if not add_zone.rect.collidepoint(args[0].pos):
                    self.is_adding = False
                    self.image = Cream.image
            if pygame.mouse.get_focused():
                all_sprites.draw(screen)
        screen.blit(fon, (0, 0))


class Milk(pygame.sprite.Sprite):
    image = load_image("milk_pitcher.png")

    def __init__(self):
        super().__init__(all_sprites, things_group)
        self.image = Milk.image
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 130
        self.true_pos = (self.rect.x, self.rect.y)
        self.is_moving = False
        self.is_adding = False
        screen.blit(self.image, self.rect)

    def update(self, *args):
        if args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            if args[0].button == 1:
                if not self.is_moving:
                    self.rect = self.image.get_rect()
                    self.rect.x = args[0].pos[0]
                    self.rect.y = args[0].pos[1] - 25
                    self.is_moving = True
                    pygame.mouse.set_visible(False)
                else:
                    if not self.is_adding and add_zone.rect.collidepoint(args[0].pos):
                        self.is_adding = True
                        self.image = pygame.transform.rotate(self.image, 30)
                        self.rect = self.image.get_rect()
                        self.rect.x = args[0].pos[0] - 10
                        self.rect.y = args[0].pos[1] - 75
                    else:
                        self.is_adding = False
                        self.image = Milk.image
                        self.rect = self.image.get_rect()
                        self.rect.x = args[0].pos[0]
                        self.rect.y = args[0].pos[1] - 25
            elif args[0].button == 3 and self.is_moving:
                self.image = Milk.image
                self.rect = self.image.get_rect()
                self.rect.x = self.true_pos[0]
                self.rect.y = self.true_pos[-1]
                self.is_moving = False
                self.is_adding = False
                pygame.mouse.set_visible(True)
        if self.is_moving and args[0].type == pygame.MOUSEMOTION:
            if not self.is_adding:
                self.rect.x = args[0].pos[0]
                self.rect.y = args[0].pos[1] - 25
            else:
                self.rect.x = args[0].pos[0] - 10
                self.rect.y = args[0].pos[1] - 75
                if not add_zone.rect.collidepoint(args[0].pos):
                    self.is_adding = False
                    self.image = Milk.image
            if pygame.mouse.get_focused():
                all_sprites.draw(screen)
        screen.blit(fon, (0, 0))


class CherrySyrup(pygame.sprite.Sprite):
    image = load_image('syrup1.png')

    def __init__(self):
        super().__init__(all_sprites, things_group)
        self.true_image = CherrySyrup.image
        self.image = self.true_image
        self.rect = self.image.get_rect()
        self.rect.x = 630
        self.rect.y = 145
        self.true_pos = (self.rect.x, self.rect.y)
        self.is_moving = False
        self.is_adding = False
        screen.blit(self.image, self.rect)

    def update(self, *args):
        if args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            if args[0].button == 1:
                if not self.is_moving:
                    self.rect = self.image.get_rect()
                    self.rect.x = args[0].pos[0] - 40
                    self.rect.y = args[0].pos[1]
                    self.is_moving = True
                    pygame.mouse.set_visible(False)
                else:
                    if not self.is_adding and add_zone.rect.collidepoint(args[0].pos):
                        self.is_adding = True
                        self.image = pygame.transform.rotate(self.image, 40)
                        self.rect = self.image.get_rect()
                        self.rect.x = args[0].pos[0] - 30
                        self.rect.y = args[0].pos[1] - 20
                    else:
                        self.is_adding = False
                        self.image = self.true_image
                        self.rect = self.image.get_rect()
                        self.rect.x = args[0].pos[0] - 40
                        self.rect.y = args[0].pos[1]
            elif args[0].button == 3 and self.is_moving:
                self.image = self.true_image
                self.rect = self.image.get_rect()
                self.rect.x = self.true_pos[0]
                self.rect.y = self.true_pos[-1]
                self.is_moving = False
                self.is_adding = False
                pygame.mouse.set_visible(True)
        if self.is_moving and args[0].type == pygame.MOUSEMOTION:
            if not self.is_adding:
                self.rect.x = args[0].pos[0] - 40
                self.rect.y = args[0].pos[1]
            else:
                self.rect.x = args[0].pos[0] - 30
                self.rect.y = args[0].pos[1] - 20
                if not add_zone.rect.collidepoint(args[0].pos):
                    self.is_adding = False
                    self.image = CherrySyrup.image
            if pygame.mouse.get_focused():
                all_sprites.draw(screen)
        screen.blit(fon, (0, 0))


class MangoSyrup(pygame.sprite.Sprite):
    image = load_image('syrup2.png')

    def __init__(self):
        super().__init__(all_sprites, things_group)
        self.true_image = MangoSyrup.image
        self.image = self.true_image
        self.rect = self.image.get_rect()
        self.rect.x = 540
        self.rect.y = 140
        self.true_pos = (self.rect.x, self.rect.y)
        self.is_moving = False
        self.is_adding = False
        screen.blit(self.image, self.rect)

    def update(self, *args):
        if args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            if args[0].button == 1:
                if not self.is_moving:
                    self.rect = self.image.get_rect()
                    self.rect.x = args[0].pos[0] - 40
                    self.rect.y = args[0].pos[1]
                    self.is_moving = True
                    pygame.mouse.set_visible(False)
                else:
                    if not self.is_adding and add_zone.rect.collidepoint(args[0].pos):
                        self.is_adding = True
                        self.image = pygame.transform.rotate(self.image, 40)
                        self.rect = self.image.get_rect()
                        self.rect.x = args[0].pos[0] - 30
                        self.rect.y = args[0].pos[1] - 20
                    else:
                        self.is_adding = False
                        self.image = self.true_image
                        self.rect = self.image.get_rect()
                        self.rect.x = args[0].pos[0] - 40
                        self.rect.y = args[0].pos[1]
            elif args[0].button == 3 and self.is_moving:
                self.image = self.true_image
                self.rect = self.image.get_rect()
                self.rect.x = self.true_pos[0]
                self.rect.y = self.true_pos[-1]
                self.is_moving = False
                self.is_adding = False
                pygame.mouse.set_visible(True)
        if self.is_moving and args[0].type == pygame.MOUSEMOTION:
            if not self.is_adding:
                self.rect.x = args[0].pos[0] - 40
                self.rect.y = args[0].pos[1]
            else:
                self.rect.x = args[0].pos[0] - 30
                self.rect.y = args[0].pos[1] - 20
                if not add_zone.rect.collidepoint(args[0].pos):
                    self.is_adding = False
                    self.image = MangoSyrup.image
            if pygame.mouse.get_focused():
                all_sprites.draw(screen)
        screen.blit(fon, (0, 0))


class Cup(pygame.sprite.Sprite):
    image = load_image('open_cup.png')
    little_image = load_image('little_open_cup.png')

    def __init__(self):
        super().__init__(all_sprites, things_group)
        self.image = Cup.image
        self.rect = self.image.get_rect()
        self.rect.x = width // 2 - self.rect.width // 2
        self.rect.y = 250
        self.true_pos = (self.rect.x, self.rect.y)
        self.is_moving = False
        self.is_in_coffee_machine = False
        screen.blit(self.image, self.rect)

    def update(self, *args):
        if args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            if args[0].button == 1:
                if not self.is_moving:
                    self.image = Cup.image
                    self.is_in_coffee_machine = False
                    self.rect = self.image.get_rect()
                    self.rect.x = args[0].pos[0] - self.rect.width // 2
                    self.rect.y = args[0].pos[1] - self.rect.height // 2
                    self.is_moving = True
                    pygame.mouse.set_visible(False)
            elif args[0].button == 3 and self.is_moving:
                if coffe_machine.rect.collidepoint(args[0].pos):
                    self.is_in_coffee_machine = True
                    self.image = Cup.little_image
                    self.rect = self.image.get_rect()
                    self.rect.x = coffe_machine.rect.x + coffe_machine.rect.width // 2 - self.rect.width // 2 + 2
                    self.rect.y = coffe_machine.rect.y + coffe_machine.rect.height - self.rect.height - 38
                else:
                    self.rect.x = self.true_pos[0]
                    self.rect.y = self.true_pos[-1]
                self.is_moving = False
                pygame.mouse.set_visible(True)
        if self.is_moving and args[0].type == pygame.MOUSEMOTION:
            self.rect.x = args[0].pos[0] - self.rect.width // 2
            self.rect.y = args[0].pos[1] - self.rect.height // 2
            if pygame.mouse.get_focused():
                all_sprites.draw(screen)
        screen.blit(fon, (0, 0))


class Liquid(pygame.sprite.Sprite):
    def __init__(self, pos, color):
        super().__init__(all_sprites, liquid_group)
        self.size = (2, 5)
        self.image = pygame.Surface(self.size, pygame.SRCALPHA, 32)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos
        pygame.draw.rect(self.image, color, (0, 0, *size))
        self.velocity_y = 0.1

    def update(self):
        self.velocity_y += GRAVITY
        self.rect.y += self.velocity_y
        screen.blit(self.image, self.rect)
        if self.rect.colliderect(cup.rect):
            self.kill()


class AddZone(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.size = (cup.rect.width - 8, 240)
        self.image = pygame.Surface(self.size, pygame.SRCALPHA, 32)
        self.rect = self.image.get_rect()
        self.rect.x = cup.rect.x + 4
        self.rect.y = 0
        screen.blit(self.image, self.rect)


if __name__ == '__main__':
    pygame.init()
    size = width, height = 720, 405
    fps = 50
    GRAVITY = 0.1
    is_open = False
    screen_is = 'start'
    screen = pygame.display.set_mode(size)
    clock = Clock()
    all_sprites = pygame.sprite.Group()
    buttons_group = pygame.sprite.Group()
    dialog_group = pygame.sprite.Group()
    things_group = pygame.sprite.Group()
    liquid_group = pygame.sprite.Group()
    running = True
    start_screen()
    global fon
    while running:
        screen.blit(fon, (0, 0))
        for event in pygame.event.get():
            recipes_book(event)
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                buttons_group.update(event)
                things_group.update(event)
            if event.type == pygame.MOUSEMOTION:
                things_group.update(event)
        if screen_is == 'cook':
            global cup, cream, milk, mango_syrup, cherry_syrup, coffee_order
            liquid_group.update()
            things_group.draw(screen)
            liquid_group.draw(screen)
            count_viz(screen)
            draw_book()
            if cup.is_in_coffee_machine:
                coffee_falling()
            if cream.is_adding:
                cream_falling()
            if milk.is_adding:
                milk_falling()
            if mango_syrup.is_adding:
                mango_syrup_falling()
            if cherry_syrup.is_adding:
                cherry_syrup_falling()
            if not is_open:
                font = pygame.font.Font(None, 30)
                order_text = font.render(f'Заказ: {coffee_order}', 1, (89, 58, 29))
                screen.blit(order_text, (width // 2 - 100, 20))
                buttons_group.draw(screen)
        elif screen_is == 'order':
            guy = load_image('guy3.png')
            screen.blit(guy, (220, 68))
            dialog_group.draw(screen)
            buttons_group.draw(screen)
        else:
            buttons_group.draw(screen)
        pygame.display.flip()
        clock.tick(fps)
