import logging

logging_format = '%(levelname)s - %(message)s'
logging_colors = {
	logging.DEBUG: '\033[37m',  # White
	logging.INFO: '\033[34m',  # Blue
	logging.WARNING: '\033[33m',  # Yellow
	logging.ERROR: '\033[31m',  # Red
	logging.CRITICAL: '\033[1;31m'  # Bold Red
}


class ColoredFormatter(logging.Formatter):
	"""
	A custom log formatter that adds color to log messages based on their severity.
	"""

	def format(self, record: logging.LogRecord) -> str:
		record.log_color = logging_colors.get(record.levelno, '\033[0m')

		return super().format(record)


def setup_logging(level: int) -> None:
	"""
	Set up colored console logging with the specified logging level.

	:parameter level: The logging level (e.g., logging.DEBUG, logging.INFO) to set for the root logger.

	:returns: None
	"""

	# Setup StreamHandler
	handler = logging.StreamHandler()
	handler.setFormatter(ColoredFormatter('%(log_color)s' + logging_format + '\033[0m'))

	# Basic configuration of logging, setting the level and handler
	logging.basicConfig(level=level, handlers=[handler])
