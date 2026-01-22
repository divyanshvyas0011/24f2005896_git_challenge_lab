"""
Main Calculator Application
"""
from sum import add, add_multiple

def main():
    print("Calculator Application")
    print("Version 1.1 - Addition Support")
    
    # Test addition
    result = add(5, 3)
    print(f"5 + 3 = {result}")
    
    result = add_multiple(1, 2, 3, 4, 5)
    print(f"1 + 2 + 3 + 4 + 5 = {result}")
    
if __name__ == "__main__":
    main()
