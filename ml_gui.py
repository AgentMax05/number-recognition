import pygame
from PIL import Image
from sys import exit
import math

from ml import predict_num

pygame.init()
window = pygame.display.set_mode((224, 224))
pygame.display.set_caption("Tic-Tac-Toe Image Creator")

drawn_squares = []
last_pos = None

image_divider = 8
holding = False

def mainloop():
    clock = pygame.time.Clock()
    while True:
        clock.tick(75)
        check_events()
        update_display()

def check_events():
    global holding
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            draw(pygame.mouse.get_pos())
            holding = True
        if event.type == pygame.MOUSEMOTION and holding:
            draw(pygame.mouse.get_pos())
        if event.type == pygame.MOUSEBUTTONUP and holding:
            holding = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                make_guess()


def make_guess():
    global drawn_squares

    surface_string = pygame.image.tostring(window, "RGBA", False)
    image = Image.frombytes("RGBA", window.get_size(), surface_string)
    image = image.resize((28, 28))
    image = image.convert("1")
    # image.show()
    pixel_data = list(image.getdata())
    print(predict_num(pixel_data))
    drawn_squares = []


def draw(mouse_pos):
    global last_pos

    mouse_pos = (math.floor(mouse_pos[0] / image_divider) * image_divider, math.floor(mouse_pos[1] / image_divider) * image_divider)
    if mouse_pos == last_pos:
        return
    
    last_pos = mouse_pos

    x, y = mouse_pos
    current_color = window.get_at(mouse_pos)
    if current_color == (0, 0, 0, 255):
        drawn_squares.append((x, y))

def update_display():
    window.fill((0, 0, 0))

    for square in drawn_squares:
        pygame.draw.rect(window, (255, 255, 255), (square[0], square[1], image_divider, image_divider))

    pygame.display.update()

mainloop()