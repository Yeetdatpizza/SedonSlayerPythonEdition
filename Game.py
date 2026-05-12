import pygame
from MrSedon import *
import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Sedon Slayer: Python Edition')
image = pygame.image.load(r"Images\SedonSlayerLogo.png")
pygame.display.set_icon(image)
clock = pygame.time.Clock()
running = True

sedon = Sedon(starting_health, starting_ammo, starting_speed, starting_direction, Vector2(screen.get_width() / 2, screen.get_height() / 2))

def update_frame():
    screen.fill("white")
    sedon_image = pygame.image.load(r"Images\MrSedon.png").convert_alpha()
    ruler_image = pygame.image.load(r"Images\SedonRuler.png").convert_alpha()
    if pygame.mouse.get_pos()[0] < sedon.get_position()[0] + sedon_image.get_width() / 2 :
        sedon_image = pygame.image.load(r"Images\MrSedon.png").convert_alpha()
        screen.blit(sedon_image, (sedon.get_position()[0], sedon.get_position()[1]))
        screen.blit(ruler_image, (sedon.get_position()[0], sedon.get_position()[1]))
    else:
        sedon_image = pygame.image.load(r"Images\MrSedon.png").convert_alpha()
        sedon_image = pygame.transform.flip(sedon_image, True, False)
        screen.blit(sedon_image, (sedon.get_position()[0], sedon.get_position()[1]))
        screen.blit(ruler_image, (sedon.get_position()[0], sedon.get_position()[1]))


    if sedon.get_position().y > screen.get_height()  - sedon_image.get_height() and sedon.get_force() >0:
        sedon.update_force(0)

        if sedon.get_is_jumping():
            sedon.update_is_jumping()

    elif not sedon.get_is_jumping():
        sedon.update_force(5)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if not sedon.get_is_jumping():
            sedon.update_is_jumping()
            sedon.update_force(-15)

    if keys[pygame.K_a]:
        sedon.update_position_x(-(4 * sedon_distance))
    if keys[pygame.K_d]:
        sedon.update_position_x((4 * sedon_distance))


    if sedon.get_force() != 15:
        sedon.update_position_y(sedon.get_force())

        if sedon.get_force() < 15:
            sedon.update_force(sedon.get_force() + 1)
        else:
            sedon.update_force(sedon.get_force() - 1)

    else:
        if sedon.get_is_jumping():
            sedon.update_is_jumping()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    update_frame()
    pygame.display.flip()

    clock.tick(60)

pygame.quit()