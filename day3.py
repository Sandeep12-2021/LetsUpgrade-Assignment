dicty={}
flag=True
while(flag):
    key=input("Enter the key:")
    value=int(input("Enter the value:"))
    dicty[key]=value
    temp=input("Do you want to continue:")
    if(temp[0]=='y'):
        flag=True
    else:
        flag=False

maxVal=0
maxKey=""
for keys,values in dicty.items():
    if(values>maxVal):
        maxVal=values
        maxKey=key

print(maxKey)



