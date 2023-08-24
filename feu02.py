import sys

# fonctions utilisées
def sentences(result):
  if result == 1:
    print("Trouvé !")
    print("Coordonnées : X,Y")
    # print(to_find_schema) #TODO à faire
  else:
    sys.exit("Introuvable")

def rows_file_transformed_into_table(name):
  file = open(name, "r")
  tab_file_line_by_line = []
  with file as lines:
    lines = file.readlines()
  for line in lines:
    tab_file_line_by_line.append(line)
  return tab_file_line_by_line


# Partie 1 : Gestion d'erreur


# Partie 2 : Parsing
path_file_board = "../board.txt"
path_form_to_find = "../to_find.txt"
board = rows_file_transformed_into_table(path_file_board)
form_to_find = rows_file_transformed_into_table(path_form_to_find)
if form_to_find[1] in board[2]:
  sentences(1)
else:
  sentences(0)

# Partie 3 : Résolution
print(board)
print(form_to_find)
# sentences(1)


# Partie 4 : Affichage

