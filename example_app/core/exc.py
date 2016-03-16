"""example_app exception classes."""

class example_Error(Exception):
    """Generic errors."""
    def __init__(self, msg):
        Exception.__init__(self)
        self.msg = msg

    def __str__(self):
        return self.msg

class example_ConfigError(example_Error):
    """Config related errors."""
    pass

class example_RuntimeError(example_Error):
    """Generic runtime errors."""
    pass

class example_ArgumentError(example_Error):
    """Argument related errors."""
    pass
