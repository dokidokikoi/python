import imp
from turtle import Screen
from matplotlib.style import available
from time import sleep
import pygame
import sys

from active.settings import Settings
from element.ship import Ship
from element.bullet import Bullet
from element.alien import Alien
from active.game_stats import GameStats

class Main():
  def __init__(self):
    pygame.init()

    self.settings = Settings()

    self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    self.ship = Ship(self)
    self.bullets = pygame.sprite.Group()

    self.aliens = pygame.sprite.Group()
    self._create_fleet()

    self.stats = GameStats(self)

  def _create_fleet(self):
    '''创建外星人群'''
    alien = Alien(self)
    alien_width, alien_height = alien.rect.size
    available_space_x = self.settings.screen_width - (2 * alien_width)
    number_aliens_x = available_space_x // (2 * alien_width)

    # 计算屏幕螚容纳多少行外星人
    ship_height = self.ship.rect.height
    available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = available_space_y // (2 * alien_height)
    
    # 创建外星人群
    for row_number in range(number_rows):
      for alien_number in range(number_aliens_x):
        alien = Alien(self)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien_height * row_number
        self.aliens.add(alien)


  def run_game(self):
    while True:
      # 监视键盘和鼠标事件
      self._check_events()

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
    print(self.stats.game_active)
    if self.stats.game_active:
      # 飞船左右移动
      self.ship.update()

      # 子弹
      self._update_bullte()

      # 外星人
      self._update_alien()

    self.screen.fill(self.settings.bg_color)
    self.ship.blitme()
    for alien in self.aliens.sprites():
      alien.blitme()
    for bullet in self.bullets.sprites():
      bullet.draw_bullet()
    pygame.display.flip()

  def _update_bullte(self):
    self.bullets.update()

    self._check_bullet_alien_collision()
    
  def _check_bullet_alien_collision(self):
    # 检查是否有子弹击中敌人
    # 如果击中，删除子弹和外星人
    collssion = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

    if not self.aliens:
      # 删除屏幕的子弹并新建一群外星人
      self.bullets.empty()
      self._create_fleet()

  def _update_alien(self):
    self._check_fleet_edges()
    self.aliens.update()

    # 检查外星人与飞船的碰撞
    if pygame.sprite.spritecollideany(self.ship, self.aliens):
      self._ship_hit()
    
    # 检查是否有外星人到达屏幕底端
    self._check_aliens_bottom()
  
  def _ship_hit(self):
    '''响应飞船被外星人撞击'''
    if self.stats.ships_left > 0:
      # 飞船数减一
      self.stats.ships_left -= 1

      # 清空屏幕子弹和外星人
      self.aliens.empty()
      self.bullets.empty()

      # 创建新外星人，飞船回到底端中心
      self._create_fleet()
      self.ship.center_ship()

      # 暂停
      sleep(0.5)
    else:
      self.stats.game_active = False
    

  def _check_aliens_bottom(self):
    '''检查是否有外星人到达屏幕底端'''
    screen_rect = self.screen.get_rect()
    for alien in self.aliens.sprites():
      if alien.rect.bottom >= screen_rect.bottom:
        self._ship_hit()
        break

  def _check_fleet_edges(self):
    for alien in self.aliens.sprites():
      if alien.check_edges():
        self._change_fleet_direction()
        break

  def _change_fleet_direction(self):
    '''外星人群整体下降'''
    for alien in self.aliens.sprites():
      alien.rect.y += self.settings.fleet_drop_speed
    self.settings.fleet_direction *= -1

  def release(self):
    # 删除消失的子弹
    for bullet in self.bullets.sprites():
      if bullet.rect.bottom <= 0:
        self.bullets.remove(bullet)
    # print(len(self.bullets))

    # 删除消失的外星人
    # for alien in self.aliens.sprites():
    #   if alien.rect.bottom >= self.screen.get_rect().height:
    #     self.aliens.remove(alien)
    # print(len(self.aliens))

if __name__ == "__main__":
  game = Main()
  game.run_game()