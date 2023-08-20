import random
seq= "heads", "tails"
countheads = 0
counttails = 0

for i in range(0,101):
    print(random.choice(seq))
    if random.choice(seq) == "heads":
        countheads +=1 
    if random.choice(seq) == "tails":
        counttails +=1 

print(countheads+counttails)

