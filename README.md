<img alt="Logo" src="https://images2.imgbox.com/a2/44/Xcip287L_o.png" width="400"/>

[![License](https://img.shields.io/badge/License-MIT-green)](license.txt)

### Requirements

![Python Version](https://img.shields.io/badge/Python-3.11%2B-blue)
![pygame Version](https://img.shields.io/badge/pygame-2.5.2%2B-red)

## Introduction

**MorseCodePy** is a versatile Python module that streamlines the **encoding** and **decoding**
of text into Morse code and back. With support for multiple languages, including **English**, **Russian**, **Ukrainian**,
**Spanish**, **French**, as well as provisions for handling **numbers** and other **special characters**, this module
offers a powerful and **user-friendly** Morse code tool.
___

## Usage

#### `encode(string, /, language, *, dot, dash, error)`

Encode a text string into Morse code.

- `string`: The text string you want to encode.
- `language`: The target language for encoding (e.g., `english`, `french`, `spanish`, `russian`, `ukranian`, `numbers`, `special`).
- `dot`: *(optional)* Symbol to represent dots (default is `.`).
- `dash`: *(optional)* Symbol to represent dashes (default is `-`).
- `error`: *(optional)* Symbol to represent errors when an unknown character is encountered (default is `*`).

```python
from MorseCodePy import encode

encoded_string = encode('Hello, world!', language='english')
print(encoded_string)
# Output: .... . .-.. .-.. --- --..-- / .-- --- .-. .-.. -.. -.-.--
```

```python
from MorseCodePy import encode

encoded_string: str = encode('10 pièces !', language='french')

print(encoded_string)
# Output: .---- ----- / .--. .. .-..- -.-. . ... / -.-.--
```

___

#### `decode(code, /, language, *, dot, dash, error)`

Decode Morse code into a text string.

- `code`: The Morse code string you want to decode.
- `language`: The target language for decoding (e.g., `english`, `french`, `spanish`, `russian`, `ukranian`, `numbers`, `special`).
- `dot`: *(optional)* Symbol to represent dots (default is `.`).
- `dash`: *(optional)* Symbol to represent dashes (default is `-`).
- `error`: *(optional)* Symbol to represent errors when an unknown Morse code sequence is encountered (default is `*`).

```python
from MorseCodePy import decode

decoded_string = decode('···· · ·-·· ·-·· --- --··-- / ·-- --- ·-· ·-·· -·· -·-·--', language='english', dot='·')
print(decoded_string)
# Output: hello, world!
```

___

#### `play_pygame(code, /, delay, volume, *, dot, dash, separator)`

Play Morse code sound using `pygame`.

- `code`: The Morse code you want to play.
- `delay`: *(optional)* The delay in seconds between characters (default is **0.3**).
- `volume`: *(optional)* The volume of the Morse code playback (default is **0.5**).
- `dot`: *(optional)* Symbol to represent dots (default is `.`).
- `dash`: *(optional)* Symbol to represent dashes (default is `-`).
- `separator`: *(optional)* Symbol to represent separators (default is `/`).

```python
from MorseCodePy import encode, play_pygame

encoded_string: str = encode('Hello', language='english')

play_pygame(encoded_string, delay=0.5, volume=0.8)
```

___

#### `play_sounddevice(code, /, delay, volume, *, dot, dash, separator)`

Play Morse code sound using `sounddevice`.

- `code`: The Morse code you want to play.
- `delay`: *(optional)* The delay in seconds between characters (default is **0.3**).
- `volume`: *(optional)* The volume of the Morse code playback (default is **0.5**).
- `dot`: *(optional)* Symbol to represent dots (default is `.`).
- `dash`: *(optional)* Symbol to represent dashes (default is `-`).
- `separator`: *(optional)* Symbol to represent separators (default is `/`).

```python
from MorseCodePy import encode, play_sounddevice

text: str = encode('Bonjour !', language='french')

play_sounddevice(text, volume=1.5)
```

___

#### `chart(*, dot, dash)`

Print a Morse code chart in the console.

- `dot`: *(optional)* Symbol to represent dots (default is `·`).
- `dash`: *(optional)* Symbol to represent dashes (default is `-`).

```python
from MorseCodePy import chart

chart(dot='·')
```

___

## Contact

- [Discord](https://discord.com/users/873920068571000833)
- [GitHub](https://github.com/CrazyFlyKite)
- [Email](mailto:karpenkoartem2846@gmail.com)
