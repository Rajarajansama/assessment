word=input('enter word:')
length=len(word)
print(length)
count=1
i=0
while i<length-1:
        if word[i]==' ':
            if word[i+1]>='a' and word[i+1]<='z':
                count+=1
        i+=1
if word[0]==' ':
    print(count-1)
elif word[0]>='a' and word[0]<='z': 
    print(count)