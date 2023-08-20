sequence= input().split()
search=input()

if search in sequence:
    count= sequence.count(search)
    print("Yes")
    print(count)
else:
    print("no")