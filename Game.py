"""
This is the main runner file for the game
It handles all of the math and other logic
Basically connects everything together so it all works properly
"""

import random
from Kiggle import Kiggle
from MrSedon import *
import pygame
import math
from Platform import *
from Ruler import *

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN | pygame.SCALED)
#screen = pygame.display.set_mode((1080, 800))
pygame.display.set_caption('Sedon Slayer: Python Edition')
image = pygame.image.load(r"Images\SedonSlayerLogo.png")
pygame.display.set_icon(image)
clock = pygame.time.Clock()
running = True
score = 0
hasRuler = True
rulerCooldown = 120 - (score * 2)

rulerWhack = pygame.mixer.Sound("Audio\Whack.mp3")

pygame.mixer.music.load(r"Audio\MenuTheme.mp3")
pygame.mixer.music.play(loops=-1)




font = pygame.font.SysFont("Arial", 60)
titleCard = font.render("SEDON SLAYER: PYTHON EDITION", True, (255, 212, 59), (0, 0, 0))
title_rect = titleCard.get_rect()
title_rect.center = (screen.get_width() // 2, int (screen.get_height() / 3))

subtitleCard = font.render("(Click anywhere to start)", True, (255, 212, 59), (0, 0, 0))
subtitle_rect = subtitleCard.get_rect()
subtitle_rect.center = (screen.get_width() // 2, int (screen.get_height() / 1.5))

screen.blit(titleCard, title_rect)
screen.blit(subtitleCard, subtitle_rect)

gameHasStarted = False

kiggles = [
    pygame.transform.scale(pygame.image.load(r"Images\billy.png"), (150, 150)),
    pygame.transform.scale(pygame.image.load(r"Images\tino.png"), (150, 150)),
    pygame.transform.scale(pygame.image.load(r"Images\jack.png"), (150, 150)),
    pygame.transform.scale(pygame.image.load(r"Images\jay.png"), (150, 150)),
    pygame.transform.scale(pygame.image.load(r"Images\spy.png"), (150, 150)),
    pygame.transform.scale(pygame.image.load(r"Images\david.png"), (150, 150)),
    pygame.transform.scale(pygame.image.load(r"Images\emma.jpg"), (150, 150)),
    pygame.transform.scale(pygame.image.load(r"Images\owen.png"), (150, 150))
]

ruler_angle = 0

sedon = Sedon(starting_health, starting_ammo, starting_speed, starting_direction, Vector2(screen.get_width() / 2, 0))

list_of_opps = []
list_of_platforms = []
list_of_rulers = []

def spawn_Kiggle():
    newOpp = Kiggle(Vector2(random.randint(int (sedon.get_position().x - 4000), int (sedon.get_position().x + 4000)), 0), random.choice(kiggles))
    list_of_opps.append(newOpp)
    
    #list_of_opps.append(Kiggle(Vector2(sedon.get_position().x, sedon.get_position().y)))

def endGame():

    pygame.mixer.music.stop()
    pygame.mixer.music.load(r"Audio\LoseTheme.mp3")
    pygame.mixer.music.play(loops=-1)

    global gameHasStarted
    gameHasStarted = False

    global score
    score = 0 

    list_of_opps.clear()

    list_of_platforms.clear()

    screen.fill("black")

    font = pygame.font.SysFont("Arial", 60)
    titleCard = font.render("You lost!", True, (255, 212, 59), (0, 0, 0))
    title_rect = titleCard.get_rect()
    title_rect.center = (screen.get_width() // 2, int(screen.get_height() / 3))

    subtitleCard = font.render("(Click anywhere to retry)", True, (255, 212, 59), (0, 0, 0))
    subtitle_rect = subtitleCard.get_rect()
    subtitle_rect.center = (screen.get_width() // 2, int(screen.get_height() / 1.5))

    screen.blit(titleCard, title_rect)
    screen.blit(subtitleCard, subtitle_rect)


def updateKiggles(list_of_opps):
    for opp in list_of_opps:

        kiggleImage = opp.getImage()

        distanceFromOppX = opp.getPosition()[0] - sedon.get_position().x
        distanceFromOppY = opp.getPosition()[1] - sedon.get_position().y

        if abs(distanceFromOppX) + abs(distanceFromOppY) < 150:
            endGame()
            return

        if distanceFromOppX >= 0:
            opp.setPosition(Vector2(opp.getPosition()[0] - (1 * (((score + 1) / 20) + 1)), opp.getPosition()[1]))
        else:
            opp.setPosition(Vector2(opp.getPosition()[0] + (1 * (((score + 1) / 20) + 1)), opp.getPosition()[1]))

        if distanceFromOppY >= 0:
            opp.setPosition(Vector2(opp.getPosition()[0], opp.getPosition()[1] - (1 * (((score + 1) / 20) + 1))))
        else:
            opp.setPosition(Vector2(opp.getPosition()[0], opp.getPosition()[1] + (1 * (((score + 1) / 20) + 1))))

        screen.blit(kiggleImage, (opp.getPosition()[0], opp.getPosition()[1]))


def update_sedon(hasRuler):

    sedon_image = pygame.image.load(r"Images\MrSedon.png").convert_alpha()
    ruler_image = pygame.image.load(r"Images\SedonRuler.png").convert_alpha()
    global ruler_angle
    ruler_angle = math.atan2((sedon.get_position()[1] + sedon_image.get_height() / 2) - pygame.mouse.get_pos()[1], (sedon.get_position()[0] + sedon_image.get_width() / 2) - pygame.mouse.get_pos()[0]) * -1
    if pygame.mouse.get_pos()[0] < sedon.get_position()[0] + sedon_image.get_width() / 2:
        sedon_image = pygame.image.load(r"Images\MrSedon.png").convert_alpha()
        screen.blit(sedon_image, (sedon.get_position()[0], sedon.get_position()[1]))
        ruler_rotated = pygame.transform.rotate(ruler_image, ruler_angle * 180 / math.pi)
        ruler_box = ruler_rotated.get_rect(center = (sedon.get_position()[0] + sedon_image.get_width() / 2,sedon.get_position()[1] + sedon_image.get_height() / 1.5))

        if hasRuler:
            screen.blit(ruler_rotated, ruler_box)
    else:
        sedon_image = pygame.image.load(r"Images\MrSedon.png").convert_alpha()
        sedon_image = pygame.transform.flip(sedon_image, True, False)
        screen.blit(sedon_image, (sedon.get_position()[0], sedon.get_position()[1]))
        ruler_rotated = pygame.transform.rotate(ruler_image, ruler_angle * 180 / math.pi)
        ruler_box = ruler_rotated.get_rect(center = (sedon.get_position()[0] + sedon_image.get_width() / 2, sedon.get_position()[1] + sedon_image.get_height() / 1.5))

        if hasRuler:
            screen.blit(ruler_rotated, ruler_box)

    for platform in list_of_platforms:
        if platform.position.x - (platform.size.x / 2) < sedon.get_position().x + sedon_image.get_width() / 2 and (platform.getTop() < sedon.get_position().y + sedon_image.get_height() and platform.position.x + (platform.size.x / 2) > sedon.get_position().x + sedon_image.get_width() / 2):
            sedon.set_position((sedon.get_position().x, platform.getTop() - sedon_image.get_height()))

    if not sedon.get_is_jumping():
        sedon.update_force(5)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if not sedon.get_is_jumping():
            sedon.update_is_jumping()
            sedon.update_force(-15)

    if keys[pygame.K_a]:
        for platform in list_of_platforms:
            platform.setPosition([platform.getPosition().x + 4, platform.getPosition().y])
        for opp in list_of_opps:
            opp.setPosition([opp.getPosition()[0] + 4, opp.getPosition()[1]])
        for ruler in list_of_rulers:
            ruler.setPosition([ruler.getPosition()[0] + 4, ruler.getPosition()[1]])
    if keys[pygame.K_d]:
        for platform in list_of_platforms:
            platform.setPosition([platform.getPosition().x - 4, platform.getPosition().y])
        for opp in list_of_opps:
            opp.setPosition([opp.getPosition()[0] - 4, opp.getPosition()[1]])
        for ruler in list_of_rulers:
            ruler.setPosition([ruler.getPosition()[0] - 4, ruler.getPosition()[1]])

    if sedon.get_force() != 15:
        sedon.update_position_y(sedon.get_force())

        if sedon.get_force() < 15:
            sedon.update_force(sedon.get_force() + 1)
        else:
            sedon.update_force(sedon.get_force() - 1)

    else:
        if sedon.get_is_jumping():
            sedon.update_is_jumping()



def update_frame(gameHasStarted):

    if gameHasStarted:

        screen.fill("aqua")

        global score

        font = pygame.font.SysFont("Arial", 60)
        scoreText = font.render(f"Score: {score}", True, (0, 0, 0), "aqua")
        score_rect = scoreText.get_rect()
        score_rect.center = (score_rect.width // 2, score_rect.height // 2)

        screen.blit(scoreText, score_rect)

        update_sedon(hasRuler)

        if random.randint(1, math.floor(180  /  (1 + (score / 20)))) == 1:
            spawn_Kiggle()
        for platform in list_of_platforms:
            pygame.draw.rect(screen, (63, 155, 11), platform.getBoundingBox())

        for ruler in list_of_rulers:

            for opp in list_of_opps:
                if abs((opp.getPosition()[0] + (opp.getImage().get_width() / 2)) - ruler.getPosition()[0]) < 75 and abs((opp.getPosition()[1] + (opp.getImage().get_height() / 2)) - ruler.getPosition()[1]) < 75:
                    list_of_opps.remove(opp)
                    list_of_rulers.remove(ruler)
                    score += 1
                    rulerWhack.play()
                    break

            ruler_image = pygame.image.load(r"Images\SedonRuler.png").convert_alpha()
            ruler_rotated = pygame.transform.rotate(ruler_image, ruler.getAngle() * 180 / math.pi)
            ruler_box = ruler_rotated.get_rect(center=(ruler.getPosition()[0],ruler.getPosition()[1]))
            screen.blit(ruler_rotated, ruler_box)

            ruler.setPosition(Vector2(ruler.getPosition()[0] - (math.cos(ruler.getAngle()) * 10), ruler.getPosition()[1] + (math.sin(ruler.getAngle()) * 10)))

        updateKiggles(list_of_opps)


while running:
    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:

            if not gameHasStarted:
                pygame.mixer.music.stop()
                pygame.mixer.music.load(r"Audio\GameTheme.mp3")
                pygame.mixer.music.play(loops=-1)
                gameHasStarted = True

                ground = Platform(Vector2(screen.get_width() / 2, (screen.get_height() / 12) * 11), Vector2(screen.get_width() * 100, screen.get_height() / 6))
                list_of_platforms.append(ground)

                for i in range(100):
                    newPlatform = Platform(Vector2(random.randint(screen.get_width() * -50, screen.get_width() * 50),(screen.get_height() / 12) * 10), Vector2(screen.get_width(), screen.get_height() / 6))
                    list_of_platforms.append(newPlatform)

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                if gameHasStarted and hasRuler:

                    hasRuler = False

                    if score * 2 > 80:
                        subtractionValue = 80
                    else:
                        subtractionValue = score * 2

                    rulerCooldown = 120 - subtractionValue

                    ruler_image = pygame.image.load(r"Images\SedonRuler.png").convert_alpha()
                    sedon_image = pygame.image.load(r"Images\MrSedon.png").convert_alpha()
                    ruler_rotated = pygame.transform.rotate(ruler_image, ruler_angle * 180 / math.pi)
                    ruler_box = ruler_rotated.get_rect(center=(sedon.get_position()[0] + sedon_image.get_width() / 2,sedon.get_position()[1] + sedon_image.get_height() / 1.5))

                    newRuler = Ruler(ruler_angle, Vector2(ruler_box.center[0], ruler_box.center[1]))
                    list_of_rulers.append(newRuler)

            if event.key == pygame.K_ESCAPE:
                running = False
                pygame.quit()

    update_frame(gameHasStarted)

    pygame.display.flip()

    if gameHasStarted and rulerCooldown > 0:
        rulerCooldown -= 1
    if gameHasStarted and rulerCooldown <= 0:
        hasRuler = True

    clock.tick(60)

pygame.quit()