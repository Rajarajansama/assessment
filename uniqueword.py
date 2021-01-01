#Finding unique word 
sen=input('Enter words: ')
l=sen.split()
i=0
word=input('enter word to find unique word:')
print('Unique words are: ')
for x in l:
    if x==word:
        print(x,end=' ')