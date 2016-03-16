"""Testing utilities for example_app."""

from example_app.cli.main import example_TestApp
from cement.utils.test import *

class example_TestCase(CementTestCase):
    app_class = example_TestApp

    def setUp(self):
        """Override setup actions (for every test)."""
        super(example_TestCase, self).setUp()

    def tearDown(self):
        """Override teardown actions (for every test)."""
        super(example_TestCase, self).tearDown()

