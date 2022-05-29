import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""一个外星人类"""
	def __init__(self, ai_game):
		"""初始化外星人设置初始位置"""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings

		# 加载外星人图像并获取外接矩形
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()

		# 每个新外星人最初在左上角
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# 存储外星人的准确位置
		self.x = float(self.rect.x)
	
	def update(self):
		"""向左右移动外星人"""
		self.x += (self.settings.alien_speed * self.settings.fleet_direction)
		self.rect.x = self.x 

	def blitme(self):
		"""在指定位置绘制外星人"""
		self.screen.blit(self.image, self.rect)

	def check_edges(self):
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right or self.rect.left < 0:
			return True












