import re
import time
import operator
import SLLStack
import ChainedHashTable
import BinaryTree


class Calculator:
    def __init__(self):
        self.dict = ChainedHashTable.ChainedHashTable()

    def balanced_parens(self, s: str) -> bool:
        """
        determines whether the given string contains balanced parentheses
        :param s: str type; the string to be checked
        :return: bool type; True if the string s contains balanced parentheses
        """
        # FIXME: Replace with your implementation from Module 3
        return False

    def store_var(self, variable, value, replace=False):
        """
        stores the given mathematical variable and its corresponding value.
        If the variable already exists and should not be replaced, error message is printed and the variable is not stored.  Otherwise, the value of the existing variable is replaced with the new value.
        :param variable: str type;
        :param value: float type;
        :param replace: boolean type; if True, replaces the value of an existing variable; otherwise, prints an error message
        """
        pass # FIXME: Replace with your implementation from Module 4
          

    def print_stored_vars(self):
        """
        displays all math variables and their corresponding values stored
        on this instance of Calculator
        """
        pass # FIXME: Replace with your implementation from Module 4
      
    def _build_parse_tree(self, expr: str) -> str:
      """
      helper method to evaluate(expression); builds the parse tree for the given expression
      """
      if not self.balanced_parens(expr):
          raise ValueError("Expression contains unmatched parenthesis.")
      t = BinaryTree.BinaryTree()
      t.r = BinaryTree.BinaryTree.Node()

      current = t.r
      variables, tokens = self._make_tokens(expr)
      for token in tokens:
          if token == '(':
              pass  # FIXME: Replace this with the correct lines of code.
          elif token in ['+', '-', '*', '/']:
              pass  # FIXME: Replace this with the correct lines of code.
          elif token == ')':
              pass  # FIXME: Replace this with the correct lines of code.
          elif token in variables:
              pass  # FIXME: Replace this with the correct lines of code.
          else:
              raise ValueError(f"{token} is an invalid token in the expression")

      return t

    def _evaluate(self, u: BinaryTree.BinaryTree.Node):
      """
      helper method to evaluate(expr); evaluates the parse tree rooted at node u
      :param u: BinaryTree.Node type
      """
      oper_dict = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

      if u.left is not None and u.right is not None:  # this is an operator
          operation = oper_dict[u.v]
          return operation(self._evaluate(u.left), self._evaluate(u.right))
      elif u.left is None and u.right is None:  # this must be a variable
          if u.k is None:
              raise ValueError(f"Missing operand after {u.parent.k}.")
          elif u.v is not None:
            
              return None  #FIXME: Replace None with the correct value
            
          else:
              raise ValueError(f"Missing value for variable '{u.k}'")
      else:
          raise ValueError(f"Missing an operand and/or operator before {u.left.v}.")


    """THE METHODS BELOW ARE FULLY IMPLEMENTED AND DO NOT NEED TO BE MODIFIED"""
    def expr_with_values(self, expression):
      """
      creates a copy of the given expression with variables replaced by stored values
      :param expression: str type;
      :return: tuple type; a tuple with two elements; the first is the expression as a string
               with replaced values for stored variables; the second element is a list of
               variables in the expression that have no stored value.
      """
      remaining_vars = []
      variables, tokens = self._make_tokens(expression)
      for i in range(len(tokens)):
          token = tokens[i]
          if token in variables:
              val = self.dict.find(token)
              if val is None:
                  remaining_vars.append(token)
              else:
                  tokens[i] = val
      new_expression = ''.join([str(t) for t in tokens])
      return (new_expression, remaining_vars)
  
    def _make_tokens(self, expr: str) -> list:
      """
      helper method; creates a list of tokens out of the given expression.
      A token is defined to be a left/right parenthesis, a variable, or an operator.
      :param expr: the expression
      :return: tuple type; a tuple with two elements.  The first element is a list
               of variables existing in the expression; the second element is the list
               of all tokens, in the order that they appear in the expression.
      """
      temp_vars = [x for x in re.split('\W+', expr) if x.isalnum()]
      ee = re.split('\w+', expr)
      tokens = []
      while len(temp_vars) > 0 and len(ee) > 0:
          if len(ee[0]) < 2:
              tokens.append(ee[0])
          else:
              for c in ee[0]:
                  tokens.append(c)
          del ee[0]
          tokens.append(temp_vars[0])
          del temp_vars[0]
  
      while len(ee) > 0:
          if len(ee[0]) < 2:
              tokens.append(ee[0])
          else:
              for c in ee[0]:
                  tokens.append(c)
          del ee[0]
      variables = [x for x in re.split('\W+', expr) if x.isalnum()]
      return variables, tokens
  
    def evaluate(self, expr: str):
      """
      evaluates the given expression with variable values stored in the calculator.
      :param expression: str type; the mathematical expression
      """
      parse_tree = self._build_parse_tree(expr)
      return self._evaluate(parse_tree.r)



