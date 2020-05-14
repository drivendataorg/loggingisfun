# Loggingisfun

A simple example of one way to organize logging across a Python package.

1. A "package logger" that is instantiated using `logging.getLogger(__package__)` during the call to the package `__init__.py`. The name of this logger is the package name, e.g., `loggingisfun`. Set the log level using an environmental variable, e.g., `LOGGINGISFUN_LOG_LEVEL=DEBUG`. Register a `StreamHandler` to print logs to the console.
2. Each package module gets its own "module logger" using `logger = logging.getLogger(__name__)` at the top of the module. The names of these loggers will contain the package hierarchy, e.g., `loggingisfun.wizard`. Logs within the module are issued from this logger, e.g. `logger.info("A message")`. Because `logging` tracks the logger hierarchy using the logger names, (i.e., it knows that `loggingisfun.wizard` descends from `loggingisfun`), these module loggers will be children of the package logger, and they will be emitted using the log level of the package logger.
3. Use of `logging.basicConfig` depends on whether you are writing an application (end-user code) or a library (code that is imported by an application). Library code **should not** use `logging.basicConfig`, as it sets up a handler on the root logger that will result in duplicate logs. See `01-script.py` for an example of what happens when an evil `demon.py` curses the root logger.
4. If another library has cursed the root logger with `basicConfig`, you can fix it by telling your package logger to not propagate messages to the root logger with: `logger.propagate = False`.

Have fun logging!
