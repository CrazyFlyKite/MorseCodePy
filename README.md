<img alt="Logo" src="https://images2.imgbox.com/a2/44/Xcip287L_o.png" width="400"/>

[![License](https://img.shields.io/badge/License-MIT-green)](license.txt)

### Requirements

![Python Version](https://img.shields.io/badge/Python-3.11%2B-blue)

## Introduction

**MorseCodePy** helps with **encoding** text into Morse code and **decoding** it back. It supports multiple languages,
including **English**, **Russian**, **Ukrainian**, **Spanish**, **French**. It also has support for **numbers** and
other **special characters**.
___

## Usage

### `encode(string, /, language, *, dot, dash, error, markup)`

Encodes the string into Morse code

- `string`: Input string
- `language`: Language for encoding (e.g., `english`, `french`, `spanish`, `russian`, `ukrainian`, `numbers`, `special`)
- `dot`: *(optional)* Symbol representing dots (default is `.`)
- `dash`: *(optional)* Symbol representing dashes (default is `-`)
- `separator`: *(optional)* Symbol separating words (default is `/`)
- `error`: *(optional)* Symbol representing errors when the index is not found in the dictionary (default is `*`)
- `markup`: *(optional)* If True, shows the original character in brackets before its Morse code (default is `False`)

```python
from MorseCodePy import encode

# Encoding a simple English sentence
encoded_string: str = encode('Python is fun!', language='english')
print(encoded_string)
# Output: .--. -.-- - .... --- -. / .. ... / ..-. ..- -. -.-.--

```

```python
from MorseCodePy import encode

# Encoding a Ukrainian sentence with custom dot and dash symbols and unsupported characters
encoded_string: str = encode('Привіт, світ! Ü', language='ukrainian', dot='*', dash='=', error='#')
print(encoded_string)
# Output: *==* *=* =*== *== ** = ==**== / *** *== ** = =*=*== / #
```

```python
from MorseCodePy import encode

# Encoding a Russian sentence with markup
encoded_string: str = encode('До встречи!', language='russian', markup=True)
print(encoded_string)

# Output: [Д] -.. [О] --- / [В] .-- [С] ... [Т] - [Р] .-. [Е] . [Ч] ---. [И] .. [!] -.-.--
```

___

### `decode(code, /, language, *, dot, dash, error, markup)`

Decode the Morse code into a string

- `code`: Input Morse code string
- `language`: Language for decoding (e.g., `english`, `french`, `spanish`, `russian`, `ukrainian`, `numbers`, `special`)
- `dot`: *(optional)* Symbol representing dots (default is `.`)
- `dash`: *(optional)* Symbol representing dashes (default is `-`)
- `separator` *(optional)* Symbol separating words (default is `/`)
- `error`: *(optional)* Symbol representing errors when the index is not found in the dictionary (default is `*`)
- `markup`: *(optional)* If True, shows the original Morse code sequence in brackets before the decoded character (default is `False`)

```python
from MorseCodePy import decode

# Decoding Morse code to Spanish text
decoded_string: str = decode('-- --- .-. ... . / -.-. --- -.. .', language='spanish')
print(decoded_string)
# Output: morse code
```

```python
from MorseCodePy import decode

# Decoding Morse code numbers with custom symbols
decoded_string: str = decode('****- **--- / *---- -----', language='numbers', dot='*', error='#')
print(decoded_string)
# Output: 42 10
```

___

### `chart(*, dot, dash)`

Print Morse code chart in the console

- `dot`: *(optional)* Symbol representing dots (default is `·`)
- `dash`: *(optional)* Symbol representing dashes (default is `-`)

```python
from MorseCodePy import chart

chart(dot='.', dash='_')
```

## Command Lines

MorseCodePy also has **terminal commands**! You can encode, decode, view a Morse code chart, list supported languages,
and more directly from the terminal. All the commands are very similar to the original Python function, so I recommend
reading the documentation for them first.

### `encode`

Encode text into Morse code

Command: `morsecodepy encode <text> <language> [--dot DOT] [--dash DASH] [--separator SEPARATOR] [--error ERROR] [--markup]`

```bash
morsecodepy encode "Python is fun!" english
```

___

### `decode`

Decode Morse code into text

Command: `morsecodepy decode <code> <language> [--dot DOT] [--dash DASH] [--separator SEPARATOR] [--error ERROR] [--markup]`

```bash
morsecodepy decode "-- --- .-. ... . / -.-. --- -.. ." spanish
```

___

### `chart`

Print out the code chart

Command: `morsecodepy chart [--dot DOT] [--dash DASH]`

```bash
morsecodepy chart --dot '*' --dash '='
```

___

### `languages`

Print out the list of supported languages

Command: `morsecodepy languages`

___

## Contact

- [Discord](https://discord.com/users/873920068571000833)
- [GitHub](https://github.com/CrazyFlyKite)
- [Email](mailto:karpenkoartem2846@gmail.com)
