class NoMoveMadeException(Exception):
	pass

class GameState(object):
	def __init__(self, board, turn, move_count=0):
		self.board = board
		self.turn = turn
		self.move_count = move_count

		assert len(board) == len(board[0])
		self.n = len(board)

		# Once a move is made, these will record the x and y index of the move most recently made on the board,
		# as well as whose turn it was when the move was made.
		self.x = None
		self.y = None
		self.old_turn = None


	def switch_turn(self):
		self.turn = 'X' if self.turn == 'O' else 'O'


	def move(self, x, y):
		# record move (for quick checking of win/loss/draw)
		self.x = x
		self.y = y
		self.old_turn = self.turn

		# make move and switch turn
		self.board[y][x] = self.turn
		self.switch_turn()

		# update move_count
		self.move_count += 1


	def __str__(self):
		ret = '\n'
		for y in range(self.n):
			for x in range(self.n):
				if y == self.y and x == self.x:
					ret += ' ({}) |'.format(self.board[y][x])
				else:
					ret += '  {}  |'.format(self.board[y][x] or ' ')
			ret = ret[:-1] + '\n-----------------\n'

		try:
			result = self.check_winner()
			if result in ('X', 'O'):
				ret += '\nWinner: {}'.format(result)
			elif result == 'draw':
				ret += '\nThe game is a draw.'
			else: # no winner yet
				ret += '\nTurn to move: {}'.format(self.turn)
		except NoMoveMadeException:
			ret += '\nTurn to move: {}'.format(self.turn)

		return ret


	def check_winner(self):
		if self.x == None or self.y == None or self.old_turn == None:
			raise NoMoveMadeException("called check_state without making a move first")

		# check row
		for x in range(self.n):
			if self.board[self.y][x] != self.old_turn:
				break
		else:
			return self.old_turn

		# check column
		for y in range(self.n):
			if self.board[y][self.x] != self.old_turn:
				break
		else:
			return self.old_turn


		if (self.x == self.y):
			# check forward diagonal
			for z in range(self.n):
				if self.board[z][z] != self.old_turn:
					break
			else:
				return self.old_turn

		if (self.x == self.n - self.y - 1):
			# check backward diagonal
			for y in range(self.n):
				if self.board[y][self.n - y - 1] != self.old_turn:
					break
			else:
				return self.old_turn

		if self.move_count == self.n ** 2:
			return 'draw'

		return None



	def next_states(self):
		raise NotImplementedError