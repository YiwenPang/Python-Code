n=eval(input())
print(2)
for i in range(3,n+1):
    for j in range(2,i):
        if i==j+1:
            print(i)
        elif i%j==0:
            break