import unittest

from tictactoe import GameState, GameDriver

class Test(unittest.TestCase):

	# @unittest.skip("")
	def test_no_winner_yet(self):
		no_winner_yet = GameState([["X", None, "X"], ["O", None, None], ["O", None, None]], "O")
		no_winner_yet.move(1,1)
		self.assertEqual(no_winner_yet.check_winner(), None)

		next = no_winner_yet.next_states_and_moves()
		self.assertEqual(len(next), 4)
		
		self.assertEqual(next[0][0].check_winner(), "X")
		self.assertEqual(next[1][0].check_winner(), None)
		self.assertEqual(next[2][0].check_winner(), None)
		self.assertEqual(next[3][0].check_winner(), None)

	# @unittest.skip("")
	def test_row_wins(self):
		one = GameState([["O", "O", "O"], [None, None, None], [None, None, None]], "X")
		two = GameState([[None, None, None], ["O", "O", "O"], [None, None, None]], "X")
		three = GameState([[None, None, None], [None, None, None], ["O", "O", "O"]], "X")
		for game in (one, two, three):
			self.assertEqual(game.check_winner(), "O")

	# @unittest.skip("")
	def test_column_wins(self):
		one = GameState([["X", None, None], ["X", None, None], ["X", None, None]], "X")
		two = GameState([[None, "X", None], [None, "X", None], [None, "X", None]], "X")
		three = GameState([[None, None, "X"], [None, None, "X"], [None, None, "X"]], "X")
		for game in (one, two, three):
			self.assertEqual(game.check_winner(), "X")

	# @unittest.skip("")
	def test_draw(self):
		draw = GameState([[None, "O", "O"], ["O", "X", "X"], ["O", "X", "O"]], "X", move_count=8)
		draw.move(0,0)
		self.assertEqual(draw.check_winner(), "draw")

	# @unittest.skip("")
	def test_diagonal_wins(self):
		fwd = GameState([["X", None, None], [None, "X", None], [None, None, "X"]], "X")
		self.assertEqual(fwd.check_winner(), "X")
		bkwd = GameState([[None, None, "O"], [None, "O", None], ["O", None, None]], "X")
		self.assertEqual(bkwd.check_winner(), "O")

	@unittest.skip("")
	def test_PlayGame(self):
		self.assertIsNotNone(GameDriver())

if __name__ == "__main__":
	unittest.main()