import unittest

from MorseCodePy.encode import encode


class TestEncoding(unittest.TestCase):
	def test_english(self):
		self.assertEqual(encode('  Hello!  ', 'english'), '.... . .-.. .-.. --- -.-.--')
		self.assertEqual(encode('Good chair.', 'english'), '--. --- --- -.. / ---- .- .. .-. .-.-.-')
		self.assertEqual(encode('Power = ^', 'english'), '.--. --- .-- . .-. / -...- / *')

	def test_french(self):
		self.assertEqual(encode('Bonjour!', 'french'), '-... --- -. .--- --- ..- .-. -.-.--')
		self.assertEqual(encode('10 pièces pour une baguette.', 'french'),
		                 '.---- ----- / .--. .. .-..- -.-. . ... / .--. --- ..- .-. / ..- -. . / -... .- --. ..- . - - . .-.-.-')
		self.assertEqual(encode('L\'âne mange.', 'french'), '.-.. .----. .--.- -. . / -- .- -. --. . .-.-.-')

	def test_spanish(self):
		self.assertEqual(encode('¡Hola!', 'spanish'), '--...- .... --- .-.. .- -.-.--')
		self.assertEqual(encode('¿Cómo estás?', 'spanish'), '..-.- -.-. ---. -- --- / . ... - .--.- ... ..--..')

	def test_russian(self):
		self.assertEqual(encode('Привет!', 'russian'), '.--. .-. .. .-- . - -.-.--')
		self.assertEqual(encode('Как дела?', 'russian'), '-.- .- -.- / -.. . .-.. .- ..--..')

	def test_ukrainian(self):
		self.assertEqual(encode('Вітаю!', 'ukrainian'), '.-- .. - .- ..-- -.-.--')
		self.assertEqual(encode('Як справи?', 'ukrainian'), '.-.- -.- / ... .--. .-. .- .-- -.-- ..--..')

	def test_numbers(self):
		self.assertEqual(encode('1234567890', 'numbers'), '.---- ..--- ...-- ....- ..... -.... --... ---.. ----. -----')
		self.assertEqual(encode('One -> 1', 'numbers'), '* * * / -....- * / .----')

	def test_special_characters(self):
		self.assertEqual(encode('. ^@ !?', 'special'), '.-.-.- / * .--.-. / -.-.-- ..--..')
		self.assertEqual(encode('S == $', 'special'), '* / -...- -...- / ...-..-')


if __name__ == '__main__':
	unittest.main()
