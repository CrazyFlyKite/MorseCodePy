import logging
from io import StringIO

from utilities import *


def decode(code: str, /, language: Language, *, dot: Optional[str] = '.', dash: Optional[str] = '-',
           separator: Optional[str] = '/', error: Optional[str] = '*', markup: Optional[bool] = False) -> Optional[str]:
	"""
	Decode the Morse code into a string

	:parameter code: Input Morse code string
	:parameter language: Language for decoding (e.g., `english`, `french`, `spanish`, `russian`, `ukrainian`, `numbers`, `special`)
	:parameter dot: Symbol representing dots (default is `.`)
	:parameter dash: Symbol representing dashes (default is `-`)
	:parameter separator: Symbol separating words (default is `/`)
	:parameter error: Symbol representing errors when the index is not found in the dictionary (default is `*`)
	:parameter markup: If True, shows the original Morse code sequence in brackets before the decoded character (default is `False`)

	:returns: Decoded string
	"""

	code = code.strip().replace(dot, '.').replace(dash, '-')
	language = language.lower().strip()

	if language not in get_decodes():
		logging.error(ERROR_MESSAGE3)
		return

	if any(len(symbol) != 1 for symbol in {dot, dash, separator}):
		logging.error(ERROR_MESSAGE1)
		return

	if any(character not in {'.', '-', separator, ' ', '\n'} for character in code):
		logging.error(ERROR_MESSAGE2)
		return

	decodes: JSONDictionary = get_decodes()
	string_io: StringIO = StringIO()

	letters: List[str] = separate_words(code, dot, dash, separator)

	for letter in letters:
		if letter == '----' and language in {'english', 'spanish', 'french'}:
			if markup:
				string_io.write(f'[{letter}] ')

			string_io.write('ch')

			if markup:
				string_io.write(' ')
		elif letter == separator:
			string_io.write(' ')
		elif letter == '\n':
			string_io.write(letter)
		elif letter in decodes.get(language):
			if markup:
				string_io.write(f'[{letter}] ')

			string_io.write(decodes.get(language).get(letter))

			if markup:
				string_io.write(' ')
		elif letter in decodes.get('numbers') and language != 'special':
			if markup:
				string_io.write(f'[{letter}] ')

			string_io.write(decodes.get('numbers').get(letter))

			if markup:
				string_io.write(' ')
		elif letter in decodes.get('special') and language != 'numbers':
			if markup:
				string_io.write(f'[{letter}] ')

			string_io.write(decodes.get('special').get(letter))

			if markup:
				string_io.write(' ')
		else:
			string_io.write(error)

	return string_io.getvalue()
