"""example_app bootstrapping."""

# All built-in application controllers should be imported, and registered
# in this file in the same way as example_BaseController.

from cement.core import handler
from example_app.cli.controllers.base import example_BaseController

def load(app):
    handler.register(example_BaseController)
