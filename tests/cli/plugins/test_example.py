"""Tests for Example Plugin."""

from example_app.utils import test

class ExamplePluginTestCase(test.example_TestCase):
    def test_load_example_plugin(self):
        self.app.setup()
        self.app.plugin.load_plugin('example')
