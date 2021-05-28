for tc in range(int(input())):
    n = int(input())
    ls = list(map(int, input().split()))
    if (0 in ls) or (1 in ls):
        print("yes")
    else:
        p = 1
        for x in ls:
            p *=x
        
        flag = 0
        for y in ls:
            a = y
            b = p//y
            if b%a == 0:
                flag = 1
        if flag == 1:
            print("yes")
        else:
            print("no")