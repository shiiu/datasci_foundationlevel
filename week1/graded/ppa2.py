#Accept the date in DD-MM-YYYY format as input and print the year as output.

def extract_year(date):
    day, month, year = date.split('-')
    print(year)

date = input(" ")
extract_year(date)