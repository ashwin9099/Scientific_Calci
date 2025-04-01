from flask import render_template, request, jsonify
from model.calculator_model import CalculatorModel

class CalculatorController:
    """
    Controller component of the MVC architecture.
    Handles communication between View and Model.
    """
    
    def __init__(self, app):
        self.app = app
        self.model = CalculatorModel()
        self.setup_routes()
    
    def setup_routes(self):
        """Sets up Flask routes for the application"""
        @self.app.route('/')
        def index():
            return render_template('index.html')
        
        @self.app.route('/calculate', methods=['POST'])
        def calculate():
            expression = request.json.get('expression', '')
            result = self.model.evaluate(expression)
            return jsonify({"result": str(result)})
        
        @self.app.route('/memory', methods=['POST'])
        def memory_operation():
            operation = request.json.get('operation', '')
            value = request.json.get('value', 0)
            
            if operation == 'store':
                success = self.model.store_in_memory(value)
                return jsonify({"success": success})
            
            elif operation == 'recall':
                memory_value = self.model.recall_memory()
                return jsonify({"value": memory_value})
            
            elif operation == 'clear':
                success = self.model.clear_memory()
                return jsonify({"success": success})
            
            return jsonify({"error": "Invalid operation"})
        
        @self.app.route('/special', methods=['POST'])
        def special_function():
            function = request.json.get('function', '')
            value = request.json.get('value', 0)
            
            result = self.model.calculate_special_function(function, value)
            return jsonify({"result": result})