import unittest
from unittest.mock import patch, Mock

from MorseCodePy.play_sounddevice import play_sounddevice


class TestAudioPlay(unittest.TestCase):
	@patch('MorseCodePy.play_sounddevice.AudioManagerSounddevice.play_dot')
	def test_dot(self, mock_play_dot: Mock):
		play_sounddevice('.')
		mock_play_dot.assert_called_once()

	@patch('MorseCodePy.play_sounddevice.AudioManagerSounddevice.play_dash')
	def test_dash(self, mock_play_dash: Mock):
		play_sounddevice('-')
		mock_play_dash.assert_called_once()

	@patch('MorseCodePy.play_sounddevice.AudioManagerSounddevice.play_error')
	def test_error(self, mock_play_error: Mock):
		play_sounddevice('^')
		mock_play_error.assert_called_once()


if __name__ == '__main__':
	unittest.main()
