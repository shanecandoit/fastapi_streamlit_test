
def calculate(operation, x, y):
    """Perform a calculation on two numbers."""
    operation = operation.lower()
    if operation.startswith("add"):
        return x + y
    elif operation.startswith("sub"):
        return x - y
    elif operation.startswith("mul"):
        return x * y
    elif operation.startswith("divide"):
        return x / y
    else:
        return "Invalid operation"
