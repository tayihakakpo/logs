#!/usr/bin/env python
# encoding: utf-8


import logging


__version__ = '1.0'


__all__ = [
    '__version__',
    'Log'
    ]


FORMAT = '[%(asctime)s] [%(levelname)s] [%(name)s] [%(funcName)s] %(message)s'
DATEFORMAT = '%Y-%m-%d %H:%M:%S %z'


class Log(object):
    """Represents a log system
    with a logger and potentially multiple handlers
    """

    def __init__(self, name, level=None, fmt=None, datefmt=None):
        """Create a logger with a default handler to stream to stdout"""

        logger = logging.getLogger(name)
        fmt = fmt or FORMAT
        datefmt = datefmt or DATEFORMAT
        formatter = logging.Formatter(fmt=fmt, datefmt=datefmt)
        level = Log.level(level)
        logger.setLevel(level)
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(level)
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

        self.logger = logger

    def __configure_handler__(self, handler, **kwargs):
        """Given a handler, configure its level and format"""

        level = Log.level(kwargs.get('level'))
        fmt = kwargs.get('fmt', FORMAT)
        datefmt = kwargs.get('datefmt', DATEFORMAT)
        formatter = logging.Formatter(fmt=fmt, datefmt=datefmt)
        handler.setLevel(level)
        handler.setFormatter(formatter)
        return handler

    @staticmethod
    def level(name=None):
        """Return a logging.name object where "name" is the log level"""

        name = name or 'DEBUG'
        try:
            level = getattr(logging, name)
        except AttributeError:
            raise ValueError('Niveau de log inconnu: "{}"'.format(name))
        else:
            return level

    def add_file_handler(self, filename, **kwargs):
        """Add a FileHandler"""

        handler = logging.FileHandler(filename=filename)
        handler = self.__configure_handler__(handler, **kwargs)
        self.logger.addHandler(handler)

    def set_file_handler(self, filename, **kwargs):
        """Set a FileHandler as the default and only handler for this logger"""

        handler = logging.FileHandler(filename=filename)
        handler = self.__configure_handler__(handler, **kwargs)
        self.logger.handlers = [handler]

# EOF
