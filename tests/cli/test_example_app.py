"""CLI tests for example_app."""

from example_app.utils import test

class CliTestCase(test.example_TestCase):
    def test_example_app_cli(self):
        self.app.setup()
        self.app.run()
        self.app.close()
