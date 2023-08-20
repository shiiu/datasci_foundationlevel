# Accept employee IDs as input
ids = [int(input()) for _ in range(5)]

# Check if the meeting condition is satisfied
if (ids[0] + ids[1]) % 2 == 0 and (ids[1] + ids[2]) % 2 == 0 and (ids[2] + ids[3]) % 2 == 0 and (ids[3] + ids[4]) % 2 == 0 and (ids[4] + ids[0]) % 2 == 0:
    print("YES")
else:
    print("NO")