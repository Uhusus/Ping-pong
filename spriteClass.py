from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, width, heigth, speed):
        self.image = transform.scale(image.load(player_image), (width, heigth))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = speed
        self.direction_x = 1  # Horizontal direction: 1 = right, -1 = left
        self.direction_y = 1  # Vertical direction: 1 = down, -1 = up

    def reset(self, window):
        window.blit(self.image, self.rect)

    def move(self, win_width, win_height, paddle_left, paddle_right):
        # Move the ball
        self.rect.x += self.speed * self.direction_x
        self.rect.y += self.speed * self.direction_y

        # Collisions with top/bottom
        if self.rect.top <= 0 or self.rect.bottom >= win_height:
            self.direction_y *= -1

        # Collisions with paddles
        if self.rect.colliderect(paddle_left.rect):
            self.direction_x *= -1
            self.rect.left = paddle_left.rect.right  # Move ball away from paddle
        if self.rect.colliderect(paddle_right.rect):
            self.direction_x *= -1
            self.rect.right = paddle_right.rect.left  # Move ball away from paddle

        # Reset if ball goes out of bounds (left or right)
        if self.rect.left <= 0 or self.rect.right >= win_width:
            self.rect.x, self.rect.y = win_width // 2, win_height // 2
            self.direction_x *= -1  # Reverse direction after reset

class Player(GameSprite):
    
    def update_p_left(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 495:
            self.rect.y += self.speed

    def update_p_right(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 495:
            self.rect.y += self.speed
