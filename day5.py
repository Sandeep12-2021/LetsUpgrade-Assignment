ls = list(range(1,101))

# generating lists that are having elements divisible by 3 and 5 using filter func
ls3 = list(filter(lambda x:(x%3==0),ls))
ls5 = list(filter(lambda x:(x%5==0),ls))

print("List of elements divisible by 3: ",ls3,"\n List of elements divisible by 5: ",ls5)
