import unittest
from unittest.mock import patch, call, Mock

from MorseCodePy.main import play


class TestAudioPlay(unittest.TestCase):
	@patch('MorseCodePy.audio_manager.AudioManager.play_dot')
	def test_dot_only(self, mock_play_dot: Mock):
		play('.')
		mock_play_dot.assert_called_once()

	@patch('MorseCodePy.audio_manager.AudioManager.play_dash')
	def test_dash_only(self, mock_play_dash: Mock):
		play('-')
		mock_play_dash.assert_called_once()

	@patch('MorseCodePy.audio_manager.AudioManager.play_error')
	def test_error_only(self, mock_play_error: Mock):
		play('^')
		mock_play_error.assert_called_once()

	@patch('MorseCodePy.audio_manager.AudioManager.play_dot')
	@patch('MorseCodePy.audio_manager.AudioManager.play_dash')
	def test_combination(self, mock_play_dash, mock_play_dot):
		play('.-')
		mock_play_dot.assert_called_once()
		mock_play_dash.assert_called_once()

	@patch('MorseCodePy.audio_manager.AudioManager.play_dot')
	@patch('MorseCodePy.audio_manager.AudioManager.play_dash')
	@patch('MorseCodePy.audio_manager.AudioManager.play_error')
	def test_complex_combination(self, mock_play_dot: Mock, mock_play_dash: Mock, mock_play_error: Mock):
		play('. -- / ^')
		mock_play_dot.assert_called_once()
		mock_play_dash.assert_has_calls([call(), call()])
		mock_play_error.assert_called_once()

	@patch('MorseCodePy.audio_manager.AudioManager.play_dash')
	@patch('MorseCodePy.audio_manager.AudioManager.play_dot')
	def test_multiple_symbols(self, mock_play_dot: Mock, mock_play_dash: Mock):
		play('.- -... / -.-. .- .. .-.-.-')
		mock_play_dot.assert_has_calls([call(), call()])
		mock_play_dash.assert_has_calls([call(), call()])


if __name__ == '__main__':
	unittest.main()
