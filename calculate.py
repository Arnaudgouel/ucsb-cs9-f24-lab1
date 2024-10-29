from collections import deque
import re

def tokenize(expression):
    """Convert a string expression into a deque of tokens (numbers and operators)."""
    if not expression.strip():
        return deque()
    
    # Split the expression into tokens
    tokens = expression.strip().split()
    result = deque()
    
    # Valid operators
    operators = {'+', '-', '*', '/', '%', '^', '~'}
    
    for token in tokens:
        # Try to convert to float first
        try:
            result.append(float(token))
            continue
        except ValueError:
            pass
        
        # Check if it's an operator
        if token in operators:
            result.append(token)
        else:
            raise RuntimeError(f'Invalid token: "{token}"')
    
    return result

def apply_operator(op, operands):
    """Apply the given operator to the operands."""
    if op == '~':
        if len(operands) < 1:
            raise RuntimeError("Not enough operands.")
        return -operands[0]
    
    if len(operands) < 2:
        raise RuntimeError("Not enough operands.")
        
    b = operands[1]  # Note: order matters for non-commutative operations
    a = operands[0]
    
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            raise RuntimeError("Division by zero.")
        return a / b
    elif op == '%':
        if b == 0:
            raise RuntimeError("Division by zero.")
        return a % b
    elif op == '^':
        return a ** b
    else:
        raise RuntimeError(f'Invalid operator: "{op}"')

def prefix(tokens):
    """Evaluate a prefix expression."""
    if not tokens:
        raise RuntimeError("No input.")
    
    def evaluate():
        if not tokens:
            raise RuntimeError("Not enough operands.")
            
        token = tokens.popleft()
        
        # If token is a number, return it
        if isinstance(token, float):
            return token
            
        # If token is an operator
        if token == '~':
            operand = evaluate()
            return -operand
        else:
            left = evaluate()
            right = evaluate()
            return apply_operator(token, [left, right])
    
    result = evaluate()
    
    # Check if there are remaining tokens
    if tokens:
        raise RuntimeError("Too much input.")
        
    return result

def postfix(tokens):
    """Evaluate a postfix expression."""
    if not tokens:
        raise RuntimeError("No input.")
        
    stack = []
    
    while tokens:
        token = tokens.popleft()
        
        if isinstance(token, float):
            stack.append(token)
        else:
            if token == '~':
                if not stack:
                    raise RuntimeError("Not enough operands.")
                operand = stack.pop()
                stack.append(-operand)
            else:
                if len(stack) < 2:
                    raise RuntimeError("Not enough operands.")
                b = stack.pop()
                a = stack.pop()
                stack.append(apply_operator(token, [a, b]))
    
    if len(stack) > 1:
        raise RuntimeError("Too many operands.")
    elif len(stack) == 0:
        raise RuntimeError("Not enough operands.")
        
    return stack[0]