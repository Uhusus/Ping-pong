from pygame import *
from spriteClass import *

bg_color = (200, 255, 255)
win_width = 600
win_height = 500

score_left = 0
score_right = 0

window = display.set_mode((win_width, win_height))
display.set_caption("Ping Pong Game")
window.fill(bg_color)

clock = time.Clock()

# Objects
ball = GameSprite(player_image='./img/Ball.png',
                   player_x=275, player_y=225, 
                   width=50, heigth=50, speed=4)  # Ball's speed

paddle_left = Player(player_image='./img/Paddle.png',
                     player_x=10, player_y=200, 
                     width=50, heigth=150, speed=4)

paddle_right = Player(player_image='./img/Paddle.png',
                      player_x=540, player_y=200, 
                      width=50, heigth=150, speed=4)
if ball.rect.x <= 0 or ball.rect.x >= win_width:
    # Update the score based on the ball's position
    if ball.rect.x <= 0:  # Right player scores
        score_right += 1
    else:  # Left player scores
        score_left += 1
    
    # Reset the ball position to the center
    ball.rect.x, ball.rect.y = win_width // 2, win_height // 2

    # Reverse the horizontal direction
    ball.direction_x *= -1

# Game Loop
running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False

    # Move the ball and handle collisions
    ball.move(win_width, win_height, paddle_left, paddle_right)


    paddle_left.update_p_left()
    paddle_right.update_p_right()

    window.fill(bg_color)
    ball.reset(window)
    paddle_left.reset(window)
    paddle_right.reset(window)

    display.update()
    clock.tick(60)

