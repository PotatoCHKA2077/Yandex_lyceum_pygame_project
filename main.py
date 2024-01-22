import os
import sys
from random import *
import pygame
from pygame.time import Clock
mango_counter = 0
chery_counter = 0
milk_counter = 0
cream_counter = 0
coffee_counter = 0


def load_image(name):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        terminate()
    image = pygame.image.load(fullname)
    return image


def terminate():
    pygame.quit()
    sys.exit()


def coffee_falling():
    global coffee_counter
    for _ in range(4):
        Liquid((choice([randrange(coffe_machine.rect.x + 80, coffe_machine.rect.x + 84),
                        randrange(coffe_machine.rect.x+102, coffe_machine.rect.x+106)]),
                coffe_machine.rect.y + 149), (99, 52, 1))
    if coffee_counter < 100:
        coffee_counter += 1


def cream_falling():
    global cream_counter
    for _ in range(3):
        Liquid((randrange(cream.rect.x + 37, cream.rect.x + 43), cream.rect.y+115), (255, 255, 255))
    if cream_counter < 100:
        cream_counter += 1


def milk_falling():
    global milk_counter
    for _ in range(3):
        Liquid((randrange(milk.rect.x + 7, milk.rect.x + 13), milk.rect.y+83), (255, 255, 255))
    if milk_counter < 100:
        milk_counter += 1


def mango_syrup_falling():
    global mango_counter
    for _ in range(3):
        Liquid((randrange(mango_syrup.rect.x + 22, mango_syrup.rect.x + 28), mango_syrup.rect.y+40), (255, 220, 28))
    if mango_counter < 100:
        mango_counter += 1


def cherry_syrup_falling():
    global chery_counter
    for _ in range(3):
        Liquid((randrange(cherry_syrup.rect.x + 22, cherry_syrup.rect.x + 28), cherry_syrup.rect.y+40), (125, 1, 1))
    if chery_counter < 100:
        chery_counter += 1


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


def count_viz(s):
    global mango_counter
    global chery_counter
    global milk_counter
    global cream_counter
    global coffee_counter
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


if __name__ == '__main__':
    pygame.init()
    size = width, height = 720, 405
    fps = 50
    GRAVITY = 0.1
    screen = pygame.display.set_mode(size)
    clock = Clock()
    all_sprites = pygame.sprite.Group()
    things_group = pygame.sprite.Group()
    liquid_group = pygame.sprite.Group()
    cur_group = pygame.sprite.Group()
    running = True
    fon = pygame.transform.scale(load_image('table_fon.png'), (width, height))
    screen.blit(fon, (0, 0))
    coffe_machine = CoffeMachine()
    cream = Cream()
    milk = Milk()
    mango_syrup = MangoSyrup()
    cherry_syrup = CherrySyrup()
    cup = Cup()
    add_zone = AddZone()
    while running:

        screen.blit(fon, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEMOTION:
                things_group.update(event)
            cur_group.update(event)
        liquid_group.update()
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
        all_sprites.draw(screen)
        count_viz(screen)
        pygame.display.flip()
        clock.tick(fps)
