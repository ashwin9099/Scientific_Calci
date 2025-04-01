import os
from flask import Flask
from controller.calculator_controller import CalculatorController

app = Flask(__name__, static_folder='view/static', template_folder='view/templates')

calculator_controller = CalculatorController(app)

if __name__ == '__main__':
    
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)  # any port