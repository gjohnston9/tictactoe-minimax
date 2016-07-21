class NoMoveMadeException(Exception):
	pass

class IllegalMoveException(Exception):
	pass


def new_copy(in_list):
		if isinstance(in_list, list):
			return list(map(new_copy, in_list))
		else:
			return in_list

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
		if self.board[y][x] != None:
			raise IllegalMoveException("there is already a symbol placed at this location (x = {}, y = {})".format(x, y))
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
		states = []
		for y in range(self.n):
			for x in range(self.n):
				if self.board[y][x] == None:
					new_state = GameState(new_copy(self.board), self.turn, move_count=self.move_count)
					new_state.move(x, y)
					states.append(new_state)
		return states


def GameDriver(object):
	def __init__(self):
		symbol = raw_input("Choose your symbol. X/O")
		while symbol != 'X' and symbol != 'O':
			symbol = raw_input("Could not understand your answer. Please enter X or O.")

		self.player_symbol = symbol

		first = raw_input("Would you like to start? Y/N")
		while first != 'Y' and first != 'N':
			first = raw_input("Could not understand your answer. Please enter Y or N.")

		if first == 'Y':
			self.game = GameState([[None, None, None], [None, None, None], [None, None, None]], self.player_symbol)
		else:
			self.game = GameState([[None, None, None], [None, None, None], [None, None, None]], 'X' if self.player_symbol == 'O' else 'O')

		self.start()

	def player_move(self):
		raise NotImplementedError

	def computer_move(self):
		raise NotImplementedError

	def start():
		raise NotImplementedError