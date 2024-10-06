# robust_division_calculator.py

def safe_divide(numerator, denominator):
    try:
        # Convert both numerator and denominator to floats
        num = float(numerator)
        denom = float(denominator)
        
        # Perform the division and handle division by zero
        if denom == 0:
            return "Error: Cannot divide by zero."
        
        # Return the result of the division
        result = num / denom
        return f"The result of the division is {result}"
    
    except ValueError:
        # Handle the case where the inputs are not numeric
        return "Error: Please enter numeric values only."