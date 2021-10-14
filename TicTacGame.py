class TicTacGame():

    @staticmethod
    def hello_players():
        print('''Добро пожаловать в игру крестики-нолики!\n
        Традиционно первый ход остается за крестиками.\n
        Поле представляет собой девять ячеек, заполнив правильным образом три из которых,
        игрок побеждает.\n
        Для того, чтобы сделать ход необходимо ввести цифру ячейки поля:\n
          0  |  1  |  2
        -----|-----|-----
          3  |  4  |  5
        -----|-----|-----
          6  |  7  |  8
        ''')

    @staticmethod
    def question(question):
        return(input(question))

    @staticmethod
    def generate_board():
        return [' ' for _ in range(9)]

    def show_board(self):
        print('''
          {0}  |  {1}  |  {2}
        -----|-----|-----
          {3}  |  {4}  |  {5}
        -----|-----|-----
          {6}  |  {7}  |  {8}
        '''.format(*self.board))

    def choose_winner(self):
        WIN_COMB = ((0, 1, 2),
                    (3, 4, 5),
                    (6, 7, 8),
                    (0, 3, 6),
                    (1, 4, 7),
                    (2, 5, 8),
                    (0, 4, 8),
                    (2, 4, 6))
        for step in WIN_COMB:
            if self.board[step[0]] == self.board[step[1]] == self.board[step[2]] != self.SPACE:
                return self.board[step[0]]
        if self.SPACE not in self.board:
            return 'TIE'
        else:
            return 'Continue'

    def next_turn(self):
        if self.turn == 'X':
            return 'O'
        else:
            return'X'

    def start_game(self):
        self.show_board()
        while self.choose_winner() == 'Continue':
            self.right_move()
            self.turn = self.next_turn()
        self.congratulations_winner()

    def congratulations_winner(self):
        if self.choose_winner() == 'TIE':
            print('Поздравляем, ничья!')
        elif self.choose_winner() == self.player_one:
            print('Поздравляем, игрок 1 одержал победу!')
        else:
            print('Поздравляем, игрок 2 одержал победу!')
    def right_move(self):
        move = -1
        if self.turn == self.player_one:
            while move not in self.legal_moves:
                print('Введите число из данного диапазона:\n', *self.legal_moves)
                move = int(input('Игрок 1 введите ячейку поля для хода:\n'))
            self.legal_moves.remove(move)
            self.board[move] = self.player_one
            self.show_board()
        else:
            while move not in self.legal_moves:
                print('Введите число из данного диапазона:\n', *self.legal_moves)
                move = int(input('Игрок 2 введите ячейку поля для хода:\n'))
            self.board[move] = self.player_two
            self.legal_moves.remove(move)
            self.show_board()
    def __init__(self):
        TicTacGame.hello_players()
        self.turn = 'X'
        self.SPACE = ' '
        if input(('Игрок 1, вы хотите играть крестиками? Введите Y или N:\n')).lower() == 'y':
            self.player_one = 'X'
            self.player_two = 'O'
        else:
            self.player_one = 'O'
            self.player_two = 'X'
        self.board = TicTacGame.generate_board()
        self.legal_moves = list(range(9))
        self.start_game()

if __name__ == '__main__':
    game = TicTacGame()