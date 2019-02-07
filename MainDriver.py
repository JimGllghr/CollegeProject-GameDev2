""" MainDriver.py
    James gallagher
"""

import pygame, math
from crate import Crate
from PlayerTank import PlayerTank
from shell import Shell
from FShell import fShell
from Scoreboard import Keeper
from explosion import Explosion
from EnemyTurretA import enemyTurretA
from EnemyTankA import enemyTankA
from mine import Mine
from enemyTankB import EnemyTank2
from health import Health
from EnemyTurretD import enemyTurretD
from EnemyTankD import enemyTankD
from PlayerTankTurret import playerTurret

pygame.init()
#pygame.mixer.init()

screen = pygame.display.set_mode((960, 640))

def game():

    background = "background.jpg"
    background = pygame.image.load(background).convert()

    screen.blit(background, (0, 0))

    """Create all Groups"""
    allSprites = pygame.sprite.OrderedUpdates()
    enemyGroup = pygame.sprite.Group()

    playerTank = PlayerTank(screen, (320, 480), allSprites, enemyGroup)
    PlayerTurret = playerTurret(screen, playerTank, allSprites, enemyGroup)
    scoreboard = Keeper()

    crate = Crate(screen, (200, 200), playerTank, scoreboard)
    enemyTankC = EnemyTank2(screen, (600, 900), crate, scoreboard)

    """Enemy Sprites"""
    EnemyTankA = enemyTankA(screen, (200, 200), playerTank, scoreboard)
    EnemyTurretA = enemyTurretA( screen, playerTank, EnemyTankA, scoreboard, allSprites)

    EnemyTankB = enemyTankA(screen, (560, 880), enemyTankC, scoreboard)
    EnemyTurretB = enemyTurretA( screen, playerTank, EnemyTankB, scoreboard, allSprites)

    EnemyTankD = enemyTankD(screen, (560, 880), playerTank, scoreboard)
    EnemyTurretD = enemyTurretD( screen, playerTank, EnemyTankD, scoreboard, allSprites)

    enemyGroup.add(EnemyTankA)
    #enemyGroup.add(EnemyTurretA)
    enemyGroup.add(EnemyTankB)
    #enemyGroup.add(EnemyTurretB)
    enemyGroup.add(enemyTankC)
    #enemyGroup.add(EnemyTurretD)
    enemyGroup.add(EnemyTankD)

    health = Health(screen, scoreboard, playerTank)

    """adds sprites to there groups"""
    allSprites.add(crate)
    allSprites.add(scoreboard)
    allSprites.add(health)

    allSprites.add(playerTank)
    allSprites.add(PlayerTurret)

    allSprites.add(EnemyTankA)
    allSprites.add(EnemyTurretA)
    allSprites.add(EnemyTankB)
    allSprites.add(EnemyTurretB)
    allSprites.add(enemyTankC)

    allSprites.add(EnemyTankD)
    allSprites.add(EnemyTurretD)

    clock = pygame.time.Clock()
    keepGoing = True
    while (keepGoing == True):
        clock.tick(30)

        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                donePlaying = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    if PlayerTurret.playerShellPower>=60:
                        FShell = fShell((PlayerTurret.x, PlayerTurret.y), PlayerTurret.dir, enemyGroup)
                        PlayerTurret.allSprites.add(FShell)
                        PlayerTurret.playerShellPower = 0
        PlayerTurret.playerShellPower+=1

        """update clear and draw all sprites"""
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)

        pygame.display.flip()
        pygame.display.update()
        if scoreboard.health <=0:
            keepGoing = False

    score = scoreboard.score

def instructions(score):
    pygame.display.set_caption("Tanks")
    background = "background.jpg"
    background = pygame.image.load(background).convert()
    screen.blit(background, (0, 0))
    insFont = pygame.font.SysFont(None, 50)
    insLabels = []
    instructions = (
    "",
    "Use up/down/left/right to move",
    "Move mouse to aim",
    "Left click to shoot",
    "Press Enter to continue...",
    "Collect The crate before the enemy does.",
    "Watch out for other tanks trying to kill you!"
    )

    for line in instructions:
        tempLabel = insFont.render(line, 1, (255, 255, 255))
        insLabels.append(tempLabel)

    keepGoing = True
    clock = pygame.time.Clock()
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                donePlaying = True
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                keepGoing = False
                donePlaying = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    keepGoing = False
                    donePlaying = True

        for i in range(len(insLabels)):
            screen.blit(insLabels[i], (50, 30*i))
        pygame.display.flip()

    pygame.mouse.set_visible(True)
    return donePlaying

def main():
    score = 0
    donePlaying = False
    while not donePlaying:
        donePlaying = instructions(score)
        if not donePlaying:
            score = game()


if __name__ == "__main__":
    main()
