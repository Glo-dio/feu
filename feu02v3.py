import sys

# fonctions utilisées
# def error_handling(arguments):
#   if not len(arguments) == 3:
#     sys.exit("Error need 2 files in argument arg1 = board and arg2 = to_find")

def read_file(filename):
  ##Fonction qui lit le contenu d'un fichier et retourne son contenu sous forme de liste de chaînes de caractères
  try:
    with open(filename, 'r') as file:
      # on transforme chaque ligne "x" en sous_liste et on supprime les retour à la ligne)
      return [list(line.strip("\n")) for line in file.readlines()]
  except:
    sys.exit(f"Erreur : {filename} ne peut être lu")

def transform_list_to_rectangle(list_input):
  # on met au format rectangle en commblant les vides par des espaces
  max_length = max(len(row) for row in list_input)
  # print(str(array[1]) + " " * 2)
  rectangle = [row + [" "] * (max_length - len(row)) for row in list_input]
  return rectangle

def find_shape(board, shape):
  # la on créer un tableau array_display qui à exacement le format de board mais ou chaque élément est remplacé par "-"
  # donc il s'agit d'une compréhension de liste 
  # for row in board donc chaque ligne du board puis on boucle dans chaque ligne et remplace chaque élément par "-" avec "-" for _ in range(len(row))
  # le _ aurait pu être i ca ne change rien mais par convention si on ne fait rien avec les valeur des élément on met _ c'est tous
  list_to_display = [["-" for _ in range(len(row))] for row in board]

  # print("x" * 20) #! test
  # for i in range(len(list_to_display)): #! test
  #     print(list_to_display[i]) #! test
  # print("x" * 20) #! test

  #trouver la taille de la forme x et y
  len_column_shape = len(shape[0])
  len_row_shape = len(shape)
  len_column_board = len(board[0])
  len_row_board = len(board)
  # de cette manière on délimite jusqu'à quel étage on peut descendre pour trouver le 1 er élément commun sans sortir du board
  # print(f"{board_y} - {shape_y} + 1 = {board_y - shape_y + 1}") #! test
  for row_board in range(len_row_board - len_row_shape + 1):
    # de cette manière on délimite jusqu'ou sur la ligne on peut trouver le 1 er élément commun sans sortir du board
    for column_board in range(len_column_board - len_column_shape + 1):
      found_space = True
      # va permettre de compté le nombre d'espace au début de la forme pour incrémenté les coordonnées de x à retourner
      left_space_in_shape = 0
      # permet de savoir si il s'agit d'espace au début de la forme ou à la fin car si se sont des espaces de la fin on n'incrément pas start_space
      first_element_of_shape = True
      # on va chercher les élément de la forme l'un apres l'autre pour et les comparer avec les éléments du tableau
      for row_shape in range(len_row_shape):
        for column_shape in range(len_column_shape):
          # lorsque l'on veut donnée les coordonnées de tableau imbriqué on donne en premier les y (étages) et ensuite les x (position dans l'étage)
          # si l'élément shape est un espace on va a l'élément suivant (permet de gérer le print de la forme en dessous de "Coordonnées")
          if shape[row_shape][column_shape] != " " and shape[row_shape][column_shape] != board[row_board + row_shape][column_board + column_shape]:
            found_space = False
            # print("false") #! test
            break
          # si élément est un espace du début de la forme on incrément notre variable start_space
          if shape[row_shape][column_shape] == " " and first_element_of_shape:
            left_space_in_shape += 1
            first_element_of_shape = True
          # ici on permet de savoir qu'il ya eu élément autre qu'un espace donc nous ne sommes plus au début de la forme on stop l'incrémentation de start_space                      
          elif shape[row_shape][column_shape] != " ":
            first_element_of_shape = False
            # on ajout au tableau array_display les valeur trouvé pour autant que l'élément de recherche shape[ys][xs] n'est pas un espace
            list_to_display[row_board + row_shape][column_board + column_shape] = shape[row_shape][column_shape]
            # print(f"{yb} \t{ys}|{xs}")
            # print("*" * 20)
            # for i in range(len(array_display)):
            #     print(array_display[i])
            # print("o" * 20)
        # permet de remonté au boucle tu tableau board pour parcourir l'élément suivant du board
        # if not found_space:
        if found_space == False:
          break
      if found_space == True:
        if left_space_in_shape > 0:
          
          # print("~" * 20) #! test
          # # for i in range(len(list_to_display)): #! test
            # # print(list_to_display[i]) #! test
          # print("~" * 20) #! test
          
          return column_board + left_space_in_shape, row_board, list_to_display
        else :
          return column_board, row_board, list_to_display
      # ici on écrase a nouveau les valeur avec "-" car nous avons pas trouvé la forme entière donc on passe a l'élément suivant du tableau.
      list_to_display = [["-" for _ in range(len(row))] for row in board]

      # print(f"{column_board} + {row_board} + {list_to_display}") #! test
  return "error"

def get_position(position):
  x_point = position[0] if position != "error" else None
  y_point = position[1]
  shape_modeled_on_board = position[2]
  #Fonction qui affiche la position de la forme ou le message 'Introuvable' si la forme n'a pas été trouvée
  if position != "error":
    print("Trouvé !")
    print(f"Coordonnées : {x_point},{y_point}")
    set_2d_array(shape_modeled_on_board)
  else:
    sys.exit("Introuvable")

def set_2d_array(array):
  for row in array:
    # on concatenate tous les élément d'une ligne en une chaine de caratère et la print
    print("".join(row))

def is_arg_valid(argument):
  if not len(argument) == 3:
    sys.exit("Erreur : 2 arguments sont nécessaires")

# Partie 1 : Gestion d'erreur
is_arg_valid(sys.argv)
# error_handling(sys.argv)

# Partie 2 : Parsing
board = read_file(sys.argv[1])
# print(f"read_line {board}") #! test
shape = read_file(sys.argv[2])
# print(f"read_line {shape}") #! test

# Partie 3 : Résolution
board = transform_list_to_rectangle(board)
# print(f"rectangle {board}") #! test
shape = transform_list_to_rectangle(shape)
# print(f"rectangle {shape}") #! test
position = find_shape(board, shape)
# print(position) #! test

# Partie 4 : Affichage
get_position(position)