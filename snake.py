x = 2050
y = 250
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

import pygame
import random

def displayScore(score):
    global value
    value = font1.render("Score: " + str(score), True, (0, 255, 0))
    win.blit(value, (5, 1))

def drawSnake(snakeList, size):
    for XnY in snakeList:
        pygame.draw.rect(win, (255, 255, 255), (XnY[0], XnY[1], size, size))


def gameOver():
    run = True
    while run:
        pygame.time.delay(50)
        pygame.time.Clock().tick(vel)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if pos[0] >= ((width - buttonText.get_width()) // 2) - 10 and pos[0] <= ((width - buttonText.get_width()) // 2) - 10 + (buttonText.get_width() + 20):
                    if pos[1] >= (height // 1.5) - 10 and pos[1] <= (height // 1.5) - 10 + buttonText.get_height() + 20:
                        run = False

        win.fill((10, 20, 44))

        if snakeLength < 840:
            gameOverText = font2.render("Game Over", True, (255, 255, 255))
        else:
            gameOverText = font2.render("CONGRATULATIONS!!", True, (255, 0, 0))
        buttonText = font1.render("Play Again?", True, (255, 0, 255))

        win.blit(gameOverText, ((width - gameOverText.get_width()) // 2, height // 3))
        win.blit(value, ((width - value.get_width()) // 2, height // 2))

        pos = pygame.mouse.get_pos()
        if pos[0] >= ((width - buttonText.get_width()) // 2) - 10 and pos[0] <= ((width - buttonText.get_width()) // 2) - 10 + (buttonText.get_width() + 20):
            if pos[1] >= (height // 1.5) - 10 and pos[1] <= (height // 1.5) - 10 + buttonText.get_height() + 20:
                buttonText = font1.render("Play Again?", True, (255, 255, 255))
                print ("hover")
            else:
                buttonText = font1.render("Play Again?", True, (255, 0, 255))
        win.blit(buttonText, ((width - buttonText.get_width()) // 2, height // 1.5))
        '''pygame.draw.rect(win, (10, 50, 44), (((width - buttonText.get_width()) // 2) - 10, (height // 1.5) - 10, buttonText.get_width() + 20, buttonText.get_height() + 20))'''

        pygame.display.update()


def loop():
    x = 40
    y = 40
    size = 20
    global vel, snakeLength
    vel = 20
    snakeLength = 1
    snakeList = []
    foodX = random.randrange(0, width, size)
    foodY = random.randrange(40, height, size)

    direction = None
    lastKey = None
    run = True
    while run:
        pygame.time.delay(50)
        pygame.time.Clock().tick(vel)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                lastKey = event.key

        if lastKey == pygame.K_LEFT:
            if direction != "right":
                x -= vel
                x %= width
                direction = "left"
            else:
                x += vel
                x %= width
                direction = "right"
        if lastKey == pygame.K_RIGHT:
            if direction != "left":
                x += vel
                x %= width
                direction = "right"
            else:
                x -= vel
                x %= width
                direction = "left"
        if lastKey == pygame.K_UP:
            if direction != "down":
                y -= vel
                direction = "up"
            else:
                y += vel
                direction = "down"
        if lastKey == pygame.K_DOWN:
            if direction != "up":
                y += vel
                direction = "down"
            else:
                y -= vel
                direction = "up"

        if y < 40:
            y += height - 40
        if y > height:
            y -= height - 40

        if x == foodX and y == foodY:
            snakeLength += 1
            foodX = random.randrange(0, width, size)
            foodY = random.randrange(40, height, size)
            print(snakeLength)

        snakeHead = []
        snakeHead.append(x)
        snakeHead.append(y)
        snakeList.append(snakeHead)
        if len(snakeList) > snakeLength:
            del snakeList[:1]
        print(snakeList)

        for XnY in snakeList:
            if XnY[0] == foodX and XnY[1] == foodY:
                foodX = random.randrange(0, width, size)
                foodY = random.randrange(40, height, size)

        for XnY in snakeList[:-1]:
            if XnY == snakeHead:
                x = 40
                y = 40
                snakeLength = 1
                snakeList = []
                snakeHead = []
                lastKey = None
                gameOver()

        win.fill((0, 0, 0))
        pygame.draw.line(win, (255, 255, 255), (0, 39), (600, 39))
        drawSnake(snakeList, size)
        displayScore((snakeLength-1)*10)
        pygame.draw.rect(win, (255, 0, 0), (foodX, foodY, size, size))
        pygame.display.update()

    pygame.quit()


def main():
    global win, width, height
    width = 600
    height = 600
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Snake")

    loop()


pygame.init()

font1 = pygame.font.SysFont("comicsansms", 28)
font2 = pygame.font.SysFont("comicsansms", 72)

main()