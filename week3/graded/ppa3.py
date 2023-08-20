x, y = 0, 0  # Bot's initial position
moves = []  # List to store the sequence of moves

# Accept the sequence of moves from the user
while True:
    move = input()
    if move == 'STOP':
        break
    moves.append(move)

# Process the moves and update the bot's coordinates
for move in moves:
    if move == 'UP':
        y += 1
    elif move == 'DOWN':
        y -= 1
    elif move == 'LEFT':
        x -= 1
    elif move == 'RIGHT':
        x += 1

# Calculate the Manhattan distance from the origin
distance = abs(x) + abs(y)

# Print the Manhattan distance
print(distance)