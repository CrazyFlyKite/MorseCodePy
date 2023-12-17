import unittest
from MorseCodePy.main import encode, decode, Language


class TestDecoding(unittest.TestCase):
	def test_english(self):
		self.assertEqual(decode('.... . .-.. .-.. --- -.-.--', Language.english), 'hello!')
		self.assertEqual(decode('--. --- --- -.. / ---- .- .. .-. .-.-.-', Language.english), 'good chair.')
		self.assertEqual(decode('.--. --- .-- . .-.', Language.english), 'power')

	def test_french(self):
		self.assertEqual(decode('-... --- -. .--- --- ..- .-. -.-.--', Language.french), 'bonjour!')
		self.assertEqual(decode(
			'.---- ----- / .--. .. .-..- -.-. . ... / .--. --- ..- .-. / ..- -. . / -... .- --. ..- . - - . .-.-.-',
			Language.french), '10 pièces pour une baguette.')
		self.assertEqual(decode('.-.. .----. .--.- -. . / -- .- -. --. . .-.-.-', Language.french), 'l\'âne mange.')

	def test_spanish(self):
		self.assertEqual(decode('--...- .... --- .-.. .- -.-.--', Language.spanish), '¡hola!')
		self.assertEqual(decode('..-.- -.-. ---. -- --- / . ... - .--.- ... ..--..', Language.spanish), '¿cómo estás?')

	def test_russian(self):
		self.assertEqual(decode('.--. .-. .. .-- . - -.-.--', Language.russian), 'привет!')
		self.assertEqual(decode('-.- .- -.- / -.. . .-.. .- ..--..', Language.russian), 'как дела?')

	def test_ukrainian(self):
		self.assertEqual(decode('.-- .. - .- ..-- -.-.--', Language.ukrainian), 'вітаю!')
		self.assertEqual(decode('.-.- -.- / ... .--. .-. .- .-- -.-- ..--..', Language.ukrainian), 'як справи?')

	def test_numbers(self):
		self.assertEqual(decode('.---- ..--- ...-- ....- ..... -.... --... ---.. ----. -----', Language.numbers),
		                 '1234567890')

	def test_special_characters(self):
		self.assertEqual(decode('.-.-.- / .--.-. / -.-.-- ..--..', Language.special), '. @ !?')
		self.assertEqual(decode('-...- -...- / ...-..-', Language.special), '== $')


if __name__ == '__main__':
	unittest.main()
