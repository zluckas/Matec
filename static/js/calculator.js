class Calculator {
    constructor() {
        this.display = '';
        this.previousValue = '';
        this.operation = '';
        this.waitingForOperand = false;
    }

    inputDigit(digit) {
        if (this.waitingForOperand) {
            this.display = String(digit);
            this.waitingForOperand = false;
        } else {
            this.display = this.display === '0' ? String(digit) : this.display + digit;
        }
    }

    inputDecimal() {
        if (this.waitingForOperand) {
            this.display = '0.';
            this.waitingForOperand = false;
        } else if (this.display.indexOf('.') === -1) {
            this.display += '.';
        }
    }

    clear() {
        this.display = '0';
        this.previousValue = '';
        this.operation = '';
        this.waitingForOperand = false;
    }

    performOperation(nextOperation) {
        const inputValue = parseFloat(this.display);

        if (this.previousValue === '') {
            this.previousValue = inputValue;
        } else if (this.operation) {
            const currentValue = this.previousValue || 0;
            const newValue = this.calculate(currentValue, inputValue, this.operation);

            this.display = String(newValue);
            this.previousValue = newValue;
        }

        this.waitingForOperand = true;
        this.operation = nextOperation;
    }

    calculate(firstValue, secondValue, operation) {
        switch (operation) {
            case '+':
                return firstValue + secondValue;
            case '-':
                return firstValue - secondValue;
            case '*':
                return firstValue * secondValue;
            case '/':
                return secondValue !== 0 ? firstValue / secondValue : 0;
            case '=':
                return secondValue;
            default:
                return secondValue;
        }
    }

    equals() {
        const inputValue = parseFloat(this.display);

        if (this.previousValue !== '' && this.operation) {
            const newValue = this.calculate(this.previousValue, inputValue, this.operation);
            this.display = String(newValue);
            this.previousValue = '';
            this.operation = '';
            this.waitingForOperand = true;
        }
    }
}

// Inicializar calculadora quando o DOM estiver carregado
document.addEventListener('DOMContentLoaded', function() {
    const calculator = new Calculator();
    const display = document.getElementById('calc-display');
    
    if (!display) return; // Se não há calculadora na página, sair

    // Atualizar display
    function updateDisplay() {
        display.value = calculator.display;
    }

    // Event listeners para botões
    document.querySelectorAll('.calc-btn').forEach(button => {
        button.addEventListener('click', function() {
            const value = this.dataset.value;
            const type = this.dataset.type;

            switch (type) {
                case 'number':
                    calculator.inputDigit(parseInt(value));
                    updateDisplay();
                    break;
                case 'decimal':
                    calculator.inputDecimal();
                    updateDisplay();
                    break;
                case 'operator':
                    calculator.performOperation(value);
                    updateDisplay();
                    break;
                case 'equals':
                    calculator.equals();
                    updateDisplay();
                    break;
                case 'clear':
                    calculator.clear();
                    updateDisplay();
                    break;
            }
        });
    });

    // Suporte para teclado
    document.addEventListener('keydown', function(event) {
        const key = event.key;
        
        if (key >= '0' && key <= '9') {
            calculator.inputDigit(parseInt(key));
            updateDisplay();
        } else if (key === '.') {
            calculator.inputDecimal();
            updateDisplay();
        } else if (['+', '-', '*', '/'].includes(key)) {
            calculator.performOperation(key);
            updateDisplay();
        } else if (key === 'Enter' || key === '=') {
            calculator.equals();
            updateDisplay();
        } else if (key === 'Escape' || key === 'c' || key === 'C') {
            calculator.clear();
            updateDisplay();
        }
    });

    // Inicializar display
    updateDisplay();
});
