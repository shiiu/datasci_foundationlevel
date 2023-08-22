def digitstowords(n):
    digitwords = {
        '0': 'zero',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9':'nine',
    }
    
    nstr= str(n)
    for digit in nstr:
        print(digitwords[digit])
        
inputnum= int(input())
ans=digitstowords(inputnum)
print(ans)