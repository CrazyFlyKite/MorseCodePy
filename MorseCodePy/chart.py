import logging
from io import StringIO
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

	string_io: StringIO = StringIO()
	encodes: JSONDict = get_encodes()

	string_io.write('Morse Code Chart\n\n' + '-' * 15 + '\n')

	for language, codes in encodes.items():
		string_io.write('\n' + language.capitalize() + '\n')

		for character, code in codes.items():
			if code not in '\n ':
				code = code.replace('.', dot).replace('-', dash)
				string_io.write(f'{character:<5} {code}\n')

		string_io.write('\n' + '-' * 15 + '\n')

	print(string_io.getvalue().rstrip())
