# day -2 assingnment
#here we are given to find the max occuring characters in the given word given the words are in lower case only

charList=[0]*26  # count of the characters
string = input("Enter the group of words:")
for i in range(len(string)):
    if(97<=ord(string[i])<=122):
        charList[ord(string[i])-ord('a')]+=1

j=0
pos=0
for i in range(len(charList)):
    if(charList[i]>j):
        j=charList[i]
        pos=i


print(chr(pos+97))
