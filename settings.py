from random import randint

class Settings:
	"""A class to store all settings for Alien Invasion."""

	def __init__(self):
		"""Initialize the game's  static settings."""
		# Screen settings
		self.full_screen = 'Y'
		self.screen_width = 1200
		self.screen_height = 800
		
		# Background colors
		self.bg_color1 = (215, 10, 115)
		self.bg_color2 = (152, 98, 15)
		self.bg_color3 = (155, 65, 0)
		self.bg_color4 = (53, 152, 27)
		self.bg_color5 = (17, 50, 240)
		self.bg_color6 = (100, 200, 70)
		self.bg_color7 = (99, 230, 19)

		# Ship settings
		self.ship_limit = 3

		# Bullet settings
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (255, 0, 0)
		self.bullets_allowed = 3

		# Alien settings
		self.fleet_drop_speed = 10

		# How quickly the game speeds up.
		self.speedup_scale = 1.1

		# How quickly the alien point values increase.
		self.score_scale = 1.5

		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		"""Initialize settings that change throughout the game."""
		self.ship_speed = 2.5
		self.bullet_speed = 3.0
		self.alien_speed = 1.0

		# fleet_direction of 1 represents right; -1 represents left.
		self.fleet_direction = 1

		# Scoring
		self.alien_points = 50

	def increase_speed(self):
		"""increase speed settings and alien point value."""
		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.alien_speed *= self.speedup_scale

		self.alien_points = int(self.alien_points * self.score_scale)

	def select_bg_color(self):
		"""Generate a random background color."""
		# Background color selection
		self.bg_color_select = randint(1, 7)
		if self.bg_color_select == 1:
			self.bg_color = self.bg_color1
		elif self.bg_color_select == 2:
			self.bg_color = self.bg_color2
		elif self.bg_color_select == 3:
			self.bg_color = self.bg_color3
		elif self.bg_color_select == 4:
			self.bg_color = self.bg_color4
		elif self.bg_color_select == 5:
			self.bg_color = self.bg_color5
		elif self.bg_color_select == 6:
			self.bg_color = self.bg_color6
		elif self.bg_color_select == 7:
			self.bg_color = self.bg_color7