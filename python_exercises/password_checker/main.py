from pass_check import check_pwned_api

while True:
    try:
        password_to_check = input("Enter a password to check (min 8 chars, or 'exit' to quit): ").strip()
        
        # exit option
        if password_to_check.lower() == 'exit':
            print("Exiting..")
            break
        
        if not password_to_check:
            print("Password cannot be empty. Try again -_-")
            continue
        elif len(password_to_check) < 8:
            print("Password must be at least 8 characters long. Try again.")
            continue

        count = check_pwned_api(password_to_check)
        if count:
            print(f"WARNING: The password '{password_to_check}' was found {count} times in data breaches. You should NOT use it!")
        else:
            print(f"SUCCESS: The password '{password_to_check}' was not found in any known data breaches. It's safer to use.")
        
        print("\n----------- Thank you for using ---------")
        again = input("Do you want to check another password?Enter y for'yes' any other means no: ").strip().lower()
        if again != 'y':
            print("Goodbye!")
            break

    except Exception as e:
        print("An error occurred while checking the password:", e)
