import math
import numpy as np

class CalculatorModel:
    """
    Model component of the MVC architecture.
    Handles all calculation logic.
    """
    
    def __init__(self):
        self.memory = 0
        self.ans = 0  # Stores the last calculated answer
    
    def evaluate(self, expression):
        """
        Evaluates a mathematical expression and returns the result.
        
        Args:
            expression (str): The mathematical expression to evaluate
            
        Returns:
            float: The result of the evaluation
        """
        try:
            # Replace common mathematical functions with their numpy equivalents
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
            
            # Calculate the result
            result = eval(expression, {"__builtins__": None}, {"np": np, "math": math})
            
            # Update the last answer
            self.ans = result
            
            # Format the result to avoid unnecessary decimal places
            if isinstance(result, (int, float)):
                if result == int(result):
                    return int(result)
                else:
                    # Limit to 10 decimal places
                    return round(result, 10)
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