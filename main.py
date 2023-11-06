"""
Pong

Description:
"""
import pygame

pygame.init()
import random
import pygame.freetype

# Create the variables
# Gameloop variable
running = True

# Score variables
pscore = 0
oscore = 0
winner = 0
tx = 100
ty = 10
wx = 156
wy = 240
lx = 156
ly = 240

# Scene variables
bg = (0, 0, 0)

# Color Variables
color = (200, 200, 200)
# get the clock
clock = pygame.time.Clock()

# Variables for the window
(width, height) = (500, 500)

# Create the window
w = pygame.display.set_mode((width, height))
# bgm = pygame.mixer.Sound("electronic_calm.mp3")
# collision = pygame.mixer.Sound("kick.mp3")
# explosion = pygame.mixer.Sound("explosion.mp3")
# Create the components
ball = pygame.Rect(243, 250, 15, 15)
bxs = 7
bys = 7
player = pygame.Rect(475, 230, 10, 75)
py_change = 0
opponent = pygame.Rect(25, 230, 10, 75)
oy_change = 4

who = random.randint(1, 2)


def component_move():
    player.y += py_change
    if who == 1:
        ball.y -= bys
        ball.x -= bxs
    if who == 2:
        ball.y += bys
        ball.x += bxs


def player_border():
    if player.y > 430:
        player.y = 430
    if player.y <= 0:
        player.y = 0


def opponent_border():
    if opponent.y > 430:
        opponent.y = 430
    if opponent.y <= 0:
        opponent.y = 0


def ball_restart():
    global bxs
    global bys
    global ball
    global player
    global opponent
    player.x = 475
    player.y = 230
    opponent.x = 25
    opponent.y = 230
    ball.x = 243
    ball.y = 250
    pygame.time.wait(500)
    global who
    who = random.randint(1, 2)
    if who == 1:
        ball.y -= bys
        ball.x -= bxs
    if who == 2:
        ball.y += bys
        ball.x += bxs


def show_score(x, y):
    global pscore
    global oscore
    global score_value
    score_value = pygame.freetype.Font("GermaniaOne-Regular.ttf", 24)
    score_value.fgcolor = (255, 0, 255)
    score_value.render_to(w, (x, y), "Opponent: " + str(oscore) + "                  You: " + str(pscore))


def ifwinner(x, y):
    win = pygame.freetype.Font("GermaniaOne-Regular.ttf", 64)
    win.fgcolor = (255, 0, 255)
    win.render_to(w, (x, y), "You won")


def ifloser(x, y):
    lose = pygame.freetype.Font("GermaniaOne-Regular.ttf", 64)
    lose.fgcolor = (255, 0, 255)
    lose.render_to(w, (x, y), "You Lost")


run = True
# if run == True:
#     bgm.play()
#     bgm.set_volume(.1)

# Game loop
while run:
    w.fill(bg)
    show_score(tx, ty)

    # Close it whenever you want
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                py_change = -10
            if event.key == pygame.K_DOWN:
                py_change = 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                py_change = 0

    # Move the player and the ball
    component_move()

    # Border player
    player_border()
    opponent_border()

    # Border the ball
    if ball.top <= 0 or ball.bottom >= height:
        bys *= -1
    if ball.left <= 0:
        ball_restart()
        py_change += 1
        oy_change += 1
        pscore += 1
        bxs += 1
        bys += 1


    if ball.right >= width:
        ball_restart()
        oy_change += 1
        oscore += 1


    # Speed limit
    if py_change > 13:
        py_change = 13
    if oy_change > 13:
        oy_change = 13

    # Detect collision
    if ball.colliderect(player) or ball.colliderect(opponent):
        bxs *= -1

    # Ai
    if opponent.y < ball.y:
        opponent.y += oy_change
    if opponent.y > ball.y:
        opponent.y -= oy_change

    # Draw the components
    pygame.draw.line(w, color, (250, 0), (250, 500), 1)
    pygame.draw.rect(w, color, player)
    pygame.draw.rect(w, color, opponent)
    pygame.draw.ellipse(w, color, ball)

    # Check is someone won
    if oscore == 10:
        winner = "opponent"
        w.fill((0, 0, 0))
        ifloser(lx, ly)
        running = False
    if pscore == 5:
        winner = "player"
        w.fill((0, 0, 0))
        ifwinner(wx, wy)
        running = False

    # Flip the display
    pygame.display.flip()
    clock.tick(244)
