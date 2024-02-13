# Hide the pygame support prompt
from os import environ, path

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import logging
from time import sleep

from pygame import mixer

from .utilities import *


class AudioManager:
	def __init__(self, *, volume: float, directory: Optional[PathLikeString] = 'sounds',
	             dot_sound_file: Optional[PathLikeString] = 'dot.wav',
	             dash_sound_file: Optional[PathLikeString] = 'dash.wav',
	             error_sound_file: Optional[PathLikeString] = 'error.wav') -> None:
		"""
		Initializes the AudioManager with the specified volume and sound files.

		:parameter volume: The volume of the Morse code playback, a float between 0.0 and 1.0.
		:parameter directory: The directory containing the sound files (default is 'sounds').
		:parameter dot_sound_file: The filename of the sound file for dots (default is 'dot.wav').
		:parameter dash_sound_file: The filename of the sound file for dashes (default is 'dash.wav').
		"""

		self.__volume = volume
		self.__directory = directory
		self.__dot_sound_file = dot_sound_file
		self.__dash_sound_file = dash_sound_file
		self.__error_sound_file = error_sound_file

		mixer.init()  # Initialize pygame version

	@property
	def volume(self) -> float:
		return self.__volume

	@volume.setter
	def volume(self, value: int | float) -> None:
		if not isinstance(value, (int, float)):
			raise TypeError('The volume must be a float or an integer')

		if not 0.0 <= value <= 1.0:
			raise ValueError('The volume must be between 0.0 and 1.0')

		self.__volume = float(value)

	@property
	def directory(self) -> PathLikeString:
		return str(self.__directory)

	@property
	def dot_sound_file(self) -> PathLikeString:
		return str(self.__dot_sound_file)

	@property
	def dash_sound_file(self) -> PathLikeString:
		return str(self.__dash_sound_file)

	@property
	def error_sound_file(self) -> PathLikeString:
		return str(self.__error_sound_file)

	def _load(self, filename: PathLikeString) -> None:
		if not path.exists(sound_path := path.join(path.dirname(__file__), self.directory, filename)):
			raise FileNotFoundError(f'Sound file {filename} not found')

		mixer.music.load(sound_path)
		mixer.music.set_volume(self.volume)

	def play_dot(self) -> None:
		"""
		Plays the sound for a dot with the specified volume.
		"""

		self._load(self.dot_sound_file)
		mixer.music.play()

	def play_dash(self) -> None:
		"""
		Plays the sound for a dash with the specified volume.
		"""

		self._load(self.dash_sound_file)
		mixer.music.play()

	def play_error(self) -> None:
		"""
		Plays the sound for an error message with the specified volume.
		"""

		self._load(self.error_sound_file)
		mixer.music.play()


def play_pygame(code: str, /, delay: float = 0.5, volume: float = 1.0, *, dot: Optional[str] = '.',
                dash: Optional[str] = '-', separator: Optional[str] = '/') -> None:
	"""
	Play Morse code sound.

	:parameter code: The Morse code string to play.
	:parameter delay: The delay in seconds between each Morse code symbol (default is 0.5).
	:parameter volume: The volume of the Morse code playback (default is 1.0).
	:parameter dot: Symbol representing a dot (default is '.').
	:parameter dash: Symbol representing a dash (default is '-').
	:parameter separator: Symbol representing a separator (default is '/').

	:returns: None
	"""

	# Error Handling: Ensure that dot, dash, and separator have only one symbol
	if any(len(symbol) != 1 for symbol in {dot, dash, separator}):
		logging.error(ERROR_MESSAGE1)
		return

	# Error Handling: Ensure that delay is smaller than 1.0
	if delay > 1.0:
		logging.warning(WARNING_MESSAGE1)

	# Error Handling: Ensure that delay is smaller than 1.0
	if delay < 0.3:
		logging.error(ERROR_MESSAGE4)
		return

	# Error Handling: Ensure that volume is within the valid range
	if not 0.0 < volume <= 1.0:
		logging.error(ERROR_MESSAGE3)
		return

	# Separate the string into individual Morse code characters
	characters: List[str] = separate_letters(separate_words(code.strip(), dot, dash, separator, sound_mode=True))

	# Initialize audio manager
	audio_manager: AudioManager = AudioManager(volume=volume)

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
