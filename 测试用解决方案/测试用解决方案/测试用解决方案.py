def is_magicsquare(ls):
    ls_width=len(ls[0])
    s=set()
    for i in range(0,ls_width):
        for j in range(0,ls_width):
            s.add(ls[i][j])
    s_width=len(s)
    if ls_width**2!=s_width:
        return False
    else:
        answer = set()
        for i in range(0,ls_width):
            sum=0
            for j in range(0,ls_width):
                sum+=ls[i][j]
            answer.add(sum)
        for j in range(0,ls_width):
            sum=0
            for i in range(0,ls_width):
                sum+=ls[i][j]
            answer.add(sum)
        sum1,sum2=0,0
        for i in range(0,ls_width):
            sum1+=ls[i][ls_width-1-i]
        answer.add(sum1)
        for i in range(0,ls_width):
            sum2+=ls[i][i]
        answer.add(sum2)
        if len(answer)==1:
            return True
        else:
            return False

if __name__=='__main__':
    n = eval(input())
    ls = []
    for i in range(n):
        ls.append(list(eval(input())))
    #print(ls)
    if is_magicsquare(ls)==True:
        print('Yes')
    else:
        print('No')