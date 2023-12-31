import logging
from io import StringIO
from time import sleep

from .audio_manager import AudioManager
from .codes import get_encodes, get_decodes
from .setup_logging import setup_logging
from .utilities import *

# Setup logging
setup_logging(level=logging.WARNING)


def encode(string: str, language: str, *, dot: Optional[str] = '.', dash: Optional[str] = '-',
           separator: Optional[str] = '/', error: Optional[str] = '*') -> str | None:
	"""
	Encodes your string into Morse code.

	:parameter string: The input string to be encoded.
	:parameter language: The language to use for encoding (e.g., "english", "french", "numbers").
	:parameter dot: The symbol to represent dots.
	:parameter dash: The symbol to represent dashes.
	:parameter separator: The symbol used to separate words.
	:parameter error: The symbol to represent errors when the index is not found in the dictionary.

	:returns: The Morse code representation of the input string.
	"""

	# Ensure that code and language don't contain any useless spaces, newlines or tabs
	string = string.lower().strip()
	language = language.lower().strip()

	# Get encodes dictionary
	encodes = get_encodes()

	# Error handling: Ensure that language is a valid string
	if not isinstance(language, str) or language not in encodes:
		logging.error(error_message5)
		return

	# Error handling: Ensure that dot, dash, and separator have only one symbol
	if any(len(symbol) != 1 for symbol in {dot, dash, separator}):
		logging.error(error_message1)
		return

	# Translating string into Morse code
	code_io = StringIO()

	index: int = 0
	while index != len(string):
		if string[index] == 'c' and string[index + 1] == 'h':
			code_io.write(dash * 4 + ' ')
			index += 1
		elif string[index] == ' ':
			code_io.write(separator + ' ')
		elif string[index] in encodes[language]:
			morse_code = encodes[language][string[index]]
			code_io.write(morse_code + ' ')
		elif string[index] in encodes['numbers']:
			morse_code = encodes['numbers'][string[index]]
			code_io.write(morse_code + ' ')
		elif string[index] in encodes['special']:
			morse_code = encodes['special'][string[index]]
			code_io.write(morse_code + ' ')
		else:
			code_io.write(error + ' ')

		index += 1

	return code_io.getvalue().rstrip()


def decode(code: str, language: str, *, dot: Optional[str] = '.', dash: Optional[str] = '-',
           separator: Optional[str] = '/', error: Optional[str] = '*') -> str | None:
	"""
	Decode Morse code into a string.

	:parameter code: The input Morse code string to be decoded.
	:parameter language: The language to use for decoding (e.g., "russian", "spanish", "special").
	:parameter dot: The symbol used to represent dots.
	:parameter dash: The symbol used to represent dashes.
	:parameter separator: The symbol used to separate words.
	:parameter error: The symbol to represent errors when an unknown Morse code sequence is encountered.

	:returns: The decoded string.
	"""

	# Ensure that language doesn't contain any useless spaces, newlines or tabs
	language = language.lower().strip()

	# Get decodes dictionary
	decodes = get_decodes()

	# Error handling: Ensure that language is a valid string
	if language not in decodes:
		logging.error(error_message5)
		return

	# Error Handling: Ensure that dot, dash, and separator have only one symbol
	if any(len(symbol) != 1 for symbol in {dot, dash, separator}):
		logging.error(error_message1)
		return

	# Error Handling: Ensure that the input string contains only valid Morse code symbols
	if any(character not in {dot, dash, separator, ' ', '\n'} for character in code):
		logging.error(error_message2)
		return

	# Replacing characters in code for consistent decoding
	code = code.strip().replace(dot, '.').replace(dash, '-')

	# Separating String: Split the input Morse code into letters and separators
	letters: List[str] = separate_words(code, dot, dash, separator)

	# Translating Morse Code into normal text
	string_io = StringIO()

	# Create dictionaries to map Morse code to characters for the selected language
	reversed_codes: Dict[str, str] = reverse_dictionary(decodes[language])
	reversed_numbers: Dict[str, str] = reverse_dictionary(decodes['numbers'])
	reversed_special: Dict[str, str] = reverse_dictionary(decodes['special'])

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


def chart(*, dot: Optional[str] = '·', dash: Optional[str] = '-') -> None:
	"""
	Print Morse code chart in the console.

	:parameter dot: The symbol to represent dots in the chart.
	:parameter dash: The symbol to represent dashes in the chart.

	:returns: None
	"""

	print('Morse Code Chart\n')
	print('-' * 15)

	# Get encodes dictionary
	encodes = get_encodes()

	# Iterate through the language codes and their corresponding characters
	for language, codes in encodes.items():
		print('\n' + language.capitalize())

		# Print characters and their Morse code representations
		for character, code in codes.items():
			if code not in {'\n', ' '}:
				code = code.replace('.', dot).replace('-', dash)
				print(f'{character:<5} {code}')

		print('\n' + '-' * 15)


def play(code: str, delay: float = 0.5, volume: float = 1.0, *, dot: Optional[str] = '.', dash: Optional[str] = '-',
         separator: Optional[str] = '/') -> None:
	"""
	Play Morse code sound.

	:parameter code: The Morse code string to play.
	:parameter delay: The delay in seconds between each Morse code symbol (default is 0.4).
	:parameter volume: The volume of the Morse code playback (default is 0.5).
	:parameter dot: Symbol representing a dot (default is '.').
	:parameter dash: Symbol representing a dash (default is '-').
	:parameter separator: Symbol representing a separator (default is '/').

	:returns: None
	"""

	# Error Handling: Ensure that dot, dash, and separator have only one symbol
	if any(len(symbol) != 1 for symbol in {dot, dash, separator}):
		logging.error(error_message1)
		return

	# Error Handling: Ensure that delay is smaller than 1.0
	if delay > 1.0:
		logging.warning(warning_message1)

	# Error Handling: Ensure that delay is smaller than 1.0
	if delay < 0.3:
		logging.error(error_message4)
		return

	# Error Handling: Ensure that volume is within the valid range
	if not 0.0 < volume <= 1.0:
		logging.error(error_message3)
		return

	# Separate the string into individual Morse code characters
	characters: List[str] = separate_letters(separate_words(code.strip(), dot, dash, separator, sound_mode=True))

	# Initialize audio manager
	audio_manager = AudioManager(volume=volume)

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
		logging.warning(warning_message2)
		return
