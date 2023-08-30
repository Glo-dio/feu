import sys

# fonctions utilisées
def board_file_to_array(filename):
  try:
    with open(filename, "r") as file:
      return [line.strip('\n') for line in file.readlines()]
  except:
    sys.exit(f"Error : \033[33;1m{filename}\033[00m can't be open")

def convert_str_tab_to_int_tab(board):
  output = []
  tmp = []
  for i in range(len(board)):
    for j in range(len(board[i])):
      if board[i][j] == '.':
        tmp.append(0)
      else:
        tmp.append(int(board[i][j]))
    output.append(tmp)
    tmp = []
  return output

def is_correct_line(line_of_board):
  for counted_num in range(1, 10):
    if line_of_board.count(counted_num) > 1:
      # print(f"{counted_num} is present {line_of_board.count(counted_num)} time")
      return False
  return True

def is_correct_board(board):
  # for row
  for i in board:
    if is_correct_line(i) == False:
      sys.exit("Error : one row on board isn't correct")

  # for column
  column = []
  tmp = []
  for j in range(0,9):
    for i in range(0,9):
      tmp.append(board[i][j])
    column.append(tmp)
    tmp = []

  for i in column:
    if is_correct_line(i) == False:
      sys.exit("Error : one colomn on board isn't correct")

def print_board_with_borders(board):
  for row in range(len(board)):
    if row % 3 == 0 and row != 0:
      print("-" * 10)

    for column in range(len(board[0])):
      if column % 3 == 0 and column != 0:
        print(" | ", end="")

      if column == len(board) - 1:
        print(board[row][column])
      else:
        print(str(board[row][column]) + " ", end="")

def print_board(board):
  output = []
  for line in board:
    output.append(''.join(str(text_on_line) for text_on_line in line))
  
  for line in output:
    print(line)

def find_empty_case(board):
  for row in range(len(board)):
    for column in range(len(board[row])):
      if board[row][column] == 0:
        return (row, column)
  return None

def check_number(board, test_number, position):
  y = position[0] # result of find_empty_case()
  x = position[1] # result of find_empty_case()
  
  # check row
  for column in range(len(board)):
    if board[y][column] == test_number and x != column:
      return False

  # check column
  for row in range(len(board[0])):
    if board[row][x] == test_number and y != row:
      return False

  # check box
  box_y = y // 3
  box_x = x // 3

  for row in range(box_y * 3, box_y * 3 + 3):
    for column in range(box_x * 3, box_x * 3 + 3):
      if board[row][column] == test_number and (row, column) != position:
        return False
  return True

def solve(board):
  find = find_empty_case(board)
  if not find:
    return True
  else:
    row, column = find  # get position of empty case

  for number in range(1, 10):
    if check_number(board, number, (row, column)):
      board[row][column] = number
      if solve(board):
        return True
      board[row][column] = 0
  return False

# Partie 1 : Gestion d'erreur

# Partie 2 : Parsing
board = board_file_to_array(sys.argv[1]) #convert file to list of board : 1 line on file equal 1 line on the list
board = convert_str_tab_to_int_tab(board) #convert list of strings to list of integers (change '.' to 0)

# Partie 3 : Résolution
is_correct_board(board)
solve(board)
print_board(board)

# Partie 4 : Affichage