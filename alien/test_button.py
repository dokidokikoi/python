from button import Button
from alien_invasion import AlienInvasion
import unittest
import time

class TestButton(unittest.TestCase):
    def draw_button(self):
        game = AlienInvasion()
        button = Button(game)
        game._update_screen()
        time.sleep(10)