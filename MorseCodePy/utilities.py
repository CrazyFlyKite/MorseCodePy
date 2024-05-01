import json
from os import PathLike, path
from typing import TypeAlias, List, Dict, Optional, Final, Literal, TypeVar

# Error and warning messages
ERROR_MESSAGE1: Final[str] = 'Invalid Symbols - Dots, dashes, and separators must be single characters!'
ERROR_MESSAGE2: Final[str] = 'Invalid Characters - Use only specified dots, dashes, spaces, and separators!'
ERROR_MESSAGE3: Final[str] = 'Invalid Volume - Volume should be between 0.0 and 1.0!'
ERROR_MESSAGE4: Final[str] = 'Invalid Volume - Volume should be between 0.0 and 3.0!'
ERROR_MESSAGE5: Final[str] = 'Invalid Delay - The specified delay should be more than 0.3!'
ERROR_MESSAGE6: Final[str] = 'Invalid Language - The specified language is not recognized or supported! Read the documentation for more details.'
WARNING_MESSAGE1: Final[str] = 'Long Delay - The specified delay is longer than recommended (1 second). Playback may be slower than expected.'
WARNING_MESSAGE2: Final[str] = 'Keyboard Interrupt - Morse code playback interrupted by user.'

# Custom types
Language: TypeAlias = Literal['english', 'spanish', 'french', 'russian', 'ukrainian', 'numbers', 'special']
JSONDictionary: TypeAlias = Dict[str, Dict[str, str]]
PathLikeString: TypeAlias = str | PathLike

# Generic types
KT = TypeVar('KT')
VT = TypeVar('VT')


# Useful functions
def reverse_dictionary(dictionary: Dict[KT, VT], /) -> Dict[VT, KT]:
	"""
	Reverse a dictionary.

	:parameter dictionary: The input dictionary to be processed.

	:returns: A list of individual Morse code characters.
	"""

	return {value: key for key, value in dictionary.items()}


def get_encodes() -> JSONDictionary:
	"""
	Load the Morse code encodings from the "encodes.json".

	:returns: A dictionary containing Morse code encodings.
	"""

	file_path: str = path.join(path.dirname(path.abspath(__file__)), 'codes', 'encodes.json')

	with open(file_path, 'r', encoding='utf-8') as file:
		return json.load(file)


def get_decodes() -> JSONDictionary:
	"""
	Load the Morse code decodings from the "decodes.json".

	:returns: A dictionary containing Morse code decodings.
	"""

	file_path: str = path.join(path.dirname(path.abspath(__file__)), 'codes', 'decodes.json')

	with open(file_path, 'r', encoding='utf-8') as file:
		return {key: reverse_dictionary(value) for key, value in json.load(file).items()}


def separate_words(words: str, /, dot: str, dash: str, separator: str, *,
                   sound_mode: Optional[bool] = False) -> List[str]:
	"""
	Separate a string into Morse code letters.

	:parameter words: The input string to be processed.
	:parameter dot: The symbol to represent dots.
	:parameter dash: The symbol to represent dashes.
	:parameter separator: The symbol used to separate words.
	:parameter sound_mode: A flag to include space characters when sound mode is enabled (default is False).

	:returns: A list of Morse code letters.
	"""

	letters: List[str] = []
	current: str = ''

	for character in words:
		if character in (dot, dash):
			current += character
		elif character == separator:
			if current:
				letters.append(current)
				current = ''
			letters.append(separator)
		elif character == ' ':
			if current:
				letters.append(current)
				current = ''
			if sound_mode:
				letters.append(' ')
		else:
			current += character

	if current:
		letters.append(current)

	return letters


def separate_letters(letters: List[str], /) -> List[str]:
	"""
	Separate Morse code letters into individual characters.

	:parameter letters: The input list to be processed.

	:returns: A list of individual Morse code characters.
	"""

	return [character for letter in letters for character in letter]
