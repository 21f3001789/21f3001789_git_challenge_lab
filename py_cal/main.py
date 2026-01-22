#!/usr/bin/env python3
"""
Calculator - main.py
"""

APP_NAME = "Calculator"
VERSION = "1.0.0"

def main():
    """Main application entry point."""
    
    a, b = int(input("Enter A : ")),int(input("Enter B : "))
    print(f"Addition: {a+b}")
    print(f"Subtraction: {a-b}")
    
    print("\n✅ Calculator modules loaded successfully!\n")
    print("=" * 50)
    print(f"{APP_NAME} v{VERSION}")
    print("=" * 50)

if __name__ == "__main__":
    main()