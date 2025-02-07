import math
from typing import List

class CalculatorModel:
  
  def evaluate(self, expression):
    try:
      expression = expression.replace("^", "**")
      expression = expression.replace("√", "math.sqrt")
      expression = expression.replace("sin", "math.sin")
      expression = expression.replace("cos", "math.cos")
      expression = expression.replace("tan", "math.tan")
      expression = expression.replace("log", "math.log")
      expression = expression.replace("ln", "math.log")
      expression = expression.replace("π", str(math.pi))
      expression = expression.replace("e", str(math.e)) # eulers number
      
      
      if '%' in expression:                             # % to  decimal
        expression = expression.replace("%", '/100')
        
      result = eval(expression, {'math': math, '__builtins__': None}, {})
      return round(result, 10) if isinstance(result, float) else result
    except:
      return 'Error'