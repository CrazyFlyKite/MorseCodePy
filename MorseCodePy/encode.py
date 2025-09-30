import logging
from io import StringIO

from .utilities import *


def encode(string: str, /, language: Language, *, dot: Optional[str] = '.', dash: Optional[str] = '-',
           separator: Optional[str] = '/', error: Optional[str] = '*', markup: Optional[bool] = False) -> Optional[str]:
	"""
	Encode the string into Morse code

	:parameter string: Input string
	:parameter language: Language for encoding (e.g., `english`, `french`, `spanish`, `russian`, `ukrainian`, `numbers`, `special`)
	:parameter dot: Symbol representing dots (default is `.`)
	:parameter dash: Symbol representing dashes (default is `-`)
	:parameter separator: Symbol separating words (default is `/`)
	:parameter error: Symbol representing errors when the index is not found in the dictionary (default is `*`)
	:parameter markup: If True, shows the original character in brackets before its Morse code (default is `False`)

	:returns: Encoded string
	"""

	string = string.lower().strip()
	language = language.lower().strip()

	string_io: StringIO = StringIO()
	encodes: JSONDictionary = get_encodes()

	if not isinstance(language, str) or language not in encodes:
		logging.error(ERROR_MESSAGE3)
		return

	if any(len(symbol) != 1 for symbol in {dot, dash, separator}):
		logging.error(ERROR_MESSAGE1)
		return

	ch_handler: bool = False
	for index, character in enumerate(string):
		if ch_handler:
			if markup:
				string_io.write('[CH] ')

			string_io.write(dash * 4 + ' ')
			ch_handler = False
		elif character == 'c' and string[index + 1] == 'h':
			ch_handler = True
		elif character == ' ':
			string_io.write(separator + ' ')
		elif character in encodes.get(language):
			if markup:
				string_io.write(f'[{character.upper()}] ')

			string_io.write(encodes.get(language).get(character).replace('.', dot).replace('-', dash) + ' ')
		elif character in encodes.get('numbers'):
			if markup:
				string_io.write(f'[{character}] ')

			string_io.write(encodes.get('numbers').get(character).replace('.', dot).replace('-', dash) + ' ')
		elif character in encodes.get('special'):
			if markup:
				string_io.write(f'[{character}] ')

			string_io.write(encodes.get('special').get(character).replace('.', dot).replace('-', dash) + ' ')
		else:
			string_io.write(error + ' ')

	return string_io.getvalue().rstrip()
