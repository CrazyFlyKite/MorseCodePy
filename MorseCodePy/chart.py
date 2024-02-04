import logging
from typing import Optional

from .codes import get_encodes
from .utilities import JSONDict, ERROR_MESSAGE1


def chart(*, dot: Optional[str] = '·', dash: Optional[str] = '-') -> None:
	"""
	Print Morse code chart in the console.

	:parameter dot: The symbol to represent dots in the chart.
	:parameter dash: The symbol to represent dashes in the chart.

	:returns: None
	"""

	# Error Handling: Ensure that dot, dash, and separator have only one symbol
	if any(len(symbol) != 1 for symbol in {dot, dash}):
		logging.error(ERROR_MESSAGE1)
		return

	print('Morse Code Chart\n')
	print('-' * 15)

	# Get encodes dictionary
	encodes: JSONDict = get_encodes()

	# Iterate through the language codes and their corresponding characters
	for language, codes in encodes.items():
		print('\n' + language.capitalize())

		# Print characters and their Morse code representations
		for character, code in codes.items():
			if code not in {'\n', ' '}:
				code = code.replace('.', dot).replace('-', dash)
				print(f'{character:<5} {code}')

		print('\n' + '-' * 15)
