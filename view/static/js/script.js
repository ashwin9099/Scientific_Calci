document.addEventListener('DOMContentLoaded', function() {
  // Elements
  const expressionElement = document.getElementById('expression');
  const resultElement = document.getElementById('result');
  
  // Calculator state
  let currentExpression = '';
  let currentResult = '0';
  let waitingForOperand = false;
  let memoryValue = 0;
  let secondMode = false;
  
  // Update the display
  function updateDisplay() {
      expressionElement.textContent = currentExpression || '0';
      resultElement.textContent = currentResult;
  }
  
  // Clear the calculator
  function clearCalculator() {
      currentExpression = '';
      currentResult = '0';
      waitingForOperand = false;
      updateDisplay();
  }
  
  // Clear just the current entry
  function clearEntry() {
      currentResult = '0';
      if (waitingForOperand) {
          waitingForOperand = false;
      }
      updateDisplay();
  }
  
  // Backspace function
  function backspace() {
      if (currentExpression.length > 0) {
          currentExpression = currentExpression.slice(0, -1);
          updateDisplay();
      }
  }
  
  // Handle number input
  function inputNumber(num) {
      if (waitingForOperand) {
          currentExpression = '';
          waitingForOperand = false;
      }
      
      if (currentExpression === '0' && num !== '.') {
          currentExpression = num;
      } else if (num === '.' && currentExpression.includes('.')) {
          // Prevent multiple decimal points
          return;
      } else {
          currentExpression += num;
      }
      
      updateDisplay();
  }
  
  // Handle operator input
  function inputOperator(operator) {
      if (currentExpression === '' && operator !== '-') {
          return;
      }
      
      if (waitingForOperand) {
          waitingForOperand = false;
      }
      
      // Map display symbols to actual operators
      const operatorMap = {
          '×': '*',
          '÷': '/',
          '−': '-'
      };
      
      const actualOperator = operatorMap[operator] || operator;
      currentExpression += actualOperator;
      updateDisplay();
  }
  
  // Handle function input
  function inputFunction(func) {
      if (func === 'clear') {
          clearCalculator();
          return;
      }
      
      if (func === 'clear-entry') {
          clearEntry();
          return;
      }
      
      if (func === 'backspace') {
          backspace();
          return;
      }
      
      if (func === 'ans') {
          if (waitingForOperand) {
              currentExpression = '';
              waitingForOperand = false;
          }
          currentExpression += 'Ans';
          updateDisplay();
          return;
      }
      
      // Memory functions
      if (func === 'mc') {
          fetch('/memory', {
              method: 'POST',
              headers: {
                  'Content-Type': 'application/json',
              },
              body: JSON.stringify({
                  operation: 'clear'
              }),
          });
          memoryValue = 0;
          return;
      }
      
      if (func === 'mr') {
          fetch('/memory', {
              method: 'POST',
              headers: {
                  'Content-Type': 'application/json',
              },
              body: JSON.stringify({
                  operation: 'recall'
              }),
          })
          .then(response => response.json())
          .then(data => {
              currentExpression += data.value;
              updateDisplay();
          });
          return;
      }
      
      if (func === 'ms') {
          fetch('/memory', {
              method: 'POST',
              headers: {
                  'Content-Type': 'application/json',
              },
              body: JSON.stringify({
                  operation: 'store',
                  value: currentResult
              }),
          });
          return;
      }
      
      if (func === 'm+') {
          fetch('/memory', {
              method: 'POST',
              headers: {
                  'Content-Type': 'application/json',
              },
              body: JSON.stringify({
                  operation: 'recall'
              }),
          })
          .then(response => response.json())
          .then(data => {
              const newValue = parseFloat(data.value) + parseFloat(currentResult);
              fetch('/memory', {
                  method: 'POST',
                  headers: {
                      'Content-Type': 'application/json',
                  },
                  body: JSON.stringify({
                      operation: 'store',
                      value: newValue
                  }),
              });
          });
          return;
      }
      
      if (func === 'm-') {
          fetch('/memory', {
              method: 'POST',
              headers: {
                  'Content-Type': 'application/json',
              },
              body: JSON.stringify({
                  operation: 'recall'
              }),
          })
          .then(response => response.json())
          .then(data => {
              const newValue = parseFloat(data.value) - parseFloat(currentResult);
              fetch('/memory', {
                  method: 'POST',
                  headers: {
                      'Content-Type': 'application/json',
                  },
                  body: JSON.stringify({
                      operation: 'store',
                      value: newValue
                  }),
              });
          });
          return;
      }
      
      if (func === '2nd') {
          secondMode = !secondMode;
          const keyboardEl = document.querySelector('.keyboard');
          if (secondMode) {
              keyboardEl.classList.add('second-mode');
          } else {
              keyboardEl.classList.remove('second-mode');
          }
          return;
      }
      
      // Special functions
      const specialFuncs = ['sin', 'cos', 'tan', 'log', 'ln', 'radical', 'square', 'cube', 'factorial', 'reciprocal'];
      
      if (specialFuncs.includes(func)) {
          if (waitingForOperand) {
              currentExpression = '';
              waitingForOperand = false;
          }
          
          // Map button functions to expressions
          const funcMap = {
              'sin': 'sin(',
              'cos': 'cos(',
              'tan': 'tan(',
              'log': 'log(',
              'ln': 'ln(',
              'radical': 'sqrt(',
              'square': '^2',
              'cube': '^3',
              'factorial': '!',
              'reciprocal': '^(-1)'
          };
          
          // Add function to expression
          const expressionFunc = funcMap[func];
          if (expressionFunc) {
              if (func === 'square' || func === 'cube' || func === 'factorial' || func === 'reciprocal') {
                  // These functions apply to the previous number
                  currentExpression += expressionFunc;
              } else {
                  // These functions require a parameter
                  currentExpression += expressionFunc;
              }
              updateDisplay();
          }
      }
  }
  
  // Handle constant input
  function inputConstant(constant) {
      if (waitingForOperand) {
          currentExpression = '';
          waitingForOperand = false;
      }
      
      const constantMap = {
          'pi': 'π',
          'e': 'e'
      };
      
      const expressionConstant = constantMap[constant] || constant;
      currentExpression += expressionConstant;
      updateDisplay();
  }
  
  // Calculate the result
  function calculate() {
      if (currentExpression === '') {
          return;
      }
      
      fetch('/calculate', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json',
          },
          body: JSON.stringify({
              expression: currentExpression
          }),
      })
      .then(response => response.json())
      .then(data => {
          currentResult = data.result;
          waitingForOperand = true;
          updateDisplay();
      })
      .catch(error => {
          currentResult = 'Error';
          waitingForOperand = true;
          updateDisplay();
          console.error('Error:', error);
      });
  }
  
  // Add event listeners to calculator buttons
  document.querySelectorAll('.key').forEach(key => {
      key.addEventListener('click', () => {
          const keyType = key.className.split(' ')[1];  // Get the second class (number, operation, etc.)
          const keyValue = key.getAttribute('data-key');
          
          switch (keyType) {
              case 'number':
                  inputNumber(keyValue);
                  break;
              case 'operation':
                  inputOperator(key.textContent);
                  break;
              case 'function':
                  inputFunction(keyValue);
                  break;
              case 'constant':
                  inputConstant(keyValue);
                  break;
              case 'equals':
                  calculate();
                  break;
          }
      });
  });
  
  // Add keyboard support
  document.addEventListener('keydown', (event) => {
      const key = event.key;
      
      // Prevent default action for calculator keys
      if (/[0-9+\-*/.=]|Enter|Backspace|Escape|Delete/.test(key)) {
          event.preventDefault();
      }
      
      // Map keyboard keys to calculator functions
      if (/[0-9.]/.test(key)) {
          inputNumber(key);
      } else if (/[+\-*\/]/.test(key)) {
          const operatorMap = {
              '*': '×',
              '/': '÷',
              '-': '−',
              '+': '+'
          };
          inputOperator(operatorMap[key] || key);
      } else if (key === '=' || key === 'Enter') {
          calculate();
      } else if (key === 'Backspace') {
          backspace();
      } else if (key === 'Escape' || key === 'Delete') {
          clearCalculator();
      } else if (key === 'p') {
          inputConstant('pi');
      } else if (key === 'e') {
          inputConstant('e');
      } else if (key === '(' || key === ')') {
          inputOperator(key);
      }
  });
  
  // Initialize the display
  updateDisplay();
});