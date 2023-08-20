def extract_details(email_id):
    
    email_parts = email_id.split('@')
    student_details = email_parts[0].split('_')

    if len(student_details) != 4:
        print("Invalid email ID. Please enter a valid student email ID.")
        return None

    # Extract the details
    branch = student_details[0]
    degree = student_details[1]
    year = student_details[2]
    roll_number = student_details[3]
    institute = email_id.split('.')[2]

    return branch, degree, year, roll_number, institute

# Test
email_id = input("")
details = extract_details(email_id)
if details:
    branch, degree, year, roll_number, institute = details
    print(branch)
    print(degree)
    print(year)
    print(roll_number)
    print(institute)
    