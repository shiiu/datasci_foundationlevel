# Input for the first person
name1 = input().capitalize()
dob1 = input()

# Input for the second person
name2 = input().capitalize()
dob2 = input()

# Extract day, month, and year from the date of birth strings
day1, month1, year1 = map(int, dob1.split('-'))
day2, month2, year2 = map(int, dob2.split('-'))

# Compare the dates of birth
if year1 < year2:
    print(name2)
elif year2 < year1:
    print(name1)
else:  # If the years are the same
    if month1 < month2:
        print(name2)
    elif month2 < month1:
        print(name1)
    else:  # If the months are the same
        if day1 < day2:
            print(name2)
        elif day2 < day1:
            print(name1)
        else:  # If the dates are the same
            print(name2 if name2 < name1 else name1)