import unittest
from card import Card
from card import Door
from card import Labyrinth

class TestCards(unittest.TestCase):
    def test_card(self):
        c = Card('Nightmare')
        self.assertEqual(c.get(), '{\'type\': \'Nightmare\'}')

if __name__ == '__main__':
    unittest.main()