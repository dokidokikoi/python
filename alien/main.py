from turtle import bgcolor
import pygame
import sys
from active.settings import Settings
from element.ship import Ship
from element.bullet import Bullet
from element.alien import Alien

class Main():
  def __init__(self):
    pygame.init()

    self.settings = Settings()

    self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    self.ship = Ship(self)
    self.bullets = pygame.sprite.Group()

  def run_game(self):
    while True:
      # 监视键盘和鼠标事件
      self._check_events()

      # 飞船左右移动
      self.ship.update()

      # 子弹
      self.bullets.update()

      # 让最近绘制的屏幕可见
      self._update_screen()

      # 回收资源
      self.release()
  
  def _check_events(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
      elif event.type == pygame.KEYDOWN:
        self._check_keydown_events(event)
      elif event.type == pygame.KEYUP:
        self._check_keyup_events(event)

  def _check_keydown_events(self, event):
    if event.key == pygame.K_RIGHT:
      self.ship.moving_right = True
    elif event.key == pygame.K_LEFT:
      self.ship.moving_left = True
    elif event.key == pygame.K_q:
      sys.exit() 
    elif event.key == pygame.K_SPACE:
      self._fir_bullet()

  def _check_keyup_events(self, event):
    if event.key == pygame.K_RIGHT:
      self.ship.moving_right = False
    elif event.key == pygame.K_LEFT:
      self.ship.moving_left = False

  def _fir_bullet(self):
    if self.settings.bullet_allowed > len(self.bullets):
      new_bullet = Bullet(self)
      self.bullets.add(new_bullet)
  
  def _update_screen(self):
    self.screen.fill(self.settings.bg_color)
    self.ship.blitme()
    for bullet in self.bullets.sprites():
      bullet.draw_bullet()
    pygame.display.flip()

  def release(self):
    # 删除消失的子弹
    for bullet in self.bullets.sprites():
      if bullet.rect.bottom <= 0:
        self.bullets.remove(bullet)
    print(len(self.bullets))

if __name__ == "__main__":
  game = Main()
  game.run_game()