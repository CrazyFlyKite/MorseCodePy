import logging
from time import sleep

from .audio_manager import AudioManager
from .codes import encodes, decodes, Language
from .setup_logging import setup_logging
from .utilities import *

# Setup logging
setup_logging(level=logging.WARNING)


def encode(string: str, language: Language, dot: str = '.', dash: str = '-', separator: str = '/',
           error: str = '*') -> str | None:
	"""
	Encodes your string into Morse code.

	:parameter string: The input string to be encoded.
	:parameter language: The language to use for encoding (e.g., Language.english, Language.french, Language.numbers).
	:parameter dot: The symbol to represent dots.
	:parameter dash: The symbol to represent dashes.
	:parameter separator: The symbol used to separate words.
	:parameter error: The symbol to represent errors when a character is not found in the dictionary.

	:returns: The Morse code representation of the input string.
	"""

	# Error handling: Ensure that dot, dash, and separator have only one symbol
	if any(len(symbol) != 1 for symbol in {dot, dash, separator}):
		logging.error(error_message1)
		return

	# Translating string into Morse code
	code: str = ''  # New string that will hold the translated text
	string = string.lower().strip()  # Convert the input string to lowercase for consistent encoding

	character: int = 0
	while character != len(string):
		if string[character] == 'c' and string[character + 1] == 'h':
			code += dash * 4 + ' '
			character += 1
		elif string[character] == ' ':
			code += separator + ' '
		elif string[character] in encodes[language]:
			morse_code = encodes[language][string[character]]
			code += morse_code.replace('0', dot).replace('1', dash) + ' '
		elif string[character] in encodes[Language.numbers]:
			morse_code = encodes[Language.numbers][string[character]]
			code += morse_code.replace('0', dot).replace('1', dash) + ' '
		elif string[character] in encodes[Language.special]:
			morse_code = encodes[Language.special][string[character]]
			code += morse_code.replace('0', dot).replace('1', dash) + ' '
		else:
			code += error + ' '

		character += 1

	return code.rstrip()


def decode(code: str, language: Language, dot: str = '.', dash: str = '-', separator: str = '/',
           error: str = '*') -> str | None:
	"""
	Decode Morse code into a string.

	:parameter code: The input Morse code string to be decoded.
	:parameter language: The language to use for decoding (e.g., Language.russian, Language.spanish, Language.special).
	:parameter dot: The symbol used to represent dots.
	:parameter dash: The symbol used to represent dashes.
	:parameter separator: The symbol used to separate words.
	:parameter error: The symbol to represent errors when an unknown Morse code sequence is encountered.

	:returns: The decoded string.
	"""

	# Error Handling: Ensure that dot, dash, and separator have only one symbol
	if any(len(symbol) != 1 for symbol in {dot, dash, separator}):
		logging.error(error_message1)
		return

	# Error Handling: Ensure that the input string contains only valid Morse code symbols
	if any(character not in {dot, dash, separator, ' ', '\n'} for character in code):
		logging.error(error_message2)
		return

	# Separating String: Split the input Morse code into letters and separators
	letters: list[str] = separate_words(code, dot, dash, separator)

	# Ensure that code doesn't contain any useless spaces, newlines or tabs
	code = code.strip()

	# Translating Morse Code into normal text
	string: str = ''

	# Create dictionaries to map Morse code to characters for the selected language
	reversed_codes: dict[str] = reversed_dictionary(decodes[language])
	reversed_numbers: dict[str] = reversed_dictionary(decodes[Language.numbers])
	reversed_special: dict[str] = reversed_dictionary(decodes[Language.special])

	# Create a mapping dictionary to translate Morse code symbols to '0' and '1'
	mapping: dict[str: str] = {dot: '0', dash: '1'}

	for letter in letters:
		# Translate Morse code symbols to '0' and '1'
		letter = ''.join(mapping.get(character, character) for character in letter)

		if letter == '1111' and language in {Language.english, Language.spanish, Language.french}:
			string += 'ch'
		elif letter == separator:
			string += ' '
		elif letter == '\n':
			string += '\n'
		elif letter in reversed_codes:
			string += reversed_codes[letter]
		elif letter in reversed_numbers and language != Language.special:
			string += reversed_numbers[letter]
		elif letter in reversed_special and language != Language.numbers:
			string += reversed_special[letter]
		else:
			string += error

	return string


def chart(dot: str = '·', dash: str = '-') -> None:
	"""
	Print Morse code chart in the console.

	:parameter dot: The symbol to represent dots in the chart.
	:parameter dash: The symbol to represent dashes in the chart.

	:returns: None
	"""

	print('Morse Code Chart\n')
	print('-' * 15)

	# Iterate through the language codes and their corresponding characters
	for language, codes in encodes.items():
		print()
		print(language.name.capitalize())

		# Print characters and their Morse code representations
		for character, code in codes.items():
			if code not in {'\n', ' '}:
				code = code.replace('0', dot).replace('1', dash)
				print(f'{character:<5} {code}')

		print()
		print('-' * 15)


def play(code: str, delay: float = 0.5, volume: float = 1.0, dot: str = '.', dash: str = '-',
         separator: str = '/') -> None:
	"""
	Play Morse code sound.

	Note:
		This function require the pygame library for audio playback.

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
		logging.error(error_message5)
		return

	# Error Handling: Ensure that volume is within the valid range
	if not 0.0 < volume <= 1.0:
		logging.error(error_message4)
		return

	# Separate the string into individual Morse code characters
	characters: list[str] = separate_letters(separate_words(code.strip(), dot, dash, separator, sound_mode=True))

	# Initialize audio manager
	audio_manager = AudioManager(volume)

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
		logging.error(error_message3)
		return
