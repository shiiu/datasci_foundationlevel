# Read input sequences of names and dates
names = input().split(',')
dates = list(map(int, input().split(',')))

# Create a dictionary to group names by their birthdates
birthdays = {}
for i, date in enumerate(dates):
    if date in birthdays:
        birthdays[date].append(names[i])
    else:
        birthdays[date] = [names[i]]

# Find pairs of names with the same birthdate
common = []
for date, name_list in birthdays.items():
    if len(name_list) >= 2:
        name_list.sort()  # Sort names in alphabetical order
        for i in range(len(name_list) - 1):
            for j in range(i + 1, len(name_list)):
                common.append([name_list[i], name_list[j]])

# Print the list of common pairs
for pair in common:
    print(','.join(map(str,pair)))