# Scientific Calculator (Python MVC)

A modern, web-based scientific calculator built with Python using the MVC (Model-View-Controller) architecture. The calculator features a realistic UI that resembles physical scientific calculators.

## Features

- Clean, modern UI resembling a real scientific calculator
- Full scientific calculator functionality including:
  - Basic arithmetic operations
  - Trigonometric functions (sin, cos, tan)
  - Logarithmic functions (log, ln)
  - Exponents and roots
  - Constants (π, e)
  - Memory functions (MC, MR, MS, M+, M-)
- Keyboard support for faster input
- Responsive design that works on mobile devices
- Built with proper MVC architecture

## Technology Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python, Flask
- **Mathematical Processing**: NumPy
- **Architecture**: Model-View-Controller (MVC)
- **Deployment**: Heroku

## MVC Architecture

This calculator follows the Model-View-Controller architecture pattern:

- **Model** (`model/calculator_model.py`): Contains all the mathematical logic and calculation functions
- **View** (`view/templates/` and `view/static/`): Contains the UI components and styling
- **Controller** (`controller/calculator_controller.py`): Handles the communication between the Model and View

## Live Demo

The calculator is deployed on Heroku and can be accessed at: [https://python-scientific-calc.herokuapp.com/](https://python-scientific-calc.herokuapp.com/)

## Local Development

1. Clone the repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the application:
   ```
   python app.py
   ```
4. Open your browser and navigate to `http://localhost:5000`
