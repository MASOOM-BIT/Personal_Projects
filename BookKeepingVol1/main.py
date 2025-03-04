from apes import Aaddhar_Payment_System

def main():
    print('Welcome to BookKeeping Vol 1')
    print('---------------------------------------------------------------')
    print('1. Apes Records')
    print('2. DMT Records')
    print('3. Forex Records')
    print('4. Records')
    
    user_input = input('Enter your choice [1 | 2 | 3 | 4]: ')

    if user_input == '1':
        Aaddhar_Payment_System()  # Ensure this is a function; if it's a class, use Aaddhar_Payment_System()
    elif user_input == '2':
        print("DMT Records selected. Feature not implemented yet.")
    elif user_input == '3':
        print("Forex Records selected. Feature not implemented yet.")
    elif user_input == '4':
        print("Records selected. Feature not implemented yet.")
    else:
        print('Invalid input. Please enter a number between 1 and 4.')

    print('----------------------------------------------------------------')
    print('Copyright 2025 @M.R.Ansari')

if __name__ == "__main__":
    main()
