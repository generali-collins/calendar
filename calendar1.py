# Collins Wanga

def main():
    n = eval(input('Input the number of days (28-31): '))
    d = eval(input('Input the starting day(0 = Sun, 1 = Mon,...): '))
    for j in range(d):
        print('  ',end=' ')
    i = 1
    while i <= n:
        
        if i < 10:
            
            print('',i,end = ' ')
        else:
            print(i,end = ' ')
        if (i+d)%8 == 0:
            print(' ')
        i = i + 1
main()
