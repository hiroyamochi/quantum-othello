import random

class Othello:
  def __init__(self, size):
    self.size = size
    self.board = [[' ' for _ in range(size)] for _ in range(size)]
    mid = size // 2
    self.board[mid-1][mid-1] = 'O'
    self.board[mid-1][mid] = 'X'
    self.board[mid][mid-1] = 'X'
    self.board[mid][mid] = 'O'
    self.current_player = 'X'

  def print_board(self):
    print('   ' + ' '.join(str(i) for i in range(self.size)))
    print('  ' + '-' * (2 * self.size + 1))
    for i, row in enumerate(self.board):
      print(f'{i}| {" ".join(row)} |')
    print('  ' + '-' * (2 * self.size + 1))

  # そこに石を置くことができるかを確認
  def is_valid_move(self, row, col):
    # col, rowがボードの範囲内であることを確認
    if not (0 <= row < self.size and 0 <= col < self.size):
      return False
    
    # すでに石が置かれている場所は除外
    if self.board[row][col] != ' ':
      return False
    
    # 8方向に対して、相手の石があるかを確認
    for dr, dc in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
      r, c = row + dr, col + dc
      if 0 <= r < self.size and 0 <= c < self.size and self.board[r][c] == self.opponent():
        # その方向に対して、空白があるまで数えていく
        while 0 <= r < self.size and 0 <= c < self.size and self.board[r][c] != ' ':
          r += dr
          c += dc
          # 自分の石があれば挟めるのでTrueを返す         
          if 0 <= r < self.size and 0 <= c < self.size and self.board[r][c] == self.current_player:
            return True
    return False

  def make_move(self, row, col):
    if self.is_valid_move(row, col):
      self.board[row][col] = self.current_player
      for dr, dc in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
        r, c = row + dr, col + dc
        if 0 <= r < self.size and 0 <= c < self.size and self.board[r][c] == self.opponent():
          to_flip = []
          while 0 <= r < self.size and 0 <= c < self.size and self.board[r][c] != ' ':
            to_flip.append((r, c))
            r += dr
            c += dc
            if 0 <= r < self.size and 0 <= c < self.size and self.board[r][c] == self.current_player:
              for flip_r, flip_c in to_flip:
                self.board[flip_r][flip_c] = self.current_player
              break
      self.current_player = self.opponent()

  def opponent(self):
    return 'O' if self.current_player == 'X' else 'X'

  def game_over(self):
    for row in self.board:
      if ' ' in row:
        return False
    return True
  
  # 量子力学的な要素を追加
  # 70%の確率で石が裏返る
  def schroedinger(self):
    for row in range(self.size):
      for col in range(self.size):
        if self.board[row][col] != ' ':
          if random.random() < 0.7:
            self.board[row][col] = self.opponent()

  def count_score(self):
    count_x = sum(row.count('X') for row in self.board)
    count_o = sum(row.count('O') for row in self.board)
    return count_x, count_o
  
  def result(self):
    print('ゲーム終了!')
    othello.print_board()

    print('シュレディンガーの猫がボードを通過しました...')
    othello.schroedinger()

    print('最終結果:')
    othello.print_board()

    count_x, count_o = othello.count_score()
    print(f'X: {count_x}、O: {count_o}')
    if count_x > count_o:
        print('Xの勝利です!')
    elif count_x < count_o:
        print('Oの勝利です!')
    else:
        print('引き分けです！')

# ゲームのメイン部分
size = input('ボードのサイズを入力してください (4-16): ')
if int(size) < 4 or int(size) > 16:
    print('サイズが無効です。デフォルトのサイズ8を使用します。')
    size = 8
othello = Othello(int(size))
while True:
    othello.print_board()
    print('-----------------------------------')
    print(f'{othello.current_player}のターンです。')

    # 有効な手があるかを確認
    valid_moves_available = False
    for row in range(8):
        for col in range(8):
            if othello.is_valid_move(row, col):
                valid_moves_available = True
                break
        if valid_moves_available: # 1列ごとに有効な手があればループを抜ける
            break
    if not valid_moves_available:
        print(f'{othello.current_player}の手がありません。パスします。')
        break
    
    # 入力を受け取る
    while True:
        try:
            row = int(input('行を選択してください (0-7): '))
            col = int(input('列を選択してください (0-7): '))
            if othello.is_valid_move(row, col):
                othello.make_move(row, col)
                break
            else:
                print('無効な動きです。再試行してください。')
        except ValueError:
            print('整数を入力してください。')

# ゲーム終了
othello.result()