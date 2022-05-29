
class GameStats():
	"""跟踪游戏的统计信息"""
	def __init__(self, ai_game):
		self.setting = ai_game.settings

		# 游戏状态
		self.game_active = True
		
		self.reset_stats()
	
	def reset_stats(self):
		'''初始化在游戏运行期间可能变化的统计信息'''
		self.ships_left = self.setting.ship_limt