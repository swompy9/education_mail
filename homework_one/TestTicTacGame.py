import unittest
from TicTacGame import TicTacGame

class TestTicTacGame(unittest.TestCase):
    def test_choose_winner(self):
        self.assertEqual(TicTacGame.choose_winner(['X', 'O', 'X', 'X', 'O', 'O', 'O', 'X', 'X']), 'TIE')
        self.assertEqual(TicTacGame.choose_winner(['X', 'O', 'O', 'X', 'O', ' ', 'X', ' ', ' ']), 'X')
        self.assertEqual(TicTacGame.choose_winner(['O', ' ', 'X', 'O', 'X', ' ', 'O', ' ', 'X']), 'O')
        self.assertEqual(TicTacGame.choose_winner(['O', 'X', 'O', 'X', 'X', 'O', 'X', 'O', 'X']), 'TIE')
        self.assertEqual(TicTacGame.choose_winner(['O', 'O', 'X', 'X', 'X', 'O', 'X', 'O', ' ']), 'X')
        self.assertEqual(TicTacGame.choose_winner(['O', 'O', 'O', 'X', 'X', 'O', 'X', 'X', ' ']), 'O')
    def test_next_turn(self):
        self.assertEqual(TicTacGame.next_turn('X'), 'O')
        self.assertEqual(TicTacGame.next_turn('O'), 'X')
    def test_check_legal_moves(self):
        self.assertEqual(TicTacGame.check_legal_moves(['O', 'X', 'O', 'X', 'X', ' ', ' ', 'O', ' ']), [5, 6, 8])
        self.assertEqual(TicTacGame.check_legal_moves(['X', 'O', 'X', ' ', 'O', ' ', ' ', 'X', ' ']), [3, 5, 6, 8])
        self.assertEqual(TicTacGame.check_legal_moves(['X', 'O', 'X', 'X', 'O', 'O', ' ', 'X', 'O']), [6])
        self.assertEqual(TicTacGame.check_legal_moves(['O', ' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ']), [1, 2, 3, 5, 6, 7, 8])
        self.assertEqual(TicTacGame.check_legal_moves(['O', ' ', 'O', ' ', ' ', ' ', 'X', ' ', 'X']), [1, 3, 4, 5, 7])
        self.assertEqual(TicTacGame.check_legal_moves(['O', 'X', 'O', 'O', 'X', 'O', 'X', 'O', 'X']), [])
    def test_validate_input(self):
        with self.assertRaises(ValueError):
            TicTacGame.validate_input('Start', [' ']*9)
            TicTacGame.validate_input('Yes', [' ']*9)
            TicTacGame.validate_input('1', [' ']*9)
            TicTacGame.validate_input(10, [' ']*9)
            TicTacGame.validate_input(9, [' ']*9)
            TicTacGame.validate_input(-1, [' ']*9)

if __name__ == '__main__':
    unittest.main()
