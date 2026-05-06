let currentInput = '0';
let previousInput = '';
let operator = null;
let shouldResetScreen = false;

const displayElement = document.getElementById('display');
const historyElement = document.getElementById('history');

function updateDisplay() {
    displayElement.textContent = currentInput;
}

function updateHistory() {
    if (operator && previousInput) {
        let opSymbol = operator;
        if (opSymbol === '*') opSymbol = '×';
        if (opSymbol === '/') opSymbol = '÷';
        if (opSymbol === '-') opSymbol = '−';
        historyElement.textContent = `${previousInput} ${opSymbol}`;
    } else {
        historyElement.textContent = '';
    }
}

function clear() {
    currentInput = '0';
    previousInput = '';
    operator = null;
    shouldResetScreen = false;
    displayElement.classList.remove('error');
    updateDisplay();
    updateHistory();
}

function backspace() {
    if (shouldResetScreen || currentInput === '0') return;
    if (currentInput.length === 1) {
        currentInput = '0';
    } else {
        currentInput = currentInput.slice(0, -1);
    }
    updateDisplay();
}

function appendNumber(number) {
    if (shouldResetScreen) {
        currentInput = '';
        shouldResetScreen = false;
    }
    if (number === '.' && currentInput.includes('.')) return;
    if (currentInput === '0' && number !== '.') {
        currentInput = number;
    } else {
        currentInput += number;
    }
    displayElement.classList.remove('error');
    updateDisplay();
}

function chooseOperation(op) {
    if (operator !== null && !shouldResetScreen) {
        calculate();
    }
    previousInput = currentInput;
    operator = op;
    shouldResetScreen = true;
    updateHistory();
}

function calculate() {
    if (operator === null || shouldResetScreen) return;

    let result;
    const prev = parseFloat(previousInput);
    const current = parseFloat(currentInput);

    if (isNaN(prev) || isNaN(current)) return;

    switch (operator) {
        case '+':
            result = prev + current;
            break;
        case '-':
            result = prev - current;
            break;
        case '*':
            result = prev * current;
            break;
        case '/':
            if (current === 0) {
                displayElement.textContent = '除数不能为0';
                displayElement.classList.add('error');
                historyElement.textContent = '';
                operator = null;
                previousInput = '';
                shouldResetScreen = true;
                return;
            }
            result = prev / current;
            break;
        case '%':
            result = prev % current;
            break;
        default:
            return;
    }

    if (!Number.isInteger(result)) {
        result = parseFloat(result.toFixed(8));
    }

    currentInput = result.toString();
    operator = null;
    previousInput = '';
    shouldResetScreen = true;
    updateDisplay();
    updateHistory();
}

document.getElementById('clear').addEventListener('click', clear);
document.getElementById('equals').addEventListener('click', calculate);

document.querySelectorAll('.number').forEach(button => {
    button.addEventListener('click', () => {
        appendNumber(button.dataset.value);
    });
});

document.querySelectorAll('.operator').forEach(button => {
    button.addEventListener('click', () => {
        chooseOperation(button.dataset.value);
    });
});

document.querySelectorAll('[data-action="backspace"]').forEach(button => {
    button.addEventListener('click', backspace);
});
