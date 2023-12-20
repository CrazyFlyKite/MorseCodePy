from setuptools import setup, find_packages

__project_name__ = 'MorseCodePy'
__project_page__ = 'https://github.com/CrazyFlyKite/MorseCodePy'
__project_version__ = '3.5'
__license__ = 'MIT'
__author__ = 'CrazyFlyKite'
__email__ = 'karpenkoartem2846@gmail.com'
__install_requires__ = ['pygame']
__package_data__ = {'MorseCodePy': ['sounds/*.wav']}
__description__ = 'Encode, decode & play Morse code easily'
__classifiers__ = [
	'Intended Audience :: Developers',
	'License :: OSI Approved :: MIT License',
	'Programming Language :: Python :: 3.10',
	'Programming Language :: Python :: 3.11',
	'Programming Language :: Python :: 3.12',
	'Programming Language :: Python :: 3.13',
	'Topic :: Utilities'
]

with open('README.md', 'r', encoding='utf-8') as readme:
	__documentation__ = readme.read()

if __name__ == '__main__':
	setup(
		name=__project_name__,
		url=__project_page__,
		version=__project_version__,
		author=__author__,
		author_email=__email__,
		license=__license__,
		description=__description__,
		long_description=__documentation__,
		long_description_content_type='text/markdown',
		install_requires=__install_requires__,
		packages=find_packages(),
		include_package_data=True,
		package_data=__package_data__,
		classifiers=__classifiers__
	)
