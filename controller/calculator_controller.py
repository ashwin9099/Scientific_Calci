import math
from model.calculator_model import CalculatorModel

class CalculatorController:
    def __init__(self):
      self.model = CalculatorModel()

    def evaluate_expression(self, expression):
        try:
          expression = expression.replace('^', '**')
          expression = expression.replace('√', 'math.sqrt')
          return str(eval(expression, {"math": math}))
        except Exception as e:
          return f"Error: {str(e)}"

    def handle_input(self, input_str, current_input):
        if input_str == "=":
          result = self.evaluate_expression(current_input)
          return result
        elif input_str == "C":
          return ""
        else:
          return current_input + input_str