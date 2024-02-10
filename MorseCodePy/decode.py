import logging
from io import StringIO

from .codes import get_decodes
from .utilities import *


def decode(code: str, /, language: Language, *, dot: Optional[str] = '.', dash: Optional[str] = '-',
           separator: Optional[str] = '/', error: Optional[str] = '*') -> str | None:
	"""
	Decode the Morse code into a string.

	:parameter code: The input Morse code string to be decoded.
	:parameter language: The language to use for decoding (e.g., russian, spanish, special).
	:parameter dot: The symbol used to represent dots.
	:parameter dash: The symbol used to represent dashes.
	:parameter separator: The symbol used to separate words.
	:parameter error: The symbol to represent errors when an unknown Morse code sequence is encountered.

	:returns: The decoded string.
	"""

	# Ensure that language doesn't contain any useless spaces, newlines or tabs
	language = language.lower().strip()

	# Get decodes dictionary
	decodes: JSONDict = get_decodes()

	# Error handling: Ensure that language is a valid string
	if language not in decodes:
		logging.error(ERROR_MESSAGE5)
		return

	# Error Handling: Ensure that dot, dash, and separator have only one symbol
	if any(len(symbol) != 1 for symbol in {dot, dash, separator}):
		logging.error(ERROR_MESSAGE1)
		return

	# Error Handling: Ensure that the input string contains only valid Morse code symbols
	if any(character not in {dot, dash, separator, ' ', '\n'} for character in code):
		logging.error(ERROR_MESSAGE2)
		return

	# Replacing characters in code for consistent decoding
	code = code.strip().replace(dot, '.').replace(dash, '-')

	# Separating String: Split the input Morse code into letters and separators
	letters: List[str] = separate_words(code, dot, dash, separator)

	# Translating Morse Code into normal text
	string_io: StringIO = StringIO()

	# Create dictionaries to map Morse code to characters for the selected language
	reversed_codes: Dict[str, str] = decodes[language]
	reversed_numbers: Dict[str, str] = decodes['numbers']
	reversed_special: Dict[str, str] = decodes['special']

	for letter in letters:
		if letter == '----' and language in {'english', 'spanish', 'french'}:
			string_io.write('ch')
		elif letter == separator:
			string_io.write(' ')
		elif letter == '\n':
			string_io.write(letter)
		elif letter in reversed_codes:
			string_io.write(reversed_codes[letter])
		elif letter in reversed_numbers and language != 'special':
			string_io.write(reversed_numbers[letter])
		elif letter in reversed_special and language != 'numbers':
			string_io.write(reversed_special[letter])
		else:
			string_io.write(error)

	return string_io.getvalue()
