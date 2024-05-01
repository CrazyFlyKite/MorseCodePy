import logging
from io import StringIO

from .utilities import *


def encode(string: str, /, language: Language, *, dot: Optional[str] = '.', dash: Optional[str] = '-',
           separator: Optional[str] = '/', error: Optional[str] = '*') -> Optional[str]:
	"""
	Encodes the string into Morse code.

	:parameter string: The input string to be encoded.
	:parameter language: The language to use for encoding (e.g., english, french, numbers).
	:parameter dot: The symbol to represent dots.
	:parameter dash: The symbol to represent dashes.
	:parameter separator: The symbol used to separate words.
	:parameter error: The symbol to represent errors when the index is not found in the dictionary.

	:returns: The Morse code representation of the input string.
	"""

	# Format string and language
	string = string.lower().strip()
	language = language.lower().strip()

	# Initialize variables
	string_io: StringIO = StringIO()
	encodes: JSONDictionary = get_encodes()

	# Error handling: Ensure that language is a valid string
	if not isinstance(language, str) or language not in encodes:
		logging.error(ERROR_MESSAGE6)
		return

	# Error handling: Ensure that dot, dash, and separator have only one symbol
	if any(len(symbol) != 1 for symbol in {dot, dash, separator}):
		logging.error(ERROR_MESSAGE1)
		return

	# Write
	ch_handler: bool = False
	for index, character in enumerate(string):
		if ch_handler:
			string_io.write(dash * 4 + ' ')
			ch_handler = False
		elif character == 'c' and string[index + 1] == 'h':
			ch_handler = True
		elif character == ' ':
			string_io.write(separator + ' ')
		elif character in encodes.get(language):
			string_io.write(encodes.get(language).get(character) + ' ')
		elif character in encodes.get('numbers'):
			string_io.write(encodes.get('numbers').get(character) + ' ')
		elif character in encodes.get('special'):
			string_io.write(encodes.get('special').get(character) + ' ')
		else:
			string_io.write(error + ' ')

	return string_io.getvalue().rstrip()
