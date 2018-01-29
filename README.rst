logs: logging made simple
=========================

I usually find it simple enough to log stuff in Python, using the **logging** module.
But when it comes to doing it properly with loggers, I often go back and forth between code and the **logging** module's documentation.

**logs** is an attempt to make it more fluent (in my opinion) to log stuff in Python code.

.. code-block:: python

   >>> from logs import Log
   >>> my_logs = Log('my_logs', level='DEBUG')
   >>> mylogs.add_file_handler('/tmp/default.log', level='INFO')

This piece of code means exactly what is written:

 - create a log system called **my_logs** with a default logger to stdout with level **logging.DEBUG**
 - add another logger to that log system, that will log to a file with level **logging.INFO**

The default format of logs is [%(asctime)s] [%(levelname)s] [%(name)s] [%(funcName)s] %(message)s

Re-using that log system, we have

.. code-block:: python

   >>> mylogs.logger.debug("This message will appear only on stdout")
   [2018-01-01 08:00:00 +0300] [DEBUG] [my_logs] [<module>] This message will appear only on stdout

   
And,
.. code-block:: python

   >>> mylogs.logger.info("This message will appear both on stdout and in /tmp/default.log")
   [2018-01-01 08:02:00 +0300] [INFO] [my_logs] [<module>] This message will appear both on stdout and in /tmp/default.log

.. code-block:: shell

   $ cat /tmp/default.log
   [2018-01-01 08:02:00 +0300] [INFO] [my_logs] [<module>] This message will appear both on stdout and in /tmp/default.log
