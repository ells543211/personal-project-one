#when it hits food game over
#reference: 
#my python teacher assisted me(with starter code and questions) while i worked on this project 
import pygame
from snake import *
from food import Food


pygame.init()
bounds = (300,300)
window = pygame.display.set_mode(bounds)
pygame.display.set_caption("Snake")

block_size = 20
snake = Snake(block_size, bounds)
food = Food(block_size,bounds)
font = pygame.font.SysFont('ariel',50, True)

run = True
while run:
  pygame.time.delay(120)
  #increase by one

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  keys = pygame.key.get_pressed()
  if keys[pygame.K_LEFT]:
    snake.steer(Direction.LEFT)
  elif keys[pygame.K_RIGHT]:
    snake.steer(Direction.RIGHT)
  elif keys[pygame.K_UP]:
    snake.steer(Direction.UP)
  elif keys[pygame.K_DOWN]:
    snake.steer(Direction.DOWN)
    
  snake.move()
  snake.check_for_food(food)

  if snake.check_bounds() == True or snake.check_tail_collision() ==True:
    text = font.render('Game Over', True, (255,25,25))
    window.blit(text, (50,120))
    pygame.display.update()
    pygame.time.delay(900)
    snake.respawn()
    food.respawn()

  window.fill((255,255,255))
  snake.draw(pygame, window)
  food.draw(pygame, window)
  pygame.display.update()