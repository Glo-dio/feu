import sys

# fonctions utilisées
def args_to_array(string):
  array = []
  for i in string:
    if i != ' ':
      array.append(i)
  # print(array)
  return array

def addition(a,b):
  return a + b

def soustraction(a,b):
  return a - b

def multiplication(a,b):
  return a * b

def division(a,b):
  return a / b

def calcul(a,b, operator):
  match operator:
    case '+':
      return addition(a,b)
    case '-':
      return soustraction(a,b)
    case '*':
      return multiplication(a,b)
    case '/':
      return division(a,b)
    case __:
      return sys.exit("error operator")

def evaluate(expression):
  postfix = []
  operator_stack = []
  sign = ["+", "-", "*", "/", "(", ")"]
  for element in expression:
  if element.isdigit():
      postfix.append(element)
    if element in sign:
      print(f"element = {element} | south = \t{operator_stack}")
      if operator_stack == True and element == sign[0]:
        postfix.append(operator_stack.pop())
        print(f"apres del + {operator_stack}")

      elif operator_stack == True and element == sign[5]:
        # print("bonjour")
        for i in range(-1, 1):
          if operator_stack[i] == "(":
            # south.pop()
            break
          postfix.append(operator_stack.pop())
      operator_stack.append(element)
  print(f"south = \t\033[41;1m{operator_stack}\033[0m")
  # for i in range(0, len(south), -1):
  for i in range(-1, 1):
    # print(i)
    postfix.append(operator_stack[i])
  print(f"south end = \t\033[42;1m{operator_stack}\033[0m")

  print(postfix)

# Partie 1 : Gestion d'erreur


# Partie 2 : Parsing
# for i in sys.argv:
#   print(i)

user_expression = args_to_array(sys.argv[1])
# a = int(args[0])
# b = int(args[2])
# b = 4
# operator = args[1]
# operator = "/"

# Partie 3 : Résolution

# result = calcul(a,b,operator)
result = evaluate(user_expression)

# Partie 4 : Affichage
# print(result)

