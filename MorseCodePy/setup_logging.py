import logging
from typing import Dict, Optional


class ColoredFormatter(logging.Formatter):
	def format(self, record: logging.LogRecord) -> str:
		colors: Dict[int, str] = {
			logging.DEBUG: '\033[37m',  # White
			logging.INFO: '\033[34m',  # Blue
			logging.WARNING: '\033[33m',  # Yellow
			logging.ERROR: '\033[31m',  # Red
			logging.CRITICAL: '\033[1;31m'  # Bold Red
		}
		record.log_color = colors.get(record.levelno, '\033[0m')

		return super().format(record)


def setup_logging(level: int = logging.INFO, logging_format: Optional[str] = '[%(levelname)s] - %(message)s') -> None:
	"""
	Set up colored console logging with the specified logging level.

	:parameter level: The logging level (e.g., logging.DEBUG, logging.INFO) to set for the root logger (default is logging.INFO).
	:parameter logging_format: The format that will be used when using logging.

	:returns: `None`
	"""

	# Setup StreamHandler
	handler = logging.StreamHandler()
	handler.setFormatter(ColoredFormatter('%(log_color)s' + logging_format + '\033[0m'))

	# Basic configuration of logging, setting the level and handler
	logging.basicConfig(level=level, handlers=[handler])
