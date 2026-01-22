#!/usr/bin/env python3
"""
Calculator with Menu
Uses modular functions
"""

from sum import add_numbers
from difference import subtract_numbers
from division import divide_numbers
from multiple import multiply_numbers

def get_number(prompt):
    """Get validated integer input"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number!")

def show_menu():
    """Display calculator menu"""
    print("\n" + "="*150)
    print("CALCULATOR")
    print("="*150)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    print("-"*40)

def calculator():
    """Main calculator loop"""
    while True:
        show_menu()
        choice = input("Choose option (1-5): ").strip()
        
        if choice == '1':
            print("\n ADDITION")
            num1 = get_number("First number: ")
            num2 = get_number("Second number: ")
            result = add_numbers(num1, num2)
            print(f"{num1} + {num2} = {result}")
            
        elif choice == '2':
            print("\n➖ SUBTRACTION")
            num1 = get_number("First number: ")
            num2 = get_number("Second number: ")
            result = subtract_numbers(num1, num2)
            print(f"{num1} - {num2} = {result}")
            
        elif choice == '3':
            print("\n Multiplication")
            num1 = get_number("First number: ")
            num2 = get_number("Second number: ")
            result = subtract_numbers(num1, num2)
            print(f"{num1} * {num2} = {result}")
            
        elif choice == '4':
            print("\n Division")
            num1 = get_number("First number: ")
            num2 = get_number("Second number: ")
            result = subtract_numbers(num1, num2)
            print(f"{num1} / {num2} = {result}")
            
        elif choice == '5':
            print("👋 Goodbye!")
            break
            
        else:
            print("Invalid choice! Try 1, 2, or 3.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    calculator()
