import logging
from io import StringIO

from .codes import get_encodes
from .utilities import *


def encode(string: str, /, language: Language, *, dot: Optional[str] = '.', dash: Optional[str] = '-',
           separator: Optional[str] = '/', error: Optional[str] = '*') -> str | None:
	"""
	Encodes the string into Morse code.

	:parameter string: The input string to be encoded.
	:parameter language: The language to use for encoding (e.g., english, french, numbers).
	:parameter dot: The symbol to represent dots.
	:parameter dash: The symbol to represent dashes.
	:parameter separator: The symbol used to separate words.
	:parameter error: The symbol to represent errors when the index is not found in the dictionary.

	:rtype: str
	:returns: The Morse code representation of the input string.
	"""

	# Ensure that code and language don't contain any useless spaces, newlines or tabs
	string = string.lower().strip()
	language = language.lower().strip()

	# Get encodes dictionary
	encodes: JSONDict = get_encodes()

	# Error handling: Ensure that language is a valid string
	if not isinstance(language, str) or language not in encodes:
		logging.error(ERROR_MESSAGE5)
		return

	# Error handling: Ensure that dot, dash, and separator have only one symbol
	if any(len(symbol) != 1 for symbol in {dot, dash, separator}):
		logging.error(ERROR_MESSAGE1)
		return

	# Translating string into Morse code
	string_io: StringIO = StringIO()

	ch_handler: bool = False
	for index, character in enumerate(string):
		if ch_handler:
			string_io.write(dash * 4 + ' ')
			ch_handler = False
		elif string[index] == 'c' and string[index + 1] == 'h':
			ch_handler = True
		elif character == ' ':
			string_io.write(separator + ' ')
		elif character in encodes[language]:
			string_io.write(encodes[language][character] + ' ')
		elif character in encodes['numbers']:
			string_io.write(encodes['numbers'][character] + ' ')
		elif character in encodes['special']:
			string_io.write(encodes['special'][character] + ' ')
		else:
			string_io.write(error + ' ')

	return string_io.getvalue().rstrip()
