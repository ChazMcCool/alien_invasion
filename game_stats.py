import json
from scoreboard import Scoreboard

class GameStats:
	"""Track statistics for Alien Invasion."""

	def __init__(self, ai_game):
		"""Initialize statistics."""
		self.settings = ai_game.settings
		self.reset_stats()

		# Start Alien Invasion in an inactive state.
		self.game_active = False

		# High score should never be reset
		filename = 'high_score.json'

		try:
			with open('high_score.json') as f:
				self.high_score = json.load(f)
		except FileNotFoundError:
			with open(filename, 'w') as f:
				f.write('0')
				self.high_score = 0

	def reset_stats(self):
		"""Initialize statistics that can change the game."""
		self.ships_left = self.settings.ship_limit
		self.score = 0
		self.level = 1

	def get_high_score(self):
		"""Get all time high score."""
		if self.high_score > 0:
			with open('high_score.json') as f:
				self.high_score = json.load(f)