#!/usr/bin/python3
""" Unitest test console """
import unittest
import pycodestyle


class TestConsole(unittest.TestCase):
    """ Test HBNBCommand class """

    def test_pycodestyle(self):
        """Test that the code conforms to pycodestyle"""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_quit_command(self):
        """Test the quit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd('quit')
            output = f.getvalue().strip()
            self.assertEqual(output, '')
