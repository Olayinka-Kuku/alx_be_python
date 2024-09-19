# pattern_drawing.py

def main():
    # Prompt user for pattern size
    size = int(input("Enter the size of the pattern: "))
    
    # Validate input
    if size <= 0:
        print("The size must be a positive integer.")
        return

    # Draw the pattern using nested loops
    row = 0
    while row < size:
        for _ in range(size):
            print("*", end="")
        print()
        row += 1

if __name__ == "__main__":
    main()