def create_dict(words):
    freq= {}
    for word in words:
        freq[word]= freq.get(word,0)+1
    return freq

inputseq= input().lower().split(',')
freq= create_dict(inputseq)
print(freq)