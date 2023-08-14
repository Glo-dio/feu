import sys

corner_logo = "o"
height_logo = "|" # y --> heuteur
widht_logo = "-" # x --> largeur

# fonctions utilisées
def first_or_last_line(columns_number):
  global corner_logo
  global widht_logo
  line = []
  line.append(corner_logo)
  if columns_number > 1:
    for number in range(1, columns_number - 1):
      line.append(widht_logo)
    line.append(corner_logo)
  line = str(''.join(line))
  print(line)
  return line

def middle_line(columns_number, rows_number):
  global height_logo
  line = []
  tmp = []
  if columns_number > 1:
    for rows in range(1, rows_number - 1):
      tmp.append(height_logo)
      for inside_rows in range(1, columns_number - 1):
        tmp.append(" ")
      tmp.append(height_logo)
      line.append("".join(tmp))
      tmp = []
  for i in line: 
    print(i)
  return line

def args_is_digit(args):
  for i in args:
    if i.isdigit() == False:
      return False

def is_arg_valid():
  if is_nb_arg_correct == False:
    return False
  if args_is_digit(sys.argv[1:]) == False:
    return False
  if int(sys.argv[1]) < 1 or int(sys.argv[2]) < 1:
    return False

# Partie 1 : Gestion d'erreur
is_nb_arg_correct = len(sys.argv) == 3

if is_arg_valid() == False:
  sys.exit("error")


# Partie 2 : Parsing
columns = int(sys.argv[1])
rows = int(sys.argv[2])


# Partie 3 : Résolution
def make_rectangle(columns, rows):
  first_or_last_line(columns)
  if rows > 1:
    middle_line(columns,rows)
    first_or_last_line(columns)

# Partie 4 : Affichage
make_rectangle(columns, rows)
