from typing import Optional, List, Dict

# Error and warning messages
error_message1: str = 'Invalid Symbols - Dots, dashes, and separators must be single characters!'
error_message2: str = 'Invalid Characters - Use only specified dots, dashes, spaces, and separators!'
error_message3: str = 'Invalid Volume - Volume should be between 0.0 and 1.0!'
error_message4: str = 'Invalid Delay - The specified delay should be more than 0.3!'
error_message5: str = 'Invalid Language - The specified language is not recognized or supported! Read the documentation for more details.'
warning_message1: str = 'Long Delay - The specified delay is longer than recommended (1 second). Playback may be slower than expected.'
warning_message2: str = 'Keyboard Interrupt - Morse code playback interrupted by user.'


def separate_words(words: str, dot: str, dash: str, separator: str, *, sound_mode: Optional[bool] = False) -> List[str]:
	"""
	Separate a string into Morse code letters.

	:parameter words: The input string to be processed.
	:parameter dot: The symbol to represent dots.
	:parameter dash: The symbol to represent dashes.
	:parameter separator: The symbol used to separate words.
	:parameter sound_mode: A flag to include space characters when sound mode is enabled (default is False).

	:returns: A list of Morse code letters.
	"""

	letters: List = []
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


def separate_letters(letters: List[str]) -> List[str]:
	"""
	Separate Morse code letters into individual characters.

	:parameter letters: The input list to be processed.

	:returns: A list of individual Morse code characters.
	"""

	return [character for letter in letters for character in letter]


def reverse_dictionary(dictionary: Dict) -> Dict:
	"""
	Reverse the keys and values of a dictionary.

	:parameter dictionary: The input dictionary to be processed.

	:returns: A dictionary with reversed keys and values.
	"""

	return {value: key for key, value in dictionary.items()}
