import unittest
from unittest.mock import patch, Mock

from MorseCodePy.play_pygame import play_pygame


class TestAudioPlay(unittest.TestCase):
	@patch('MorseCodePy.play_pygame.AudioManagerPygame.play_dot')
	def test_dot(self, mock_play_dot: Mock):
		play_pygame('.')
		mock_play_dot.assert_called_once()

	@patch('MorseCodePy.play_pygame.AudioManagerPygame.play_dash')
	def test_dash(self, mock_play_dash: Mock):
		play_pygame('-')
		mock_play_dash.assert_called_once()

	@patch('MorseCodePy.play_pygame.AudioManagerPygame.play_error')
	def test_error(self, mock_play_error: Mock):
		play_pygame('^')
		mock_play_error.assert_called_once()


if __name__ == '__main__':
	unittest.main()
