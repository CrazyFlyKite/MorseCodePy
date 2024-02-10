import json
from os import path

from .utilities import JSONDict


def get_encodes() -> JSONDict:
	"""
	Load the Morse code encodings from the "encodes.json".

	:returns: A dictionary containing Morse code encodings.
	"""

	file_path: str = path.join(path.dirname(path.abspath(__file__)), 'codes', 'encodes.json')

	with open(file_path, 'r', encoding='utf-8') as file:
		return json.load(file)


def get_decodes() -> JSONDict:
	"""
	Load the Morse code decodings from the "decodes.json".

	:returns: A dictionary containing Morse code decodings.
	"""

	file_path: str = path.join(path.dirname(path.abspath(__file__)), 'codes', 'decodes.json')

	with open(file_path, 'r', encoding='utf-8') as file:
		return {key: {v: k for k, v in value.items()} for key, value in json.load(file).items()}
