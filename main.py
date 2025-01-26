from pygame import *
from spriteClass import *

# Colors
bg_color = (0, 0, 0)
text_color = (255, 255, 255)
win_score = 5

# Window settings
win_width = 600
win_height = 500

# Scores
score_left = 0
score_right = 0


font.init()

window = display.set_mode((win_width, win_height))
display.set_caption("Ping Pong Game")
window.fill(bg_color)

# Clock
clock = time.Clock()

# Font for displaying scores
font_score = font.Font(None, 36)

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

# Ball direction
ball.direction_x = 1  # 1 for moving right, -1 for moving left
ball.direction_y = 1  # 1 for moving down, -1 for moving up

# Game Loop
running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False

    # Move the ball
    ball.rect.x += ball.speed * ball.direction_x
    ball.rect.y += ball.speed * ball.direction_y

    # Bounce the ball off the top and bottom
    if ball.rect.y <= 0 or ball.rect.y + ball.rect.height >= win_height:
        ball.direction_y *= -1

    # Bounce the ball off the paddles and increase speed
    if ball.rect.colliderect(paddle_left.rect):
        ball.direction_x = 1
        ball.rect.x = paddle_left.rect.right + 1
        ball.speed = ball.speed + 0.1  # Increase speed 

    if ball.rect.colliderect(paddle_right.rect):
        ball.direction_x = -1
        ball.rect.x = paddle_right.rect.left - ball.rect.width - 1
        ball.speed = ball.speed + 0.1  # Increase speed

    # Check if the ball goes out of bounds
    if ball.rect.x <= 0:  # Right player scores
        score_right += 1
        ball.rect.x, ball.rect.y = win_width // 2, win_height // 2
        ball.direction_x = 1  # Reset direction to right
        ball.speed = 4  # Reset speed after a point

    elif ball.rect.x >= win_width:  # Left player scores
        score_left += 1
        ball.rect.x, ball.rect.y = win_width // 2, win_height // 2
        ball.direction_x = -1  # Reset direction to left
        ball.speed = 4  # Reset speed after a point

    # Check for a winner
    if score_left == win_score:
        winner_text = font_score.render("Left Player Wins!", True, text_color)
        window.blit(winner_text, (win_width // 2 - winner_text.get_width() // 2, win_height // 2))
        display.update()
        time.delay(3000)  # Pause for 3 seconds to show the message
        running = False  # Exit the game loop

    elif score_right == win_score:
        winner_text = font_score.render("Right Player Wins!", True, text_color)
        window.blit(winner_text, (win_width // 2 - winner_text.get_width() // 2, win_height // 2))
        display.update()
        time.delay(3000)  # Pause for 3 seconds to show the message
        running = False  # Exit the game loop

    # Update paddles
    paddle_left.update_p_left()
    paddle_right.update_p_right()

    # Render the game
    window.fill(bg_color)
    ball.reset(window)
    paddle_left.reset(window)
    paddle_right.reset(window)

    # Display scores
    score_text = font_score.render(f"{score_left} - {score_right}", True, text_color)
    window.blit(score_text, (win_width // 2 - score_text.get_width() // 2, 20))


    display.update()
    clock.tick(60)


quit()