password = input()

# Condition 1: Check the length of the password
if len(password) < 8 or len(password) > 32:
    print(False)
else:
    # Condition 2: Check if the password starts with an uppercase or lowercase letter
    if not password[0].isalpha():
        print(False)
    else:
        # Condition 3: Check if the password contains any forbidden characters
        forbidden_chars = "/\\='\""
        if any(char in forbidden_chars for char in password):
            print(False)
        else:
            # Condition 4: Check if the password contains any spaces
            if ' ' in password:
                print(False)
            else:
                # All conditions satisfied
                print(True)