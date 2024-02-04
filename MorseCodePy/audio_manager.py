# Hide the pygame support prompt
from os import environ, path

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

from pygame import mixer
from typing import Optional, Any
from .utilities import PathLikeString


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

		# Initialize the pygame mixer
		mixer.init()

	@property
	def volume(self) -> float:
		return self.__volume

	@volume.setter
	def volume(self, value: Any) -> None:
		self.__volume = float(value)

	@property
	def directory(self) -> PathLikeString:
		return self.__directory

	@property
	def dot_sound_file(self) -> PathLikeString:
		return self.__dot_sound_file

	@property
	def dash_sound_file(self) -> PathLikeString:
		return self.__dash_sound_file

	@property
	def error_sound_file(self) -> PathLikeString:
		return self.__error_sound_file

	def _load(self, filename: PathLikeString) -> None:
		if not path.exists(sound_path := path.join(path.dirname(__file__), self.directory, filename)):
			raise FileNotFoundError(f'Sound file {filename} not found!')

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
