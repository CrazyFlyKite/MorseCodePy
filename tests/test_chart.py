import unittest
from io import StringIO
from unittest.mock import patch, Mock

from MorseCodePy.chart import chart


class TestChart(unittest.TestCase):
	@patch('sys.stdout', new_callable=StringIO)
	def test_chart(self, mock_stdout: Mock):
		chart()

		chart_output: str = mock_stdout.getvalue()
		expected_output = r'''Morse Code Chart

---------------

English
a     ·-
b     -···
c     -·-·
d     -··
e     ·
f     ··-·
g     --·
h     ····
i     ··
j     ·---
k     -·-
l     ·-··
m     --
n     -·
o     ---
p     ·--·
q     --·-
r     ·-·
s     ···
t     -
u     ··-
v     ···-
w     ·--
x     -··-
y     -·--
z     --··

---------------

Spanish
a     ·-
á     ·--·-
b     -···
c     -·-·
d     -··
e     ·
é     ··-··
f     ··-·
g     --·
h     ····
i     ··
í     ··
j     ·---
k     -·-
l     ·-··
m     --
n     -·
ñ     --·--
o     ---
ó     ---·
p     ·--·
q     --·-
r     ·-·
s     ···
t     -
u     ··-
ú     ··-
ü     ··--
v     ···-
w     ·--
x     -··-
y     -·--
z     --··
¿     ··-·-
¡     --···-

---------------

French
a     ·-
à     ·--·-
â     ·--·-
b     -···
c     -·-·
ç     -·-··
d     -··
e     ·
è     ·-··-
é     ··-··
ê     -··-·
ë     ··-··
f     ··-·
g     --·
h     ····
i     ··
î     ··
ï     -··--
j     ·---
k     -·-
l     ·-··
m     --
n     -·
o     ---
ô     ---
p     ·--·
q     --·-
r     ·-·
s     ···
t     -
u     ··-
ù     ··-
ü     ··--
v     ···-
w     ·--
x     -··-
y     -·--
z     --··

---------------

Russian
а     ·-
б     -···
в     ·--
г     --·
д     -··
е     ·
ё     ·
ж     ···-
з     --··
и     ··
й     ·---
к     -·-
л     ·-··
м     --
н     -·
о     ---
п     ·--·
р     ·-·
с     ···
т     -
у     ··-
ф     ··-·
х     ····
ц     -·-·
ч     ---·
ш     ----
щ     --·-
ъ     --·--
ы     -·--
ь     -··-
э     ··-··
ю     ··--
я     ·-·-

---------------

Ukrainian
а     ·-
б     -···
в     ·--
г     --·
ґ     --·
д     -··
е     ·
є     ··-··
ж     ···-
з     --··
и     -·--
і     ··
ї     ·---·
й     ·---
к     -·-
л     ·-··
м     --
н     -·
о     ---
п     ·--·
р     ·-·
с     ···
т     -
у     ··-
ф     ··-·
х     ····
ц     -·-·
ч     ---·
ш     ----
щ     --·-
ь     -··-
ю     ··--
я     ·-·-

---------------

Numbers
0     -----
1     ·----
2     ··---
3     ···--
4     ····-
5     ·····
6     -····
7     --···
8     ---··
9     ----·

---------------

Special
.     ·-·-·-
,     --··--
!     -·-·--
?     ··--··
@     ·--·-·
/     -··-·
\     -··-·
&     ·-···
;     -·-·-·
:     ---···
"     ·-··-·
'     ·----·
$     ···-··-
+     ·-·-·
-     -····-
=     -···-
_     ··--·-

---------------
'''

		self.assertEqual(chart_output, expected_output)


if __name__ == '__main__':
	unittest.main()
