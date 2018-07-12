s='cgprgkqnwfjbpruuviskwps' # cgprw
substr='' # initialize an empty string
length = len(s)
countLongest=0
startSlice=0         
endOfLongest=0
L=[0]

# cut the string into different substrs and get the index of begining of each substr
for i in range(length-1):
    if ord(s[i+1])<ord(s[i]):
        L.append(i+1)
L.append(length)
print(L) #注意index在最后一位时，减前面的之后，这一位也要算进substr的长度

# find the longest substr length 
temp=0
comparison=0
for index in range(len(L)-2):
    if (L[index+1]-L[index]) >= (L[index+2]-L[index+1]):
        temp=L[index+1]-L[index]
        if temp>comparison:
            comparison=temp
    else:
        temp=L[index+2]-L[index+1]
        if temp>comparison:
            comparison=temp
print(comparison)

# get the index of longest string
for indexII in range(len(L)-1):
    if L[indexII+1]-L[indexII] == comparison:
        countLongest=L[indexII]
        break # the break is to prevent further loop
print(countLongest)

for NewIndex in range(len(L)-1):
    if countLongest==L[NewIndex]:
        startSlice=L[NewIndex]
        endOfLongest=L[NewIndex+1]

substr=s[startSlice:endOfLongest]

print('Longest substring in alphabetical order is: '+ substr)
