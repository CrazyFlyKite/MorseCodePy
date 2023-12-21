# Hide the pygame support prompt
from os import environ

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

from pygame import mixer
from os import path
from pathlib import Path


class AudioManager:
	"""
	The AudioManager class manages audio playback for Morse code.
	"""

	def __init__(self, *, volume: float, directory: Path = Path('sounds'), dot_sound_file: Path = Path('dot.wav'),
	             dash_sound_file: Path = Path('dash.wav'), error_sound_file: Path = Path('error.wav')) -> None:
		"""
		Initializes the AudioManager with the specified volume and sound files.

		:parameter volume: The volume of the Morse code playback, a float between 0.0 and 1.0.
		:parameter directory: The directory containing the sound files (default is 'sounds').
		:parameter dot_sound_file: The filename of the sound file for dots (default is 'dot.wav').
		:parameter dash_sound_file: The filename of the sound file for dashes (default is 'dash.wav').
		"""

		self.__volume = volume
		self.__directory = directory
		self.__dot_sound_file = str(dot_sound_file)
		self.__dash_sound_file = str(dash_sound_file)
		self.__error_sound_file = str(error_sound_file)

		mixer.init()  # Initialize the pygame mixer

	def _load(self, filename: str) -> None:
		sound_path = path.join(path.dirname(__file__), self.__directory, filename)

		if not path.exists(sound_path):
			raise FileNotFoundError(f'Sound file {filename} not found!')

		mixer.music.load(sound_path)
		mixer.music.set_volume(self.__volume)

	def play_dot(self) -> None:
		"""
		Plays the sound for a dot with the specified volume.
		"""

		self._load(self.__dot_sound_file)
		mixer.music.play()

	def play_dash(self) -> None:
		"""
		Plays the sound for a dash with the specified volume.
		"""

		self._load(self.__dash_sound_file)
		mixer.music.play()

	def play_error(self) -> None:
		"""
		Plays the sound for an error message with the specified volume.
		"""

		self._load(self.__error_sound_file)
		mixer.music.play()
