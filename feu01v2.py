import sys

def calculate_expression(expression):
  tokens = tokenize(expression)
  postfix = infix_to_postfix(tokens)
  result = evaluate_postfix(postfix)
  return result

def tokenize(expression):
    import re
    tokens = re.findall(r'\d+|\+|-|\*|/|%|\(|\)', expression)
    return tokens

def precedence(operator):
  if operator in ["+", "-"]:
    return 1
  elif operator in ["*", "/", "%"]:
    return 2
  else:
    return 0

def infix_to_postfix(tokens):
  postfix = []
  operator_stack = []

  for token in tokens:
    if token.isdigit():
      postfix.append(token)
    elif token == "(":
      operator_stack.append(token)
    elif token == ")":
      while operator_stack and operator_stack[-1] != "(":
        postfix.append(operator_stack.pop())
      operator_stack.pop()
    else:
      while operator_stack and operator_stack[-1] != "(" and precedence(operator_stack[-1]) >= precedence(token): # si t'es un operateur
        postfix.append(operator_stack.pop())
      operator_stack.append(token)
  while operator_stack:
    postfix.append(operator_stack.pop())
  return postfix

def evaluate_postfix(postfix):
  operand_stack = []
  for token in postfix:
    if token.isdigit():
      operand_stack.append(int(token))
      # operand_stack.append(float(token))
    else:
      operand2, operand1 = operand_stack.pop(), operand_stack.pop()
      if token == "+":
        result = operand1 + operand2
      elif token == "-":
        result = operand1 - operand2
      elif token == "*":
        result = operand1 * operand2
      elif token == "/":
        result = operand1 / operand2
      elif token == "%":
        result = operand1 % operand2
      operand_stack.append(result)
  return operand_stack.pop()





expression = sys.argv[1]

result = calculate_expression(expression)

print(result)