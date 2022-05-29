
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""一个外星人类"""
	def __init__(self, ai_game):
		"""初始化外星人设置初始位置"""
		super().__init__()
		self.screen = ai_game.screen # 加self的可以供类中所有方法使用
		self.ai_game = ai_game

		# 加载外星人图像并获取外接矩形
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()

		# 每个新外星人最初在左上角
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		# 存储外星人的准确位置
		self.x = float(self.rect.x)











