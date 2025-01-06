<img alt="Logo" src="https://images2.imgbox.com/a2/44/Xcip287L_o.png" width="400"/>

[![License](https://img.shields.io/badge/License-MIT-green)](license.txt)

### Requirements

![Python Version](https://img.shields.io/badge/Python-3.11%2B-blue)
![pygame Version](https://img.shields.io/badge/pygame-2.5.2%2B-red)

## Introduction

**MorseCodePy** is a versatile Python library that streamlines the **encoding** and **decoding**
of text into Morse code and back. With support for multiple languages, including
**English**, **Russian**, **Ukrainian**,**Spanish**, **French**, as well as provisions for handling
**numbers** and other **special characters**. This library offers a powerful and **user-friendly** Morse code tool.
___

## Usage

### `encode(string, /, language, *, dot, dash, error)`

Encode a text string into Morse code.

- `string`: The text string you want to encode.
- `language`: The target language for encoding (
  e.g., `english`, `french`, `spanish`, `russian`, `ukrainian`, `numbers`, `special`).
- `dot`: *(optional)* Symbol to represent dots (default is `.`).
- `dash`: *(optional)* Symbol to represent dashes (default is `-`).
- `error`: *(optional)* Symbol to represent errors when an unknown character is encountered (default is `*`).

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
encoded_string: str = encode('Привіт, світ! Ø', language='ukrainian', dot='*', dash='=', error='#')
print(encoded_string)
# Output: *==* *=* =*== *== ** = ==**== / *** *== ** = =*=*== / #
```

___

### `decode(code, /, language, *, dot, dash, error)`

Decode Morse code into a text string.

- `code`: The Morse code string you want to decode.
- `language`: The target language for decoding (
  e.g., `english`, `french`, `spanish`, `russian`, `ukrainian`, `numbers`, `special`).
- `dot`: *(optional)* Symbol to represent dots (default is `.`).
- `dash`: *(optional)* Symbol to represent dashes (default is `-`).
- `error`: *(optional)* Symbol to represent errors when an unknown Morse code sequence is encountered (default is `*`).

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

Print a Morse code chart in the console.

- `dot`: *(optional)* Symbol to represent dots (default is `·`).
- `dash`: *(optional)* Symbol to represent dashes (default is `-`).

```python
from MorseCodePy import chart

chart(dot='·')  # Try it yourself :)
```

## Command Lines

MorseCodePy also offers **terminal commands**! You can perform encoding, decoding, view a Morse code chart,
list supported languages, and more directly from the terminal. All the commands are very similar to the original
Python function, so I recommend to read the documentation for them first.

### `encode`

Encode text into Morse code

Command: `morsecodepy encode <text> <language> [--dot DOT] [--dash DASH] [--separator SEPARATOR] [--error ERROR]`

```bash
morsecodepy encode "Python is fun!" english
```

___

### `decode`

Decode Morse code into text

Command: `morsecodepy decode <code> <language> [--dot DOT] [--dash DASH] [--separator SEPARATOR] [--error ERROR]`

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
