list1=[int(ele) for ele in input("Enter list element:").split()]
sum1=0
sum2=0
for i in list1:
    if i%2==0:
        sum1+=i
    else:
        sum2+=i    
print("Sum of even number:",sum1)
print("Sum of odd number:",sum2)
