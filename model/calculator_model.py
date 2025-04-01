import math
import numpy as np

class CalculatorModel:
    
    def __init__(self):
        self.memory = 0
        self.ans = 0
    
    def evaluate(self, expression):
        
        try:
            expression = expression.replace("^", "**")
            expression = expression.replace("sin(", "np.sin(")
            expression = expression.replace("cos(", "np.cos(")
            expression = expression.replace("tan(", "np.tan(")
            expression = expression.replace("log(", "np.log10(")
            expression = expression.replace("ln(", "np.log(")
            expression = expression.replace("sqrt(", "np.sqrt(")
            expression = expression.replace("π", "np.pi")
            expression = expression.replace("pi", "np.pi")
            expression = expression.replace("e", "np.e")
            expression = expression.replace("Ans", str(self.ans))
            
          
            result = eval(expression, {"__builtins__": None}, {"np": np, "math": math})
            
            self.ans = result
            
            if isinstance(result, (int, float)):
                if result == int(result):
                    return int(result)
                else:
                   
                    return round(result, 10)  # Limit to 10 decimal places
            return result
            
        except Exception as e:
            return f"Error: {str(e)}"
    
    def store_in_memory(self, value):
        """Stores a value in calculator memory"""
        try:
            self.memory = float(value)
            return True
        except:
            return False
    
    def recall_memory(self):
        """Returns the value stored in memory"""
        return self.memory
    
    def clear_memory(self):
        """Clears the calculator memory"""
        self.memory = 0
        return True
    
    def calculate_special_function(self, function, value):
        """
        Calculates various special mathematical functions
        
        Args:
            function (str): The name of the function
            value (float): The input value
            
        Returns:
            float: The result of the function
        """
        try:
            value = float(value)
            
            if function == "square":
                return value ** 2
            elif function == "cube":
                return value ** 3
            elif function == "sqrt":
                return math.sqrt(value)
            elif function == "factorial":
                return math.factorial(int(value))
            elif function == "reciprocal":
                return 1 / value
            else:
                return "Invalid function"
        except Exception as e:
            return f"Error: {str(e)}"