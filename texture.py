import pygame
from OpenGL.GL import *
import numpy as np

def load_texture():

    texture_surface = pygame.image.load('gif&img/tekstura.png')
    texture_data = pygame.image.tostring(texture_surface, "RGBA", 1)
    width, height = texture_surface.get_width(), texture_surface.get_height()

    texture = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, texture_data)

    return texture, width, height

pygame.init()
window_width, window_height = 800, 600
pygame.display.set_mode((window_width, window_height), pygame.OPENGL | pygame.DOUBLEBUF)

# Загрузка текстуры
texture, texture_width, texture_height = load_texture()

# Установка параметров OpenGL
glEnable(GL_TEXTURE_2D)
glClearColor(0.0, 0.0, 0.0, 1.0)
glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

clock = pygame.time.Clock()

cursor_x, cursor_y = 0, 0
is_texture_drawn = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = event.pos
            cursor_x = mouse_x / window_width * 2 - 1
            cursor_y = 1 - mouse_y / window_height * 2
            is_texture_drawn = True

    # Очистка экрана цветом белого
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glLoadIdentity()

    if is_texture_drawn:
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex2f(-1, 1)
        glTexCoord2f(1, 0)
        glVertex2f(cursor_x, 1)
        glTexCoord2f(1, 1)
        glVertex2f(cursor_x, cursor_y)
        glTexCoord2f(0, 1)
        glVertex2f(-1, cursor_y)
        glEnd()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
