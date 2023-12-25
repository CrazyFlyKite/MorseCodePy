import json
from os import path


# Load the encodes.json
def get_encodes() -> dict[str: dict[str: str]]:
	"""
	Load the Morse code encodings from the "encodes.json" file.

	:returns: A dictionary containing Morse code encodings.
	"""

	file_path = path.join(path.dirname(path.abspath(__file__)), 'codes', 'encodes.json')

	with open(file_path, 'r', encoding='utf-8') as file:
		return json.load(file)


# Load the decodes.json
def get_decodes() -> dict[str: dict[str: str]]:
	"""
	Load the Morse code decodings from the "decodes.json" file.

	:returns: A dictionary containing Morse code decodings.
	"""

	file_path = path.join(path.dirname(path.abspath(__file__)), 'codes', 'decodes.json')

	with open(file_path, 'r', encoding='utf-8') as file:
		return json.load(file)
