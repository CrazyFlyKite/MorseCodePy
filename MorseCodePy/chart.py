import logging
from io import StringIO

from .utilities import *


def chart(*, dot: Optional[str] = '·', dash: Optional[str] = '-') -> None:
	"""
	Print Morse code chart in the console

	:parameter dot: Symbol representing dots (default is `·`)
	:parameter dash: Symbol representing dashes (default is `-`)

	:returns: `None`
	"""

	if any(len(symbol) != 1 for symbol in {dot, dash}):
		logging.error(ERROR_MESSAGE1)
		return

	string_io: StringIO = StringIO()
	encodes: JSONDictionary = get_encodes()

	string_io.write('Morse Code Chart\n\n' + '-' * 15 + '\n')

	for language, codes in encodes.items():
		string_io.write('\n' + language.capitalize() + '\n')

		for character, code in codes.items():
			if code not in '\n ':
				code = code.replace('.', dot).replace('-', dash)
				string_io.write(f'{character:<5} {code}\n')

		string_io.write('\n' + '-' * 15 + '\n')

	# Output
	print(string_io.getvalue().rstrip())
