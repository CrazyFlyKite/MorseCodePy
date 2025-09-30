from argparse import ArgumentParser, Namespace

from .chart import chart
from .decode import decode
from .encode import encode
from .utilities import SUPPORTED_LANGUAGES


def main() -> None:
	parser: ArgumentParser = ArgumentParser(description='MorseCodePy - Easily Encode & Decode Morse Code')
	subparsers = parser.add_subparsers(dest='command', help='Sub-commands: encode, decode, chart, languages')
	parser.add_argument('--version', action='version', version='MorseCodePy 4.1')

	encode_parser: ArgumentParser = subparsers.add_parser('encode', help='Encode text into Morse code')
	encode_parser.add_argument('text', type=str, help='Text to encode')
	encode_parser.add_argument('language', type=str, help='Language for encoding')
	encode_parser.add_argument('--dot', type=str, default='.', help='Symbol for dots')
	encode_parser.add_argument('--dash', type=str, default='-', help='Symbol for dashes')
	encode_parser.add_argument('--separator', type=str, default='/', help='Symbol for separator between words')
	encode_parser.add_argument('--error', type=str, default='*', help='Symbol for error if the symbol is not supported')
	encode_parser.add_argument('--markup', type=bool, default=False, help='If True, shows the original character in brackets before its Morse code')

	decode_parser: ArgumentParser = subparsers.add_parser('decode', help='Decode Morse code into text')
	decode_parser.add_argument('code', type=str, help='Morse code to decode')
	decode_parser.add_argument('language', type=str, help='Language for decoding')
	decode_parser.add_argument('--dot', type=str, default='.', help='Symbol for dots')
	decode_parser.add_argument('--dash', type=str, default='-', help='Symbol for dashes')
	decode_parser.add_argument('--separator', type=str, default='/', help='Symbol for separator between words')
	decode_parser.add_argument('--error', type=str, default='*', help='Symbol for error if the symbol is not supported')
	decode_parser.add_argument('--markup', type=bool, default=False, help='If True, shows the original Morse code sequence in brackets before the decoded character')

	chart_parser: ArgumentParser = subparsers.add_parser('chart', help='Print out the code chart')
	chart_parser.add_argument('--dot', type=str, default='.', help='Symbol for dots')
	chart_parser.add_argument('--dash', type=str, default='-', help='Symbol for dashes')

	languages_parser: ArgumentParser = subparsers.add_parser('languages', help='List of supported languages')

	args: Namespace = parser.parse_args()
	if args.command == 'encode':
		text: str = encode(args.text, language=args.language, dot=args.dot, dash=args.dash, separator=args.separator,
		                   error=args.error, markup=args.markup)
		if text is not None:
			print(text)
	elif args.command == 'decode':
		text: str = decode(args.code, language=args.language, dot=args.dot, dash=args.dash, separator=args.separator,
		                   error=args.error, markup=args.markup)
		if text is not None:
			print(text)
	elif args.command == 'chart':
		chart(dot=args.dot, dash=args.dash)
	elif args.command == 'languages':
		print('Supported languages for encoding and decoding')
		for language in SUPPORTED_LANGUAGES:
			print(f'  - {language.capitalize()} \t\t({language})')
		print('  - Numbers \t\t(numbers)\n  - Special Characters \t(special)')
	else:
		parser.print_help()
