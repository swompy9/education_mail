class TicTacGame():

    def __init__(self):
        TicTacGame.hello_players()
        self.turn = self.check_first_turn()
        self.board = TicTacGame.generate_board()
        self.legal_moves = list(range(9))

    def check_first_turn(self):
        player_one = input('Игрок 1, представьтесь: ')
        player_two = input('Игрок 2, представьтесь: ')
        if input('Игрок 1,хотите взять "X"? Ввод Y или N:\n').lower() == 'y':
            self.player_one = ('X', player_one)
            self.player_two = ('O', player_two)
            return self.player_one[0]
        else:
            self.player_one = ('O', player_one)
            self.player_two = ('X', player_two)
            return self.player_two[0]

    @staticmethod
    def hello_players():
        print('''Добро пожаловать в игру крестики-нолики!\n
        Традиционно первый ход остается за крестиками.\n
        Поле представляет собой девять ячеек, заполнив три верных,
        игрок побеждает.\n
        Для того, чтобы сделать ход необходимо ввести цифру ячейки поля:\n
          0  |  1  |  2
        -----|-----|-----
          3  |  4  |  5
        -----|-----|-----
          6  |  7  |  8
        ''')

    @staticmethod
    def generate_board():
        return [' ' for _ in range(9)]

    @staticmethod
    def show_board(board):
        print('''
          {0}  |  {1}  |  {2}
        -----|-----|-----
          {3}  |  {4}  |  {5}
        -----|-----|-----
          {6}  |  {7}  |  {8}
        '''.format(*board))

    @staticmethod
    def choose_winner(board):
        WIN_COMB = ((0, 1, 2),
                    (3, 4, 5),
                    (6, 7, 8),
                    (0, 3, 6),
                    (1, 4, 7),
                    (2, 5, 8),
                    (0, 4, 8),
                    (2, 4, 6))
        for step in WIN_COMB:
            if board[step[0]] == board[step[1]] == board[step[2]] != ' ':
                return board[step[0]]
        if ' ' not in board:
            return 'TIE'
        else:
            return 'Continue'

    @staticmethod
    def next_turn(turn):
        if turn == 'X':
            return 'O'
        else:
            return 'X'

    def congratulations_winner(self):
        if TicTacGame.choose_winner(self.board) == 'TIE':
            print('Поздравляем, ничья!')
        elif TicTacGame.choose_winner(self.board) == self.player_one[0]:
            print('Поздравляем,', self.player_one[1], 'одержал победу!')
        else:
            print('Поздравляем,', self.player_two[1], 'одержал победу!')

    @staticmethod
    def check_legal_moves(board):
        return [i for i in range(9) if board[i] == ' ']

    @staticmethod
    def validate_input(value, board):
        try:
            value = int(value)
        except TypeError:
            raise TypeError
        if value not in TicTacGame.check_legal_moves(board):
            raise ValueError
        else:
            return value

    def start_game(self):
        TicTacGame.show_board(self.board)
        while TicTacGame.choose_winner(self.board) == 'Continue':
            if self.player_one == self.turn:
                print(self.player_one[1], '- ваш ход!')
            else:
                print(self.player_two[1], '- ваш ход!')
            print('Доступны:\n', *TicTacGame.check_legal_moves(self.board))
            try:
                move = TicTacGame.validate_input(input(), self.board)
            except ValueError:
                print('Введите числа из диапазона!\n')
                continue
            except TypeError:
                print('Неккоректный ввод числа!\n')
                continue
            else:
                self.legal_moves.remove(move)
                self.board[move] = self.turn
                TicTacGame.show_board(self.board)
            self.turn = TicTacGame.next_turn(self.turn)
        self.congratulations_winner()


if __name__ == '__main__':
    game = TicTacGame()
    game.start_game()
