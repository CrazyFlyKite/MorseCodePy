import logging
from time import sleep

import sounddevice
import soundfile

from MorseCodePy.utilities import *


class AudioManagerSounddevice:
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

		self.__volume = volume
		self.__directory = directory
		self.__dot_sound_file = dot_sound_file
		self.__dash_sound_file = dash_sound_file
		self.__error_sound_file = error_sound_file

		self.__audio_cache = {}

	def _load_sound(self, filename: PathLikeString) -> None:
		if filename not in self.__audio_cache:
			if not path.exists(sound_path := path.join(path.dirname(__file__), self.__directory, filename)):
				raise FileNotFoundError(f'Sound file {filename} not found!')

			data, frequency = soundfile.read(sound_path)
			self.__audio_cache[filename] = (data, frequency)

	def _play(self, filename: PathLikeString) -> None:
		if filename not in self.__audio_cache:
			self._load_sound(filename)

		data, frequency = self.__audio_cache[filename]
		sounddevice.play(data * self.__volume, frequency)
		sounddevice.wait()

	def play_dot(self) -> None:
		self._play(self.__dot_sound_file)

	def play_dash(self) -> None:
		self._play(self.__dash_sound_file)

	def play_error(self) -> None:
		self._play(self.__error_sound_file)


def play_sounddevice(code: str, /, delay: float = 0.3, volume: float = 0.5, *, dot: Optional[str] = '.',
                     dash: Optional[str] = '-', separator: Optional[str] = '/') -> None:
	"""
	Play Morse code sound using `sounddevice`.

	:parameter code: The Morse code string to play.
	:parameter delay: The delay in seconds between each Morse code symbol (default is 0.5).
	:parameter volume: The volume of the Morse code playback (default is 0.5).
	:parameter dot: Symbol representing a dot (default is '.').
	:parameter dash: Symbol representing a dash (default is '-').
	:parameter separator: Symbol representing a separator (default is '/').

	:returns: `None`
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
		logging.error(ERROR_MESSAGE5)
		return

	# Error Handling: Ensure that volume is within the valid range
	if not 0.0 < volume <= 3.0:
		logging.error(ERROR_MESSAGE3)
		return

	# Separate the string into individual Morse code characters
	characters: List[str] = separate_letters(separate_words(code.strip(), dot, dash, separator, sound_mode=True))

	# Initialize audio manager
	audio_manager: AudioManagerSounddevice = AudioManagerSounddevice(volume=volume)

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
