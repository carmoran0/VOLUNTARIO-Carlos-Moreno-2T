# define a function to initialize the game board
def init_board():
  # create an empty 3x3 grid
  board = [[' ' for _ in range(3)] for _ in range(3)]
  return board

# define a function to print the game board
def print_board(board):
  # print the top row of column indices
  print("  0 1 2")

  # print each row of the board
  for i, row in enumerate(board):
    # print the row number and each cell in the row
    print(i, " ".join(row))

# define a function to get the player's move
def get_move(player):
  # prompt the player for their move
  move = input(f"Player {player}, enter your move (row column): ")

  # split the move into the row and column indices
  row, col = move.split()

  # return the move as a tuple of ints
  return int(row), int(col)

# define a function to update the game board with a move
def make_move(board, player, move):
  # unpack the row and column indices from the move tuple
  row, col = move

  # update the board with the player's move
  board[row][col] = player

# define the main game loop
def tic_tac_toe():
  # initialize the game board
  board = init_board()

  # initialize the current player
  player = 'X'

  # run the game until it is over
  while True:
    # print the game board
    print_board(board)

    # get the player's move
    move = get_move(player)

    # make the move on the game board
    make_move(board, player, move)

    # check if the game is over
    if player_wins(board, player):
      # print the game board one last time
      print_board(board)

      # print a message to the player
      print(f"Player {player} wins!")
      break

    # switch to the other player
    player = 'O' if player == 'X' else 'X'

# define a function to check if a player has won the game
def player_wins(board, player):
  # check the rows
  for row in board:
    if row == [player, player, player]:
      return True

  # check the columns
  for col in range(3):
    if (board[0][col] == player and
        board[1][col] == player and
        board[2][col] == player):
      return True

  # check the diagonals
  if (board[0][0] == player and
      board[1][1] == player and
      board[2][2] == player):
    return True

  if (board[0][2] == player and
      board[1][1] == player and
      board[2][0] == player):
    return True

  # if none of the above conditions are met, the player has not won
  return False

# run the game
tic_tac_toe()
