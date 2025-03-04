import csv
import time

def Aaddhar_Payment_System():
    from main import main
    file_path = 'resources/Apes.csv'

    # Get user input
    addhr_last_4_digit = input('Enter the last 4 digits of your Aadhaar number: ')
    while not (addhr_last_4_digit.isdigit() and len(addhr_last_4_digit) == 4):
        print("Invalid input! Please enter exactly 4 digits.")
        addhr_last_4_digit = input('Enter the last 4 digits of your Aadhaar number: ')

    Amount = input('Enter the amount: ')
    while not Amount.replace('.', '', 1).isdigit():  # Allows decimal amounts
        print("Invalid input! Please enter a valid amount.")
        Amount = input('Enter the amount: ')

    # Check if file exists and add headers if needed
    try:
        with open(file_path, 'r') as file:
            is_file_empty = file.read().strip() == ''
    except FileNotFoundError:
        is_file_empty = True

    # Write data to CSV file
    with open(file_path, 'a+', newline='') as file:
        writer = csv.writer(file)

        # Add headers only if the file is new or empty
        if is_file_empty:
            writer.writerow(["Aadhaar Last 4 Digits", "Amount"])

        writer.writerow([addhr_last_4_digit, Amount])
        print('Data saved successfully!')

    # Pause before returning
    time.sleep(2)

    # Ask if the user wants to return to main menu
    go_back = input("Do you want to go back to the main menu? (yes/no): ").strip().lower()
    if go_back in ['yes', 'y']:
        main()
    else:
        print("Exiting... Have a great day!")

