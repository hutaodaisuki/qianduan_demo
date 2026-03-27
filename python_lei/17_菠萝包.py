import os

class GobangGame:
    def __init__(self, board_size=15):
        self.board_size = board_size
        self.board = [[0 for _ in range(board_size)] for _ in range(board_size)]
        self.current_player = 1  # 1 表示黑棋，2 表示白棋
        self.game_over = False
        self.winner = 0

    def print_board(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('  ', end='')
        for i in range(self.board_size):
            print(f'{i:2d}', end='')
        print()
        for i in range(self.board_size):
            print(f'{i:2d}', end='')
            for j in range(self.board_size):
                if self.board[i][j] == 0:
                    print(' ·', end='')
                elif self.board[i][j] == 1:
                    print(' ●', end='')
                else:
                    print(' ○', end='')
            print()

    def is_valid_move(self, row, col):
        return 0 <= row < self.board_size and 0 <= col < self.board_size and self.board[row][col] == 0

    def make_move(self, row, col):
        if not self.is_valid_move(row, col):
            return False
        self.board[row][col] = self.current_player
        self.check_winner(row, col)
        self.current_player = 2 if self.current_player == 1 else 1
        return True

    def check_winner(self, row, col):
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        player = self.board[row][col]

        for dr, dc in directions:
            count = 1

            # 正方向检查
            for i in range(1, 5):
                r, c = row + dr * i, col + dc * i
                if 0 <= r < self.board_size and 0 <= c < self.board_size and self.board[r][c] == player:
                    count += 1
                else:
                    break

            # 反方向检查
            for i in range(1, 5):
                r, c = row - dr * i, col - dc * i
                if 0 <= r < self.board_size and 0 <= c < self.board_size and self.board[r][c] == player:
                    count += 1
                else:
                    break

            if count >= 5:
                self.game_over = True
                self.winner = player
                return

    def get_move(self):
        while True:
            try:
                move = input(f"玩家 {'黑' if self.current_player == 1 else '白'} 的回合，请输入行和列（例如：3 5）：").strip()
                if move.lower() == 'q':
                    return None, None
                row, col = map(int, move.split())
                return row, col
            except (ValueError, IndexError):
                print("输入无效，请输入两个整数，用空格分隔。")

    def play(self):
        while not self.game_over:
            self.print_board()
            row, col = self.get_move()
            if row is None:
                print("游戏已退出。")
                return
            if not self.make_move(row, col):
                print("无效的移动，请选择其他位置。")

        self.print_board()
        if self.winner == 1:
            print("黑棋获胜！")
        else:
            print("白棋获胜！")

if __name__ == "__main__":
    game = GobangGame()
    game.play()