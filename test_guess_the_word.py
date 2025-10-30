import random
import unittest
import importlib
import io
import sys
import builtins
from unittest import mock
import guess_the_word as game

class TestGuess(unittest.TestCase):
    # Test random module is picking from predefined list.
    def test_if_in_predefined_list(self):
        with mock.patch.object(random, "choice", lambda seq: seq[0]):
            # reload to run with "choice"
            importlib.reload(game)
        self.assertTrue(game.word_choice in game.random_word)

    # Test correct guesses diplay message.
    def test_correct_guesses(self):
        importlib.reload(game)
        game.word_choice = "roses"
        game.limit = 7
        game.guesses = []

        # Input what should be in list.
        input = ["r", "o", "s", "e", "s"]
        with mock.patch.object(builtins, "input", side_effect=input):
            x = io.StringIO()
            with mock.patch.object(sys, "stdout", x):
                game.guess_word()
        o = x.getvalue()

        self.assertTrue("Congratulations" in o)
        self.assertTrue("roses" in o)

    # Testing if exhausting wrong guesses will limit.
    def test_wrong_guesses(self):
        importlib.reload(game)
        game.word_choice = "road"
        game.limit = 7
        game.guesses = []

        # Test system is identifying wrong words.
        wrong_word = ["x", "y", "z", "q", "t"]
        with mock.patch.object(builtins, "input", side_effect=wrong_word):
            x = io.StringIO()
            with mock.patch.object(sys, "stdout", x):
                game.guess_word()
        o = x.getvalue()

        # Ensure messages are correct.
        self.assertTrue("Incorrect" in o)
        self.assertTrue("Game over" in o)


if __name__ == "__main__":
    unittest.main()
