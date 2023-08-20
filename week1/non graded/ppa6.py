#Accept the registration number of a vehicle as input and print its state-code as output.

registration_number = input("")
state_codes = {
    "TN": ["TN"],
    "HR": ["HR"],
    
}
state_code = None
for code, patterns in state_codes.items():
    for pattern in patterns:
        if registration_number[:len(pattern)].upper() == pattern:
            state_code = code
            break
if state_code is not None:
    print(state_code)
else:
    print("State Code not found.")

