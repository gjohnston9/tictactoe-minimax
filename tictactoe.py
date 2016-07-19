class GameState(object):
	def __init__(self, new_turn, new_x_y, board=None, move_count=0, n=3):
		self.board = board or [[None, None, None], [None, None, None], [None, None, None]]
		self.new_turn = new_turn
		self.new_x_y = new_x_y
		self.move_count = move_count
		self.n = n
		self.move(new_turn, new_x_y)


	def move(self, new_turn, new_x_y):
		self.new_turn = new_turn
		self.new_x_y = new_x_y

		# make move
		self.board[new_x_y[1]][new_x_y[0]] = new_turn

		# reverse turns
		self.old_turn = new_turn
		self.new_turn = 'O' if new_turn == 'X' else 'X'

		# update move_count
		self.move_count += 1


	def __str__(self):
		ret = '\n'
		for y in range(self.n):
			for x in range(self.n):
				if y == self.new_x_y[1] and x == self.new_x_y[0]:
					ret += ' ({}) |'.format(self.board[y][x])
				else:
					ret += '  {}  |'.format(self.board[y][x] or ' ')
			# ret += '\n----------\n'
			ret = ret[:-1] + '\n-----------------\n'

		ret += '\nturn to move: {}'.format(self.new_turn)
		return ret


	def check_state(self):
		new_x = self.new_x_y[0]
		new_y = self.new_x_y[1]
		# check row
		for x in range(self.n):
			if self.board[new_y][x] != self.old_turn:
				break
		else:
			return self.old_turn

		# check column
		for y in range(self.n):
			if self.board[y][new_x] != self.old_turn:
				break
		else:
			return self.old_turn


		if (new_x == new_y):
			# check forward diagonal
			for z in range(self.n):
				if self.board[z][z] != self.old_turn:
					break
			else:
				return self.old_turn

		if (new_x == self.n - new_y - 1):
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


# testing
no_winner = GameState('O', (1,1), board=[['X', None, 'X'], ['O', None, None], ['O', None, None]])
print no_winner.check_state()
x = GameState('X', (0,2), board=[[None, None, 'X'], [None, 'X', None], [None, None, None]])
print x
print x.check_state()
draw = GameState('X', (0, 0), board=[[None, 'O', 'O'], ['O', 'X', 'X'], ['O', 'X', 'O']], move_count=8)
print draw
print draw.check_state()