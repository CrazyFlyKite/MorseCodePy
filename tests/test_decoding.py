import unittest

from MorseCodePy.decode import decode


class TestDecoding(unittest.TestCase):
	def test_english(self):
		self.assertEqual(decode('.... . .-.. .-.. --- -.-.--', 'english'), 'hello!')
		self.assertEqual(decode('--. --- --- -.. / ---- .- .. .-. .-.-.-', 'english'), 'good chair.')
		self.assertEqual(decode('.--. --- .-- . .-.', 'english'), 'power')

	def test_french(self):
		self.assertEqual(decode('-... --- -. .--- --- ..- .-. -.-.--', 'french'), 'bonjour!')
		self.assertEqual(decode(
			'.---- ----- / .--. .. .-..- -.-. . ... / .--. --- ..- .-. / ..- -. . / -... .- --. ..- . - - . .-.-.-',
			'french'), '10 pièces pour une baguette.')
		self.assertEqual(decode('.-.. .----. .--.- -. . / -- .- -. --. . .-.-.-', 'french'), 'l\'âne mange.')

	def test_spanish(self):
		self.assertEqual(decode('--...- .... --- .-.. .- -.-.--', 'spanish'), '¡hola!')
		self.assertEqual(decode('..-.- -.-. ---. -- --- / . ... - .--.- ... ..--..', 'spanish'), '¿cómo estás?')

	def test_russian(self):
		self.assertEqual(decode('.--. .-. .. .-- . - -.-.--', 'russian'), 'привет!')
		self.assertEqual(decode('-.- .- -.- / -.. . .-.. .- ..--..', 'russian'), 'как дела?')

	def test_ukrainian(self):
		self.assertEqual(decode('.-- .. - .- ..-- -.-.--', 'ukrainian'), 'вітаю!')
		self.assertEqual(decode('.-.- -.- / ... .--. .-. .- .-- -.-- ..--..', 'ukrainian'), 'як справи?')

	def test_numbers(self):
		self.assertEqual(decode('.---- ..--- ...-- ....- ..... -.... --... ---.. ----. -----', 'numbers'), '1234567890')

	def test_special_characters(self):
		self.assertEqual(decode('.-.-.- / .--.-. / -.-.-- ..--..', 'special'), '. @ !?')
		self.assertEqual(decode('-...- -...- / ...-..-', 'special'), '== $')


if __name__ == '__main__':
	unittest.main()
