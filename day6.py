def mod_div(func):
    def inner(a,b):
        if(a<b):
            a,b=b,a
        return  func(a,b)
    return inner
  

       
@mod_div
def div(a,b):
    return a//b

num1 = int(input("Enter a number:"))
num2 = int(input("Enter another number:"))
obj = div(num1,num2)
print(obj)


        
