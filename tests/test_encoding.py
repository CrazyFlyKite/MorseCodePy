import unittest

from MorseCodePy.main import encode, Language


class TestEncoding(unittest.TestCase):
	def test_english(self):
		self.assertEqual(encode('  Hello!  ', Language.english), '.... . .-.. .-.. --- -.-.--')
		self.assertEqual(encode('Good chair.', Language.english), '--. --- --- -.. / ---- .- .. .-. .-.-.-')
		self.assertEqual(encode('Power = ^', Language.english), '.--. --- .-- . .-. / -...- / *')

	def test_french(self):
		self.assertEqual(encode('Bonjour!', Language.french), '-... --- -. .--- --- ..- .-. -.-.--')
		self.assertEqual(encode('10 pièces pour une baguette.', Language.french),
		                 '.---- ----- / .--. .. .-..- -.-. . ... / .--. --- ..- .-. / ..- -. . / -... .- --. ..- . - - . .-.-.-')
		self.assertEqual(encode('L\'âne mange.', Language.french), '.-.. .----. .--.- -. . / -- .- -. --. . .-.-.-')

	def test_spanish(self):
		self.assertEqual(encode('¡Hola!', Language.spanish), '--...- .... --- .-.. .- -.-.--')
		self.assertEqual(encode('¿Cómo estás?', Language.spanish), '..-.- -.-. ---. -- --- / . ... - .--.- ... ..--..')

	def test_russian(self):
		self.assertEqual(encode('Привет!', Language.russian), '.--. .-. .. .-- . - -.-.--')
		self.assertEqual(encode('Как дела?', Language.russian), '-.- .- -.- / -.. . .-.. .- ..--..')

	def test_ukrainian(self):
		self.assertEqual(encode('Вітаю!', Language.ukrainian), '.-- .. - .- ..-- -.-.--')
		self.assertEqual(encode('Як справи?', Language.ukrainian), '.-.- -.- / ... .--. .-. .- .-- -.-- ..--..')

	def test_numbers(self):
		self.assertEqual(encode('1234567890', Language.numbers),
		                 '.---- ..--- ...-- ....- ..... -.... --... ---.. ----. -----')
		self.assertEqual(encode('One -> 1', Language.numbers), '* * * / -....- * / .----')

	def test_special_characters(self):
		self.assertEqual(encode('. ^@ !?', Language.special), '.-.-.- / * .--.-. / -.-.-- ..--..')
		self.assertEqual(encode('S == $', Language.special), '* / -...- -...- / ...-..-')


if __name__ == '__main__':
	unittest.main()
