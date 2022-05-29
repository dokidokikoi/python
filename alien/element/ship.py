import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	"""一个飞船类,方便创建飞船编组"""
	def __init__(self, ai_game):
		'''初始化飞船并设置其初始位置'''
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()
		self.moving_right = False
		self.moving_left = False
		self.settings = ai_game.settings

			# 加载飞船图像并获取外接矩形
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()

		# 将每艘新飞船放在屏幕底部中央
		self.rect.midbottom = self.screen_rect.midbottom

		# 飞船属性 x 存储浮点数
		self.x = float(self.rect.x)
	
	def blitme(self):
		"""在指定位置绘制飞船"""
		self.screen.blit(self.image, self.rect)

	def update(self):
		"""根据移动调整飞船的位置"""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed
		if self.moving_left  and self.rect.left > 0: 
			self.x -= self.settings.ship_speed
		self.rect.centerx = self.x