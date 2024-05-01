# Hide the pygame support prompt
from os import environ

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import logging
from time import sleep

import pygame

from MorseCodePy.utilities import *


class AudioManagerPygame:
	def __init__(self, volume: float, *, directory: Optional[PathLikeString] = 'sounds',
	             dot_sound_file: Optional[PathLikeString] = 'dot.wav',
	             dash_sound_file: Optional[PathLikeString] = 'dash.wav',
	             error_sound_file: Optional[PathLikeString] = 'error.wav') -> None:
		"""
		Initializes the AudioManager with the specified volume and sound files.

		:parameter volume: The volume of the Morse code playback, a float between 0.0 and 1.0.
		:parameter directory: The directory containing the sound files (default is 'sounds').
		:parameter dot_sound_file: The filename of the sound file for dots (default is 'dot.wav').
		:parameter dash_sound_file: The filename of the sound file for dashes (default is 'dash.wav').
		:parameter error_sound_file: The filename of the sound file for error messages (default is 'error.wav').
		"""

		self._volume = volume
		self._directory = directory
		self._dot_sound_file = dot_sound_file
		self._dash_sound_file = dash_sound_file
		self._error_sound_file = error_sound_file

		self._audio_cache = {}

		# Initialize the pygame mixer
		pygame.init()
		pygame.mixer.init()

	def _load_sound(self, filename: PathLikeString) -> None:
		if not path.exists(sound_path := path.join(path.dirname(__file__), self._directory, filename)):
			raise FileNotFoundError(f'Sound file {filename} not found!')

		pygame.mixer.music.load(sound_path)
		pygame.mixer.pre_init(44100, -16, 2, 2048)
		pygame.mixer.music.set_volume(self._volume)

	def _load_all_sounds(self) -> None:
		for filename in (self._dot_sound_file, self._dash_sound_file, self._error_sound_file):
			self._load_sound(filename)
			self._audio_cache[filename] = mixer.Sound()  # NOQA

	def play_dot(self) -> None:
		self._load_sound(self._dot_sound_file)
		pygame.mixer.music.play()

	def play_dash(self) -> None:
		self._load_sound(self._dash_sound_file)
		pygame.mixer.music.play()

	def play_error(self) -> None:
		self._load_sound(self._error_sound_file)
		pygame.mixer.music.play()


def play_pygame(code: str, /, delay: float = 0.5, volume: float = 0.5, *, dot: Optional[str] = '.',
                dash: Optional[str] = '-', separator: Optional[str] = '/') -> None:
	"""
	Play Morse code sound using `pygame`.

	:parameter code: The Morse code string to play.
	:parameter delay: The delay in seconds between each Morse code symbol (default is 0.5).
	:parameter volume: The volume of the Morse code playback (default is 0.5).
	:parameter dot: Symbol representing a dot (default is '.').
	:parameter dash: Symbol representing a dash (default is '-').
	:parameter separator: Symbol representing a separator (default is '/').

	:returns: `None`
	"""

	# Error Handling
	if any(len(symbol) != 1 for symbol in {dot, dash, separator}):
		logging.error(ERROR_MESSAGE1)
		return

	if delay > 1.0:
		logging.warning(WARNING_MESSAGE1)

	if delay < 0.3:
		logging.error(ERROR_MESSAGE5)
		return

	if not 0.0 < volume <= 3.0:
		logging.error(ERROR_MESSAGE4)
		return

	# Separate the string into individual Morse code characters
	characters: List[str] = separate_letters(separate_words(code.strip(), dot, dash, separator, sound_mode=True))

	# Initialize audio manager
	audio_manager: AudioManagerPygame = AudioManagerPygame(volume)

	try:
		for character in characters:
			match character:
				case '.':
					audio_manager.play_dot()
					sleep(delay / 2.0)
				case '-':
					audio_manager.play_dash()
					sleep(delay)
				case ' ':
					sleep(delay * 2.7)
				case '/':
					sleep(delay * 3.0)
				case _:
					audio_manager.play_error()
					sleep(delay / 1.5)
	except KeyboardInterrupt:
		logging.warning(WARNING_MESSAGE2)
		return
	finally:
		pygame.quit()
