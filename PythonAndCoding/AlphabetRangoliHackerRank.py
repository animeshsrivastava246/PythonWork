def print_rangoli(N):
    # your code goes here
    for i in range(N):
        s = "-".join(chr(ord('A')+N-j-1) for j in range(i+1))
        print((s+s[::-1][1:]).center(N*4-3, '-'))

    for i in range(N-1):
        s = "-".join(chr(ord('a')+N-j-1) for j in range(N-i-1))
        print((s+s[::-1][1:]).center(N*4-3, '-'))
if __name__ == '__main__':
    print('Enter an odd number:')
    n = int(input())
    print_rangoli(n)