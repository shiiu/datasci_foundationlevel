# Accept the phone number as input
phone_number = input()

# Check the length of the phone number
if len(phone_number) != 10:
    print("invalid")
else:
    # Check the starting digit of the phone number
    starting_digit = phone_number[0]
    if starting_digit not in ['6', '7', '8', '9']:
        print("invalid")
    else:
        # Check if no digit appears more than 7 times
        digit_counts = {}
        for digit in phone_number:
            digit_counts[digit] = digit_counts.get(digit, 0) + 1
            if digit_counts[digit] > 7:
                print("invalid")
                break
        else:
            # Check if no digit appears more than 5 times in a row
            for i in range(len(phone_number) - 5):
                if phone_number[i] == phone_number[i + 1] == phone_number[i + 2] == phone_number[i + 3] == phone_number[i + 4] == phone_number[i + 5]:
                    print("invalid")
                    break
            else:
                print("valid")